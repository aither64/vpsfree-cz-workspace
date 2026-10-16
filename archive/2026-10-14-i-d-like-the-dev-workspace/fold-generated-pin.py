#!/usr/bin/env python3
import pathlib,sys
p=pathlib.Path(sys.argv[1]); s=p.read_text(); lines=s.splitlines(); picks=[i for i,x in enumerate(lines) if x.startswith("pick ")]; assert len(picks)==2; lines[picks[1]]=lines[picks[1]].replace("pick ","fixup ",1); p.write_text("\n".join(lines)+"\n")
