#!/usr/bin/env python3
import pathlib,sys
p=pathlib.Path(sys.argv[1]);rows=[line.split() for line in p.read_text().splitlines() if line and not line.startswith('#')];expected=[('pick','605d274'),('fixup',None),('pick','42f1e9e'),('fixup','ddcf8ed'),('pick','3ab9740'),('pick','018520c'),('fixup','e617335'),('pick','34ad7d5')];assert len(rows)==8,rows
for row,(action,prefix) in zip(rows,expected):
 assert row[0]==action,(row,action)
 if prefix:assert row[1].startswith(prefix),(row,prefix)
 else:assert [x for x in row[2:] if x != '#'] == ['fixup!', '605d274310890aac5f514924d9b6566033feaee4'],row
out=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves/assessment/implementer1/history-consolidation/authorized-todo.txt');out.write_text(p.read_text())
print('Exact8todoentries verified:5original commits+3authorized fixups',flush=True)
