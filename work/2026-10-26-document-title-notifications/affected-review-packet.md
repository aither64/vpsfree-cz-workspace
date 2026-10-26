# Affected final review after native Firefox fixture correction

Same retained reviewer0, saved gpt-6.1-sol/xhigh/read_only; original final-review.md
and exact reviewed ranges retained. This is a new committed final revision with a
necessary changed verification boundary, not a request to repeat unchanged lanes.
Read runtime-fixture-followup.md and original verification/firefox.log failure.
Apply affected general/architecture/scope/risk concerns to fixture loss/idempotency
contract and consumer selections/history/compatibility, retaining original review
for unchanged production source. No checks/builds/edits/claims/deployment. Return
report via report_to_lead; lead saves it. All current heads committed, published,
clean, quick gates pass, and no long new-head checks started by this session.

## dev-workspace

Base 7e6d7c9cdb3388ab7abc720c034c15c21afbd686
Old reviewed head ef85bd0ae50714dbce51ba5807c0234875212a53
New final head d2099c62656bc2a36c306918a92832ba1e1a0cc0

```text
1:  ef85bd0a ! 1:  d2099c62 portal: refresh attention titles in background tabs
    @@ Commit message
         late results in the browser tests and the existing native Firefox fixture.
         Refresh the asset version and document the narrow background exception.
     
    +    Keep the Firefox stand-in idempotent on replay and inject an incomplete
    +    gateway error after acceptance to exercise recovery with the original ID.
    +
         Attention event semantics and persisted formats remain unchanged. Existing
         pages use the correction after reloading.
     
    @@ portal/internal/web/firefox_tabs_acceptance.cjs: function assertBackgroundUnchan
          await until(()=>execute('return document.getElementById("pending").textContent.includes("Disposable Firefox question");'),"typed question invalidation",5000);
     
      ## portal/internal/web/firefox_tabs_test.go ##
    +@@ portal/internal/web/firefox_tabs_test.go: package web
    + 
    + import (
    + 	"context"
    ++	"encoding/json"
    ++	"errors"
    + 	"fmt"
    ++	"io"
    + 	"net/http"
    + 	"net/http/httptest"
    + 	"net/url"
     @@ portal/internal/web/firefox_tabs_test.go: import (
      
      	"github.com/aither64/codex-web/codex"
    @@ portal/internal/web/firefox_tabs_test.go: import (
      	"github.com/aither64/dev-workspace/portal/internal/teamruntime"
      )
      
    +@@ portal/internal/web/firefox_tabs_test.go: import (
    + // proves that the lost response/retry dispatches only one accepted turn.
    + type firefoxTabsCodex struct {
    + 	*browserContractCodex
    ++	muSend   sync.Mutex
    + 	muTabs   sync.Mutex
    + 	watchers map[chan struct{}]struct{}
    + 	revision atomic.Uint64
    +@@ portal/internal/web/firefox_tabs_test.go: func (c *firefoxTabsCodex) PromptsWithItems(context.Context, string) ([]codex.Pr
    + }
    + 
    + func (c *firefoxTabsCodex) Send(ctx context.Context, thread, text, id, action string) (codex.SendReceipt, error) {
    ++	c.muSend.Lock()
    ++	defer c.muSend.Unlock()
    ++	if receipt, found, err := c.ReconcileSend(ctx, thread, text, id, action); err != nil || found {
    ++		return receipt, err
    ++	}
    + 	receipt, err := c.browserContractCodex.Send(ctx, thread, text, id, action)
    + 	if err != nil {
    + 		return receipt, err
    +@@ portal/internal/web/firefox_tabs_test.go: func TestFirefoxFixtureJournalReconcilesOriginalAttempt(t *testing.T) {
    + 	if err != nil {
    + 		t.Fatal(err)
    + 	}
    +-	replay, found, err := c.ReconcileSend(context.Background(), "thread-1", "disposable input", "attempt-1", "")
    +-	if err != nil || !found || replay != receipt || c.sendCount != 1 {
    +-		t.Fatal("reconciliation redispatched fixture turn", err)
    ++	for range 2 {
    ++		replay, err := c.Send(context.Background(), "thread-1", "disposable input", "attempt-1", "")
    ++		if err != nil || replay != receipt || c.sendCount != 1 {
    ++			t.Fatal("duplicate send redispatched fixture turn", err)
    ++		}
    ++	}
    ++	for _, mismatch := range []struct{ text, action string }{{"different input", ""}, {"disposable input", "other-action"}} {
    ++		if _, err := c.Send(context.Background(), "thread-1", mismatch.text, "attempt-1", mismatch.action); err == nil || c.sendCount != 1 {
    ++			t.Fatal("reused fixture identity accepted different content", err)
    ++		}
    + 	}
    + 	data, err := os.ReadFile(c.journal)
    + 	if err != nil || strings.Count(string(data), "\n") != 1 {
    +@@ portal/internal/web/firefox_tabs_test.go: func TestFirefoxFixtureJournalReconcilesOriginalAttempt(t *testing.T) {
    + 	}
    + }
    + 
    ++// A zero-byte close can be transparently replayed by Firefox before fetch sees
    ++// a failure. Send an incomplete gateway error after native acceptance instead.
    ++// A 2xx response is unsuitable: the client tolerates an unreadable JSON body.
    ++func loseFirefoxAcceptedResponse(w http.ResponseWriter) error {
    ++	w.Header().Set("Content-Type", "application/json")
    ++	w.Header().Set("Content-Length", "2")
    ++	w.WriteHeader(http.StatusBadGateway)
    ++	if _, err := io.WriteString(w, "{"); err != nil {
    ++		return err
    ++	}
    ++	w.(http.Flusher).Flush()
    ++	connection, _, err := w.(http.Hijacker).Hijack()
    ++	if err != nil {
    ++		return err
    ++	}
    ++	return connection.Close()
    ++}
    ++
    ++func TestFirefoxFixtureLostResponseRetriesOriginalThroughHTTP(t *testing.T) {
    ++	server := newTestServer(t)
    ++	defer server.Close()
    ++	prepareInteractiveConversation(t, server, "example")
    ++	controller := &firefoxTabsCodex{browserContractCodex: &browserContractCodex{}, journal: filepath.Join(t.TempDir(), "accepted-turns")}
    ++	server.config.Codex = controller
    ++	handler := server.Handler()
    ++	var attempts atomic.Int64
    ++	upstream := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
    ++		attempt := attempts.Add(1)
    ++		response := httptest.NewRecorder()
    ++		handler.ServeHTTP(response, r)
    ++		if response.Code != http.StatusAccepted {
    ++			t.Errorf("fixture handler did not accept original identity: %d", response.Code)
    ++		}
    ++		if attempt == 1 {
    ++			if err := loseFirefoxAcceptedResponse(w); err != nil {
    ++				t.Error(err)
    ++			}
    ++			return
    ++		}
    ++		for key, values := range response.Header() {
    ++			w.Header()[key] = values
    ++		}
    ++		w.WriteHeader(response.Code)
    ++		_, _ = w.Write(response.Body.Bytes())
    ++	}))
    ++	defer upstream.Close()
    ++	const id = "12c12a7b-1898-4d29-85b4-012345678901"
    ++	for _, retry := range []bool{false, true} {
    ++		body := fmt.Sprintf(`{"message":"Disposable lost response","clientUserMessageId":%q,"retry":%t}`, id, retry)
    ++		request, err := http.NewRequest(http.MethodPost, upstream.URL+"/api/sessions/example/message", strings.NewReader(body))
    ++		if err != nil {
    ++			t.Fatal(err)
    ++		}
    ++		request.Header.Set("Origin", server.config.BaseURL)
    ++		request.Header.Set("Content-Type", "application/json")
    ++		response, err := upstream.Client().Do(request)
    ++		if err != nil {
    ++			t.Fatal(err)
    ++		}
    ++		data, readErr := io.ReadAll(response.Body)
    ++		response.Body.Close()
    ++		if !retry {
    ++			if response.StatusCode != http.StatusBadGateway || string(data) != "{" || !errors.Is(readErr, io.ErrUnexpectedEOF) {
    ++				t.Fatalf("fixture must expose headers and a truncated unknown outcome: %d %q %v", response.StatusCode, data, readErr)
    ++			}
    ++		} else {
    ++			var receipt codex.SendReceipt
    ++			if readErr != nil || response.StatusCode != http.StatusAccepted || json.Unmarshal(data, &receipt) != nil || receipt.ClientUserMessageID != id {
    ++				t.Fatalf("original identity retry did not recover acceptance: %d %s %v", response.StatusCode, data, readErr)
    ++			}
    ++		}
    ++	}
    ++	journal, err := os.ReadFile(controller.journal)
    ++	if err != nil || string(journal) != id+"\n" || controller.sendCount != 1 || attempts.Load() != 2 {
    ++		t.Fatalf("lost response must retain one native acceptance across two HTTP attempts: %q %d %d %v", journal, controller.sendCount, attempts.Load(), err)
    ++	}
    ++}
    ++
    + func TestFirefoxFixtureReadiness(t *testing.T) {
    + 	output, err := exec.Command("node", "--test", "firefox_tabs_readiness_test.cjs").CombinedOutput()
    + 	if err != nil {
     @@ portal/internal/web/firefox_tabs_test.go: func runFirefoxFixture(t *testing.T, readBudget bool) {
      	if err != nil {
      		t.Fatal(err)
    @@ portal/internal/web/firefox_tabs_test.go: func runFirefoxFixture(t *testing.T, r
      		if lane == "pending" && failPending.CompareAndSwap(true, false) {
      			if count != nil {
      				mu.Lock()
    +@@ portal/internal/web/firefox_tabs_test.go: func runFirefoxFixture(t *testing.T, readBudget bool) {
    + 			handler.ServeHTTP(response, r)
    + 			lastHandlerStatus.Store(int64(response.Code))
    + 			if response.Code < 300 && lostResponse.CompareAndSwap(false, true) {
    +-				connection, _, err := w.(http.Hijacker).Hijack()
    +-				if err != nil {
    ++				if err := loseFirefoxAcceptedResponse(w); err != nil {
    + 					lossHijackError.Store(true)
    +-					t.Error("fixture could not lose the accepted response")
    ++					t.Error("fixture could not lose the accepted response", err)
    + 					return
    + 				}
    +-				_ = connection.Close()
    + 				lossInjected.Store(true)
    + 				return
    + 			}
     
      ## portal/internal/web/static/session-attention.js ##
     @@
```

