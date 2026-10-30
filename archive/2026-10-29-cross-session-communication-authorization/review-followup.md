# Narrow native fixture repair after review

Independent final review remains preserved in review-report.md for exact
base 08f3dbb92bc8585929edee85a824d44dfb3b0846 and head c43904a72d705562b79dcf9d59a29cf743bc9de7.
The initial long native run failed before delivery. B proved missing fixture
markers at the native MCP filtered environment boundary with startup-only red
(0.661s) and green (0.680s) checks. See implementation-b.md for exact evidence.

Lead directly inspected the repair: explicit disposable fixture MCP environment,
a 5s handshake regression, and bounded startup failure log. Only the tagged
native test file differs (+28/-2). No production, policy, docs, schema, transport,
authority boundary or recovery behavior changed. Focused command roundtrip and
native compile checks pass. Mandatory review narrow-fix rule applies; no affected
lane rerun is needed. This does not convert native compile proof to acceptance.

B repair was folded into its unpublished owning commit. New final head:
124be7794936b84c4b26811c7deb74ff3843666b. A is unchanged. Same base and two coherent commits;
no obsolete iteration, migrations or repeated dependency streams introduced.
Full native execution and packaged/CI results remain separate requirements.

## Range comparison

```text
1:  ed16c606 = 1:  ed16c606 communication: attach verified grant context to deliveries
2:  c43904a7 ! 2:  124be779 communication: clarify bidirectional runtime authorization
    @@ portal/cmd/workspace-portal/session_communication_native_integration_test.go (ne
     +	}
     +}
     +
    ++func TestNativeSessionCommunicationMCPHandshake(t *testing.T) {
    ++	native := os.Getenv("LIVE_SWITCH_CODEX")
    ++	if !filepath.IsAbs(native) {
    ++		t.Fatal("LIVE_SWITCH_CODEX must select the exact pinned native")
    ++	}
    ++	nativeCommunicationRoundTrip(t, native, "handshake")
    ++}
    ++
     +func nativeCommunicationRoundTrip(t *testing.T, native, mode string) {
     +	f := newCommunicationCommandFixture(t)
     +	home := filepath.Join(f.root, "codex-home")
     +	if err := os.MkdirAll(home, 0700); err != nil {
     +		t.Fatal(err)
     +	}
    -+	ctx, cancel := context.WithTimeout(context.Background(), 75*time.Second)
    ++	timeout := 75 * time.Second
    ++	if mode == "handshake" {
    ++		timeout = 5 * time.Second
    ++	}
    ++	ctx, cancel := context.WithTimeout(context.Background(), timeout)
     +	defer cancel()
     +	const firstID = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
     +	const replyID = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    @@ portal/cmd/workspace-portal/session_communication_native_integration_test.go (ne
     +		"[model_providers.fixture]\nname=\"Fixture\"\nwire_api=\"responses\"\nsupports_websockets=false\nenv_key=\"OPENAI_API_KEY\"\nbase_url=" + strconv.Quote(backend.URL+"/v1") + "\n" +
     +		"[mcp_servers.team_reporting]\ncommand=" + strconv.Quote(f.binary) + "\nargs=" + string(mcpArgs) + "\nrequired=true\nenabled_tools=[\"session_communication\"]\n" +
     +		"[mcp_servers.team_reporting.tools.session_communication]\napproval_mode=\"approve\"\n"
    ++	// Native MCP children inherit a filtered environment. Pass the disposable
    ++	// helper's markers explicitly, including its fixture-child startup guard.
    ++	config += "[mcp_servers.team_reporting.env]\n"
    ++	for _, entry := range f.environment() {
    ++		key, value, _ := strings.Cut(entry, "=")
    ++		config += key + "=" + strconv.Quote(value) + "\n"
    ++	}
     +	if err := os.WriteFile(filepath.Join(home, "config.toml"), []byte(config), 0600); err != nil {
     +		t.Fatal(err)
     +	}
    @@ portal/cmd/workspace-portal/session_communication_native_integration_test.go (ne
     +		}
     +		thread, err := client.StartThreadWithSettings(ctx, dir, map[string]string{}, settings)
     +		if err != nil {
    -+			t.Fatal(err)
    ++			body, _ := os.ReadFile(log.Name())
    ++			if len(body) > 4000 {
    ++				body = body[len(body)-4000:]
    ++			}
    ++			t.Fatalf("native thread startup: %v; log tail: %s", err, body)
    ++		}
    ++		if mode == "handshake" {
    ++			return
     +		}
     +		identities = append(identities, f.session(t, slug, thread))
     +		if _, err := client.SendWithOptions(ctx, thread, "materialize-communication-fixture", "seed-"+slug, "fixture", codex.TurnOptions{}); err != nil {
```

