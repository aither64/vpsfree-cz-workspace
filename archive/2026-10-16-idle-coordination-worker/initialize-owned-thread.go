package main

import (
 "context"
 "crypto/sha256"
 "encoding/hex"
 "encoding/json"
 "fmt"
 "os"
 "path/filepath"
 "strings"
 "time"
 "github.com/aither64/codex-web/codex"
)

func must(err error) { if err != nil { panic(err) } }

func main() {
 root := "/home/aither/workspace/ai/vpsfree.cz"
 slug := "2026-10-16-idle-coordination-worker"
 thread := "01a14685-4f0d-7d73-b864-8fad3359d62c"
 socket := "/run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock"
 cwd := filepath.Join(root,"work",slug)
 ctx,cancel := context.WithTimeout(context.Background(),50*time.Second); defer cancel()
 textBytes,err := os.ReadFile(filepath.Join(cwd,"managed-ownership-goal.txt")); must(err)
 text := strings.TrimSpace(string(textBytes))
 hash := sha256.Sum256([]byte(text))
 if hex.EncodeToString(hash[:]) != "27cf3068685254adb713bcb91574b0f2fc1e99d531657a0206f61d2a3aa4a406" { panic("frozen goal changed") }
 link,err := filepath.EvalSymlinks("/home/aither/.local/state/dev-workspaces/profile"); must(err)
 if link != "/nix/store/52w0v2bcl77igbnx53wx9062k9d0dy1w-dev-workspace-0.2.0" { panic("selected generation changed") }
 identity := sha256.Sum256([]byte(socket))
 ledger := filepath.Join("/home/aither/.local/state/dev-workspaces/submissions",hex.EncodeToString(identity[:])+".json")
 client := codex.NewWithOptions(socket,codex.ClientOptions{PreserveThreadInstructionsOnResume:true,SubmissionLedgerPath:ledger}); defer client.Close()
 metadata,err := client.ReadThreadMetadata(ctx,thread,true); must(err)
 if metadata.ID != thread || metadata.Cwd != cwd || metadata.Source != "vscode" { panic("owned native identity changed") }
 settings,err := client.ReadThreadSettings(ctx,thread); must(err)
 options := codex.TurnOptions{Model:settings.Model,ReasoningEffort:settings.ReasoningEffort}
 id := "owned-initial-"+thread
 action := "initial-request-recovery:"+slug
 receipt,found,err := client.ReconcileSendWithOptions(ctx,thread,text,id,action,options); must(err)
 if !found {
  must(client.RequireThreadIdle(ctx,thread,cwd))
  var page struct { Data *[]json.RawMessage `json:"data"`; NextCursor *string `json:"nextCursor"` }
  must(client.Request(ctx,"thread/turns/list",map[string]any{"threadId":thread,"limit":1,"sortDirection":"asc","itemsView":"full"},&page))
  if page.Data == nil || len(*page.Data) != 0 || page.NextCursor != nil { panic("thread is not provably empty") }
  receipt,err = client.SendWithOptions(ctx,thread,text,id,action,options); must(err)
 }
 must(json.NewEncoder(os.Stdout).Encode(map[string]any{"threadId":thread,"goalSha256":hex.EncodeToString(hash[:]),"messageId":id,"receipt":receipt,"reconciled":found}))
 fmt.Fprintln(os.Stderr,"Owned initial request submitted with retained identity; run ordinary session startup to reconcile.")
}
