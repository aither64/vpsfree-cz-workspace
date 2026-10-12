package web

import (
 "context"
 "encoding/json"
 "fmt"
 "net/http"
 "net/http/httptest"
 "os"
 "path/filepath"
 "strconv"
 "strings"
 "sync"
 "sync/atomic"
 "testing"
 "time"

 "github.com/aither64/codex-web/codex"
 "github.com/aither64/codex-web/conversation"
)

type recoveryBrowserCodex struct {
 *browserContractCodex
 lock sync.Mutex
 entries []codex.TranscriptEntry
}
func(c *recoveryBrowserCodex) ReadThread(context.Context,string)(codex.Transcript,error){
 c.lock.Lock();defer c.lock.Unlock()
 return codex.Transcript{ThreadID:"thread-1",Status:"idle",Model:"model-1",ReasoningEffort:"medium",CollaborationMode:"default",Entries:append([]codex.TranscriptEntry{},c.entries...)},nil
}
func(c *recoveryBrowserCodex) PromptsWithItems(context.Context,string)([]codex.Prompt,error){return []codex.Prompt{{ID:"question-1",Kind:"userInput",ThreadID:"thread-1",AuthorityAvailable:true,Questions:[]codex.Question{{ID:"q1",Header:"Answer",Question:"Preserve this answer"}}}},nil}
func(c *recoveryBrowserCodex) ListQueue(context.Context,string)([]codex.QueueEntry,error){return nil,nil}
func(c *recoveryBrowserCodex) ReconcileQueueDeletionsWithCompletion(context.Context,string,func(string)error)error{return nil}

type recoveryStreamWriter struct{http.ResponseWriter; silent *atomic.Bool}
func(w recoveryStreamWriter) Write(b []byte)(int,error){if w.silent.Load(){return len(b),nil};return w.ResponseWriter.Write(b)}
func(w recoveryStreamWriter) Flush(){if !w.silent.Load(){w.ResponseWriter.(http.Flusher).Flush()}}

func TestRecoveryBrowserFixture(t *testing.T){
 output:=os.Getenv("PORTAL_RECOVERY_FIXTURE");if output==""{t.Skip("manual acceptance")}
 server,_,worktree,_:=reviewWebFixture(t);defer server.Close()
 manifest:=filepath.Join(server.config.Workspace,"work","example","portal.yml")
 saved,err:=os.ReadFile(manifest);if err!=nil{t.Fatal(err)}
 prepareInteractiveConversation(t,server,"example")
 saved=append(saved,[]byte("codex:\n  thread_id: thread-1\n  socket_path: /run/dev-workspace-codex/app-server.sock\n  client_version: 0.154.0\ncreation:\n  state: ready\n  initial_goal_sent: true\n")...)
 if err=os.WriteFile(manifest,saved,0644);err!=nil{t.Fatal(err)}
 changes:=make(chan struct{},1)
 client:=&recoveryBrowserCodex{browserContractCodex:&browserContractCodex{events:changes}}
 for i:=0;i<70;i++{client.entries=append(client.entries,codex.TranscriptEntry{TurnID:"old",ItemID:fmt.Sprint(i),Kind:"agentMessage",Text:fmt.Sprintf("Initial reply %d.\n\nDetails to establish transcript scrolling.",i)})}
 server.config.Codex=client;server.uploadStore.MinFreeBytes=0
 httpServer:=httptest.NewUnstartedServer(nil)
 server.config.BaseURL="https://"+httpServer.Listener.Addr().String()
 server.conversation,err=conversation.NewHandler(conversation.Options{AllowedOrigins:[]string{server.config.BaseURL},BasePath:"/codex",Shutdown:server.stopping,Resolver:conversation.ResolverFunc(server.resolveConversation)})
 if err!=nil{t.Fatal(err)};if err=server.initUploads();err!=nil{t.Fatal(err)}
 handler:=server.Handler();stop:=make(chan struct{});var silent atomic.Bool;var mode atomic.Int32;var reads atomic.Int64;var streams atomic.Int64
 httpServer.Config.Handler=http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
  if strings.HasPrefix(r.URL.Path,"/fixture/"){
   action:=strings.TrimPrefix(r.URL.Path,"/fixture/")
   if action == "shared.js" {
    w.Header().Set("Content-Type", "text/javascript")
    w.Write([]byte(`import {mountConversation} from '/codex/assets/conversation.js?v=7';
const root=document.createElement('div');root.id='shared-check';document.body.append(root);
window.destroyShared=mountConversation(root,{id:'example',basePath:'/codex',capabilities:{settings:false,queue:false,interrupt:false}});
root.style.cssText='position:fixed;inset:10px;background:#101822;z-index:9999;overflow:auto';
root.querySelector('.codex-conversation-transcript').style.cssText='height:150px;overflow:auto';`));return
   }
   switch action{
   case "silent":silent.Store(true)
   case "stall":mode.Store(1)
   case "failure":mode.Store(2)
   case "recover":mode.Store(0);silent.Store(false)
   case "hint":select{case changes<-struct{}{}:default:}
   case "reply":client.lock.Lock();client.entries=append(client.entries,codex.TranscriptEntry{TurnID:"final",ItemID:strconv.Itoa(len(client.entries)),Kind:"agentMessage",Text:r.URL.Query().Get("text")});client.lock.Unlock()
   case "commits":count,_:=strconv.Atoi(r.URL.Query().Get("count"));for i:=0;i<count;i++{runWebGit(t,"-C",worktree,"commit","--allow-empty","-m",fmt.Sprintf("Extra commit %d",i))}
   case "stop":select{case <-stop:default:close(stop)}
   }
   w.Header().Set("Content-Type","application/json");json.NewEncoder(w).Encode(map[string]any{"reads":reads.Load(),"streams":streams.Load()});return
  }
  if strings.HasSuffix(r.URL.Path,"/events"){
   streams.Add(1);handler.ServeHTTP(recoveryStreamWriter{w,&silent},r);return
  }
  if strings.HasSuffix(r.URL.Path,"/thread"){
   reads.Add(1)
   switch mode.Load(){case 1:<-r.Context().Done();return;case 2:w.Header().Set("Content-Type","application/json");w.WriteHeader(503);w.Write([]byte(`{"error":"Fixture service unavailable"}`));return}
  }
  if strings.HasSuffix(r.URL.Path,"/activity"){
   w.Header().Set("Content-Type","application/json");json.NewEncoder(w).Encode(map[string]any{"threadId":"thread-1","currentState":"waiting","stateSinceMs":time.Now().Add(-time.Minute).UnixMilli(),"observedAtMs":time.Now().UnixMilli(),"coverageComplete":true});return
  }
  handler.ServeHTTP(w,r)
 })
 httpServer.StartTLS();defer httpServer.Close()
 data,_:=json.Marshal(map[string]string{"url":httpServer.URL,"workspace":server.config.Workspace})
 if err=os.WriteFile(output,data,0600);err!=nil{t.Fatal(err)}
 <-stop
}