```text
 portal/internal/web/firefox_tabs_test.go | 106 +++++++++++++++++++++++++++++--
 1 file changed, 99 insertions(+), 7 deletions(-)
```
## workspace

Base 978a2f280185f3ae114c2db13130f13e6976b159
Old reviewed head 6521561ff57caf84b7ddfa62eee59c7c47d62590
New final head e3b44a8b59c656e0ecec0bd692ad7f72963f7e61

```text
1:  6521561ff ! 1:  e3b44a8b5 inputs: select background title attention correction
    @@ flake.lock
            "locked": {
     -        "lastModified": 1793039518,
     -        "narHash": "sha256-WX2++51WBDKFFp37i1IHZC6lz1GlcVOiNM2Vgl2BDCg=",
    -+        "lastModified": 1793044596,
    -+        "narHash": "sha256-yPBaMwSpf1354Q/qiZcgJq/C3EMxsuqtNZ69qYH45PI=",
    ++        "lastModified": 1793046024,
    ++        "narHash": "sha256-kQkKnjQVSYZw3ZDNan8EakG7HS29wIbHGZ14B7Xq5vA=",
              "owner": "aither64",
              "repo": "dev-workspace",
     -        "rev": "7e6d7c9cdb3388ab7abc720c034c15c21afbd686",
    -+        "rev": "ef85bd0ae50714dbce51ba5807c0234875212a53",
    ++        "rev": "d2099c62656bc2a36c306918a92832ba1e1a0cc0",
              "type": "github"
            },
            "original": {
              "owner": "aither64",
              "repo": "dev-workspace",
     -        "rev": "7e6d7c9cdb3388ab7abc720c034c15c21afbd686",
    -+        "rev": "ef85bd0ae50714dbce51ba5807c0234875212a53",
    ++        "rev": "d2099c62656bc2a36c306918a92832ba1e1a0cc0",
              "type": "github"
            }
          },
    @@ flake.nix
          vpsfree-dev-workspace = {
            url = "github:vpsfreecz/dev-workspace/767dfd587e346168e1443e65ccdb67ce748f3fe3";
     -      inputs.dev-workspace.url = "github:aither64/dev-workspace/7e6d7c9cdb3388ab7abc720c034c15c21afbd686";
    -+      inputs.dev-workspace.url = "github:aither64/dev-workspace/ef85bd0ae50714dbce51ba5807c0234875212a53";
    ++      inputs.dev-workspace.url = "github:aither64/dev-workspace/d2099c62656bc2a36c306918a92832ba1e1a0cc0";
          };
        };
      
```

