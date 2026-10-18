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
 "syscall"
 "time"

 "github.com/aither64/codex-web/codex"
 "gopkg.in/yaml.v3"
)

func must(err error) { if err != nil { panic(err) } }
func main() {
 const root = "/home/aither/workspace/ai/vpsfree.cz"
 const slug = "2026-10-16-session-archive-local-first"
 const thread = "01a145d0-7a59-7a03-af9f-a66366f5875f"
 const socket = "/run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock"
 const authority = "/run/user/1000/dev-workspaces/vpsfree-cz/authority"
 const expectedGoal = "a9a93057f0b1aaf570e8198d82d5fbc7e362dff3f3e72018059bd2878641aa82"
 const clientID = "5ac86771-bb22-44a1-a2cc-b1d7399fa53f"
 record := filepath.Join(root,"work",slug)
 for _,suffix := range []string{".creation.lock",".lock"} {
  lock,err := os.OpenFile(filepath.Join(authority,slug+suffix),os.O_RDWR,0); must(err)
  must(syscall.Flock(int(lock.Fd()),syscall.LOCK_EX|syscall.LOCK_NB))
  defer lock.Close()
 }
 var owner struct { State string `json:"state"`; Slug string `json:"slug"`; Workspace string `json:"workspace"`; Thread string `json:"codex_thread_id"`; Socket string `json:"codex_socket_path"` }
 raw,err := os.ReadFile(filepath.Join(authority,slug+".json")); must(err); must(json.Unmarshal(raw,&owner))
 if owner.State!="creating" || owner.Slug!=slug || owner.Workspace!=root || owner.Thread!=thread || owner.Socket!=socket { panic("creation authority mismatch") }
 var manifest struct { Slug string `yaml:"slug"`; Codex struct { Thread string `yaml:"thread_id"`; Socket string `yaml:"socket_path"` } `yaml:"codex"`; Creation struct { State string `yaml:"state"`; Goal string `yaml:"goal_sha256"`; Sent bool `yaml:"initial_goal_sent"`; Attempted bool `yaml:"initial_goal_attempted"` } `yaml:"creation"` }
 raw,err=os.ReadFile(filepath.Join(record,"portal.yml"));must(err);must(yaml.Unmarshal(raw,&manifest))
 if manifest.Slug!=slug || manifest.Codex.Thread!=thread || manifest.Codex.Socket!=socket || manifest.Creation.State!="creating" || manifest.Creation.Sent || !manifest.Creation.Attempted || manifest.Creation.Goal!=expectedGoal { panic("manifest no longer matches exact pending goal") }
 raw,err=os.ReadFile(filepath.Join(record,"native-anchor-goal.txt"));must(err)
 goal:=strings.TrimSpace(string(raw)); hash:=sha256.Sum256([]byte(goal))
 if hex.EncodeToString(hash[:])!=expectedGoal { panic("goal changed") }
 socketHash:=sha256.Sum256([]byte(socket))
 client:=codex.NewWithOptions(socket,codex.ClientOptions{PreserveThreadInstructionsOnResume:true,SubmissionLedgerPath:filepath.Join("/home/aither/.local/state/dev-workspaces/submissions",hex.EncodeToString(socketHash[:])+".json"),LegacySubmissionLedgerPath:socket+".submission-attempts-v3.json"})
 defer client.Close()
 ctx,cancel:=context.WithTimeout(context.Background(),45*time.Second);defer cancel()
 var metadata struct { Thread struct { ID string `json:"id"`; Cwd string `json:"cwd"`; Status struct { Type string `json:"type"` } `json:"status"` } `json:"thread"` }
 must(client.Request(ctx,"thread/read",map[string]any{"threadId":thread},&metadata))
 if metadata.Thread.ID!=thread || metadata.Thread.Cwd!=record || metadata.Thread.Status.Type!="idle" { panic(fmt.Sprintf("unexpected native thread: %#v",metadata.Thread)) }
 var page struct { Data *[]json.RawMessage `json:"data"` }
 must(client.Request(ctx,"thread/turns/list",map[string]any{"threadId":thread,"limit":1,"sortDirection":"asc","itemsView":"full"},&page))
 if page.Data==nil || len(*page.Data)!=0 { panic("native history is no longer empty; refusing another initial request") }
 proof:=map[string]any{"schema":1,"thread":thread,"socket":socket,"cwd":record,"goal_sha256":expectedGoal,"clientUserMessageID":clientID,"beforeTurns":0,"beforeStatus":"idle","state":"prepared"}
 proofPath:=filepath.Join(record,"native-initial-recovery.json")
 if _,err:=os.Stat(proofPath);!os.IsNotExist(err) { panic("recovery already has a receipt; reconcile it instead of replaying") }
 encoded,err:=json.MarshalIndent(proof,"","  ");must(err);must(os.WriteFile(proofPath,append(encoded,'\n'),0600))
 receipt,err:=client.Send(ctx,thread,goal,clientID,"session-initial-recovery:"+slug);must(err)
 proof["state"]="accepted";proof["receipt"]=receipt
 encoded,err=json.MarshalIndent(proof,"","  ");must(err);must(os.WriteFile(proofPath,append(encoded,'\n'),0600))
 fmt.Println(string(encoded))
}
