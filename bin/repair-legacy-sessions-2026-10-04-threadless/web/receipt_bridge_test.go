package web

import (
	"bytes"
	"os"
	"path/filepath"
	"strings"
	"testing"
	"time"
)

func TestDatedRepairReceiptOwner(t *testing.T) {
	for _, test := range []struct {
		name, state, selected string
		wantError             bool
	}{
		{"absent", "", "", false},
		{"empty", "empty", "", false},
		{"complete", "complete", "fixture", false},
		{"unrelated_pending", "running", "other", false},
		{"selected_running", "running", "fixture", true},
		{"selected_paused", "paused", "fixture", true},
		{"selected_failed_missing_journal", "failed", "fixture", true},
	} {
		t.Run(test.name, func(t *testing.T) {
			workspace, stateRoot := t.TempDir(), t.TempDir()
			store, err := newLifecycleOperationStore(workspace, stateRoot)
			if err != nil {
				t.Fatal(err)
			}
			if test.state != "" {
				operations := map[string]lifecycleOperation{}
				if test.state != "empty" {
					now := time.Now().UTC().Format(time.RFC3339Nano)
					operations[test.selected] = lifecycleOperation{
						Slug: test.selected, Kind: "archive", State: test.state, Phase: "fixture", StartedAt: now, UpdatedAt: now, Redirect: "/",
						Options: lifecycleOperationOptions{Mode: "complete", JournalID: strings.Repeat("a", 64), JournalExpected: true},
					}
				}
				if err := store.save(operations); err != nil {
					t.Fatal(err)
				}
			}
			before, _ := os.ReadFile(store.path)
			err = DatedLegacyRepairRequireNoPendingBrowserOperation(workspace, "fixture", stateRoot)
			if (err != nil) != test.wantError {
				t.Fatalf("proof: %v", err)
			}
			after, _ := os.ReadFile(store.path)
			if !bytes.Equal(before, after) {
				t.Fatal("read-only proof changed persistent receipt bytes")
			}
		})
	}
}

func TestDatedRepairRefusesUnknownStoreAndCreationResidue(t *testing.T) {
	for _, kind := range []string{"foreign", "duplicate", "unsafe", "invalid_unrelated", "current_creation", "rotated_creation"} {
		t.Run(kind, func(t *testing.T) {
			workspace, stateRoot := t.TempDir(), t.TempDir()
			store, _ := newLifecycleOperationStore(workspace, stateRoot)
			if err := store.save(map[string]lifecycleOperation{}); err != nil {
				t.Fatal(err)
			}
			before, _ := os.ReadFile(store.path)
			switch kind {
			case "foreign":
				before = bytes.ReplaceAll(before, []byte(workspace), []byte(workspace+"-foreign"))
			case "duplicate":
				before = []byte(`{"schema":1,"schema":1,"workspace":"` + workspace + `","operations":[]}`)
			case "unsafe":
				if err := os.Chmod(store.path, 0644); err != nil {
					t.Fatal(err)
				}
			case "invalid_unrelated":
				before = []byte(`{"schema":1,"workspace":"` + workspace + `","operations":[{"slug":"other","state":"unknown"}]}`)
			default:
				directory := filepath.Join(store.directory, "creations")
				if err := os.Mkdir(directory, 0700); err != nil {
					t.Fatal(err)
				}
				name := "fixture.json"
				if kind == "rotated_creation" {
					name = "fixture." + strings.Repeat("b", 64) + ".complete.json"
				}
				if err := os.WriteFile(filepath.Join(directory, name), []byte("owner-only input"), 0600); err != nil {
					t.Fatal(err)
				}
			}
			if err := os.WriteFile(store.path, before, 0600); err != nil {
				t.Fatal(err)
			}
			if err := DatedLegacyRepairRequireNoPendingBrowserOperation(workspace, "fixture", stateRoot); err == nil {
				t.Fatal("unknown/residue proof must refuse")
			}
			after, _ := os.ReadFile(store.path)
			if !bytes.Equal(before, after) {
				t.Fatal("bridge changed input")
			}
		})
	}
}
