package web

import (
 "bytes"
 "context"
 "crypto/sha256"
 "encoding/json"
 "fmt"
 "net/http"
 "net/http/httptest"
 "os"
 "path/filepath"
 "runtime"
 "strings"
 "sync"
 "sync/atomic"
 "testing"
 "time"

 "github.com/aither64/codex-web/codex"
 "github.com/aither64/codex-web/conversation"
)

type uploadBrowserCodex struct {
 *browserContractCodex
 lock sync.Mutex
 entries []codex.TranscriptEntry
 queue []codex.QueueEntry
 busy bool
}
// Keep this fixture free of unrelated approval prompts.
func(c *uploadBrowserCodex) PromptsWithItems(context.Context,string)([]codex.Prompt,error){return nil,nil}
func(c *uploadBrowserCodex) ReadThread(context.Context,string)(codex.Transcript,error){
 c.lock.Lock();defer c.lock.Unlock();status:="idle";if c.busy{status="active"}
 return codex.Transcript{ThreadID:"thread-1",Status:status,Model:"model-1",ReasoningEffort:"medium",CollaborationMode:"default",Entries:append([]codex.TranscriptEntry{},c.entries...)},nil
}
func(c *uploadBrowserCodex) Send(_ context.Context,_,message,id,_ string)(codex.SendReceipt,error){
 c.lock.Lock();defer c.lock.Unlock()
 for _,e:=range c.entries {if e.ClientUserMessageID==id{return codex.SendReceipt{TurnID:"turn-1",ClientUserMessageID:id},nil}}
 c.entries=append(c.entries,codex.TranscriptEntry{TurnID:"turn-1",ItemID:id,Kind:"userMessage",Text:message,ClientUserMessageID:id,ClientUserMessageDigest:fmt.Sprintf("%x",sha256.Sum256([]byte(message)))})
 return codex.SendReceipt{TurnID:"turn-1",ClientUserMessageID:id,Steered:c.busy},nil
}
func(c *uploadBrowserCodex) ListQueue(context.Context,string)([]codex.QueueEntry,error){c.lock.Lock();defer c.lock.Unlock();return append([]codex.QueueEntry{},c.queue...),nil}
func(c *uploadBrowserCodex) Queue(_ context.Context,_,message,id string)(codex.QueueEntry,error){
 c.lock.Lock();defer c.lock.Unlock();for _,e:=range c.queue {if e.ClientUserMessageID==id{return e,nil}}
 entry:=codex.QueueEntry{ID:id,Text:message,ClientUserMessageID:id};c.queue=append(c.queue,entry);return entry,nil
}
func(c *uploadBrowserCodex) DeleteQueueEntry(_ context.Context,_,id string)error{c.lock.Lock();defer c.lock.Unlock();for i,e:=range c.queue{if e.ID==id{c.queue=append(c.queue[:i],c.queue[i+1:]...);break}};return nil}
func(c *uploadBrowserCodex) StartQueue(ctx context.Context,thread,id string)error{c.lock.Lock();if len(c.queue)==0{c.lock.Unlock();return nil};entry:=c.queue[0];c.queue=c.queue[1:];c.lock.Unlock();_,err:=c.Send(ctx,thread,entry.Text,entry.ClientUserMessageID,"");return err}

