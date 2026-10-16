package web

import (
	"context"
	"io"
	"log"
	"net/http"
	"net/http/httptest"
	"os"
	"os/exec"
	"path/filepath"
	"sync"
	"testing"
	"time"

	"github.com/aither64/dev-workspace/portal/internal/session"
)

// Disposable verification only. Exercise the shipped transport, registration,
// worker and Test action; do not reconcile native activity or create sessions.
func TestNotificationProviderProbe(t *testing.T) {
	if os.Getenv("PORTAL_PROVIDER_PROBE") != "1" {
		t.Skip("explicit provider probe required")
	}
	n := testNotifications(t)
	prepareInteractiveConversation(t, n.server, "example")
	fixture := httptest.NewUnstartedServer(nil)
	fixture.Config.ErrorLog = log.New(io.Discard, "", 0)
	n.server.config.BaseURL = "https://" + fixture.Listener.Addr().String()
	n.server.trustedOrigins = []string{n.server.config.BaseURL}
	summary, err := session.Find(n.server.config.Workspace, "example")
	if err != nil {
		t.Fatal("fixture session unavailable")
	}
	identity, err := session.ObservationIdentity(n.server.config.Workspace, "example",
		filepath.Join(n.server.config.Workspace, "work", "example"), summary.Codex.ThreadID)
	if err != nil {
		t.Fatal("fixture identity unavailable")
	}
	handler := n.server.Handler()
	fixture.Config.Handler = http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		switch {
		case r.URL.Path == "/fixture/summary" && r.Method == http.MethodGet:
			n.store.mu.Lock()
			result := map[string]any{"registrations": len(n.store.state.Browsers), "pending": len(n.store.state.Outbox)}
			n.store.mu.Unlock()
			n.server.writeJSON(w, http.StatusOK, result)
		case r.URL.Path == "/api/sessions/example/attention" && r.Method == http.MethodGet:
			n.server.writeJSON(w, http.StatusOK, map[string]any{"version": 1, "identity": identity,
				"rootThread": "thread-1", "enabled": true, "fresh": true, "event": nil, "revision": 0})
		case r.URL.Path == "/api/sessions/example/coordination":
			n.server.writeJSON(w, http.StatusOK, map[string]any{"reservationHolders": []any{}})
		default:
			handler.ServeHTTP(w, r)
		}
	})
	fixture.StartTLS()
	defer fixture.Close()
	ctx, cancel := context.WithCancel(context.Background())
	var sender sync.WaitGroup
	sender.Add(1)
	go func() {
		defer sender.Done()
		ticker := time.NewTicker(time.Second)
		defer ticker.Stop()
		for {
			select {
			case <-ctx.Done():
				return
			case now := <-ticker.C:
				n.sendNext(ctx, now)
			}
		}
	}()
	defer func() { cancel(); sender.Wait() }()
	command := exec.CommandContext(ctx, "node", "notifications_browser_test.cjs", fixture.URL)
	if out, err := command.CombinedOutput(); err != nil {
		t.Log(string(out))
		t.Fatal("provider probe harness did not complete; inspect sanitized results")
	} else {
		t.Log(string(out))
	}
}
