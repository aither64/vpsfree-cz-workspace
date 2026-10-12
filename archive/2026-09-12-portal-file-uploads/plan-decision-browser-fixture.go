package web

import (
	"context"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"os"
	"path/filepath"
	"strings"
	"sync/atomic"
	"testing"
	"time"

	"github.com/aither64/codex-web/codex"
	"github.com/aither64/codex-web/conversation"
)

// Reuse the retained upload fixture's in-memory transport and queue.
type planBrowserCodex struct {
	*uploadBrowserCodex
	latest, mode string
}

func (c *planBrowserCodex) ReadThread(context.Context, string) (codex.Transcript, error) {
	c.lock.Lock()
	defer c.lock.Unlock()
	status := "idle"
	if c.busy {
		status = "active"
	}
	return codex.Transcript{ThreadID: "thread-1", LatestTurnID: c.latest, Status: status, Model: "model-1", ReasoningEffort: "medium", CollaborationMode: c.mode, Entries: append([]codex.TranscriptEntry{}, c.entries...)}, nil
}
func (c *planBrowserCodex) UpdateThreadSettings(_ context.Context, _ string, u codex.ThreadSettingsUpdate) (codex.ThreadSettings, error) {
	c.lock.Lock()
	defer c.lock.Unlock()
	if u.CollaborationMode != nil {
		c.mode = *u.CollaborationMode
	}
	return codex.ThreadSettings{Model: "model-1", ReasoningEffort: "medium", CollaborationMode: c.mode}, nil
}
func (c *planBrowserCodex) Send(ctx context.Context, thread, text, id, action string) (codex.SendReceipt, error) {
	receipt, err := c.uploadBrowserCodex.Send(ctx, thread, text, id, action)
	c.lock.Lock()
	c.browserContractCodex.mu.Lock()
	c.browserContractCodex.message, c.browserContractCodex.messageID, c.browserContractCodex.actionContext = text, id, action
	c.browserContractCodex.sendCount++
	first := c.browserContractCodex.sendCount == 1
	c.browserContractCodex.mu.Unlock()
	// Hold correlation of the first implementation to keep its receipt visible
	// while a later identical plan is offered. Its text is already in history.
	if first {
		c.entries[len(c.entries)-1].ClientUserMessageID = ""
		c.entries[len(c.entries)-1].ClientUserMessageDigest = ""
	}
	c.latest = "implementation"
	c.busy = true
	c.lock.Unlock()
	return receipt, err
}
func TestPlanDecisionBrowserFixture(t *testing.T) {
	output := os.Getenv("PORTAL_PLAN_BROWSER_FIXTURE")
	if output == "" {
		t.Skip("manual acceptance")
	}
	server := newTestServer(t)
	defer server.Close()
	prepareInteractiveConversation(t, server, "example")
	directory := filepath.Join(server.config.Workspace, "work", "example")
	changes := make(chan struct{}, 1)
	client := &planBrowserCodex{uploadBrowserCodex: &uploadBrowserCodex{browserContractCodex: &browserContractCodex{events: changes}}, mode: "default", latest: "ordinary"}
	client.entries = []codex.TranscriptEntry{
		{TurnID: "old", ItemID: "old-plan", Kind: "plan", TurnStatus: "completed", Text: "1. Inspect the code.\n2. Implement the change.\n3. Verify the result."},
		{TurnID: "ordinary", ItemID: "reply", Kind: "agentMessage", TurnStatus: "completed", Text: strings.Repeat("An ordinary reply establishing the facts.\n\n", 30)},
	}
	server.config.Codex = client
	server.uploadStore.MinFreeBytes = 0
	httpServer := httptest.NewUnstartedServer(nil)
	server.config.BaseURL = "https://" + httpServer.Listener.Addr().String()
	var err error
	server.conversation, err = conversation.NewHandler(conversation.Options{AllowedOrigins: []string{server.config.BaseURL}, BasePath: "/codex", Shutdown: server.stopping, Resolver: conversation.ResolverFunc(server.resolveConversation)})
	if err != nil {
		t.Fatal(err)
	}
	if err = server.initUploads(); err != nil {
		t.Fatal(err)
	}
	handler := server.Handler()
	stop := make(chan struct{})
	var slow atomic.Bool
	var acknowledge atomic.Bool
	var recoveryWaiting atomic.Bool
	releaseRecovery := make(chan struct{})
	httpServer.Config.Handler = http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if strings.HasPrefix(r.URL.Path, "/fixture/") {
			action := strings.TrimPrefix(r.URL.Path, "/fixture/")
			if action == "recovery-status" {
				json.NewEncoder(w).Encode(map[string]any{"waiting": recoveryWaiting.Load()})
				return
			}
			if action == "release-recovery" {
				close(releaseRecovery)
				w.Write([]byte("{}"))
				return
			}
			client.lock.Lock()
			switch action {
			case "plan", "plan-again", "failed", "interrupted":
				client.latest = action
				client.mode = "plan"
				client.busy = false
				status := "completed"
				if action == "failed" || action == "interrupted" {
					status = action
				}
				client.entries = append(client.entries, codex.TranscriptEntry{TurnID: action, ItemID: action, Kind: "plan", TurnStatus: status, Text: client.entries[0].Text})
			case "ordinary", "empty", "missing":
				client.latest = action
				client.busy = false
				if action == "missing" {
					client.latest = ""
				}
			case "legacy-prepared":
				client.browserContractCodex.mu.Lock()
				client.browserContractCodex.message = "Implement the plan."
				client.browserContractCodex.messageID = "00000000-0000-4000-8000-000000000099"
				client.browserContractCodex.actionContext = "plan:" + planDigest(client.entries[0].Text)
				client.browserContractCodex.sendCount = 0
				client.browserContractCodex.mu.Unlock()
			case "legacy-submitted":
				client.browserContractCodex.mu.Lock()
				client.browserContractCodex.message = "Implement the plan."
				client.browserContractCodex.messageID = "00000000-0000-4000-8000-000000000099"
				client.browserContractCodex.actionContext = "plan:" + planDigest(client.entries[0].Text)
				client.browserContractCodex.sendCount = 1
				client.browserContractCodex.mu.Unlock()
				client.entries = append(client.entries, codex.TranscriptEntry{TurnID: "legacy", ItemID: "legacy", Kind: "userMessage", Text: "Implement the plan.", ClientUserMessageID: "00000000-0000-4000-8000-000000000099", ClientUserMessageDigest: planDigest("Implement the plan.")})
				acknowledge.Store(true)
			case "legacy-reset":
				client.entries = client.entries[:2]
				client.browserContractCodex.mu.Lock()
				client.browserContractCodex.messageID = ""
				client.browserContractCodex.sendCount = 0
				client.browserContractCodex.mu.Unlock()
				acknowledge.Store(false)
			case "queue":
				client.queue = []codex.QueueEntry{{ID: "queued-1", Text: "Preserved queued message", ClientUserMessageID: "queued-1"}}
			case "slow":
				slow.Store(true)
			case "fast":
				slow.Store(false)
			case "stop":
				select {
				case <-stop:
				default:
					close(stop)
				}
			}
			client.lock.Unlock()
			select {
			case changes <- struct{}{}:
			default:
			}
			w.Header().Set("Content-Type", "application/json")
			w.Write([]byte("{}"))
			return
		}
		if strings.HasSuffix(r.URL.Path, "/implement-plan") && acknowledge.Load() {
			recoveryWaiting.Store(true)
			<-releaseRecovery
		}
		// Retain accepted browser receipts to exercise identical later plans.
		if strings.HasSuffix(r.URL.Path, "/message-ack") {
			w.Header().Set("Content-Type", "application/json")
			if acknowledge.Load() {
				var body struct {
					Acknowledgements []struct {
						ID string `json:"clientUserMessageId"`
					} `json:"acknowledgements"`
				}
				json.NewDecoder(r.Body).Decode(&body)
				var ids []string
				for _, item := range body.Acknowledgements {
					ids = append(ids, item.ID)
				}
				json.NewEncoder(w).Encode(map[string]any{"acknowledgedClientUserMessageIds": ids})
				return
			}
			w.WriteHeader(http.StatusServiceUnavailable)
			w.Write([]byte(`{"error":"receipt acknowledgement held by fixture"}`))
			return
		}
		if strings.HasSuffix(r.URL.Path, "/activity") {
			w.Header().Set("Content-Type", "application/json")
			json.NewEncoder(w).Encode(map[string]any{"threadId": "thread-1", "currentState": "waiting", "stateSinceMs": time.Now().Add(-time.Minute).UnixMilli(), "observedAtMs": time.Now().UnixMilli(), "coverageComplete": true})
			return
		}
		if r.Method == "PATCH" && slow.Load() {
			time.Sleep(time.Second)
		}
		handler.ServeHTTP(w, r)
	})
	httpServer.StartTLS()
	defer httpServer.Close()
	data, _ := json.Marshal(map[string]string{"url": httpServer.URL, "workspace": server.config.Workspace, "tracking": directory})
	if err = os.WriteFile(output, data, 0600); err != nil {
		t.Fatal(err)
	}
	<-stop
}
