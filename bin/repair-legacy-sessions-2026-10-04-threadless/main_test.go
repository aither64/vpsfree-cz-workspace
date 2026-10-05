package main

import (
	"net"
	"os"
	"path/filepath"
	"testing"
)

func TestSelectedCoordinatesAndLedger(t *testing.T) {
	root := t.TempDir()
	home := filepath.Join(root, "codex")
	socket := filepath.Join(root, "socket")
	if err := os.Mkdir(home, 0700); err != nil {
		t.Fatal(err)
	}
	// Parsing checks a genuine owned keeper alias without dialing the server.
	backend := filepath.Join(root, "backend.sock")
	listener, err := net.Listen("unix", backend)
	if err != nil {
		t.Fatal(err)
	}
	t.Cleanup(func() { listener.Close() })
	if err := os.Symlink(backend, socket); err != nil {
		t.Fatal(err)
	}
	arguments := []string{"--workspace", root, "--session-slug", "2026-10-04-fixture", "--socket", socket, "--codex-home", home}
	values, err := parse(arguments, home)
	if err != nil || values.socket != socket || values.home != home {
		t.Fatalf("exact selection: %#v %v", values, err)
	}
	if clientOptions(socket).SubmissionLedgerPath != socket+".submission-attempts-v3.json" {
		t.Fatal("proof must use the selected ordinary public ledger")
	}
	if _, err := parse(arguments, root); err == nil {
		t.Fatal("another Codex home must refuse")
	}
	if _, err := parse(arguments, ""); err == nil {
		t.Fatal("missing host selection must refuse")
	}
	if _, err := parse(append(arguments, "unexpected"), home); err == nil {
		t.Fatal("extra argument must refuse")
	}
	for _, invalid := range []string{"", "socket", root + "/./socket"} {
		if _, err := parse([]string{"--workspace", root, "--session-slug", "fixture", "--socket", invalid, "--codex-home", home}, home); err == nil {
			t.Fatalf("malformed selected socket must refuse: %q", invalid)
		}
	}
	state := filepath.Join(root, "state")
	if err := os.Mkdir(state, 0700); err != nil {
		t.Fatal(err)
	}
	if values, err := parse([]string{"--mode", "receipts", "--workspace", root, "--session-slug", "fixture", "--user-state-root", state}, ""); err != nil || values.mode != "receipts" {
		t.Fatalf("local receipt coordinates must not require/dial Codex: %#v %v", values, err)
	}
	if _, err := parse(append(arguments, "--mode", "receipts", "--user-state-root", state), home); err == nil {
		t.Fatal("mixed receipt/native arguments must refuse")
	}
	if _, err := parse([]string{"--workspace", root, "--session-slug", "../other", "--socket", socket, "--codex-home", home}, home); err == nil {
		t.Fatal("invalid exact slug must refuse")
	}
	link := filepath.Join(root, "home-link")
	if err := os.Symlink(home, link); err != nil {
		t.Fatal(err)
	}
	if _, err := parse([]string{"--workspace", root, "--session-slug", "fixture", "--socket", socket, "--codex-home", link}, link); err == nil {
		t.Fatal("noncanonical selection must refuse")
	}
	regular := filepath.Join(root, "regular-file")
	if err := os.WriteFile(regular, nil, 0600); err != nil {
		t.Fatal(err)
	}
	if err := os.Remove(socket); err != nil {
		t.Fatal(err)
	}
	if err := os.Symlink(regular, socket); err != nil {
		t.Fatal(err)
	}
	if _, err := parse(arguments, home); err == nil {
		t.Fatal("selected alias to a non-socket target must refuse")
	}
}
