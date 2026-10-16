package web

import (
	"bytes"
	"context"
	"encoding/json"
	"io"
	"log"
	"net/http"
	"net/http/httptest"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"sync"
	"testing"
	"time"

	"github.com/aither64/dev-workspace/portal/internal/session"
)

// Forward the actual response while retaining at most 4096 bytes in memory for
// classification. No response body, request body or header is logged.
type providerProbeResponse struct {
	http.ResponseWriter
	status int
	body   bytes.Buffer
}

func (w *providerProbeResponse) WriteHeader(status int) {
	if w.status == 0 {
		w.status = status
		w.ResponseWriter.WriteHeader(status)
	}
}

func (w *providerProbeResponse) Write(data []byte) (int, error) {
	if w.status == 0 {
		w.WriteHeader(http.StatusOK)
	}
	if remaining := 4096 - w.body.Len(); remaining > 0 {
		_, _ = w.body.Write(data[:min(remaining, len(data))])
	}
	return w.ResponseWriter.Write(data)
}

func providerProbeCategory(status int, body []byte) string {
	if status >= 200 && status < 300 {
		return "accepted"
	}
	var value struct {
		Error string `json:"error"`
	}
	if json.Unmarshal(body, &value) != nil {
		return "unclassified_response"
	}
	known := map[string]string{
		"Workspace package changed. Reload before saving.":                 "package_admission",
		"Notification origin is invalid.":                                  "origin_invalid",
		"Browser notifications are unavailable.":                           "notifications_unavailable",
		"Notification storage is unavailable.":                             "storage_unavailable",
		"notification storage is unavailable":                              "storage_unavailable",
		"invalid JSON request":                                             "invalid_json",
		"request must contain one JSON value":                              "multiple_json_values",
		"unsupported push provider endpoint":                               "unsupported_endpoint",
		"invalid push public key":                                          "invalid_public_key",
		"invalid push authentication key":                                  "invalid_auth_key",
		"push subscription has expired":                                    "subscription_expired",
		"This subscription belongs to another portal origin.":              "registration_origin_conflict",
		"Registration could not be created.":                               "registration_randomness",
		"Browser registration is unavailable. Enable notifications again.": "registration_unavailable",
		"Browser notifications are disabled.":                              "notifications_disabled",
		"Invalid notification action.":                                     "invalid_action",
		"notification record limit reached":                                "record_limit",
		"notification state exceeds its size limit":                        "state_size_limit",
	}
	if category, ok := known[value.Error]; ok {
		return category
	}
	return "unclassified_product_error"
}

type providerProbeHTTP struct {
	Sequence              int    `json:"sequence"`
	Action                string `json:"action"`
	Status                int    `json:"status"`
	Category              string `json:"category"`
	HostProfileCurrent    bool   `json:"hostProfileCurrent"`
	ProviderAdmission     bool   `json:"providerAdmission"`
	HostOriginMatched     bool   `json:"hostOriginMatched"`
	MutationOriginMatched bool   `json:"mutationOriginMatched"`
	RegistrationsBefore   int    `json:"registrationsBefore"`
	RegistrationsAfter    int    `json:"registrationsAfter"`
	StoreFailed           bool   `json:"storeFailed"`
}

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
	var diagnosticsMu sync.Mutex
	diagnostics := []providerProbeHTTP{}
	sequence := 0
	fixture.Config.Handler = http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		switch {
		case r.URL.Path == "/fixture/summary" && r.Method == http.MethodGet:
			n.store.mu.Lock()
			result := map[string]any{"registrations": len(n.store.state.Browsers), "pending": len(n.store.state.Outbox)}
			n.store.mu.Unlock()
			diagnosticsMu.Lock()
			result["httpDiagnostics"] = append([]providerProbeHTTP{}, diagnostics...)
			result["httpDiagnosticCount"] = sequence
			diagnosticsMu.Unlock()
			n.server.writeJSON(w, http.StatusOK, result)
		case r.Method == http.MethodPost && (r.URL.Path == "/api/browser-notifications/register" ||
			r.URL.Path == "/api/browser-notifications/disable" || r.URL.Path == "/api/browser-notifications/test"):
			profile, profileErr := readHostProfileIdentity(n.server.config.HostProfile)
			origin := n.server.notificationOrigin(r)
			record := providerProbeHTTP{Action: strings.TrimPrefix(r.URL.Path, "/api/browser-notifications/"),
				HostProfileCurrent: profileErr == nil && profile == n.server.hostProfile,
				ProviderAdmission:  n.server.requireProviderAdmission() == nil,
				HostOriginMatched:  origin != "", MutationOriginMatched: origin != "" && r.Header.Get("Origin") == origin}
			n.store.mu.Lock()
			record.RegistrationsBefore = len(n.store.state.Browsers)
			n.store.mu.Unlock()
			response := &providerProbeResponse{ResponseWriter: w}
			handler.ServeHTTP(response, r)
			record.Status = response.status
			record.Category = providerProbeCategory(response.status, response.body.Bytes())
			n.store.mu.Lock()
			record.RegistrationsAfter, record.StoreFailed = len(n.store.state.Browsers), n.store.failed
			n.store.mu.Unlock()
			diagnosticsMu.Lock()
			sequence++
			record.Sequence = sequence
			diagnostics = append(diagnostics, record)
			if len(diagnostics) > 24 {
				diagnostics = diagnostics[len(diagnostics)-24:]
			}
			diagnosticsMu.Unlock()
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
