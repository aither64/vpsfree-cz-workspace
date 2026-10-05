// Copy only into the disposable committed-R build, as internal/web/
// dated_legacy_repair_bridge.go. This export never enters the runtime package.
package web

import (
	"errors"
	"os"
	"path/filepath"
	"strings"

	"github.com/aither64/dev-workspace/portal/internal/session"
)

func DatedLegacyRepairRequireNoPendingBrowserOperation(workspace, slug, stateRoot string) error {
	if !session.ValidSlug(slug) {
		return errors.New("invalid exact repair slug")
	}
	for _, path := range []string{workspace, stateRoot} {
		resolved, err := filepath.EvalSymlinks(path)
		if !filepath.IsAbs(path) || filepath.Clean(path) != path || err != nil || resolved != path {
			return errors.New("repair receipt coordinates are not canonical")
		}
	}
	store, err := newLifecycleOperationStore(workspace, stateRoot)
	if err != nil {
		return err
	}
	operations, err := store.loadReadOnly()
	if err != nil {
		return err
	}
	if operation, exists := operations[slug]; exists && operation.State != "complete" {
		return errors.New("selected browser operation must finish through its ordinary owner")
	}
	// This tool excludes portal-created rows, including genuine ready receipts:
	// those stay with their ordinary creation owner. Only exact path presence is
	// consumed here; this bridge never corroborates or parses creation proof.
	entries, err := os.ReadDir(filepath.Join(store.directory, "creations"))
	if err != nil && !errors.Is(err, os.ErrNotExist) {
		return err
	}
	for _, entry := range entries {
		if entry.Name() == slug+".json" || strings.HasPrefix(entry.Name(), slug+".") {
			return errors.New("selected private creation evidence must finish through its ordinary owner")
		}
	}
	return nil
}