## Native first-turn fixture repair

The next native run at 124be779 passed MCP startup but failed seed submission
before communication delivery with no rollout found. B reproduced it with a
short seed diagnostic (0.691s). Fresh fixture threads now receive a real native
turn/start using fixture model/effort, as the existing native reporting fixture
does, before managed sends. Startup/seed passes in 1.036s. The explored managed
initial-message helper correctly refused raw source=vscode; that uncommitted
approach was removed and its production refusal preserved.

Lead directly inspected +11/-7 against 124be779: tagged test only, startup
coverage plus actual seed ordering, no fake rollout/source/receipt. Compile and
real-command checks pass (0.053s/0.514s). Same narrow-fix rule; no new design,
authority boundary, production change or affected review lane. Repair folded
into B. Final head 0bb745041fa508252e1c6d7f2bed26a31b7619fc; original review remains intact.
No migration/history boundary changed. Fresh native execution is pending.

```text
1:  ed16c606 = 1:  ed16c606 communication: attach verified grant context to deliveries
2:  c43904a7 ! 2:  0bb74504 communication: clarify bidirectional runtime authorization
    @@ portal/cmd/workspace-portal/session_communication_native_integration_test.go (ne
     +	}
     +}
     +
    ++func TestNativeSessionCommunicationStartup(t *testing.T) {
    ++	native := os.Getenv("LIVE_SWITCH_CODEX")
    ++	if !filepath.IsAbs(native) {
    ++		t.Fatal("LIVE_SWITCH_CODEX must select the exact pinned native")
    ++	}
    ++	nativeCommunicationRoundTrip(t, native, "startup")
    ++}
    ++
     +func nativeCommunicationRoundTrip(t *testing.T, native, mode string) {
     +	f := newCommunicationCommandFixture(t)
     +	home := filepath.Join(f.root, "codex-home")
     +	if err := os.MkdirAll(home, 0700); err != nil {
     +		t.Fatal(err)
     +	}
    -+	ctx, cancel := context.WithTimeout(context.Background(), 75*time.Second)
    ++	timeout := 75 * time.Second
    ++	if mode == "startup" {
    ++		timeout = 5 * time.Second
    ++	}
    ++	ctx, cancel := context.WithTimeout(context.Background(), timeout)
     +	defer cancel()
     +	const firstID = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
     +	const replyID = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    @@ portal/cmd/workspace-portal/session_communication_native_integration_test.go (ne
     +		"[model_providers.fixture]\nname=\"Fixture\"\nwire_api=\"responses\"\nsupports_websockets=false\nenv_key=\"OPENAI_API_KEY\"\nbase_url=" + strconv.Quote(backend.URL+"/v1") + "\n" +
     +		"[mcp_servers.team_reporting]\ncommand=" + strconv.Quote(f.binary) + "\nargs=" + string(mcpArgs) + "\nrequired=true\nenabled_tools=[\"session_communication\"]\n" +
     +		"[mcp_servers.team_reporting.tools.session_communication]\napproval_mode=\"approve\"\n"
    ++	// Native MCP children inherit a filtered environment. Pass the disposable
    ++	// helper's markers explicitly, including its fixture-child startup guard.
    ++	config += "[mcp_servers.team_reporting.env]\n"
    ++	for _, entry := range f.environment() {
    ++		key, value, _ := strings.Cut(entry, "=")
    ++		config += key + "=" + strconv.Quote(value) + "\n"
    ++	}
     +	if err := os.WriteFile(filepath.Join(home, "config.toml"), []byte(config), 0600); err != nil {
     +		t.Fatal(err)
     +	}
    @@ portal/cmd/workspace-portal/session_communication_native_integration_test.go (ne
     +		}
     +		thread, err := client.StartThreadWithSettings(ctx, dir, map[string]string{}, settings)
     +		if err != nil {
    -+			t.Fatal(err)
    ++			body, _ := os.ReadFile(log.Name())
    ++			if len(body) > 4000 {
    ++				body = body[len(body)-4000:]
    ++			}
    ++			t.Fatalf("native thread startup: %v; log tail: %s", err, body)
     +		}
     +		identities = append(identities, f.session(t, slug, thread))
    -+		if _, err := client.SendWithOptions(ctx, thread, "materialize-communication-fixture", "seed-"+slug, "fixture", codex.TurnOptions{}); err != nil {
    ++		// Fresh thread/start has no rollout for managed resume yet. Materialize
    ++		// its first native turn as the existing native reporting fixture does.
    ++		if err := client.Request(ctx, "turn/start", map[string]any{"threadId": thread,
    ++			"input": []any{map[string]any{"type": "text", "text": "materialize-communication-fixture"}},
    ++			"model": settings.Model, "effort": settings.ReasoningEffort}, nil); err != nil {
     +			t.Fatal(err)
     +		}
     +		wait("materialize "+slug, func() bool { return client.RequireThreadIdle(ctx, thread, dir) == nil })
    ++		if mode == "startup" {
    ++			return
    ++		}
     +	}
     +	a, b := identities[0], identities[1]
     +	store, err := teamruntime.NewStore(f.state, f.root)
```

