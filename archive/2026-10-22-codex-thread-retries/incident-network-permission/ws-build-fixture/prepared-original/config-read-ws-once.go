// Prepared operational source only. Do not build or dispatch without lead release.
// Transport/initialization follows codex-web 5743f94c2fbd codex/client.go:966-1001
// and workspace-portal live_switch_integration_test.go:337-368. No thread client.
package main

import (
	"bytes"
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"net"
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
	"reflect"
	"strconv"
	"strings"
	"sync/atomic"
	"syscall"
	"time"

	"github.com/coder/websocket"
)

const (
	workspace    = "/home/aither/workspace/ai/vpsfree.cz"
	slug         = "2026-10-22-codex-thread-retries"
	devSession   = "/nix/store/1zkafvr6ns84wdmdh7qrmhx77c90wpxw-dev-workspace-0.2.0/bin/dev-session"
	systemctl    = "/nix/store/kmzlca218j6j1ar292fxj7707qzypij8-systemd-260.5/bin/systemctl"
	unit         = "workspace-codex@vpsfree-cz.service"
	claimID      = "201af6c8-08a2-48e6-be3e-b69ce916eee1"
	ownerID      = "7cbe38cb-30c7-452d-8015-3907552c550d"
	socketPath   = "/run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock"
	socketTarget = "/tmp/codex-daemon-1000/bced879de15a05f23836072b53ea2860aa13a982415f07bf83ab93a6ee8c9ea6"
	nativeExe    = "/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0/libexec/codex/bin/codex"
	invocation   = "84b92a0a1c5a4fffa9a0c7beaf0693f1"
	nativePID    = 3387667
)

type fileID struct {
	Device  uint64 `json:"device"`
	Inode   uint64 `json:"inode"`
	CTimeNs int64  `json:"ctimeNs"`
	UID     uint32 `json:"uid"`
}

type identity struct {
	Unit         string    `json:"unit"`
	PID          int       `json:"pid"`
	InvocationID string    `json:"invocationId"`
	StartTicks   uint64    `json:"startTicks"`
	Exe          string    `json:"exe"`
	UIDs         [4]uint32 `json:"uids"`
	GIDs         [4]uint32 `json:"gids"`
	Restarts     uint64    `json:"restarts"`
	Socket       string    `json:"socket"`
	SocketTarget string    `json:"socketTarget"`
	Link         fileID    `json:"linkIdentity"`
	Target       fileID    `json:"targetIdentity"`
	DevSession   string    `json:"devSession"`
	ClaimID      string    `json:"claimId"`
	ClaimOwnerID string    `json:"claimOwnerId"`
	ClaimState   string    `json:"claimState"`
	Resource     string    `json:"resource"`
}

var expected = identity{
	Unit: unit, PID: nativePID, InvocationID: invocation, StartTicks: 1162579375,
	Exe: nativeExe, UIDs: [4]uint32{1000, 1000, 1000, 1000}, GIDs: [4]uint32{100, 100, 100, 100},
	Socket: socketPath, SocketTarget: socketTarget,
	Link:       fileID{77, 121544, 1792318082724922848, 1000},
	Target:     fileID{64769, 18745722, 1792318082724922848, 1000},
	DevSession: devSession, ClaimID: claimID, ClaimOwnerID: ownerID,
	ClaimState: "held", Resource: "machine:vpsfree:aitherdev",
}

type peerID struct {
	PID int32  `json:"pid"`
	UID uint32 `json:"uid"`
	GID uint32 `json:"gid"`
}

type receipt struct {
	StartedAtUTC           string    `json:"startedAtUTC"`
	CompletedAtUTC         string    `json:"completedAtUTC"`
	Method                 string    `json:"method"`
	Before                 *identity `json:"before,omitempty"`
	BeforeRequest          *identity `json:"beforeRequest,omitempty"`
	PeerBefore             *peerID   `json:"peerBefore,omitempty"`
	PeerAfter              *peerID   `json:"peerAfter,omitempty"`
	After                  *identity `json:"after,omitempty"`
	Success                bool      `json:"success"`
	ErrorCategory          string    `json:"errorCategory,omitempty"`
	PostcheckErrorCategory string    `json:"postcheckErrorCategory,omitempty"`
}

