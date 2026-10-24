import pathlib,sys
p=pathlib.Path(sys.argv[1]);s=p.read_text();rows=s.splitlines(True);changed=0
for i,row in enumerate(rows):
 parts=row.split()
 if len(parts)>1 and parts[0]=="pick" and "62308a7f640389a1d8d5b4a12b568e5b752235c4".startswith(parts[1]): rows[i]=row.replace("pick ","reword ",1);changed+=1
assert changed==1
p.write_text("".join(rows))
