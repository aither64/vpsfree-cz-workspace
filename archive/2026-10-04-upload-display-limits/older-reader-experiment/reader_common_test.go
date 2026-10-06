//go:build preparation_compatibility

package web

import (
	"bytes"
	"crypto/sha256"
	"encoding/json"
	"fmt"
	"io/fs"
	"os"
	"path/filepath"
	"strings"
	"testing"
)

// This file is injected into both exact archived revisions. It supplies only
// experiment bookkeeping; readPreparation and loadPreparations remain intact.
type uploadReaderFixture struct {
	Workspace       string
	PreparationRoot string
	UploadDirectory string
	ScopeID         string
	RequestID       string
	ReceiptID       string
	InputDigest     string
	SnapshotDigest  string
	IDs             []string
	RawPrompt       string
	Wire            string
	Slug            string
	Epoch           string
}

func uploadReaderRoot(t *testing.T) string {
	t.Helper()
	root := os.Getenv("PREPARATION_FIXTURE_ROOT")
	if !filepath.IsAbs(root) {
		t.Fatal("PREPARATION_FIXTURE_ROOT must name the disposable experiment directory")
	}
	marker, err := os.ReadFile(filepath.Join(root, "upload-reader-experiment.marker"))
	if err != nil || string(marker) != "disposable-upload-reader-experiment\n" {
		t.Fatal("missing disposable experiment marker", err)
	}
	return root
}

func uploadReaderMetadata(t *testing.T) uploadReaderFixture {
	t.Helper()
	root := uploadReaderRoot(t)
	encoded, err := os.ReadFile(filepath.Join(root, "upload-reader-fixture.json"))
	if err != nil {
		t.Fatal(err)
	}
	var fixture uploadReaderFixture
	if err := json.Unmarshal(encoded, &fixture); err != nil {
		t.Fatal(err)
	}
	if fixture.Workspace != filepath.Join(root, "workspace") || len(fixture.IDs) != 50 ||
		!validPreparationID(fixture.RequestID) || !messageDigestPattern.MatchString(fixture.ReceiptID) ||
		!messageDigestPattern.MatchString(fixture.InputDigest) || !messageDigestPattern.MatchString(fixture.SnapshotDigest) {
		t.Fatal("invalid experiment identity")
	}
	for _, path := range []string{fixture.PreparationRoot, fixture.UploadDirectory} {
		if !filepath.IsAbs(path) || !strings.HasPrefix(path, root+string(filepath.Separator)) {
			t.Fatal("experiment state path is outside the disposable root")
		}
	}
	return fixture
}

func saveUploadReaderMetadata(t *testing.T, fixture uploadReaderFixture) {
	t.Helper()
	encoded, err := json.Marshal(fixture)
	if err != nil {
		t.Fatal(err)
	}
	if err := os.WriteFile(filepath.Join(uploadReaderRoot(t), "upload-reader-fixture.json"), append(encoded, '\n'), 0600); err != nil {
		t.Fatal(err)
	}
}

func uploadReaderPath(fixture uploadReaderFixture, completed bool) string {
	directory := "session-preparations"
	if completed {
		directory = "session-preparation-mappings"
	}
	return filepath.Join(fixture.PreparationRoot, directory, fixture.RequestID+".json")
}

// Fingerprint all disposable persistent state, including uploads, metadata,
// directory entries, modes, mtimes and symlink targets. Reads may change atime;
// it is deliberately excluded. Go build/test logs live outside this tree.
func uploadReaderFingerprint(t *testing.T) [32]byte {
	t.Helper()
	root := uploadReaderRoot(t)
	var snapshot bytes.Buffer
	err := filepath.WalkDir(root, func(path string, entry fs.DirEntry, walkErr error) error {
		if walkErr != nil {
			return walkErr
		}
		info, err := entry.Info()
		if err != nil {
			return err
		}
		relative, err := filepath.Rel(root, path)
		if err != nil {
			return err
		}
		fmt.Fprintf(&snapshot, "%q %v %d %d\n", relative, info.Mode(), info.Size(), info.ModTime().UnixNano())
		switch {
		case info.Mode().IsRegular():
			encoded, err := os.ReadFile(path)
			if err != nil {
				return err
			}
			fmt.Fprintf(&snapshot, "%x\n", sha256.Sum256(encoded))
		case info.Mode()&os.ModeSymlink != 0:
			target, err := os.Readlink(path)
			if err != nil {
				return err
			}
			fmt.Fprintf(&snapshot, "%q\n", target)
		case !info.IsDir():
			return fmt.Errorf("unexpected disposable state entry %s", relative)
		}
		return nil
	})
	if err != nil {
		t.Fatal(err)
	}
	return sha256.Sum256(snapshot.Bytes())
}