// All returned errors are constant categories. Never retain subprocess stderr,
// WebSocket errors, remote RPC messages, HTTP response bodies or config fields.
func category(s string) error { return errors.New(s) }

func command(ctx context.Context, path string, args ...string) ([]byte, error) {
	short, cancel := context.WithTimeout(ctx, 1500*time.Millisecond)
	defer cancel()
	c := exec.CommandContext(short, path, args...)
	c.Dir = workspace
	c.Stderr = io.Discard
	c.WaitDelay = 100 * time.Millisecond
	b, err := c.Output()
	if err != nil {
		clear(b)
		return nil, category("metadata_command_unavailable")
	}
	return b, nil
}

func fileIdentity(p string, link bool) (fileID, os.FileMode, error) {
	var info os.FileInfo
	var err error
	if link {
		info, err = os.Lstat(p)
	} else {
		info, err = os.Stat(p)
	}
	if err != nil {
		return fileID{}, 0, category("socket_metadata_unavailable")
	}
	s, ok := info.Sys().(*syscall.Stat_t)
	if !ok {
		return fileID{}, 0, category("socket_metadata_unavailable")
	}
	return fileID{uint64(s.Dev), s.Ino, s.Ctim.Sec*1e9 + s.Ctim.Nsec, s.Uid}, info.Mode(), nil
}

func snapshot(ctx context.Context) (*identity, error) {
	a, b := os.Getenv("DEV_SESSION_SLUG"), os.Getenv("DEV_SESSION_WORKSPACE")
	if (a != "" || b != "") && (a != slug || b != workspace) {
		return nil, category("binding_mismatch")
	}
	selected, err := filepath.EvalSymlinks("/home/aither/bin/dev-session")
	if err != nil || selected != devSession {
		return nil, category("selected_helper_changed")
	}
	current, err := command(ctx, devSession, "current")
	if err != nil {
		return nil, err
	}
	bound := strings.TrimSpace(string(current)) == slug
	clear(current)
	if !bound {
		return nil, category("binding_mismatch")
	}
	raw, err := command(ctx, devSession, "coordination", "claim-status", slug, "--as-is", "--id", claimID, "--json")
	if err != nil {
		return nil, err
	}
	var claim struct {
		ID        string   `json:"id"`
		OwnerID   string   `json:"ownerId"`
		State     string   `json:"state"`
		Resources []string `json:"resources"`
	}
	err = json.Unmarshal(raw, &claim)
	clear(raw)
	if err != nil || claim.ID != claimID || claim.OwnerID != ownerID || claim.State != "held" ||
		len(claim.Resources) != 1 || claim.Resources[0] != expected.Resource {
		return nil, category("machine_claim_mismatch")
	}
	raw, err = command(ctx, systemctl, "--user", "show", unit, "--property=MainPID", "--property=InvocationID", "--property=NRestarts", "--property=ActiveState", "--property=SubState")
	if err != nil {
		return nil, err
	}
	props := map[string]string{}
	for _, line := range strings.Split(string(raw), "\n") {
		k, v, ok := strings.Cut(line, "=")
		if ok {
			props[k] = v
		}
	}
	clear(raw)
	if props["MainPID"] != strconv.Itoa(nativePID) || props["InvocationID"] != invocation ||
		props["NRestarts"] != "0" || props["ActiveState"] != "active" || props["SubState"] != "running" {
		return nil, category("native_identity_mismatch")
	}
	exe, err := os.Readlink(fmt.Sprintf("/proc/%d/exe", nativePID))
	if err != nil || exe != nativeExe {
		return nil, category("native_identity_mismatch")
	}
	raw, err = os.ReadFile(fmt.Sprintf("/proc/%d/stat", nativePID))
	if err != nil {
		return nil, category("native_metadata_unavailable")
	}
	end := bytes.LastIndexByte(raw, ')')
	if end < 0 {
		clear(raw)
		return nil, category("native_metadata_invalid")
	}
	fields := strings.Fields(string(raw[end+1:]))
	clear(raw)
	if len(fields) < 20 {
		return nil, category("native_metadata_invalid")
	}
	start, err := strconv.ParseUint(fields[19], 10, 64)
	if err != nil || start != expected.StartTicks {
		return nil, category("native_identity_mismatch")
	}
	raw, err = os.ReadFile(fmt.Sprintf("/proc/%d/status", nativePID))
	if err != nil {
		return nil, category("native_metadata_unavailable")
	}
	uids, gids := "", ""
	for _, line := range strings.Split(string(raw), "\n") {
		if strings.HasPrefix(line, "Uid:") {
			uids = strings.Join(strings.Fields(line)[1:], ",")
		}
		if strings.HasPrefix(line, "Gid:") {
			gids = strings.Join(strings.Fields(line)[1:], ",")
		}
	}
	clear(raw)
	if uids != "1000,1000,1000,1000" || gids != "100,100,100,100" {
		return nil, category("native_identity_mismatch")
	}
	link, mode, err := fileIdentity(socketPath, true)
	if err != nil {
		return nil, err
	}
	target, modeTarget, err := fileIdentity(socketPath, false)
	if err != nil {
		return nil, err
	}
	resolved, err := filepath.EvalSymlinks(socketPath)
	if err != nil || mode&os.ModeSymlink == 0 || modeTarget&os.ModeSocket == 0 ||
		resolved != socketTarget || link != expected.Link || target != expected.Target {
		return nil, category("socket_identity_mismatch")
	}
	copy := expected
	return &copy, nil
}

