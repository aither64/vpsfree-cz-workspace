package web

import (
 "context"
 "crypto/sha256"
 "encoding/hex"
 "errors"
 "os"
 "os/exec"
 "path/filepath"
 "testing"
 "time"
)

// This fixture launches only its own disposable shell through the real user manager.
func TestArchiveWorkerLiveUserManagerRestartAcceptance(t *testing.T) {
 directory := t.TempDir()
 bin := filepath.Join(directory, "bin")
 if err := os.Mkdir(bin,0700); err != nil { t.Fatal(err) }
 script := "#!/bin/sh\nset -eu\n: > started\nwhile [ ! -e release ]; do sleep 0.1; done\n"
 if err := os.WriteFile(filepath.Join(bin,"dev-session"), []byte(script), 0700); err != nil { t.Fatal(err) }
 digest := sha256.Sum256([]byte(directory))
 operation := lifecycleOperation{Slug:"disposable-acceptance",Kind:"archive",State:"running",ReceiptID:hex.EncodeToString(digest[:]),Attempt:1}
 unit := archiveUnit(operation)
 t.Cleanup(func(){ exec.Command("systemctl","--user","stop",unit).Run(); exec.Command("systemctl","--user","reset-failed",unit).Run() })
 config := Config{Workspace:directory,WorkspaceName:"disposable-acceptance",HostProfile:directory,PackageRoot:directory,UserStateRoot:directory}
 server := &Server{config:config,operations:map[string]lifecycleOperation{operation.Slug:operation}}
 ctx,cancel := context.WithCancel(context.Background())
 defer cancel()
 done := make(chan error,1)
 go func(){done<-server.runSupervisedArchive(ctx,operation.Slug,[]string{"archive",operation.Slug,"--as-is"})}()
 deadline := time.Now().Add(15*time.Second)
 for {
  if _,err:=os.Stat(filepath.Join(directory,"started")); err==nil {break}
  select {case err:=<-done:t.Fatalf("worker launch: %v",err); default:}
  if time.Now().After(deadline){t.Fatal("owned test helper did not start")}
  time.Sleep(50*time.Millisecond)
 }
 cancel()
 if err:=<-done;!errors.Is(err,context.Canceled){t.Fatalf("portal cancellation: %v",err)}
 restarted := &Server{config:config,operations:map[string]lifecycleOperation{operation.Slug:operation}}
 status,err := restarted.archiveWorker(context.Background(),operation)
 if err!=nil || status==nil || status.State!="running" {t.Fatalf("worker after observer restart: %#v, %v",status,err)}
 if err:=os.WriteFile(filepath.Join(directory,"release"),nil,0600);err!=nil{t.Fatal(err)}
 for {
  status,err=restarted.archiveWorker(context.Background(),operation)
  if err!=nil {t.Fatal(err)}
  if status!=nil && status.State=="complete" {break}
  if time.Now().After(deadline){t.Fatalf("owned test helper result: %#v",status)}
  time.Sleep(50*time.Millisecond)
 }
 if status.FinishedAt=="" {t.Fatal("real systemd finish timestamp was not decoded")}
 t.Logf("real user unit %s survived observer cancellation and was recovered as complete at %s",unit,status.FinishedAt)
}