## Final production-worker fixture correction and acceptance

Affected independent review-report-production.md covers exact08f3dbb9..a6c0e10f.
The subsequent native run correctly failed on inactive recovery records: contrary
to the fixture comment, Set(automatic=false,activate=true) clears ActiveThreads.
Architect source confirmation and existing recovery tests establish Set(true,true)
as normal exact-socket active headless execution. Public UI cached idle is not
admission authority. The final fixture uses normal active records, exact epoch/
root assertions, and an actual portal-worker receipt steering the exact held
native turn. Its explicit test-only unsupported host-command dispatcher records
actual exit64 and complete sidecar preservation. No real terminal is required by
this Native.Ready/observer contract. Original report assumptions stay verbatim
with this correction recorded, rather than relabeling old evidence as passed.

Lead directly inspected the tagged-only +88/-25 repair. It adds prerequisites,
short diagnostics and stricter receipt/effect assertions; it does not weaken
admission or change production/API/design. Exact short proof3.724s, compile0.051s,
real-command0.457s. Narrow-fix rule applies without another review. Original
production C and A are unchanged; final history has three coherent commits and
no obsolete fixture/fixup, migration or repeated update stream.

Final head4155d0099d03028b43d5f08d225a88156cb4155a; fixup8eeeb163 and final
trees equal9b80c67e2f800c3354776404711c458b02c0881e. Full native production
worker exchange PASSED both idle/steer on final head (Go12.043s/wall17.9s).
See verification/native-final-result.md and implementation-b.md. Exact remote
feature head was verified after SSH publication. CI/full packaged result remains
separate in state.md; no integration/deployment approval is implied.

