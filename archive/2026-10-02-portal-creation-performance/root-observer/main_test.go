package main

import (
	"errors"
	"testing"
)

func TestSummarizeOmitsUnrecognizedMessages(t *testing.T) {
	for _, input := range []string{
		"credential-or-prompt-text",
		"Codex RPC -32600: credential-or-prompt-text",
		"Codex RPC -32600: thread not loaded: another-id",
		"Codex RPC -32600: thread not loaded: " + threadID + " extra content",
	} {
		if got := summarize(errors.New(input)); got["message"] != "details omitted" {
			t.Fatalf("unrecognized error message was exposed")
		}
	}
}

func TestSummarizeKeepsOnlyExactTargetDiagnostic(t *testing.T) {
	message := "thread not loaded: " + threadID
	got := summarize(errors.New("Codex RPC -32600: " + message))
	if got["kind"] != "rpc-error" || got["code"] != -32600 || got["message"] != message {
		t.Fatal("exact diagnostic metadata was not preserved")
	}
	if summarize(nil) != nil {
		t.Fatal("successful probe acquired an error")
	}
}
