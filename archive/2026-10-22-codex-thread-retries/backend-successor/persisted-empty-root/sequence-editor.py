import pathlib,sys
p=pathlib.Path(sys.argv[1]);rows=p.read_text().splitlines(True);changed=0
for i,row in enumerate(rows):
 parts=row.split()
 if len(parts)>1 and parts[0]=='pick' and '87d5b493abe1976530ee9c73fe67103263cb7328'.startswith(parts[1]): rows[i]=row.replace('pick ','reword ',1);changed+=1
assert changed==1
p.write_text(''.join(rows))
