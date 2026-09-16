package web

import (
 "encoding/json"
 "net/http"
 "net/http/httptest"
 "os"
 "path/filepath"
 "strings"
 "sync/atomic"
 "testing"

 "github.com/aither64/codex-web/codex"
 "github.com/aither64/codex-web/conversation"
)

// Manual acceptance fixture: real portal templates, browser assets and upload
// storage, with only the unrelated App Server conversation replaced.
func TestUploadRecoveryBrowserFixture(t *testing.T) {
 output:=os.Getenv("PORTAL_UPLOAD_RECOVERY_FIXTURE"); if output=="" {t.Skip("manual acceptance")}
 server:=newTestServer(t)
 prepareInteractiveConversation(t,server,"example")
 server.config.Codex=&browserContractCodex{emptyPrompts:true,events:make(chan struct{}),transcript:codex.Transcript{
  ThreadID:"thread-1",Status:"idle",Model:"model-1",ReasoningEffort:"medium",CollaborationMode:"default",
 }}
 server.uploadStore.MinFreeBytes=0
 endpoint:=httptest.NewUnstartedServer(nil)
 server.config.BaseURL="https://"+endpoint.Listener.Addr().String()
 var err error
 server.conversation,err=conversation.NewHandler(conversation.Options{AllowedOrigins:[]string{server.config.BaseURL},BasePath:"/codex",Shutdown:server.stopping,Resolver:conversation.ResolverFunc(server.resolveConversation)})
 if err!=nil {t.Fatal(err)}
 server.uploadHandler,err=conversation.NewUploadHandler(conversation.UploadOptions{AllowedOrigins:[]string{server.config.BaseURL},BasePath:"/uploads",Resolve:server.resolveUploads})
 if err!=nil {t.Fatal(err)}
 handler:=server.Handler()
 var baseline atomic.Bool
 var creates,deletes atomic.Int64
 stop:=make(chan struct{})
 legacy:=os.Getenv("PORTAL_UPLOAD_RECOVERY_LEGACY")
 endpoint.Config.Handler=http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
  if strings.HasPrefix(r.URL.Path,"/fixture/") {
   switch strings.TrimPrefix(r.URL.Path,"/fixture/") {
   case "baseline": baseline.Store(true)
   case "current": baseline.Store(false)
   case "stats": json.NewEncoder(w).Encode(map[string]int64{"creates":creates.Load(),"deletes":deletes.Load()});return
   case "stop": close(stop)
   }
   w.Header().Set("Content-Type","application/json");w.Write([]byte("{}"));return
  }
  if baseline.Load() && legacy!="" && (r.URL.Path=="/static/app.js" || r.URL.Path=="/codex/assets/conversation.js" || r.URL.Path=="/codex/assets/uploads.js") {
   if r.URL.Path=="/static/app.js" {w.Header().Set("Cache-Control","no-store")} else {w.Header().Set("Cache-Control","public, max-age=300")}
   w.Header().Set("Content-Type","text/javascript")
   http.ServeFile(w,r,filepath.Join(legacy,filepath.Base(r.URL.Path)));return
  }
  if strings.HasPrefix(r.URL.Path,"/uploads/") {
   if r.Method=="POST" && strings.Count(r.URL.Path,"/")==2 {creates.Add(1)}
   if r.Method=="DELETE" {deletes.Add(1)}
  }
  handler.ServeHTTP(w,r)
 })
 endpoint.StartTLS()
 data,_:=json.Marshal(map[string]string{"url":endpoint.URL,"uploads":server.uploadStore.Directory})
 if err=os.WriteFile(output,data,0600);err!=nil {t.Fatal(err)}
 <-stop
 server.Close()
 endpoint.Close()
}
