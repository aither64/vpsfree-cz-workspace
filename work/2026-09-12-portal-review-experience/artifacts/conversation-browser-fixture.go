package web

import (
 "context"
 "crypto/sha256"
 "encoding/json"
 "fmt"
 "net/http"
 "net/http/httptest"
 "os"
 "path/filepath"
 "strings"
 "sync"
 "testing"
 "time"

 "github.com/aither64/codex-web/codex"
 "github.com/aither64/codex-web/conversation"
)

type manualBrowserCodex struct {
 *browserContractCodex
 lock sync.Mutex
 entries []map[string]any
 queue []codex.QueueEntry
 busy bool
 prompts bool
 changes chan struct{}
 activityReads map[string]int
 verify func(context.Context,string,string)error
}
func (c *manualBrowserCodex) VerifyThread(ctx context.Context,thread,cwd string)error{return c.verify(ctx,thread,cwd)}
func (c *manualBrowserCodex) notify() { select { case c.changes <- struct{}{}: default: } }
func (c *manualBrowserCodex) entry(kind, text, id string) map[string]any {
 return map[string]any{"turnId":"turn-1", "itemId":id, "kind":kind, "text":text, "timestamp":time.Now().UTC().Format(time.RFC3339), "turnStatus":"completed"}
}
func (c *manualBrowserCodex) ReadThread(_ context.Context, thread string) (codex.Transcript,error) {
 c.lock.Lock(); defer c.lock.Unlock()
 status:="idle"; if c.busy {status="active"}
 payload,_:=json.Marshal(map[string]any{"threadId":thread,"status":status,"model":"model-1","reasoningEffort":"medium","collaborationMode":"default","entries":c.entries})
 var result codex.Transcript; err:=json.Unmarshal(payload,&result); return result,err
}
func (c *manualBrowserCodex) Send(_ context.Context, _, message, clientID, _ string) (codex.SendReceipt,error) {
 c.lock.Lock()
 entry:=c.entry("userMessage",message,clientID)
 entry["clientUserMessageId"]=clientID; entry["clientUserMessageDigest"]=fmt.Sprintf("%x",sha256.Sum256([]byte(message)))
 c.entries=append(c.entries,entry); c.busy=true; c.lock.Unlock(); c.notify()
 go func(){time.Sleep(500*time.Millisecond);c.lock.Lock();c.entries=append(c.entries,c.entry("agentMessage","Reply to: "+message,"reply-"+clientID));c.busy=false;c.lock.Unlock();c.notify()}()
 return codex.SendReceipt{TurnID:"turn-1",ClientUserMessageID:clientID},nil
}
func (c *manualBrowserCodex) ListQueue(_ context.Context,_ string)([]codex.QueueEntry,error){c.lock.Lock();defer c.lock.Unlock();return append([]codex.QueueEntry{},c.queue...),nil}
func (c *manualBrowserCodex) Queue(_ context.Context,_,message,id string)(codex.QueueEntry,error){c.lock.Lock();defer c.lock.Unlock();entry:=codex.QueueEntry{ID:id,Text:message,ClientUserMessageID:id};c.queue=append(c.queue,entry);c.notify();return entry,nil}
func (c *manualBrowserCodex) DeleteQueueEntry(_ context.Context,_,id string)error{c.lock.Lock();defer c.lock.Unlock();for i,e:=range c.queue{if e.ID==id{c.queue=append(c.queue[:i],c.queue[i+1:]...);break}};c.notify();return nil}
func (c *manualBrowserCodex) StartQueue(ctx context.Context,thread,id string)error{c.lock.Lock();if len(c.queue)==0{c.lock.Unlock();return nil};e:=c.queue[0];c.queue=c.queue[1:];c.lock.Unlock();_,err:=c.Send(ctx,thread,e.Text,e.ClientUserMessageID,"");return err}
func (c *manualBrowserCodex) Subscribe(_ context.Context,_ string)(<-chan struct{},func(),error){return c.changes,func(){},nil}
func (c *manualBrowserCodex) PromptsWithItems(_ context.Context,thread string)([]codex.Prompt,error){
 c.lock.Lock();defer c.lock.Unlock();if !c.prompts{return nil,nil}
 opts:=[]codex.Option{{Label:"Use the local repository",Description:strings.Repeat("Keep changes available for local review. ",8)},{Label:"Use a separate branch",Description:strings.Repeat("Preserve an independent comparison. ",8)},{Label:"Keep the current setting",Description:strings.Repeat("Continue with the saved configuration. ",8)}}
 return []codex.Prompt{{ID:"question-1",Kind:"userInput",Method:"item/tool/requestUserInput",ThreadID:thread,AuthorityAvailable:true,IsBlocking:true,Questions:[]codex.Question{{ID:"choice",Header:"Repository",Question:"How should this repository be reviewed?",IsOther:true,Options:opts},{ID:"layout",Header:"Layout",Question:"Which comparison layout should be used?",IsOther:true,Options:opts}}}},nil
}
func (c *manualBrowserCodex) RespondAnswers(ctx context.Context,id,thread string,answers map[string]map[string][]string)error{
 if err:=c.browserContractCodex.RespondAnswers(ctx,id,thread,answers);err!=nil{return err};c.lock.Lock();c.prompts=false;c.busy=false;c.lock.Unlock();c.notify();return nil
}
func (c *manualBrowserCodex) ReadActivity(_ context.Context,thread string)(codex.ActivitySnapshot,error){
 c.lock.Lock();defer c.lock.Unlock();if c.activityReads==nil{c.activityReads=map[string]int{}};c.activityReads[thread]++;state:="idle";if c.busy{state="working"};if c.prompts{state="waiting"};now:=time.Now().UnixMilli()
 return codex.ActivitySnapshot{ThreadID:thread,Messages:3,ToolCalls:7,StartedAtMS:now-76000,WorkingMS:60000,WaitingMS:10000,BetweenTurnsMS:120000,OpenWaitingMS:5000,ObservedAtMS:now,CurrentState:state,StateSinceMS:now-5000,Scope:"thread",CoverageComplete:true},nil
}

