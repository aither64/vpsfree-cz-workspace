import json,sys
x=json.load(open(sys.argv[1]));d=x.get('derivations',x);result={}
for key,value in d.items():
 key=key if key.startswith('/') else '/nix/store/'+key
 for output in value['outputs'].values():
  if 'path' in output and not output['path'].startswith('/'):output['path']='/nix/store/'+output['path']
 result[key]=value
print(json.dumps(result,indent=2))
