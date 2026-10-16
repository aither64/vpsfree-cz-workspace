#!/usr/bin/env python3
"""Prepare an owned short-path attempt only after final committed review."""
import json,os,shlex,subprocess,sys,tempfile
from pathlib import Path
record=Path(__file__).resolve().parent
product=record.parents[1]/"worktrees"/record.name/"vpsadminos"
head=(record/"compatibility-final-head").read_text().strip()
def git(*args):return subprocess.check_output(["git",*args],cwd=product,text=True).strip()
assert git("rev-parse","HEAD")==head
assert git("status","--porcelain")==""
assert (record/"compatibility-review-runtime-clearance").read_text().strip()==head
pattern=sys.argv[1] if len(sys.argv)>1 else "dist-config/nixos-persistence-upgrade#*"
assert pattern in ["dist-config/nixos-persistence-upgrade#*", "dist-config/nixos-persistence-upgrade#upgrade-26.05"]
attempt=Path(tempfile.mkdtemp(prefix="runtime-attempt.",dir=record))
state=Path(tempfile.mkdtemp(prefix="ni.",dir="/tmp"))
owner={"session":record.name,"workspace":str(record.parents[1]),"uid":os.getuid(),"source":str(product),"head":head,"tree":git("rev-parse","HEAD^{tree}"),"state_dir":str(state),"patterns":[pattern]}
(attempt/"ownership.json").write_text(json.dumps(owner,indent=2)+"\n")
(attempt/"state-dir").write_text(str(state)+"\n")
(attempt/"host-metadata.nix").write_text('{ system.vpsadminos = { revision = "'+head+'"; revisionDirty = false; versionSuffix = ".git.'+head[:9]+'"; }; }\n')
command="./test-runner.sh test --state-dir "+str(state)+" --test-config "+str(record/"image-test-config.nix")+" --no-destructive --jobs 1 "+shlex.quote(pattern)
(attempt/"command.txt").write_text(command+"\n")
(record/"compatibility-runtime-attempt").write_text(str(attempt)+"\n")
print(json.dumps(owner))