func TestManualBrowserFixture(t *testing.T) {
 if os.Getenv("PORTAL_BROWSER_FIXTURE")=="" {t.Skip("manual browser fixture")}
 server:=newTestServer(t)
 server.config.CodexVersion="0.154.0"
 directory:=filepath.Join(server.config.Workspace,"work","example")
 if err:=os.MkdirAll(directory,0755);err!=nil{t.Fatal(err)}
 manifest:="schema: 1\nslug: example\ncodex:\n  thread_id: thread-1\n  socket_path: /run/dev-workspace-codex/app-server.sock\n  client_version: 0.154.0\ncreation:\n  state: ready\n  initial_goal_sent: true\n"
 if err:=os.WriteFile(filepath.Join(directory,"portal.yml"),[]byte(manifest),0644);err!=nil{t.Fatal(err)}
 writeWebTrackingFiles(t,directory,"active");writeWebRuntimeAuthority(t,server,"example")
 for _, path := range []string{filepath.Join(server.config.AuthorityDir,"example.json"),server.config.Tmux} {
  data,err:=os.ReadFile(path);if err!=nil{t.Fatal(err)}
  if err:=os.WriteFile(path,[]byte(strings.ReplaceAll(string(data),"0.152.1","0.154.0")),0600);err!=nil{t.Fatal(err)}
 }
 server.config.VerifyThread=func(_ context.Context,thread,cwd string)error{
  slug:="example";if thread=="archived-thread"{slug="finished-example"}else if thread!="thread-1"{return fmt.Errorf("unexpected fixture thread")}
  if cwd!=filepath.Join(server.config.Workspace,"work",slug){return fmt.Errorf("unexpected fixture working directory")};return nil
 }

 archived:=filepath.Join(server.config.Workspace,"archive","finished-example");os.MkdirAll(archived,0755);writeWebTrackingFiles(t,archived,"complete");os.WriteFile(filepath.Join(archived,"portal.yml"),[]byte("schema: 1\nslug: finished-example\ncodex:\n  thread_id: archived-thread\n  socket_path: /run/dev-workspace-codex/app-server.sock\n  client_version: 0.154.0\nfinalized_at: '2026-09-10T12:00:00Z'\n"),0644)
 client:=&manualBrowserCodex{browserContractCodex:&browserContractCodex{},verify:server.config.VerifyThread,changes:make(chan struct{},20)}
 for i:=0;i<50;i++{
  client.entries=append(client.entries,client.entry("userMessage",fmt.Sprintf("Check item %d and explain the results.",i),fmt.Sprintf("user-%d",i)))
  entry:=client.entry("agentMessage",fmt.Sprintf("Result %d: the fixture data is ready for review.\n\nThis paragraph gives the conversation enough height to check scrolling and preserve the reading position during updates.",i),fmt.Sprintf("agent-%d",i));if i<25{entry["timestamp"]="2026-09-10T09:15:00Z"};if i==3{entry["timestampApproximate"]=true};client.entries=append(client.entries,entry)
  client.entries=append(client.entries,map[string]any{"turnId":"turn-1","itemId":fmt.Sprintf("command-%d",i),"kind":"commandExecution","summary":"$ ruby test/check.rb","details":"Checks passed\n"+strings.Repeat("fixture output\n",10),"timestamp":time.Now().UTC().Format(time.RFC3339)})
 }
 client.entries=append(client.entries,map[string]any{"kind":"webSearch","summary":"Web search","itemId":"search-1","activity":map[string]any{"queries":[]string{"CodeMirror maintained repository"},"links":[]map[string]any{{"url":"https://codemirror.net/","title":"CodeMirror"}}}},map[string]any{"kind":"collabAgentToolCall","itemId":"agent-call-1","summary":"Agent: spawn","activity":map[string]any{"status":"completed","agents":[]map[string]any{{"threadId":"child-1","status":"completed","message":"Review completed with no findings."}}}})
 server.config.Codex=client
 httpServer:=httptest.NewUnstartedServer(nil)
 server.config.BaseURL="http://"+httpServer.Listener.Addr().String()
 var err error
 server.conversation,err=conversation.NewHandler(conversation.Options{AllowedOrigins:[]string{server.config.BaseURL},BasePath:"/codex",Shutdown:server.stopping,Resolver:conversation.ResolverFunc(server.resolveConversation)})
 if err!=nil{t.Fatal(err)}
 handler:=server.Handler(); stop:=make(chan struct{})
 httpServer.Config.Handler=http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
  if !strings.HasPrefix(r.URL.Path,"/fixture/"){handler.ServeHTTP(w,r);return}
  switch strings.TrimPrefix(r.URL.Path,"/fixture/"){
  case "push":client.lock.Lock();client.entries=append(client.entries,client.entry("agentMessage","Background update "+time.Now().Format("15:04:05"),fmt.Sprintf("background-%d",len(client.entries))));client.lock.Unlock();client.notify()
  case "queue":client.lock.Lock();client.busy=true;for i:=0;i<20;i++{client.queue=append(client.queue,codex.QueueEntry{ID:fmt.Sprintf("queue-%d",i),Text:fmt.Sprintf("Queued work item %d: inspect another part of the fixture and report the result.",i),ClientUserMessageID:fmt.Sprintf("queue-%d",i)})};client.lock.Unlock();client.notify()
  case "approval":client.lock.Lock();client.prompts=true;client.busy=true;client.lock.Unlock();client.notify()
  case "answers":client.mu.Lock();data,_:=json.Marshal(client.answers);client.mu.Unlock();w.Header().Set("Content-Type","application/json");w.Write(data);return
  case "activity-reads":client.lock.Lock();data,_:=json.Marshal(client.activityReads);client.lock.Unlock();w.Header().Set("Content-Type","application/json");w.Write(data);return
  case "clear":client.lock.Lock();client.queue=nil;client.prompts=false;client.busy=false;client.lock.Unlock();client.notify()
  case "artifact":os.WriteFile(filepath.Join(directory,"evidence.txt"),[]byte("Live artifact added after page load.\n"),0644);os.WriteFile(filepath.Join(directory,"portal.yml"),[]byte(manifest+"artifacts:\n- label: Live evidence\n  path: evidence.txt\n"),0644)
  case "session":d:=filepath.Join(server.config.Workspace,"work","new-example");os.MkdirAll(d,0755);writeWebTrackingFiles(t,d,"active");os.WriteFile(filepath.Join(d,"portal.yml"),[]byte("schema: 1\nslug: new-example\n"),0644)
  case "stop":select{case<-stop:default:close(stop)}
  }
  w.Header().Set("Content-Type","application/json");w.Write([]byte("{}"))
 })
 httpServer.Start()
 data,_:=json.Marshal(map[string]string{"url":httpServer.URL,"workspace":server.config.Workspace})
 if err:=os.WriteFile(os.Getenv("PORTAL_BROWSER_FIXTURE"),data,0600);err!=nil{t.Fatal(err)}
 <-stop
 server.Close();httpServer.Close()
}