```text
 flake.lock | 8 ++++----
 flake.nix  | 2 +-
 2 files changed, 5 insertions(+), 5 deletions(-)
```
## vpsfree-cz-configuration

Base 880a6253f8d6cc1368e633f936b174792e86bff7
Old reviewed head c6fa188bfe10bf8acbe728ce8197b77e46705975
New final head 514e6a06ef72c3c2b4c50a592ff58b3d6fcd7cd2

```text
1:  c6fa188b ! 1:  514e6a06 inputs: set devWorkspace to ef85bd0a
    @@ Metadata
     Author: Jakub Skokan <jakub.skokan@havefun.cz>
     
      ## Commit message ##
    -    inputs: set devWorkspace to ef85bd0a
    +    inputs: set devWorkspace to d2099c62
     
    -    devWorkspace: 7e6d7c9c -> ef85bd0a
    -    git log for 7e6d7c9cdb3388ab7abc720c034c15c21afbd686..ef85bd0ae50714dbce51ba5807c0234875212a53
    -    > ef85bd0 portal: refresh attention titles in background tabs
    +    devWorkspace: 7e6d7c9c -> d2099c62
    +    git log for 7e6d7c9cdb3388ab7abc720c034c15c21afbd686..d2099c62656bc2a36c306918a92832ba1e1a0cc0
    +    > d2099c6 portal: refresh attention titles in background tabs
     
      ## flake.lock ##
     @@
    @@ flake.lock
            "locked": {
     -        "lastModified": 1793039518,
     -        "narHash": "sha256-WX2++51WBDKFFp37i1IHZC6lz1GlcVOiNM2Vgl2BDCg=",
    -+        "lastModified": 1793044596,
    -+        "narHash": "sha256-yPBaMwSpf1354Q/qiZcgJq/C3EMxsuqtNZ69qYH45PI=",
    ++        "lastModified": 1793046024,
    ++        "narHash": "sha256-kQkKnjQVSYZw3ZDNan8EakG7HS29wIbHGZ14B7Xq5vA=",
              "owner": "aither64",
              "repo": "dev-workspace",
     -        "rev": "7e6d7c9cdb3388ab7abc720c034c15c21afbd686",
    -+        "rev": "ef85bd0ae50714dbce51ba5807c0234875212a53",
    ++        "rev": "d2099c62656bc2a36c306918a92832ba1e1a0cc0",
              "type": "github"
            },
            "original": {
```

