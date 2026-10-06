// Disposable rollout probe: no credentials, real threads, or model turns.
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"syscall"
	"time"

	"github.com/aither64/codex-web/codex"
)

const fixture = "Synthetic Codex package upgrade fixture; no model turn."
const queued = "Synthetic queued package fixture; do not execute."

func must(err error) {
	if err != nil {
		panic(err)
	}
}

func request(client *codex.Client, method string, params any) map[string]any {
	ctx, cancel := context.WithTimeout(context.Background(), 20*time.Second)
	defer cancel()
	var result map[string]any
	if err := client.Request(ctx, method, params, &result); err != nil {
		panic(fmt.Errorf("%s: %w", method, err))
	}
	return result
}

func thread(result map[string]any) map[string]any {
	value, ok := result["thread"].(map[string]any)
	if !ok || value["id"] == nil {
		panic("response missing thread identity")
	}
	return value
}

func inject(client *codex.Client, id, text string) {
	request(client, "thread/inject_items", map[string]any{
		"threadId": id,
		"items": []any{map[string]any{
			"type": "message", "role": "developer",
			"content": []any{map[string]any{"type": "input_text", "text": text}},
		}},
	})
}

func inspect(client *codex.Client, id, effort string) {
	request(client, "thread/resume", map[string]any{"threadId": id, "excludeTurns": true})
	metadata := thread(request(client, "thread/read", map[string]any{"threadId": id, "excludeTurns": true}))
	if metadata["model"] != "gpt-6.1-sol" || metadata["reasoningEffort"] != effort {
		panic(fmt.Sprintf("thread %s: settings mismatch: model=%v effort=%v; expected gpt-6.1-sol/%s", id, metadata["model"], metadata["reasoningEffort"], effort))
	}
	path, ok := metadata["path"].(string)
	if !ok || !filepath.IsAbs(path) {
		panic("missing persisted rollout path")
	}
	content, err := os.ReadFile(path)
	must(err)
	if !strings.Contains(string(content), fixture) {
		panic("synthetic rollout content was not preserved")
	}
}

func inspectQueue(client *codex.Client, id string) {
	// Never resume this dedicated thread: a loaded idle thread auto-dispatches.
	data := request(client, "thread/queue/list", map[string]any{"threadId": id, "limit": 100})
	encoded, err := json.Marshal(data)
	must(err)
	if !strings.Contains(string(encoded), queued) {
		panic("synthetic queue content was not preserved")
	}
}

func runServer(binary, root, label, expected string, body func(*codex.Client)) {
	socket := filepath.Join(root, label+".sock")
	log, err := os.Create(filepath.Join(root, label+".log"))
	must(err)
	defer log.Close()
	cmd := exec.Command(binary, "app-server", "--listen", "unix://"+socket)
	cmd.Env = append(os.Environ(), "CODEX_HOME="+filepath.Join(root, "home"), "CODEX_SQLITE_HOME="+filepath.Join(root, "home"), "OPENAI_API_KEY=", "CODEX_API_KEY=")
	cmd.Stdout, cmd.Stderr = log, log
	cmd.SysProcAttr = &syscall.SysProcAttr{Setpgid: true}
	must(cmd.Start())
	defer func() {
		_ = syscall.Kill(-cmd.Process.Pid, syscall.SIGTERM)
		_ = cmd.Wait()
	}()
	deadline := time.Now().Add(20 * time.Second)
	for {
		info, err := os.Stat(socket)
		if err == nil && info.Mode()&os.ModeSocket != 0 {
			break
		}
		if time.Now().After(deadline) {
			panic("isolated server socket did not become ready; see " + label + ".log")
		}
		time.Sleep(50 * time.Millisecond)
	}
	client := codex.New(socket)
	defer client.Close()
	actual, err := os.Readlink(fmt.Sprintf("/proc/%d/exe", cmd.Process.Pid))
	must(err)
	identity := exec.Command(actual, "--version")
	identity.Env = cmd.Env
	identity.Stderr = log
	version, err := identity.Output()
	must(err)
	if strings.TrimSpace(string(version)) != "codex-cli "+expected {
		panic(fmt.Sprintf("%s: running executable version %q, expected %s", label, version, expected))
	}
	fmt.Printf("%s server executable: %s (%s)\n", label, actual, strings.TrimSpace(string(version)))
	ctx, cancel := context.WithTimeout(context.Background(), 20*time.Second)
	defer cancel()
	must(client.Ensure(ctx))
	body(client)
}

