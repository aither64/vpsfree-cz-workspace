from pathlib import Path
import json,subprocess,time
root=Path(__file__).resolve().parent
configuration=root.parents[1]/"worktrees"/root.name/"vpsfree-cz-configuration"
command=["nix","develop","--command","dev-session","coordination","prepare",root.name,"--as-is","--request",str(root/"machine_activate-prepare-2-request.json"),"--json"]
started=time.monotonic()
with (root/"machine_activate-prepare-2.stdout").open("w") as out,(root/"machine_activate-prepare-2.log").open("w") as err:
 process=subprocess.run(command,cwd=configuration,stdout=out,stderr=err)
result={"exitStatus":process.returncode,"elapsed":time.monotonic()-started}
(root/"machine_activate-prepare-2-result.json").write_text(json.dumps(result)+"\n")
print(json.dumps(result))
raise SystemExit(process.returncode)
