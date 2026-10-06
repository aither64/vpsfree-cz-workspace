//go:build preparation_compatibility

package web

import (
	"strings"
	"testing"
	"unicode/utf8"

	"github.com/aither64/dev-workspace/portal/internal/session"
)

// Injected only into exact base 6a972b9ab01077611b2c60e0fc726c185e050315.
// Construct only the state needed by the unchanged production directory loader:
// calling New would create unrelated state before returning a reader failure.
func previousUploadReader(fixture uploadReaderFixture) *Server {
	return &Server{config: Config{Workspace: fixture.Workspace}, operationStore: &lifecycleOperationStore{
		workspace: fixture.Workspace, directory: fixture.PreparationRoot,
	}}
}

func TestUploadReaderExperimentPreviousRejectsFifty(t *testing.T) {
	fixture := uploadReaderMetadata(t)
	before := uploadReaderFingerprint(t)
	record, err := readPreparation(uploadReaderPath(fixture, false), fixture.Workspace)
	if err == nil || err.Error() != "invalid preparation prompt" {
		t.Fatalf("previous reader must refuse the full 50-file record at its prompt bound: %v", err)
	}
	// The unchanged strict reader returned parsed data with its validation error.
	// Verify the actual workspace, schema and digests, so a corrupt synthetic
	// fixture cannot substitute for the attachment-count boundary.
	if record.Schema != 1 || record.InputVersion != 1 || record.Workspace != fixture.Workspace || record.RequestID != fixture.RequestID ||
		record.ReceiptID != fixture.ReceiptID || record.InputDigest != fixture.InputDigest || record.SnapshotDigest != fixture.SnapshotDigest ||
		record.State != "paused" || record.Snapshot == nil || len(record.Snapshot.Input.Attachments) != 50 ||
		record.InputDigest != inputPreparationDigest(record.Snapshot.Input) || record.SnapshotDigest != preparationDigest(record.Snapshot) {
		t.Fatal("previous reader did not reject the genuine frozen 50-file preparation")
	}
	if record.Snapshot.Input.RawPrompt != fixture.RawPrompt || !utf8.ValidString(fixture.RawPrompt) ||
		len(fixture.RawPrompt) > session.MaxMessageBytes || strings.TrimSpace(fixture.RawPrompt) == "" || record.Snapshot.Goal != fixture.Wire {
		t.Fatal("fixture has an invalid prompt rather than the intended count boundary")
	}
	reader := previousUploadReader(fixture)
	if err := reader.loadPreparations(); err == nil || !strings.Contains(err.Error(), "invalid preparation prompt") ||
		!strings.Contains(err.Error(), fixture.RequestID) || len(reader.preparations) != 0 {
		t.Fatalf("previous directory loader failed to refuse the same identity: %v", err)
	}
	if after := uploadReaderFingerprint(t); before != after {
		t.Fatal("previous reader/loader mutated disposable persistent state while rejecting the record")
	}
	t.Logf("exact prior reader rejected the 50-file snapshot and directory load; request=%s; persistent-state fingerprint unchanged: %x", fixture.RequestID, before)
}

func TestUploadReaderExperimentPreviousAcceptsMapping(t *testing.T) {
	fixture := uploadReaderMetadata(t)
	before := uploadReaderFingerprint(t)
	record, err := readPreparation(uploadReaderPath(fixture, true), fixture.Workspace)
	if err != nil || record.State != "terminal" || record.Terminal != "ready" || record.Snapshot != nil || record.Handoff != nil ||
		record.SnapshotDigest != "" || record.Base != "" || record.InputVersion != 1 || record.Workspace != fixture.Workspace ||
		record.RequestID != fixture.RequestID || record.ReceiptID != fixture.ReceiptID || record.InputDigest != fixture.InputDigest ||
		record.Slug != fixture.Slug || record.Epoch != fixture.Epoch {
		t.Fatalf("previous strict reader rejected or changed the normal terminal mapping: %#v %v", record, err)
	}
	reader := previousUploadReader(fixture)
	if err := reader.loadPreparations(); err != nil {
		t.Fatal("previous directory loader rejected the normally compacted mapping", err)
	}
	loaded, ok := reader.preparations[fixture.RequestID]
	if !ok || len(reader.preparations) != 1 || loaded.State != "terminal" || loaded.ReceiptID != fixture.ReceiptID || loaded.InputDigest != fixture.InputDigest {
		t.Fatal("previous directory loader did not load the same compact identity")
	}
	if after := uploadReaderFingerprint(t); before != after {
		t.Fatal("previous reader/loader mutated disposable persistent state while accepting the mapping")
	}
	t.Logf("exact prior reader accepted the normal terminal mapping and directory load; request=%s receipt=%s; persistent-state fingerprint unchanged: %x", fixture.RequestID, fixture.ReceiptID, before)
}
