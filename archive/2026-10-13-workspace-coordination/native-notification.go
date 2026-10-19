// Operational acceptance fixture: private native server and synthetic provider.
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net"
	"net/http"
	"net/http/httptest"
	"os"
	"os/exec"
	"path/filepath"
	"strconv"
	"strings"
	"sync"
	"sync/atomic"
	"syscall"
	"time"

	"github.com/aither64/codex-web/codex"
	"github.com/coder/websocket"
)

func require(err error) {
	if err != nil {
		panic(err)
	}
}
func main() {
	packageRoot := os.Args[1]
	root, err := os.MkdirTemp("/tmp", "coord-native-")
	require(err)
	defer os.RemoveAll(root)
	home, workspace, state := filepath.Join(root, "home"), filepath.Join(root, "workspace"), filepath.Join(root, "state")
	slug := "2026-10-13-native-fixture"
	cwd := filepath.Join(workspace, "work", slug)
	for _, p := range []string{home, cwd, state} {
		require(os.MkdirAll(p, 0700))
	}
	ctx, cancel := context.WithTimeout(context.Background(), 150*time.Second)
	defer cancel()
	hold := make(chan struct{})
	var release sync.Once
	var hits atomic.Int64
	provider := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path != "/v1/responses" {
			w.WriteHeader(404)
			return
		}
		index := hits.Add(1)
		select {
		case <-hold:
		case <-r.Context().Done():
			return
		}
		w.Header().Set("Content-Type", "text/event-stream")
		event := func(v any) { b, _ := json.Marshal(v); fmt.Fprintf(w, "data: %s\n\n", b) }
		id := fmt.Sprintf("fixture-%d", index)
		event(map[string]any{"type": "response.created", "response": map[string]any{"id": id}})
		event(map[string]any{"type": "response.output_item.done", "item": map[string]any{"type": "message", "role": "assistant", "id": "answer-" + id, "phase": "final_answer", "content": []any{map[string]any{"type": "output_text", "text": "Fixture complete."}}}})
		event(map[string]any{"type": "response.completed", "response": map[string]any{"id": id, "usage": map[string]any{"input_tokens": 1, "output_tokens": 1, "total_tokens": 2}}})
	}))
	defer func() {
		release.Do(func() { close(hold) })
		provider.Close()
	}()
	config := "model_provider = \"fixture\"\nmodel = \"gpt-6.1-sol\"\nmodel_reasoning_effort = \"low\"\n[model_providers.fixture]\nname = \"Local fixture\"\nbase_url = " + strconv.Quote(provider.URL+"/v1") + "\nwire_api = \"responses\"\nrequires_openai_auth = false\n"
	require(os.WriteFile(filepath.Join(home, "config.toml"), []byte(config), 0600))
	nativeSocket, proxySocket := filepath.Join(root, "native.sock"), filepath.Join(root, "proxy.sock")
	log, err := os.Create(filepath.Join(root, "native.log"))
	require(err)
	defer log.Close()
	native := exec.CommandContext(ctx, filepath.Join(packageRoot, "libexec/codex/libexec/codex/bin/codex"), "app-server", "--strict-config", "--listen", "unix://"+nativeSocket)
	native.Dir = cwd
	native.Env = []string{"PATH=" + os.Getenv("PATH"), "HOME=" + home, "CODEX_HOME=" + home, "XDG_CONFIG_HOME=" + home, "XDG_STATE_HOME=" + home, "XDG_CACHE_HOME=" + home, "RUST_LOG=error"}
	native.Stdout, native.Stderr = log, log
	native.SysProcAttr = &syscall.SysProcAttr{Setpgid: true}
	require(native.Start())
	defer func() { syscall.Kill(-native.Process.Pid, syscall.SIGKILL); native.Wait() }()
	deadline := time.Now().Add(15 * time.Second)
	for {
		if _, err := os.Stat(nativeSocket); err == nil {
			break
		}
		if time.Now().After(deadline) {
			panic("native socket timeout")
		}
		time.Sleep(50 * time.Millisecond)
	}
	var mutations, dropped atomic.Int64
	proxy := &http.Server{Handler: http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		down, err := websocket.Accept(w, r, &websocket.AcceptOptions{InsecureSkipVerify: true})
		if err != nil {
			return
		}
		defer down.CloseNow()
		transport := &http.Transport{DialContext: func(ctx context.Context, network, address string) (net.Conn, error) {
			return (&net.Dialer{}).DialContext(ctx, "unix", nativeSocket)
		}}
		defer transport.CloseIdleConnections()
		up, _, err := websocket.Dial(ctx, "ws://localhost/", &websocket.DialOptions{HTTPClient: &http.Client{Transport: transport}})
		if err != nil {
			return
		}
		defer up.CloseNow()
		connectionCtx, stop := context.WithCancel(ctx)
		defer stop()
		var mutex sync.Mutex
		discard := map[string]bool{}
		go func() {
			defer stop()
			for {
				kind, b, err := down.Read(connectionCtx)
				if err != nil {
					return
				}
				var v map[string]json.RawMessage
				json.Unmarshal(b, &v)
				var method string
				json.Unmarshal(v["method"], &method)
				if method == "turn/start" || method == "turn/steer" {
					mutations.Add(1)
					mutex.Lock()
					discard[string(v["id"])] = true
					mutex.Unlock()
				}
				if up.Write(connectionCtx, kind, b) != nil {
					return
				}
			}
		}()
		for {
			kind, b, err := up.Read(connectionCtx)
			if err != nil {
				return
			}
			var v map[string]json.RawMessage
			json.Unmarshal(b, &v)
			mutex.Lock()
			skip := discard[string(v["id"])]
			if skip {
				delete(discard, string(v["id"]))
			}
			mutex.Unlock()
			if skip {
				dropped.Add(1)
				continue
			}
			if down.Write(connectionCtx, kind, b) != nil {
				return
			}
		}
	})}
	listener, err := net.Listen("unix", proxySocket)
	require(err)
	defer listener.Close()
	go proxy.Serve(listener)
	defer proxy.Close()
	client := codex.NewWithOptions(proxySocket, codex.ClientOptions{ThreadSourceKinds: []string{"vscode"}, SubmissionLedgerPath: filepath.Join(root, "fixture-client-ledger.json")})
	defer client.Close()
	project, err := client.CreateProject(ctx, "Notification fixture", "notification-fixture")
	require(err)
	thread, err := client.StartThreadWithSettings(ctx, cwd, map[string]string{"DEV_SESSION_SLUG": slug, "DEV_SESSION_WORKSPACE": workspace}, codex.ThreadSettings{ProjectID: project.ID, Model: "gpt-6.1-sol", ReasoningEffort: "low"})
	require(err)
	require(client.BootstrapHeadlessThread(ctx, thread, cwd, project.ID, "Private notification fixture "+thread+"."))
	for name, data := range map[string]string{"portal.yml": fmt.Sprintf("schema: 1\nslug: %s\nrepositories: []\nartifacts: []\ncodex:\n  thread_id: %s\n  socket_path: %s\n  client_version: 0.160.0\n", slug, thread, proxySocket), "state.md": "---\nlifecycle: active\n---\n", "plan.md": "Private notification acceptance fixture.\n"} {
		require(os.WriteFile(filepath.Join(cwd, name), []byte(data), 0600))
	}
	request := map[string]any{"schema": 1, "action": "prepare", "workspace": workspace, "slug": slug, "socket": proxySocket, "thread": thread, "stateRoot": state}
	call := func() ([]byte, error) {
		b, _ := json.Marshal(request)
		path := filepath.Join(root, "request.json")
		require(os.WriteFile(path, b, 0600))
		cmd := exec.CommandContext(ctx, filepath.Join(packageRoot, "bin/workspace-portal"), "coordination-notify", "--request", path)
		cmd.Env = append(native.Env, "DEV_WORKSPACE_CODEX_HOME="+home)
		return cmd.CombinedOutput()
	}
	b, err := call()
	if err != nil {
		panic(fmt.Sprintf("prepare: %s: %v", b, err))
	}
	var prepared map[string]any
	require(json.Unmarshal(b, &prepared))
	request["action"], request["options"] = "send", prepared["options"]
	for index, message := range []string{"idle-notification", "busy-notification"} {
		request["text"], request["messageId"], request["actionContext"] = message, message, "fixture:"+message
		b, err = call()
		fmt.Printf("lost reply %d: error=%v output=%s\n", index, err, b)
		if index == 1 {
			// Native steering is queued while the first provider request is
			// active; release it so accepted input reaches durable history.
			release.Do(func() { close(hold) })
		}
		reconcileDeadline := time.Now().Add(15 * time.Second)
		for {
			b, err = call()
			if err == nil || time.Now().After(reconcileDeadline) {
				break
			}
			time.Sleep(100 * time.Millisecond)
		}
		if err != nil {
			fmt.Printf("reconcile failed %d: %s: %v\n", index, b, err)
			panic(fmt.Sprintf("reconcile %d: %s: %v", index, b, err))
		}
		fmt.Printf("reconciled %d: %s\n", index, b)
		var received struct {
			Receipt struct {
				Steered bool `json:"steered"`
			} `json:"receipt"`
		}
		require(json.Unmarshal(b, &received))
		if received.Receipt.Steered != (index == 1) {
			panic("incorrect idle/busy receipt")
		}
		if mutations.Load() != int64(index+1) {
			panic("retry issued duplicate native mutation")
		}
	}
	if dropped.Load() != 2 || hits.Load() < 1 {
		panic("native lost-response fixture did not execute")
	}
	release.Do(func() { close(hold) })
	var history map[string]any
	require(client.Request(ctx, "thread/read", map[string]any{"threadId": thread, "includeTurns": true}, &history))
	b, _ = json.Marshal(history)
	for _, message := range []string{"idle-notification", "busy-notification"} {
		if textCount(history, message) != 1 {
			panic("native message count differs")
		}
	}
	var threads struct {
		Data []struct {
			ID string `json:"id"`
		} `json:"data"`
	}
	require(client.Request(ctx, "thread/list", map[string]any{"limit": 100}, &threads))
	if len(threads.Data) != 1 || threads.Data[0].ID != thread {
		panic("replacement conversation created")
	}
	fmt.Printf("PASS: selected native Codex, idle start, busy steer, two lost replies, exact retries, one conversation; mutations=%d\n", mutations.Load())
}

func textCount(value any, needle string) int {
	n := 0
	switch v := value.(type) {
	case map[string]any:
		for key, child := range v {
			if key == "text" {
				if text, ok := child.(string); ok && strings.Contains(text, needle) {
					n++
				}
			} else {
				n += textCount(child, needle)
			}
		}
	case []any:
		for _, child := range v {
			n += textCount(child, needle)
		}
	}
	return n
}
