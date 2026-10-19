from pathlib import Path
import json, subprocess, time
root=Path(__file__).resolve().parent
source=root.parents[1]/"worktrees"/root.name/"workspace"
command=["nix","build","--no-link","--print-out-paths","--print-build-logs",".#default"]
started=time.monotonic()
with (root/"application-build.log").open("w") as err, (root/"application-build.stdout").open("w") as out:
 process=subprocess.run(command,cwd=source,stdout=out,stderr=err)
result={"exitStatus":process.returncode,"elapsed":time.monotonic()-started,"revision":subprocess.check_output(["git","rev-parse","HEAD"],cwd=source,text=True).strip()}
(root/"application-build-result.json").write_text(json.dumps(result)+"\n")
print(json.dumps(result))
raise SystemExit(process.returncode)
