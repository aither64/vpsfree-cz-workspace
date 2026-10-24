package main

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"net"
	"net/http"
	"path/filepath"
	"strings"
	"sync/atomic"
	"testing"
	"time"

	"github.com/coder/websocket"
)

// These fixtures exercise only the connection exchanges and receipt type.
// They never call main, perform, snapshot, peer or any hardcoded live endpoint.
func TestConfigReadUnixSocket(t *testing.T) {
	const sentinel = "opaque-fixture-value-9c34fe35"
	for _, tc := range []struct {
		name                       string
		wantCategory               string
		wantAttempted, wantWritten bool
	}{
		{"success", "", true, true},
		{"initialize_mismatched_id", "response_identity_mismatch", false, false},
		{"config_mismatched_id", "response_identity_mismatch", true, true},
		{"remote_error", "rpc_error", true, true},
		{"canceled_before_config", "request_deadline_before_write", false, false},
		{"config_write_failure", "request_write_outcome_uncertain", true, false},
	} {
		t.Run(tc.name, func(t *testing.T) {
			ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
			defer cancel()
			socket := filepath.Join(t.TempDir(), "app.sock")
			if socket == socketPath || socket == socketTarget {
				t.Fatal("fixture endpoint must be disposable")
			}
			listener, err := net.Listen("unix", socket)
			if err != nil {
				t.Fatal(err)
			}
			defer listener.Close()
			serverResult := make(chan error, 1)
			var configCount atomic.Int32
			server := &http.Server{Handler: http.HandlerFunc(func(w http.ResponseWriter, req *http.Request) {
				c, err := websocket.Accept(w, req, nil)
				if err != nil {
					serverResult <- fmt.Errorf("fixture upgrade failed")
					return
				}
				defer c.CloseNow()
				read := func() (map[string]json.RawMessage, error) {
					kind, raw, err := c.Read(ctx)
					if err != nil {
						return nil, err
					}
					defer clear(raw)
					if kind != websocket.MessageText {
						return nil, fmt.Errorf("fixture expected text")
					}
					var m map[string]json.RawMessage
					err = json.Unmarshal(raw, &m)
					return m, err
				}
				write := func(raw string) error { return c.Write(ctx, websocket.MessageText, []byte(raw)) }
				fail := func(message string) { serverResult <- fmt.Errorf("%s", message) }
				first, err := read()
				if err != nil || string(first["id"]) != "1" || string(first["method"]) != `"initialize"` {
					fail("fixture initialization order or identity changed")
					return
				}
				var initParams struct {
					Capabilities map[string]bool   `json:"capabilities"`
					ClientInfo   map[string]string `json:"clientInfo"`
				}
				if json.Unmarshal(first["params"], &initParams) != nil ||
					len(initParams.Capabilities) != 1 || !initParams.Capabilities["experimentalApi"] ||
					initParams.ClientInfo["name"] != "dev-workspace-network-recovery" ||
					initParams.ClientInfo["version"] != "0.1.0" {
					fail("fixture initialization capability/client identity changed")
					return
				}
				initID := "1"
				if tc.name == "initialize_mismatched_id" {
					initID = "99"
				}
				if write(`{"id":`+initID+`,"result":{"opaque":"`+sentinel+`"}}`) != nil {
					fail("fixture initialization response failed")
					return
				}
				if tc.name == "initialize_mismatched_id" {
					if _, err := read(); err == nil {
						fail("client wrote after refused initialization")
						return
					}
					serverResult <- nil
					return
				}
				notification, err := read()
				if err != nil || len(notification) != 1 || string(notification["method"]) != `"initialized"` {
					fail("fixture initialized notification missing or out of order")
					return
				}
				request, err := read()
				if tc.name == "canceled_before_config" || tc.name == "config_write_failure" {
					if err == nil {
						fail("fixture received an unexpected config request")
						return
					}
					serverResult <- nil
					return
				}
				if err != nil || len(request) != 3 || string(request["id"]) != "2" || string(request["method"]) != `"config/read"` {
					fail("fixture config request identity or order changed")
					return
				}
				var params map[string]json.RawMessage
				if json.Unmarshal(request["params"], &params) != nil || len(params) != 1 || string(params["includeLayers"]) != "false" {
					fail("fixture config params must have only includeLayers false, with cwd absent")
					return
				}
				configCount.Add(1)
				reply := `{"id":2,"result":{"config":{"opaque":"` + sentinel + `"},"origins":{"opaque":"` + sentinel + `"},"layers":["` + sentinel + `"]}}`
				if tc.name == "config_mismatched_id" {
					reply = strings.Replace(reply, `"id":2`, `"id":99`, 1)
				}
				if tc.name == "remote_error" {
					reply = `{"id":2,"error":{"code":-32000,"message":"` + sentinel + `","data":{"config":"` + sentinel + `"}}}`
				}
				if write(reply) != nil {
					fail("fixture config response failed")
					return
				}
				if _, err := read(); err == nil {
					fail("client sent an extra application message")
					return
				}
				serverResult <- nil
			})}
			defer server.Close()
			go func() { _ = server.Serve(listener) }()
			var dials atomic.Int32
			transport := &http.Transport{Proxy: nil, DialContext: func(ctx context.Context, _, _ string) (net.Conn, error) {
				if dials.Add(1) != 1 {
					return nil, fmt.Errorf("fixture refuses another connection")
				}
				return (&net.Dialer{}).DialContext(ctx, "unix", socket)
			}}
			defer transport.CloseIdleConnections()
			client := &http.Client{Transport: transport, CheckRedirect: func(*http.Request, []*http.Request) error { return fmt.Errorf("fixture refuses redirect") }}
			c, _, err := websocket.Dial(ctx, "ws://localhost/", &websocket.DialOptions{HTTPClient: client})
			if err != nil {
				t.Fatal("disposable WebSocket dial failed")
			}
			defer c.CloseNow()
			c.SetReadLimit(64 * 1024 * 1024)
			r := receipt{Method: "config/read", StartedAtUTC: time.Now().UTC().Format(time.RFC3339Nano)}
			err = initialize(ctx, c)
			if err == nil {
				configCtx := ctx
				if tc.name == "canceled_before_config" {
					canceled, stop := context.WithCancel(ctx)
					stop()
					configCtx = canceled
				}
				if tc.name == "config_write_failure" {
					_ = c.CloseNow()
				}
				err = readConfig(configCtx, c, &r)
			}
			if err != nil {
				r.ErrorCategory = err.Error()
			}
			r.Success = err == nil
			r.CompletedAtUTC = time.Now().UTC().Format(time.RFC3339Nano)
			_ = c.CloseNow()
			select {
			case err := <-serverResult:
				if err != nil {
					t.Fatal(err)
				}
			case <-ctx.Done():
				t.Fatal("disposable fixture did not finish within its deadline")
			}
			if r.ErrorCategory != tc.wantCategory || r.ConfigReadAttempted != tc.wantAttempted || r.ConfigReadFullyWritten != tc.wantWritten {
				t.Fatalf("category/attempt/write mismatch: %q/%t/%t", r.ErrorCategory, r.ConfigReadAttempted, r.ConfigReadFullyWritten)
			}
			wantCount := int32(0)
			if tc.wantWritten {
				wantCount = 1
			}
			if configCount.Load() != wantCount || dials.Load() != 1 {
				t.Fatal("fixture request/connection count mismatch")
			}
			var emitted bytes.Buffer
			if json.NewEncoder(&emitted).Encode(r) != nil {
				t.Fatal("receipt encoding failed")
			}
			if bytes.Contains(emitted.Bytes(), []byte(sentinel)) {
				t.Fatal("opaque payload reached emitted receipt")
			}
			var fields map[string]json.RawMessage
			if json.Unmarshal(emitted.Bytes(), &fields) != nil {
				t.Fatal("receipt invalid")
			}
			allowed := map[string]bool{"startedAtUTC": true, "completedAtUTC": true, "method": true, "success": true, "errorCategory": true, "configReadAttempted": true, "configReadFullyWritten": true}
			for field := range fields {
				if !allowed[field] {
					t.Fatalf("unexpected receipt field %q", field)
				}
			}
		})
	}
}