```text
1:  ed16c606 = 1:  ed16c606 communication: attach verified grant context to deliveries
2:  99da3951 ! 2:  b0279514 communication: clarify bidirectional runtime authorization
    @@ portal/cmd/workspace-portal/session_communication_native_integration_test.go (ne
     +			}
     +			mu.Unlock()
     +		}
    -+		if messageID == firstID && authorized && !toolOutput {
    ++		if messageID == firstID && authorized && !toolOutput && mode != "startup" {
     +			arguments, _ := json.Marshal(communication.Request{Action: "reply", Peer: "session-a", MessageID: replyID, ReplyTo: firstID, Message: replyText})
     +			item := map[string]any{"type": "function_call", "id": responseID + "-tool", "call_id": responseID + "-call",
     +				"namespace": "mcp__team_reporting", "name": "session_communication", "arguments": string(arguments)}
    @@ portal/cmd/workspace-portal/session_communication_native_integration_test.go (ne
     +		_ = syscall.Kill(-daemon.Process.Pid, syscall.SIGTERM)
     +		_ = daemon.Wait()
     +	}()
    ++	var latestEvidence string
     +	wait := func(description string, check func() bool) {
     +		t.Helper()
    ++		deadline := time.Now().Add(10 * time.Second)
     +		for !check() {
     +			mu.Lock()
     +			problem := strings.Join(failures, "; ")
    @@ portal/cmd/workspace-portal/session_communication_native_integration_test.go (ne
     +			if problem != "" {
     +				t.Fatal(problem)
     +			}
    -+			if ctx.Err() != nil {
    ++			if ctx.Err() != nil || time.Now().After(deadline) {
     +				body, _ := os.ReadFile(log.Name())
     +				if len(body) > 4000 {
     +					body = body[len(body)-4000:]
     +				}
    -+				t.Fatalf("%s: %v; native log tail: %s", description, ctx.Err(), body)
    ++				t.Fatalf("%s prerequisite/delivery wait: context=%v latest=%s; native log tail: %s", description, ctx.Err(), latestEvidence, body)
     +			}
     +			time.Sleep(20 * time.Millisecond)
     +		}
    @@ portal/cmd/workspace-portal/session_communication_native_integration_test.go (ne
     +		if err := os.WriteFile(filepath.Join(dir, "portal.yml"), []byte(manifest), 0600); err != nil {
     +			t.Fatal(err)
     +		}
    -+		// Keep execution active while disabling unrelated automatic restoration
    -+		// of this fixture's intentionally absent terminal/tmux runtime.
    -+		if err := (session.RecoveryStore{Root: f.state, Workspace: f.root}).Set(ctx, slug, thread, f.socket, false, true); err != nil {
    ++		// Automatic recovery permission is part of normal active execution;
    ++		// disabling it also clears ActiveThreads, even with activate=true.
    ++		if err := (session.RecoveryStore{Root: f.state, Workspace: f.root}).Set(ctx, slug, thread, f.socket, true, true); err != nil {
     +			t.Fatal(err)
     +		}
     +		// Fresh thread/start has no rollout for managed resume yet. Materialize
    @@ portal/cmd/workspace-portal/session_communication_native_integration_test.go (ne
     +		t.Fatal(err)
     +	}
     +	registry := communication.Service{Store: registryStore} // read-only status inspection
    ++	recoveryBefore := make(map[string][]byte)
    ++	for _, id := range identities {
    ++		record, err := (session.RecoveryStore{Root: f.state, Workspace: f.root}).Load(id.Slug)
    ++		if err != nil {
    ++			t.Fatal(err)
    ++		}
    ++		recoveryBefore[id.Slug], _ = json.Marshal(record)
    ++	}
     +	t.Setenv("DEV_WORKSPACES_CODEX_PROVIDERS", filepath.Join(f.root, "absent-providers.json"))
     +	t.Setenv("DEV_WORKSPACE_NAME", "communication-fixture")
     +	t.Setenv("DEV_WORKSPACE_CODEX_HOME", home)
    @@ portal/cmd/workspace-portal/session_communication_native_integration_test.go (ne
     +	if err := os.Symlink(packageRoot, f.profile); err != nil {
     +		t.Fatal(err)
     +	}
    ++	commandTrace := filepath.Join(f.root, "host-command-trace")
    ++	dispatcher := filepath.Join(f.profile, "bin/dev-session")
    ++	script, err := os.ReadFile(dispatcher)
    ++	if err != nil {
    ++		t.Fatal(err)
    ++	}
    ++	tracePath := "'" + strings.ReplaceAll(commandTrace, "'", "'\\''") + "'"
    ++	traceLine := "printf '%s\\n' \"$*\" >> " + tracePath + "\n" +
    ++		"if [ \"$1\" != communication ]; then\n" +
    ++		"  printf 'exit=64 unsupported=%s\\n' \"$*\" >> " + tracePath + "\n" +
    ++		"  printf '%s\\n' 'fixture explicitly refuses unsupported host command' >&2\n  exit 64\nfi\n"
    ++	if err := os.WriteFile(dispatcher, []byte(strings.Replace(string(script), "#!/bin/sh\n", "#!/bin/sh\n"+traceLine, 1)), 0700); err != nil {
    ++		t.Fatal(err)
    ++	}
     +	history := codex.NewHistoryPool(f.socket)
     +	defer history.Close()
     +	client := newCodexClientWithHistory(f.socket, f.root, history, f.state)
    @@ portal/cmd/workspace-portal/session_communication_native_integration_test.go (ne
     +		t.Fatal(err)
     +	}
     +	defer func() { releaseOnce.Do(func() { close(release) }); application.Close() }()
    -+	if mode == "startup" {
    -+		out := httptest.NewRecorder()
    -+		application.Handler().ServeHTTP(out, httptest.NewRequest(http.MethodGet, "/healthz", nil))
    -+		if out.Code != http.StatusOK {
    -+			t.Fatalf("production constructor health: %d", out.Code)
    ++	epoch, err := session.SocketIdentity(f.socket)
    ++	if err != nil {
    ++		t.Fatal(err)
    ++	}
    ++	for _, id := range identities {
    ++		record, err := (session.RecoveryStore{Root: f.state, Workspace: f.root}).Load(id.Slug)
    ++		if err != nil || !record.Automatic || record.ThreadID != id.Thread || record.SocketPath != f.socket ||
    ++			record.SocketIdentity != epoch || !record.Active(id.Thread, epoch) {
    ++			t.Fatalf("recipient recovery prerequisite: slug=%s automatic=%v root=%s socket=%s epoch=%s active=%v error=%v",
    ++				id.Slug, record.Automatic, record.ThreadID, record.SocketPath, record.SocketIdentity, record.Active(id.Thread, epoch), err)
     +		}
    -+		return
    ++	}
    ++	pending, err := registry.Pending(ctx)
    ++	if err != nil || len(pending) != 0 {
    ++		t.Fatalf("unexpected worker pending traffic: %d error=%v", len(pending), err)
    ++	}
    ++	if mode == "startup" {
    ++		defer func() {
    ++			trace, traceErr := os.ReadFile(commandTrace)
    ++			for _, id := range identities {
    ++				record, err := (session.RecoveryStore{Root: f.state, Workspace: f.root}).Load(id.Slug)
    ++				encoded, _ := json.Marshal(record)
    ++				if err != nil || !bytes.Equal(recoveryBefore[id.Slug], encoded) {
    ++					t.Errorf("automatic loop changed sidecar: slug=%s error=%v record=%s", id.Slug, err, encoded)
    ++				}
    ++				out := httptest.NewRecorder()
    ++				application.Handler().ServeHTTP(out, httptest.NewRequest(http.MethodGet, "/api/sessions/"+id.Slug+"/recovery", nil).WithContext(ctx))
    ++				t.Logf("recovery result slug=%s status=%d body=%s", id.Slug, out.Code, strings.TrimSpace(out.Body.String()))
    ++				if strings.Contains(string(trace), "resume "+id.Slug+" --as-is\n") &&
    ++					(!strings.Contains(string(trace), "exit=64 unsupported=resume "+id.Slug+" --as-is\n") ||
    ++						!strings.Contains(out.Body.String(), "fixture explicitly refuses unsupported host command")) {
    ++					t.Errorf("unsupported automatic helper call lacks verified refusal outcome")
    ++				}
    ++			}
    ++			t.Logf("actual fixture host commands=%q readError=%v; complete recovery sidecars preserved", trace, traceErr)
    ++		}()
     +	}
     +	call := func(thread string, request communication.Request) communication.View {
     +		t.Helper()
    @@ portal/cmd/workspace-portal/session_communication_native_integration_test.go (ne
     +	mu.Lock()
     +	expectedGrant = grant
     +	mu.Unlock()
    -+	if mode == "steer" {
    ++	var heldTurn string
    ++	if mode == "steer" || mode == "startup" {
     +		heldReceipt, err := client.SendWithOptions(ctx, b.Thread, "hold-communication-fixture", "held-turn", "fixture", codex.TurnOptions{})
     +		if err != nil {
     +			t.Fatal(err)
     +		}
    ++		heldTurn = heldReceipt.TurnID
     +		select {
     +		case <-held:
     +		case <-ctx.Done():
     +			t.Fatal("active provider did not enter")
     +		}
    -+		// The public read uses the actual portal-owned background observer;
    -+		// the operational client remains recorder-free and never subscribes.
    -+		wait("production active observation", func() bool {
    -+			out := httptest.NewRecorder()
    -+			application.Handler().ServeHTTP(out, httptest.NewRequest(http.MethodGet, "/codex/conversations/"+b.Slug+"/activity", nil).WithContext(ctx))
    -+			var activity codex.ActivitySnapshot
    -+			return out.Code == http.StatusOK && json.Unmarshal(out.Body.Bytes(), &activity) == nil &&
    -+				activity.CurrentState == "working" && activity.CurrentTurnID == heldReceipt.TurnID
    -+		})
    ++		// Public activity is diagnostic only: its display cache is not admission
    ++		// authority. The real worker's fresh observer read must accept the steer.
    ++		out := httptest.NewRecorder()
    ++		application.Handler().ServeHTTP(out, httptest.NewRequest(http.MethodGet, "/codex/conversations/"+b.Slug+"/activity", nil).WithContext(ctx))
    ++		latestEvidence = fmt.Sprintf("held native turn=%s public activity status=%d body=%s", heldReceipt.TurnID, out.Code, strings.TrimSpace(out.Body.String()))
    ++		if mode == "startup" {
    ++			t.Log(latestEvidence)
    ++		}
    ++
     +	}
     +	call(a.Thread, communication.Request{Action: "send", Peer: b.Slug, MessageID: firstID, Message: peerText})
     +	var delivered communication.Message
     +	wait("production worker first delivery", func() bool {
     +		view, err := registry.Read(ctx, b)
     +		if err != nil {
    -+			t.Fatal(err)
    ++			latestEvidence = "registry read: " + err.Error()
    ++			return false
     +		}
     +		for _, message := range view.Messages {
     +			if message.ID == firstID {
    ++				latestEvidence = fmt.Sprintf("registry message status=%s detail=%q nativeReceipt=%v", message.Status, message.Detail, message.Receipt != nil)
     +				if message.Status == "canceled" {
     +					t.Fatalf("worker canceled delivery: %s", message.Detail)
     +				}
    @@ portal/cmd/workspace-portal/session_communication_native_integration_test.go (ne
     +		return false
     +	})
     +	if delivered.Receipt == nil || delivered.Receipt.ClientUserMessageID != firstID ||
    -+		delivered.Receipt.Steered != (mode == "steer") {
    ++		delivered.Receipt.Steered != (mode != "idle") || heldTurn != "" && delivered.Receipt.TurnID != heldTurn {
     +		t.Fatalf("wrong production native delivery receipt: %+v", delivered.Receipt)
     +	}
    ++	if mode == "startup" {
    ++		t.Logf("actual worker active receipt: thread=%s turn=%s clientMessage=%s steered=%v; pending was empty before admission",
    ++			b.Thread, delivered.Receipt.TurnID, delivered.Receipt.ClientUserMessageID, delivered.Receipt.Steered)
    ++		return
    ++	}
     +	releaseOnce.Do(func() { close(release) })
     +	wait("production worker reverse reply", func() bool {
     +		view, err := registry.Read(ctx, a)
     +		if err != nil {
    -+			t.Fatal(err)
    ++			latestEvidence = "reverse registry read: " + err.Error()
    ++			return false
     +		}
     +		for _, message := range view.Messages {
     +			if message.ID == replyID && message.ReplyTo == firstID && message.From == b && message.To == a &&
3:  a6c0e10f = 3:  4155d009 communication: use fresh observer activity for delivery admission
```

## Final readiness checkpoint

CI40975812804 completed successfully on exact4155d009 at2026-10-30T00:08:21Z
(17m52s): fast/package, archive and creation passed; host skipped. Complete
workspacecodex and Ruby shard coverage are confirmed by retained compact CI
result and inspected fast logs, closing the partial45s local-suite obligation.
Final fresh origin fetch still08f3dbb9; exact SSH feature head4155d009 and clean
source/tree9b80c67e2f800c3354776404711c458b02c0881e verified. Portal comparison
captured. All local monitoring processes have exited. No merge, deployment or
session lifecycle action; initiative remains active awaiting explicit approval.
