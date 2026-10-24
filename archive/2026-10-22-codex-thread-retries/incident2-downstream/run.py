import datetime,json,os,pathlib,subprocess,sys,time
name,cwd,*argv=sys.argv[1:]
r=pathlib.Path(__file__).parent
env=os.environ.copy();env.update(DEV_SESSION_SLUG="2026-10-22-codex-thread-retries",DEV_SESSION_WORKSPACE="/home/aither/workspace/ai/vpsfree.cz")
start=time.monotonic()
(r/(name+".command.json")).write_text(json.dumps({"argv":argv,"cwd":cwd,"time":datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2)+"\n")
with (r/(name+".stdout")).open("w") as out,(r/(name+".stderr")).open("w") as err:
 p=subprocess.run(argv,cwd=cwd,env=env,stdout=out,stderr=err)
status={"exit":p.returncode,"elapsed":time.monotonic()-start}
(r/(name+".status.json")).write_text(json.dumps(status,indent=2)+"\n")
print(json.dumps({"name":name,**status}))
print((r/(name+".stdout")).read_text()[-3500:])
print((r/(name+".stderr")).read_text()[-3500:])
sys.exit(p.returncode)