func main() {
	if len(os.Args) != 3 {
		panic("usage: compat_probe OLD_CODEX NEW_CODEX")
	}
	root, err := os.MkdirTemp("", "codex-package-state-")
	must(err)
	must(os.Mkdir(filepath.Join(root, "home"), 0700))
	fmt.Println("private probe artifacts:", root)
	for index, binary := range os.Args[1:] {
		identity := exec.Command(binary, "--version")
		identity.Stderr = os.Stderr
		version, err := identity.Output()
		must(err)
		expected := []string{"0.159.2", "0.160.0"}[index]
		if strings.TrimSpace(string(version)) != "codex-cli "+expected {
			panic(fmt.Sprintf("reader version %q, expected %s", version, expected))
		}
		fmt.Printf("reader: %s\n", strings.TrimSpace(string(version)))
	}
	var id, forkID, queueID string
	runServer(os.Args[1], root, "old-create", "0.159.2", func(client *codex.Client) {
		created := thread(request(client, "thread/start", map[string]any{
			"cwd": root, "model": "gpt-6.1-sol",
			"config": map[string]any{"model_reasoning_effort": "high"},
		}))
		id = created["id"].(string)
		inject(client, id, fixture)
		request(client, "thread/name/set", map[string]any{"threadId": id, "name": "Synthetic package upgrade"})
		inspect(client, id, "high")
		queueThread := thread(request(client, "thread/start", map[string]any{"cwd": root, "model": "gpt-6.1-sol"}))
		queueID = queueThread["id"].(string)
		inject(client, queueID, fixture)
	})
	// Restart the old server so the queue fixture is persisted but unloaded.
	// Queue add/list use the thread store without loading it; no turn is started.
	runServer(os.Args[1], root, "old-enqueue", "0.159.2", func(client *codex.Client) {
		inspect(client, id, "high")
		request(client, "thread/queue/add", map[string]any{
			"threadId":            queueID,
			"clientUserMessageId": "00000000-0000-4000-8000-000000000045",
			"input":               []any{map[string]any{"type": "text", "text": queued}},
		})
		inspectQueue(client, queueID)
	})
	fmt.Println("old reader: persisted thread, settings and queue created")
	runServer(os.Args[2], root, "new-load", "0.160.0", func(client *codex.Client) {
		inspectQueue(client, queueID)
		inspect(client, id, "high")
		request(client, "thread/settings/update", map[string]any{"threadId": id, "effort": "medium"})
		inspect(client, id, "medium")
		forked := thread(request(client, "thread/fork", map[string]any{
			"threadId": id, "cwd": root, "model": "gpt-6.1-sol",
			"config": map[string]any{"model_reasoning_effort": "medium"},
		}))
		forkID = forked["id"].(string)
		fmt.Println("new reader: validating explicit medium fork settings")
		inject(client, forkID, fixture)
		inspect(client, forkID, "medium")
		inspectQueue(client, queueID)
	})
	fmt.Println("new reader: old state preserved; settings changed and fork persisted")
	runServer(os.Args[1], root, "old-reload", "0.159.2", func(client *codex.Client) {
		inspect(client, id, "medium")
		inspect(client, forkID, "medium")
		inspectQueue(client, queueID)
	})
	fmt.Println("old reader: new settings, fork and original queue loaded")
	check := exec.Command("python3", "-c", `import pathlib, sqlite3, sys
paths = list(pathlib.Path(sys.argv[1]).glob('*.sqlite'))
assert paths, 'no persistent SQLite stores'
for path in paths:
    db = sqlite3.connect('file:' + str(path) + '?mode=ro', uri=True)
    assert db.execute('PRAGMA integrity_check').fetchall() == [('ok',)], path.name
    db.close()
print('SQLite integrity: passed for', len(paths), 'stores')
rollouts = list(pathlib.Path(sys.argv[1]).glob('sessions/**/*.jsonl'))
assert rollouts, 'no persistent rollouts'
for path in rollouts:
    for line in path.read_text().splitlines():
        import json
        event = json.loads(line)
        assert not (event.get('type') == 'event_msg' and
                    event.get('payload', {}).get('type') == 'task_started'), 'unexpected model turn'
print('No model turns: verified in all synthetic rollouts')
`, filepath.Join(root, "home"))
	check.Stdout, check.Stderr = os.Stdout, os.Stderr
	must(check.Run())
	fmt.Println("PASS: disposable old -> new -> old state loading; no model turns")
}
