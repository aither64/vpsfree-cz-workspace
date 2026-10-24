#!/usr/bin/env python3
import pathlib,sys
p=pathlib.Path(sys.argv[1]);s=p.read_text()
for sha in ["ae1f7a0"]:
 s=s.replace("pick "+sha,"edit "+sha)
p.write_text(s)