```text
 flake.lock | 6 +++---
 1 file changed, 3 insertions(+), 3 deletions(-)
```

Runtime delta only firefox_tabs_test.go +99/-7 and commit explanation; all
production JS/assets/prose/runner unchanged. Native zero-byte loss after upstream
acceptance was transparently replayed; fake Send lacked real idempotency. Fixture
now serializes exact reconciliation before dispatch and journals once; response
loss injects headers/truncated 502 body after actual acceptance because pinned
browser client tolerates bad JSON on 2xx. Quick actual-handler regression plus
same-ID duplicate/mismatch tests passed (3 tests/0.499s). Original native Retry
original controls/two HTTP attempts/one dispatch/journal remain asserted.
Assess this meaningful fixture boundary and any unproven weakening, not a blind
rerun. No production recovery/API/codex-web changes; no migrations.

Each consumer now has one final pin commit from its original accepted base.
Config generated history correctly states 7e6d7c9c->d2099c62; no obsolete pin
iteration. Semantic graph checks show only runtime node changed since original
review, all edges/follows/siblings preserved; same extension/codex-web/Codex.
Both select d2099c62656bc2a36c306918a92832ba1e1a0cc0 with
sha256-kQkKnjQVSYZw3ZDNan8EakG7HS29wIbHGZ14B7Xq5vA=.
Deployment contract passed and config hooks passed; leases bound old heads,
SSH remote exact new heads verified. No superseded consumer workflows existed.
Candidate application drv wvbhwr6zl16rd51yfpmjf31vwjl368b5-dev-workspace-0.2.0.drv,
expected output ch3lnb3cd89xkqrnb0va3yizq3sq71x1-dev-workspace-0.2.0 (not built).
Graph SHA256 workspace e0036e4a7217e8633d701279e1f7f03a3ec0be0dd9c10398f91c8c5214a64482;
configuration 1af2521240337460f2cd2e60e07ec151477d8ba9179973d724cc423b861a862c.

Original composed/package/config/CI results prove original ranges only. After
review a fresh utility runs native Firefox and exact refreshed composed/config
checks/builds plus monitors runtime CI40394771174. No deployment occurred, so no
equivalent-deployed-head exception is needed. User approval unchanged for bounded
fix and all three master targets. Confirm complete final histories, consolidation
and no-migration conclusion explicitly for new ranges. Keep this review focused.