func TestUploadBrowserFixture(t *testing.T){
 output:=os.Getenv("PORTAL_UPLOAD_BROWSER_FIXTURE");if output==""{t.Skip("manual acceptance")}
 server:=newTestServer(t);defer server.Close()
 directory:=filepath.Join(server.config.Workspace,"work","example");os.MkdirAll(directory,0755)
 os.WriteFile(filepath.Join(directory,"portal.yml"),[]byte("schema: 1\nslug: example\ncodex:\n  thread_id: thread-1\n  socket_path: /run/dev-workspace-codex/app-server.sock\n  client_version: 0.152.1\ncreation:\n  state: ready\n  initial_goal_sent: true\n"),0644)
 writeWebTrackingFiles(t,directory,"active");writeWebRuntimeAuthority(t,server,"example")
 changes:=make(chan struct{}, 1)
 client:=&uploadBrowserCodex{browserContractCodex:&browserContractCodex{events:changes}}
 server.config.Codex=client;server.uploadStore.MinFreeBytes=0
 httpServer:=httptest.NewUnstartedServer(nil)
 server.config.BaseURL="https://"+httpServer.Listener.Addr().String()
 var err error
 server.conversation,err=conversation.NewHandler(conversation.Options{AllowedOrigins:[]string{server.config.BaseURL},BasePath:"/codex",Shutdown:server.stopping,Resolver:conversation.ResolverFunc(server.resolveConversation)})
 if err!=nil{t.Fatal(err)}
 if err=server.initUploads();err!=nil{t.Fatal(err)}
 handler:=server.Handler();stop:=make(chan struct{});var slow atomic.Bool; var baseline atomic.Bool
 legacyAssets:=os.Getenv("PORTAL_UPLOAD_LEGACY_ASSETS")
 httpServer.Config.Handler=http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
  if strings.HasPrefix(r.URL.Path,"/fixture/"){
   switch strings.TrimPrefix(r.URL.Path,"/fixture/"){
   case "shared-composer.js":
    w.Header().Set("Content-Type","text/javascript")
    w.Write([]byte(`import {mountConversation} from '/codex/assets/conversation.js?v=6';
const root=document.createElement('div');root.id='shared-acceptance';document.body.append(root);
window.destroySharedAcceptance=mountConversation(root,{id:'shared-acceptance',basePath:'/codex',uploadBasePath:'/uploads/s-example',
 client:{thread:async()=>({status:'idle',entries:[]})},capabilities:{pending:false,queueRead:false,queue:false,interrupt:false,settings:false,respond:false,eventStream:false}});`));return
   case "baseline":baseline.Store(true)
   case "current":baseline.Store(false)
   case "busy":client.lock.Lock();client.busy=true;client.lock.Unlock()
   case "idle":client.lock.Lock();client.busy=false;client.lock.Unlock()
   case "slow":slow.Store(true)
   case "fast":slow.Store(false)
   case "stats":var stats runtime.MemStats;runtime.ReadMemStats(&stats);json.NewEncoder(w).Encode(map[string]any{"heapAlloc":stats.HeapAlloc,"sys":stats.Sys,"pid":os.Getpid(),"workspace":server.config.Workspace,"uploads":server.uploadStore.Directory});return
   case "stop":select{case <-stop:default:close(stop)}
   }
   select{case changes<-struct{}{}:default:}
   w.Header().Set("Content-Type","application/json");w.Write([]byte("{}"));return
  }
  if baseline.Load() && legacyAssets!="" {
   if strings.HasPrefix(r.URL.Path,"/codex/assets/") || r.URL.Path=="/static/app.js" {
    if r.URL.Path=="/static/app.js" {w.Header().Set("Cache-Control","no-store")} else {w.Header().Set("Cache-Control","public, max-age=300")}
    http.ServeFile(w,r,filepath.Join(legacyAssets,filepath.Base(r.URL.Path)));return
   }
   if r.URL.Path=="/" || r.URL.Path=="/example/" {
    capture:=httptest.NewRecorder();handler.ServeHTTP(capture,r)
    for name,values:=range capture.Header(){w.Header()[name]=values}
    w.Header().Del("Content-Length");w.WriteHeader(capture.Code)
    w.Write(bytes.ReplaceAll(capture.Body.Bytes(),[]byte("/codex/assets/uploads.css?v=2"),[]byte("/codex/assets/uploads.css")));return
   }
  }
  if r.Method=="PATCH" && slow.Load(){time.Sleep(750*time.Millisecond)}
  handler.ServeHTTP(w,r)
 })
 httpServer.StartTLS();defer httpServer.Close()
 data,_:=json.Marshal(map[string]string{"url":httpServer.URL,"workspace":server.config.Workspace,"uploads":server.uploadStore.Directory})
 if err=os.WriteFile(output,data,0600);err!=nil{t.Fatal(err)}
 <-stop
}

func(c *uploadBrowserCodex) DeleteQueueEntryWithCompletion(ctx context.Context, thread, id string, complete func() error) error {
 if err := c.DeleteQueueEntry(ctx, thread, id); err != nil { return err }; return complete()
}
func(c *uploadBrowserCodex) ReconcileQueueDeletionsWithCompletion(context.Context, string, func(string) error) error { return nil }
