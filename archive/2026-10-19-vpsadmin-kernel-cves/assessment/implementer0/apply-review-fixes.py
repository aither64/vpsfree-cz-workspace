import datetime,hashlib,json,pathlib,re,subprocess
s=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves');o=s/'assessment/implementer0';w=s.parents[1]/'worktrees'/s.name/'security-advisories';prep=json.loads((o/'primary-citation-fix-preparation.json').read_text());head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=w,text=True).strip();assert head=='34ad7d5785382215cbe00b5140174cad5661a132';assert not subprocess.check_output(['git','diff','--cached','--name-only'],cwd=w,text=True).strip();baseline=[]
old='Allocator freelist hardening/randomization, allocation/free zeroing, stack initialization/protection, KASLR and FORTIFY in the archived build can raise exploit difficulty. They do not prove trigger prevention or repair this defect.'
for row in prep['rows']:
 c=row['cve'];d=w/'advisories'/c;p=d/'analysis.md';b=p.read_bytes();assert hashlib.sha256(b).hexdigest()==row['analysis_sha256_before'];text=b.decode();assert text.count(row['old_url'])==2;committed=json.loads(subprocess.check_output(['git','show',f'HEAD:advisories/{c}/evaluation.json'],cwd=w,text=True));assert committed==json.loads((d/'evaluation.json').read_text());yaml=(d/'advisory.yml').read_bytes();baseline.append(dict(cve=c,analysis_sha256=hashlib.sha256(b).hexdigest(),yaml_sha256=hashlib.sha256(yaml).hexdigest(),evaluation=committed))
 text=text.replace(row['old_url'],row['replacement_url'])
 if c in ['CVE-2026-98720','CVE-2026-89929','CVE-2026-89930','CVE-2026-89932']:
  assert text.count(old)==1,c
  if c.endswith('98720'):
   new='Allocator freelist hardening/randomization, allocation/free zeroing, stack initialization/protection, KASLR and FORTIFY in the archived build do not address the demonstrated direct access to L0\'s task-priority register. The reviewed source and reports establish no dependent exploitation step for which those settings provide relevant protection. Correct MSR-bitmap refresh repairs the defect; Intel VMX and enlightened nested-virtualization prerequisites still limit its reachability.'
  else:
   new='Allocator freelist hardening/randomization, allocation/free zeroing, stack initialization/protection, KASLR and FORTIFY in the archived build do not address this stale-translation primitive. The reviewed source and reports establish no dependent exploitation step for which those settings provide relevant protection. Correct TLB invalidation repairs the defect; hardware and nested-virtualization prerequisites still limit its reachability.'
  text=text.replace(old,new)
 assert row['old_url']not in text;assert text.count(row['replacement_url'])==2;p.write_text(text)
(o/'review-fix-baseline.json').write_text(json.dumps(dict(base_head=head,recorded_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),rows=baseline),indent=2)+'\n');print('applied40verifiedURLreplacements+4KVMparagraphs;20YAMLunchanged;committedbaselinecaptured')
