//go:build preparation_compatibility

package web

import (
	"bytes"
	"context"
	"crypto/sha256"
	"encoding/hex"
	"errors"
	"fmt"
	"io"
	"net/url"
	"os"
	"path/filepath"
	"slices"
	"strings"
	"testing"
	"time"

	"github.com/aither64/codex-web/conversation"
	"github.com/aither64/dev-workspace/portal/internal/uploads"
)

// Reuse the repository's disposable compatibilityServer, POST/retry helpers,
// receipt wait and creation-proof helper. No installed program is launched.
func TestUploadReaderExperimentWriteFifty(t *testing.T) {
	root := uploadReaderRoot(t)
	server, _ := compatibilityServer(t, true)
	defer server.Close()
	if server.config.Workspace != filepath.Join(root, "workspace") || server.uploadStore.UploadLimits.Files != 50 {
		t.Fatal("experiment is not using the disposable current 50-file flow")
	}
	ctx := context.Background()
	server.uploadStore.MinFreeBytes = 0
	scope, err := server.uploadStore.NewDraft(ctx)
	if err != nil {
		t.Fatal(err)
	}
	backend := &uploads.Backend{Store: server.uploadStore, ScopeID: scope.ID}
	ids := make([]string, 50)
	contents := []byte("x")
	checksum := sha256.Sum256(contents)
	for i := range ids {
		file, err := backend.Create(ctx, conversation.UploadRequest{ClientID: preparationTestID(2000+i), Name: fmt.Sprintf("f-%02d.txt", i), Size: 1})
		if err != nil {
			t.Fatal(err)
		}
		if _, err := backend.Append(ctx, file.ID, 0, hex.EncodeToString(checksum[:]), bytes.NewReader(contents)); err != nil {
			t.Fatal(err)
		}
		if _, err := backend.Complete(ctx, file.ID); err != nil {
			t.Fatal(err)
		}
		ids[i] = file.ID
	}
	entered := make(chan struct{})
	server.config.SessionNamer = func(ctx context.Context, _ string) (string, error) {
		close(entered)
		<-ctx.Done()
		return "", ctx.Err()
	}
	id, prompt := preparationTestID(1), " bounded reader experiment "
	response := postPreparation(t, server, id, prompt, "", url.Values{"uploadScope": {scope.ID}, "attachmentIds": ids})
	if response.Code != 202 {
		t.Fatalf("50-file admission=%d %s", response.Code, response.Body.String())
	}
	select {
	case <-entered:
	case <-time.After(3*time.Second):
		t.Fatal("naming did not start")
	}
	server.Close()
	record, err := readPreparation(server.preparationPath(id, false), server.config.Workspace)
	if err != nil || record.State != "paused" || record.Snapshot == nil || record.Slug != "" ||
		!slices.Equal(record.Snapshot.Input.Attachments, ids) || strings.Count(record.Snapshot.Goal, `"name":`) != 50 {
		t.Fatalf("current unfinished record=%#v %v", record, err)
	}
	if record.InputDigest != inputPreparationDigest(record.Snapshot.Input) || record.SnapshotDigest != preparationDigest(record.Snapshot) {
		t.Fatal("current fixture digests do not bind the actual input and wire snapshot")
	}
	fixture := uploadReaderFixture{Workspace: server.config.Workspace, PreparationRoot: server.operationStore.directory,
		UploadDirectory: server.uploadStore.Directory, ScopeID: scope.ID, RequestID: id, ReceiptID: record.ReceiptID,
		InputDigest: record.InputDigest, SnapshotDigest: record.SnapshotDigest, IDs: ids, RawPrompt: prompt, Wire: record.Snapshot.Goal}
	saveUploadReaderMetadata(t, fixture)
	t.Logf("current flow durably accepted %d ready attachments; request=%s receipt=%s inputDigest=%s", len(ids), id, record.ReceiptID, record.InputDigest)
}

