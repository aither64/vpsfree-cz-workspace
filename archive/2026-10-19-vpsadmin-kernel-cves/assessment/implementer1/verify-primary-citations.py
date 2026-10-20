import base64,concurrent.futures,datetime,hashlib,json,pathlib,re,time,urllib.request,urllib.error
P=pathlib.Path('assessment/implementer1');W=pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories');REV='56fdb3bed3f95b64b83c9f1a42ccb603452ec5c9';ids=json.load(open('assessment/packages.json'))['groups']['implementer1'];O=P/'primary-citation-verification';O.mkdir(exist_ok=True)
def get(url):
 req=urllib.request.Request(url,headers={'User-Agent':'vpsFree-security-source-verification/1.0'})
 for attempt in range(4):
  try:
   time.sleep(0.6)
   with urllib.request.urlopen(req,timeout=30) as response:return response.status,response.read(),response.geturl()
  except urllib.error.HTTPError as e:
   if e.code!=429 or attempt==3:raise
   delay=max(int(e.headers.get('Retry-After','0') or '0'),10*(attempt+1));print('HTTP429 backoff',delay,'seconds',flush=True);time.sleep(min(delay,50))
def check(c):
 receipt=O/(c+'.receipt.json')
 if receipt.exists():return json.loads(receipt.read_text())
 analysis=W/'advisories'/c/'analysis.md';raw=analysis.read_bytes();text=raw.decode();urls=sorted(set(re.findall(r'https://github\.com/CVEProject/cvelistV5/blob/'+REV+r'/[^\s)]+',text)));assert len(urls)==1,(c,urls)
 retained=pathlib.Path('research/cve-evidence/records')/(c+'.json');original=retained.read_bytes();own=(P/'primary'/c/'record.json').read_bytes();assert own==original,c
 human='https://kernel.googlesource.com/pub/scm/linux/security/vulns/+/'+REV+'/cve/published/2026/'+c+'.json';data=human+'?format=TEXT'
 hs,html,hu=get(human);ds,encoded,du=get(data);decoded=base64.b64decode(encoded,validate=False);assert decoded==original,(c,'record bytes differ');assert c in html.decode();assert json.loads(decoded)['cveMetadata']['cveId']==c
 (O/(c+'.json')).write_bytes(decoded)
 row={'cve':c,'analysis_path':str(analysis),'analysis_sha256_before':hashlib.sha256(raw).hexdigest(),'old_url':urls[0],'old_occurrences':text.count(urls[0]),'replacement_url':human,'replacement_http_status':hs,'replacement_final_url':hu,'html_response_sha256':hashlib.sha256(html).hexdigest(),'verification_url':data,'verification_http_status':ds,'verification_final_url':du,'retained_record_path':str(retained),'verified_record_path':str(O/(c+'.json')),'retained_sha256':hashlib.sha256(original).hexdigest(),'decoded_sha256':hashlib.sha256(decoded).hexdigest(),'bytes':len(decoded),'exact_bytes_match':True,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 receipt.write_text(json.dumps(row,indent=2)+'\n');return row
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as ex:
 for future in concurrent.futures.as_completed([ex.submit(check,c) for c in ids]):
  row=future.result();rows.append(row);print(row['cve'],'HTML/TEXT200 exactbytes',flush=True)
rows.sort(key=lambda r:ids.index(r['cve']));assert all(hashlib.sha256(pathlib.Path(r['analysis_path']).read_bytes()).hexdigest()==r['analysis_sha256_before'] for r in rows),'Frozen analyses changed during preparation'
out={'schema':1,'status':'prepared_only_dossiers_and_git_frozen','source_repository':'https://kernel.googlesource.com/pub/scm/linux/security/vulns','source_revision':REV,'frozen_source_head_lead':'34ad7d (not queried or mutated)','diagnosis':'Linux security/vulns revision was incorrectly used in CVEProject GitHub blob URLs. Exact Gitiles provider/path replacements preserve the already-reviewed snapshot bytes.','counts':{'cves':len(rows),'broken_occurrences':sum(r['old_occurrences'] for r in rows),'replacement_human_urls_200':sum(r['replacement_http_status']==200 for r in rows),'replacement_text_urls_200':sum(r['verification_http_status']==200 for r in rows),'exact_byte_matches':sum(r['exact_bytes_match'] for r in rows)},'rows':rows,'mutation_scope':'Only assessment/implementer1 citation verification scripts/receipts downloaded records written. No source/dossier/evaluation/Git/API/collection mutation, no fresh CVE search, draft-sync packet untouched.'}
(P/'primary-citation-fix-preparation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out['counts']))
