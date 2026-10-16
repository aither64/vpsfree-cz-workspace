// Isolated acceptance evidence; run from the runtime's portal Go module.
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/http/httptest"
	"os"
	"os/exec"
	"path/filepath"
	"strconv"
	"strings"
	"sync/atomic"
	"syscall"
	"time"

	"github.com/aither64/codex-web/codex"
)

func must(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {
	if len(os.Args) != 2 {
		panic("pass exact built runtime package")
	}
	pkg := os.Args[1]
	native := filepath.Join(pkg, "libexec/codex/bin/codex")
	versionOutput, err := exec.Command(native, "--version").Output()
	must(err)
	version := strings.TrimPrefix(strings.TrimSpace(string(versionOutput)), "codex-cli ")
	root, err := os.MkdirTemp("", "idle-coordination-native-")
	must(err)
	defer os.RemoveAll(root)
	home, state := filepath.Join(root, "codex"), filepath.Join(root, "state")
	must(os.MkdirAll(home, 0700))
	must(os.MkdirAll(state, 0700))
	var calls atomic.Int32
	backend := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			w.WriteHeader(404)
			return
		}
		_, _ = io.Copy(io.Discard, r.Body)
		id := fmt.Sprintf("fixture-%d", calls.Add(1))
		w.Header().Set("Content-Type", "text/event-stream")
		event := func(v any) { data, _ := json.Marshal(v); _, _ = fmt.Fprintf(w, "data: %s\n\n", data) }
		event(map[string]any{"type": "response.created", "response": map[string]any{"id": id}})
		event(map[string]any{"type": "response.output_item.done", "item": map[string]any{"type": "message", "role": "assistant", "id": id + "-answer", "phase": "final_answer", "content": []any{map[string]any{"type": "output_text", "text": "native-fixture-complete"}}}})
		event(map[string]any{"type": "response.completed", "response": map[string]any{"id": id, "usage": map[string]any{"input_tokens": 0, "output_tokens": 0, "total_tokens": 0}}})
	}))
	defer backend.Close()
	config := "model_provider = \"fixture\"\nmodel = \"gpt-5.5\"\nmodel_reasoning_effort = \"high\"\napproval_policy = \"never\"\n[model_providers.fixture]\nname = \"Isolated fixture\"\nwire_api = \"responses\"\nsupports_websockets = false\nenv_key = \"OPENAI_API_KEY\"\nbase_url = " + strconv.Quote(backend.URL+"/v1") + "\n"
	must(os.WriteFile(filepath.Join(home, "config.toml"), []byte(config), 0600))
	// An allowlist prevents inherited real credentials, services or user config.
	env := []string{"HOME=" + root, "CODEX_HOME=" + home, "DEV_WORKSPACE_CODEX_HOME=" + home, "PATH=" + os.Getenv("PATH"), "OPENAI_API_KEY=synthetic-only"}
	socket := filepath.Join(root, "native.sock")
	log, err := os.Create(filepath.Join(root, "native.log"))
	must(err)
	defer log.Close()
	ctx, cancel := context.WithTimeout(context.Background(), 120*time.Second)
	defer cancel()
	var daemon *exec.Cmd
	stop := func() {
		if daemon != nil {
			_ = syscall.Kill(-daemon.Process.Pid, syscall.SIGTERM)
			_ = daemon.Wait()
			daemon = nil
		}
	}
	defer stop()
	start := func() *codex.Client {
		_ = os.Remove(socket)
		daemon = exec.CommandContext(ctx, native, "app-server", "--listen", "unix://"+socket)
		daemon.Env = env
		daemon.Dir = root
		daemon.Stdout = log
		daemon.Stderr = log
		daemon.SysProcAttr = &syscall.SysProcAttr{Setpgid: true}
		must(daemon.Start())
		for {
			if _, err := os.Stat(socket); err == nil {
				break
			}
			if ctx.Err() != nil {
				panic(ctx.Err())
			}
			time.Sleep(20 * time.Millisecond)
		}
		return codex.NewWithOptions(socket, codex.ClientOptions{PreserveThreadInstructionsOnResume: true})
	}
	client := start()
	defer func() { client.Close() }()
	threadCwds := map[string]string{}
	waitIdle := func(thread string, responses int32) {
		for {
			if calls.Load() >= responses && client.RequireThreadIdle(ctx, thread, threadCwds[thread]) == nil {
				return
			}
			if ctx.Err() != nil {
				data, _ := os.ReadFile(log.Name())
				panic(fmt.Sprintf("idle wait: %v %s", ctx.Err(), data))
			}
			time.Sleep(20 * time.Millisecond)
		}
	}
	type recipient struct {
		slug, thread string
		options      any
	}
	recipients := []recipient{}
	for i := 0; i < 2; i++ {
		slug := fmt.Sprintf("native-fixture-%d", i)
		cwd := filepath.Join(root, "work", slug)
		must(os.MkdirAll(cwd, 0700))
		var response struct {
			Thread struct {
				ID string `json:"id"`
			} `json:"thread"`
		}
		must(client.Request(ctx, "thread/start", map[string]any{"cwd": cwd, "model": "gpt-5.5", "permissions": ":workspace", "approvalPolicy": "never", "config": map[string]any{"model_reasoning_effort": "high"}}, &response))
		thread := response.Thread.ID
		threadCwds[thread] = cwd
		var turn map[string]any
		must(client.Request(ctx, "turn/start", map[string]any{"threadId": thread, "input": []any{map[string]any{"type": "text", "text": "materialize isolated fixture"}}, "model": "gpt-5.5", "effort": "high"}, &turn))
		waitIdle(thread, int32(i+1))
		manifest := fmt.Sprintf("schema: 1\nslug: %s\nrepositories: []\nartifacts: []\ncodex:\n  thread_id: %s\n  socket_path: %s\n  client_version: %s\n", slug, thread, socket, version)
		for name, content := range map[string]string{"portal.yml": manifest, "state.md": "---\nlifecycle: active\n---\n", "plan.md": "Isolated native acceptance fixture\n"} {
			must(os.WriteFile(filepath.Join(cwd, name), []byte(content), 0600))
		}
		recipients = append(recipients, recipient{slug: slug, thread: thread})
	}
	// Loaded and persisted idle threads must not issue model requests.
	before := calls.Load()
	time.Sleep(2 * time.Second)
	if calls.Load() != before {
		panic("idle threads issued provider requests")
	}
	call := func(r recipient, action string, options any) map[string]any {
		req := map[string]any{"schema": 1, "action": action, "workspace": root, "slug": r.slug, "socket": socket, "thread": r.thread, "stateRoot": state}
		if action == "send" {
			req["options"] = options
			req["text"] = "coordination completed: review isolated result"
			req["messageId"] = "fixture-event-" + r.slug
			req["actionContext"] = "coordination:fixture:" + r.slug
		}
		data, _ := json.Marshal(req)
		path := filepath.Join(root, "request.json")
		must(os.WriteFile(path, data, 0600))
		cmd := exec.CommandContext(ctx, filepath.Join(pkg, "bin/workspace-portal"), "coordination-notify", "--request", path)
		cmd.Env = env
		out, err := cmd.CombinedOutput()
		if err != nil {
			panic(fmt.Sprintf("%s: %v %s", action, err, out))
		}
		var result map[string]any
		must(json.Unmarshal(out, &result))
		return result
	}
	for i := range recipients {
		r := &recipients[i]
		r.options = call(*r, "prepare", nil)["options"]
		data, _ := json.Marshal(r.options)
		if !strings.Contains(string(data), "gpt-5.5") || !strings.Contains(string(data), "high") {
			panic("settings not retained")
		}
		call(*r, "send", r.options)
		waitIdle(r.thread, int32(3+i))
	}
	client.Close()
	stop()
	client = start()
	// New helper process and native-server restart reconcile the same identities.
	for _, r := range recipients {
		call(r, "send", r.options)
		transcript, err := client.ReadThread(ctx, r.thread)
		must(err)
		count := 0
		for _, entry := range transcript.Entries {
			if entry.Kind == "userMessage" && strings.Contains(entry.Text, "coordination completed") {
				count++
			}
		}
		if count != 1 {
			panic(fmt.Sprintf("expected one notice in %s, got %d: %+v", r.slug, count, transcript.Entries))
		}
		settings, err := client.ReadThreadSettings(ctx, r.thread)
		must(err)
		if settings.Model != "gpt-5.5" || settings.ReasoningEffort != "high" {
			panic(fmt.Sprintf("settings changed: %+v", settings))
		}
	}
	time.Sleep(time.Second)
	if calls.Load() != 4 {
		panic(fmt.Sprintf("duplicate provider requests: %d", calls.Load()))
	}
	fmt.Printf("PASS: package=%s native=%s; two idle threads, no idle provider requests, one native wakeup each, retained gpt-5.5/high, duplicate sends after native restart reconciled; provider requests=%d\n", pkg, native, calls.Load())
}
