// Fixed-target, metadata-only diagnostic. No repair or acceptance decision.
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"runtime/debug"
	"slices"
	"strconv"
	"strings"
	"time"

	"github.com/aither64/codex-web/codex"
)

const (
	sdkVersion = "v0.0.0-20261002145902-4c170393a96e"
	socketPath = "/tmp/pcp-oct02-a/r/bench/app-server.sock"
	threadID   = "01a0fe38-b8e0-76c1-b8f0-fd84783964a5"
	cwd        = "/tmp/pcp-oct02-a/workspace/work/2026-10-02-creation-root-loss"
)

// Preserve exact known diagnostics, but never print arbitrary server messages.
func summarize(err error) map[string]any {
	if err == nil {
		return nil
	}
	text := err.Error()
	result := map[string]any{"kind": "client-or-transport-error", "message": "details omitted"}
	if tail, ok := strings.CutPrefix(text, "Codex RPC "); ok {
		code, message, ok := strings.Cut(tail, ": ")
		if number, parseErr := strconv.Atoi(code); ok && parseErr == nil {
			result["kind"], result["code"] = "rpc-error", number
			known := []string{
				"thread not loaded: " + threadID,
				"no rollout found for thread id " + threadID,
				"invalid paginated history lineage for " + threadID + ": missing source rollout",
				"thread " + threadID + " is not materialized yet; thread/turns/list is unavailable before first user message",
				"thread not found",
			}
			if slices.Contains(known, message) {
				result["message"] = message
			}
		}
	}
	return result
}

func emit(method string, err error, metadata map[string]any) {
	row := map[string]any{"at": time.Now().UTC().Format(time.RFC3339Nano), "method": method,
		"ok": err == nil, "error": summarize(err), "metadata": metadata}
	_ = json.NewEncoder(os.Stdout).Encode(row)
}

func requirePinnedSDK() bool {
	info, ok := debug.ReadBuildInfo()
	if ok {
		for _, dependency := range info.Deps {
			if dependency.Path == "github.com/aither64/codex-web" {
				return dependency.Version == sdkVersion && dependency.Replace == nil
			}
		}
	}
	return false
}

func main() {
	if len(os.Args) != 1 || !requirePinnedSDK() {
		fmt.Fprintln(os.Stderr, "fixed-target observer requires the pinned SDK module without replacement and no arguments")
		os.Exit(2)
	}
	emit("observer/identity", nil, map[string]any{"sdk": sdkVersion, "socket": socketPath,
		"targetThreadID": threadID, "expectedCwd": cwd, "observationsAreNotAtomic": true})
	options := codex.ClientOptions{ClientInfo: codex.ClientInfo{Name: "creation-root-observer", Version: "1"},
		ThreadSourceKinds: []string{"vscode"}}
	// The parent explicitly authorized the production loaded-list client policy.
	// No watch/subscription, prompt handler or nonblocking-input policy is added.
	loadedClient := codex.NewWithOptions(socketPath, options)
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	ids, err := loadedClient.LoadedThreadIDs(ctx)
	cancel()
	loadedClient.Close()
	var loaded map[string]any
	if err == nil {
		loaded = map[string]any{"targetLoaded": slices.Contains(ids, threadID), "loadedCount": len(ids)}
	}
	emit("thread/loaded/list", err, loaded)

	options.ObserverOnly = true
	client := codex.NewWithOptions(socketPath, options)
	defer client.Close()
	var read struct {
		Thread struct {
			ID          string          `json:"id"`
			Cwd         string          `json:"cwd"`
			Source      json.RawMessage `json:"source"`
			Ephemeral   *bool           `json:"ephemeral"`
			HistoryMode string          `json:"historyMode"`
			Status      struct {
				Type string `json:"type"`
			} `json:"status"`
		} `json:"thread"`
	}
	ctx, cancel = context.WithTimeout(context.Background(), 10*time.Second)
	err = client.Request(ctx, "thread/read", map[string]any{"threadId": threadID, "includeTurns": false}, &read)
	cancel()
	var metadata map[string]any
	identityMatches := false
	if err == nil {
		var source string
		_ = json.Unmarshal(read.Thread.Source, &source)
		identityMatches = read.Thread.ID == threadID && read.Thread.Cwd == cwd && source == "vscode"
		// Emit source equality only when it is the exact expected application kind.
		metadata = map[string]any{"threadID": read.Thread.ID, "cwd": read.Thread.Cwd,
			"sourceIsVscode": source == "vscode", "identityMatches": identityMatches,
			"ephemeral": read.Thread.Ephemeral, "paginated": read.Thread.HistoryMode == "paginated",
			"statusIsIdle": read.Thread.Status.Type == "idle", "includeTurns": false}
	}
	emit("thread/read", err, metadata)

	if identityMatches {
		ctx, cancel = context.WithTimeout(context.Background(), 10*time.Second)
		materialized, materialErr := client.HistoryMaterialized(ctx, threadID, cwd)
		cancel()
		var material map[string]any
		if materialErr == nil {
			material = map[string]any{"materialized": materialized}
		}
		// SDK reads metadata and stats its rollout path; it never opens the payload.
		emit("thread/read + stat (SDK HistoryMaterialized)", materialErr, material)
	} else {
		emit("materialization/skipped", fmt.Errorf("identity unavailable"), nil)
	}

	var turns struct {
		Data *[]struct {
			Status string `json:"status"`
		} `json:"data"`
	}
	ctx, cancel = context.WithTimeout(context.Background(), 10*time.Second)
	err = client.Request(ctx, "thread/turns/list", map[string]any{"threadId": threadID,
		"limit": 1, "sortDirection": "desc", "itemsView": "notLoaded"}, &turns)
	cancel()
	var turnMetadata map[string]any
	if err == nil && turns.Data == nil {
		err = fmt.Errorf("missing turns metadata")
	}
	if err == nil {
		turnMetadata = map[string]any{"returnedTurnCount": len(*turns.Data), "itemsView": "notLoaded"}
		if len(*turns.Data) == 1 {
			status := (*turns.Data)[0].Status
			if !slices.Contains([]string{"completed", "failed", "interrupted", "inProgress"}, status) {
				status = "unrecognized"
			}
			turnMetadata["latestTurnStatus"] = status
		}
	}
	emit("thread/turns/list", err, turnMetadata)
	ctx, cancel = context.WithTimeout(context.Background(), 10*time.Second)
	err = client.RequireThreadTurnsIdle(ctx, threadID)
	cancel()
	emit("SDK RequireThreadTurnsIdle: thread/turns/list; thread/read fallback on failure", err,
		map[string]any{"turnsIdleProved": err == nil, "queueOrPendingRequestsProved": false})
}
