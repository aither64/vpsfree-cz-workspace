#!/usr/bin/env python3
import sys,pathlib
p=pathlib.Path(sys.argv[1]);s=p.read_text();lines=s.splitlines();count=0
for i,line in enumerate(lines):
 if line.startswith("pick "):
  count+=1
  if count==2:lines[i]="fixup "+line[5:]
assert count==2
p.write_text("\n".join(lines)+"\n")
