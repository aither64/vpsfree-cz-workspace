// Source-only maintenance caller. Build inside the reviewed runtime's exported
// portal module, never as an installed command or a separate Go module.
package main

import (
	"context"
	"errors"
	"flag"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"syscall"
	"time"

	codex "github.com/aither64/codex-web/codex"
	"github.com/aither64/dev-workspace/portal/internal/session"
	"github.com/aither64/dev-workspace/portal/internal/web"
	"github.com/aither64/dev-workspace/portal/internal/workspacecodex"
)

type coordinates struct {
	workspace, slug, socket, home string
	mode, stateRoot               string
}

func canonical(path string) (string, error) {
	if !filepath.IsAbs(path) || filepath.Clean(path) != path {
		return "", errors.New("expected a canonical absolute path")
	}
	resolved, err := filepath.EvalSymlinks(path)
	if err != nil || resolved != path {
		return "", errors.New("path is unavailable or differs from its canonical identity")
	}
	return resolved, nil
}

func selectedSocket(path string) error {
	if !filepath.IsAbs(path) || filepath.Clean(path) != path {
		return errors.New("expected an absolute normalized selected socket path")
	}
	// Follow the keeper alias for type/ownership, retaining its logical identity.
	info, err := os.Stat(path)
	if err != nil {
		return fmt.Errorf("selected socket is unavailable: %w", err)
	}
	if info.Mode()&os.ModeSocket == 0 {
		return errors.New("selected path is not a Unix socket")
	}
	owner, ok := info.Sys().(*syscall.Stat_t)
	if !ok {
		return errors.New("selected socket ownership is unavailable")
	}
	if owner.Uid != uint32(os.Geteuid()) {
		return fmt.Errorf("selected socket belongs to uid %d, expected uid %d", owner.Uid, os.Geteuid())
	}
	return nil
}

func parse(arguments []string, selectedHome string) (coordinates, error) {
	var values coordinates
	flags := flag.NewFlagSet("dated-legacy-threadless", flag.ContinueOnError)
	flags.SetOutput(io.Discard)
	flags.StringVar(&values.workspace, "workspace", "", "exact workspace")
	flags.StringVar(&values.slug, "session-slug", "", "reviewed exact slug")
	flags.StringVar(&values.socket, "socket", "", "selected socket")
	flags.StringVar(&values.home, "codex-home", "", "selected Codex home")
	flags.StringVar(&values.mode, "mode", "threadless", "threadless or receipts")
	flags.StringVar(&values.stateRoot, "user-state-root", "", "selected private state")
	if err := flags.Parse(arguments); err != nil || flags.NArg() != 0 || !session.ValidSlug(values.slug) {
		return values, errors.New("invalid or incomplete threadless proof arguments")
	}
	paths := []string{values.workspace}
	switch values.mode {
	case "threadless":
		if values.stateRoot != "" {
			return values, errors.New("threadless mode does not accept receipt coordinates")
		}
		paths = append(paths, values.home, selectedHome)
	case "receipts":
		if values.socket != "" || values.home != "" {
			return values, errors.New("receipts mode does not accept native coordinates")
		}
		paths = append(paths, values.stateRoot)
	default:
		return values, errors.New("unsupported source proof mode")
	}
	for _, path := range paths {
		if _, err := canonical(path); err != nil {
			return values, err
		}
	}
	if values.mode == "threadless" {
		if values.home != selectedHome {
			return values, errors.New("selected Codex home differs from --codex-home")
		}
		if err := selectedSocket(values.socket); err != nil {
			return values, err
		}
	}
	return values, nil
}

func clientOptions(socket string) codex.ClientOptions {
	return codex.ClientOptions{
		ClientInfo:           codex.ClientInfo{Name: "dev-workspace", Title: "Development Workspace", Version: "0.1.0"},
		SubmissionLedgerPath: socket + ".submission-attempts-v3.json",
	}
}

func prove(values coordinates) error {
	if values.mode == "receipts" {
		return web.DatedLegacyRepairRequireNoPendingBrowserOperation(values.workspace, values.slug, values.stateRoot)
	}
	client := workspacecodex.NewWithOptions(values.socket, values.workspace, clientOptions(values.socket))
	defer client.Close()
	ctx, cancel := context.WithTimeout(context.Background(), time.Minute)
	defer cancel()
	return workspacecodex.RequireThreadlessConversations(ctx, client, filepath.Join(values.workspace, "work", values.slug))
}

func main() {
	values, err := parse(os.Args[1:], os.Getenv("DEV_WORKSPACE_CODEX_HOME"))
	if err == nil {
		err = prove(values)
	}
	if err != nil {
		message := err.Error()
		if len(message) > 4096 {
			message = message[:4096]
		}
		fmt.Fprintln(os.Stderr, "dated threadless proof: "+message)
		os.Exit(1)
	}
}