func peer(c *net.UnixConn) (*peerID, error) {
	raw, err := c.SyscallConn()
	if err != nil {
		return nil, category("peer_identity_unavailable")
	}
	var cred *syscall.Ucred
	var inner error
	err = raw.Control(func(fd uintptr) {
		cred, inner = syscall.GetsockoptUcred(int(fd), syscall.SOL_SOCKET, syscall.SO_PEERCRED)
	})
	if err != nil || inner != nil || cred == nil {
		return nil, category("peer_identity_unavailable")
	}
	if cred.Pid != nativePID || cred.Uid != 1000 || cred.Gid != 100 {
		return nil, category("peer_identity_mismatch")
	}
	return &peerID{cred.Pid, cred.Uid, cred.Gid}, nil
}

// json.Unmarshal validates syntax but these fields never retain or decode values.
type discarded struct {
	Present bool
	Object  bool
	NonNull bool
}

func (d *discarded) UnmarshalJSON(b []byte) error {
	b = bytes.TrimSpace(b)
	d.Present = true
	d.Object = len(b) > 0 && b[0] == '{'
	d.NonNull = !bytes.Equal(b, []byte("null"))
	return nil
}

func response(ctx context.Context, c *websocket.Conn, id uint64) error {
	// Bounded receive only, never an RPC retry. Unsolicited notification params
	// are skipped without decoding; server requests are never answered.
	for n := 0; n < 64; n++ {
		kind, raw, err := c.Read(ctx)
		if err != nil {
			clear(raw)
			if ctx.Err() != nil {
				return category("response_deadline")
			}
			return category("connection_closed_or_read_error")
		}
		var envelope struct {
			ID     *uint64   `json:"id"`
			Method string    `json:"method"`
			Result discarded `json:"result"`
			Error  discarded `json:"error"`
		}
		err = json.Unmarshal(raw, &envelope)
		clear(raw)
		if err != nil || kind != websocket.MessageText {
			return category("response_protocol_invalid")
		}
		if envelope.ID == nil && envelope.Method != "" {
			continue
		}
		if envelope.Method != "" {
			return category("unexpected_server_request")
		}
		if envelope.ID == nil || *envelope.ID != id {
			return category("response_identity_mismatch")
		}
		if envelope.Error.NonNull {
			return category("rpc_error")
		}
		if !envelope.Result.Present || !envelope.Result.Object {
			return category("response_protocol_invalid")
		}
		return nil
	}
	return category("notification_limit")
}

func write(ctx context.Context, c *websocket.Conn, raw string) error {
	if ctx.Err() != nil {
		return category("request_deadline_before_write")
	}
	if c.Write(ctx, websocket.MessageText, []byte(raw)) != nil {
		return category("request_write_outcome_uncertain")
	}
	return nil
}