func TestUploadReaderExperimentCompactFifty(t *testing.T) {
	fixture := uploadReaderMetadata(t)
	server, _ := compatibilityServer(t, false)
	defer server.Close()
	current, ok := server.preparationStatus(fixture.RequestID)
	if !ok || current.State != "paused" || current.ReceiptID != fixture.ReceiptID || current.Attempt != 1 {
		t.Fatalf("current restart lost the unfinished request: %#v", current)
	}
	response := postPreparation(t, server, fixture.RequestID, fixture.RawPrompt, "", url.Values{"uploadScope": {fixture.ScopeID}, "attachmentIds": fixture.IDs})
	if response.Code != 202 {
		t.Fatalf("identical 50-file replay=%d %s", response.Code, response.Body.String())
	}
	server.config.SessionNamer = func(context.Context, string) (string, error) {
		return `{"name":"reader-boundary-experiment"}`, nil
	}
	retry := postCreation(t, server, "/api/session-creations/"+fixture.RequestID+"/retry", fmt.Sprintf(`{"receiptId":%q,"attempt":1}`, fixture.ReceiptID), "application/json")
	if retry.Code != 202 {
		t.Fatalf("retry=%d %s", retry.Code, retry.Body.String())
	}
	record := awaitPreparation(t, server, fixture.RequestID)
	if record.State != "handed_off" || record.Snapshot == nil || record.ReceiptID != fixture.ReceiptID ||
		record.InputDigest != fixture.InputDigest || record.SnapshotDigest != fixture.SnapshotDigest ||
		record.Snapshot.Goal != fixture.Wire || !slices.Equal(record.Snapshot.Input.Attachments, fixture.IDs) {
		t.Fatalf("normal handoff changed the frozen request: %#v", record)
	}
	receipt := awaitCreation(t, server, record.Slug)
	if receipt.ReceiptID != fixture.ReceiptID || receipt.Goal != fixture.Wire {
		t.Fatal("ordinary receipt lost the original request")
	}
	// The fixture's DevSession path cannot start a real session. Supply its
// existing exact receipt/proof helper, then exercise production ready update,
// creation proof, upload binding, compaction and receipt retirement unchanged.
	receipt.State, receipt.Validated, receipt.Error = "ready", true, ""
	writeCreationProof(t, server, receipt)
	if err := server.updateCreation(receipt); err != nil {
		t.Fatal("normal ready update/compaction", err)
	}
	ready, ok := server.currentCreation(record.Slug)
	if !ok || ready.State != "ready" {
		t.Fatal("ready receipt was not installed")
	}
	server.operationMu.Lock()
	err := server.retireIdleCreation(ready)
	server.operationMu.Unlock()
	if err != nil {
		t.Fatal("normal receipt retirement", err)
	}
	compact, err := readPreparation(server.preparationPath(fixture.RequestID, true), server.config.Workspace)
	if err != nil || compact.State != "terminal" || compact.Terminal != "ready" || compact.Snapshot != nil ||
		compact.Handoff != nil || compact.SnapshotDigest != "" || compact.Base != "" ||
		compact.InputDigest != fixture.InputDigest || compact.ReceiptID != fixture.ReceiptID || compact.Slug != record.Slug || compact.Epoch != record.Epoch {
		t.Fatalf("normal compact mapping=%#v %v", compact, err)
	}
	if _, err := os.Stat(server.preparationPath(fixture.RequestID, false)); !errors.Is(err, os.ErrNotExist) {
		t.Fatal("normal compaction did not remove the full record from the unfinished directory", err)
	}
	backend := &uploads.Backend{Store: server.uploadStore, ScopeID: fixture.ScopeID}
	for _, id := range fixture.IDs {
		content, err := backend.Open(context.Background(), id)
		if err != nil {
			t.Fatal("normal compaction lost a selected file", err)
		}
		encoded, readErr := io.ReadAll(content.File)
		content.File.Close()
		if readErr != nil || string(encoded) != "x" {
			t.Fatal("normal compaction changed selected bytes", readErr)
		}
	}
	fixture.Slug, fixture.Epoch = record.Slug, record.Epoch
	saveUploadReaderMetadata(t, fixture)
	t.Logf("normal ready update compacted request=%s into terminal mapping for %s; all %d uploaded files remain", fixture.RequestID, fixture.Slug, len(fixture.IDs))
}