func perform(ctx context.Context, start time.Time, r *receipt) (err error) {
	r.Before, err = snapshot(ctx)
	if err != nil {
		return err
	}
	// Six seconds of the 19-second total budget are reserved for postchecks.
	// Leave one second below the required 20-second ceiling for command overhead.
	rpcCtx, cancel := context.WithDeadline(ctx, start.Add(13*time.Second))
	defer cancel()
	var unixConn *net.UnixConn
	var wsConn *websocket.Conn
	defer func() {
		if unixConn != nil {
			var errPeer error
			r.PeerAfter, errPeer = peer(unixConn)
			if errPeer != nil {
				r.PostcheckErrorCategory = errPeer.Error()
			}
		}
		if wsConn != nil {
			_ = wsConn.CloseNow()
		} else if unixConn != nil {
			_ = unixConn.Close()
		}
	}()
	var dialed atomic.Bool
	transport := &http.Transport{Proxy: nil, DialContext: func(dialCtx context.Context, _, _ string) (net.Conn, error) {
		if dialed.Swap(true) {
			return nil, category("second_connection_refused")
		}
		c, dialErr := (&net.Dialer{}).DialContext(dialCtx, "unix", socketPath)
		if dialErr != nil {
			return nil, category("connection_unavailable")
		}
		var ok bool
		unixConn, ok = c.(*net.UnixConn)
		if !ok {
			_ = c.Close()
			return nil, category("unix_transport_required")
		}
		r.PeerBefore, dialErr = peer(unixConn)
		if dialErr != nil {
			_ = c.Close()
			return nil, dialErr
		}
		return c, nil
	}}
	defer transport.CloseIdleConnections()
	client := &http.Client{Transport: transport, CheckRedirect: func(*http.Request, []*http.Request) error { return category("redirect_refused") }}
	c, _, dialErr := websocket.Dial(rpcCtx, "ws://localhost/", &websocket.DialOptions{HTTPClient: client})
	if dialErr != nil {
		return category("websocket_upgrade_failed")
	}
	// Keep the Unix connection open through the peer postcheck. The outer defer
	// closes only this short-lived client connection, never the native service.
	wsConn = c
	c.SetReadLimit(64 * 1024 * 1024) // Same bound as the pinned production client.
	initCtx, initCancel := context.WithTimeout(rpcCtx, 10*time.Second)
	defer initCancel()
	if err = write(initCtx, c, `{"id":1,"method":"initialize","params":{"capabilities":{"experimentalApi":true},"clientInfo":{"name":"dev-workspace-network-recovery","title":"Development Workspace network recovery","version":"0.1.0"}}}`); err != nil {
		return err
	}
	if err = response(initCtx, c, 1); err != nil {
		return err
	}
	if err = write(initCtx, c, `{"method":"initialized"}`); err != nil {
		return err
	}
	r.BeforeRequest, err = snapshot(rpcCtx)
	if err != nil {
		return err
	}
	// Sole config/read write site. cwd is omitted, rather than null/empty.
	if err = write(rpcCtx, c, `{"id":2,"method":"config/read","params":{"includeLayers":false}}`); err != nil {
		return err
	}
	return response(rpcCtx, c, 2)
}

func main() {
	// A separate lead release is required. Merely running/building the helper
	// without this exact explicit argument never opens a socket.
	if len(os.Args) != 2 || os.Args[1] != "--dispatch-once-after-lead-release" {
		os.Exit(64)
	}
	start := time.Now()
	ctx, cancel := context.WithDeadline(context.Background(), start.Add(19*time.Second))
	defer cancel()
	r := receipt{StartedAtUTC: start.UTC().Format(time.RFC3339Nano), Method: "config/read"}
	err := perform(ctx, start, &r)
	if err != nil {
		r.ErrorCategory = err.Error()
	}
	r.After, err = snapshot(ctx)
	if err != nil {
		r.PostcheckErrorCategory = err.Error()
	}
	if r.After != nil && r.Before != nil && !reflect.DeepEqual(r.Before, r.After) {
		r.PostcheckErrorCategory = "identity_changed_after"
	}
	r.Success = r.ErrorCategory == "" && r.PostcheckErrorCategory == "" && r.PeerBefore != nil && r.PeerAfter != nil
	r.CompletedAtUTC = time.Now().UTC().Format(time.RFC3339Nano)
	// This whitelist struct is the sole output. No remote object/error survives.
	if json.NewEncoder(os.Stdout).Encode(r) != nil {
		os.Exit(74)
	}
	if !r.Success {
		os.Exit(1)
	}
}
