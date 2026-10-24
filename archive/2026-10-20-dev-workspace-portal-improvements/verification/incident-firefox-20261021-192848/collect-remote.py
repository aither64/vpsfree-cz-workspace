import os,re,json,datetime,shlex,collections,subprocess,urllib.parse,hashlib,signal
signal.alarm(25)
UTC=datetime.timezone.utc
IP='172.16.107.34'
START=datetime.datetime(2026,10,21,18,20,tzinfo=UTC)
END=datetime.datetime(2026,10,21,19,35,tzinfo=UTC)
RESET=datetime.datetime(2026,10,21,19,28,48,tzinfo=UTC)
now=datetime.datetime.now(UTC)
unit='/etc/systemd/system/nginx.service'
u=open(unit).read()
a=shlex.split(re.search(r'^ExecStart=(.+)$',u,re.M).group(1))
conf=a[a.index('-c')+1]
s=open(conf).read()
meta={'capture_utc':now.isoformat(),'window_utc':[START.isoformat(),END.isoformat()],'window_cest':['2026-10-21T20:20:00+02:00','2026-10-21T21:35:00+02:00'],'recovery_anchor_utc':RESET.isoformat(),'client_ip':IP,'config_path':conf,'config_sha256':hashlib.sha256(s.encode()).hexdigest(),'unit_path':os.path.realpath(unit),'log_formats':[{'name':m.group(1),'fields':re.findall(r'\$\w+|\$\{[^}]+\}',m.group(2))} for m in re.finditer(r'\blog_format\s+(\S+)\s+(.*?);',s,re.S)],'access_log_directives':re.findall(r'^\s*access_log\s+([^;]+);',s,re.M),'error_log_directives':re.findall(r'^\s*error_log\s+([^;]+);',s,re.M)}
rx=re.compile(r'^(?P<ip>\S+) (?P<ident>\S+) (?P<user>\S+) \[(?P<date>[^]]+)\] "(?P<method>\S+) (?P<target>\S+) (?P<proto>[^" ]+)" (?P<status>\d{3}) (?P<bytes>\S+) "(?P<ref>[^"\n]*)" "(?P<ua>[^"\n]*)"\s*$')
minutes=collections.defaultdict(collections.Counter)
groups=collections.Counter();phases=collections.defaultdict(collections.Counter)
firsts={};lasts={};last_before={};first_after={}
errors=[]
counts=collections.Counter()
def category(path):
 parts=path.split('/')
 if parts[-1] in ('events','stream') or path.endswith('/events/'):
  return 'sse_candidate'
 return 'ordinary'
def endpoint(path):
 last=path.rstrip('/').split('/')[-1]
 if last in {'events','stream','pending','queue','limits','activity','team','team-status','index-status','status','health','conversation','transcript','history','thread','requests','request','details','files','auth','models','settings','members','index','state'}:return last
 if last.endswith(('.js','.css','.woff','.woff2','.png','.svg','.ico','.webmanifest')):return 'static_asset'
 return 'other_redacted'
path='/var/log/nginx/access.log'
st=os.stat(path)
meta['access_file']={'inode':st.st_ino,'device':st.st_dev,'size_at_open':st.st_size,'mtime_utc':datetime.datetime.fromtimestamp(st.st_mtime,UTC).isoformat()}
with open(path,'rb') as f:
 limit=st.st_size; read_bytes=0
 for raw in f:
  read_bytes+=len(raw)
  if read_bytes>limit:break
  if not raw.startswith(IP.encode()+b' '):continue
  counts['client_lines_examined']+=1
  if b'[21/Oct/2026:20:' not in raw and b'[21/Oct/2026:21:' not in raw:continue
  line=raw.decode('utf-8','replace')
  m=rx.match(line)
  if not m:
   # No raw line, URL, ID, auth or user-agent output on parse failure.
   counts['client_combined_parse_failures']+=1;continue
  dt=datetime.datetime.strptime(m['date'],'%d/%b/%Y:%H:%M:%S %z').astimezone(UTC)
  if not START<=dt<=END:continue
  counts['window_completions']+=1
  urlpath=urllib.parse.urlsplit(m['target']).path
  cat=category(urlpath);ep=endpoint(urlpath)
  status=m['status'];proto=m['proto']
  key=(cat,ep,status,proto,m['method'])
  groups[key]+=1
  minute=dt.strftime('%Y-%m-%dT%H:%MZ')
  minutes[minute][cat]+=1
  minutes[minute]['status_'+status]+=1
  ph='before_reset' if dt<RESET else 'at_or_after_reset'
  phases[ph][cat]+=1;phases[ph]['status_'+status]+=1
  stamp=dt.isoformat()
  firsts.setdefault(cat,stamp);lasts[cat]=stamp
  if dt<RESET:last_before[cat]=stamp
  else:first_after.setdefault(cat,stamp)
  if status[0] in '45':errors.append({'completed_utc':stamp,'kind':cat,'endpoint_class':ep,'status':int(status),'protocol':proto})
  if 'Firefox/' in m['ua']:counts['window_firefox_completions']+=1
meta['access_file']['size_after_read']=os.stat(path).st_size
meta['access_file']['inode_after_read']=os.stat(path).st_ino
errpath='/var/log/nginx/error.log'
try:
 es=os.stat(errpath);meta['error_file']={'size':es.st_size,'mtime_utc':datetime.datetime.fromtimestamp(es.st_mtime,UTC).isoformat()}
except FileNotFoundError:meta['error_file']={'missing':True}
jargs=['journalctl','-u','nginx.service','--since','@'+str(int(START.timestamp())),'--until','@'+str(int(END.timestamp())),'--no-pager','-o','json','--output-fields=__REALTIME_TIMESTAMP,MESSAGE,PRIORITY','--grep='+r'172\.16\.107\.34|worker_connections are not enough|too many open files|no live upstreams|upstream timed out|\[emerg\]|\[alert\]|\[crit\]']
j=subprocess.run(jargs,text=True,capture_output=True,timeout=8)
journal=[];journal_skipped=0
patterns=[('upstream_timeout',r'upstream timed out'),('client_closed',r'client (?:prematurely )?closed'),('connection_reset',r'connection reset|reset by peer'),('upstream_closed',r'upstream (?:prematurely )?closed'),('client_timeout',r'client timed out'),('worker_limit',r'worker_connections are not enough'),('fd_limit',r'too many open files'),('no_live_upstreams',r'no live upstreams'),('goaway_text',r'GOAWAY|goaway'),('critical',r'\[(?:emerg|alert|crit)\]')]
for l in j.stdout.splitlines():
 try:obj=json.loads(l)
 except json.JSONDecodeError:journal_skipped+=1;continue
 msg=obj.get('MESSAGE','');mine=bool(re.search(r'(?<![\d.])172\.16\.107\.34(?![\d.])',msg))
 matched=[name for name,pat in patterns if re.search(pat,msg,re.I)]
 if mine or matched:
  journal.append({'time_utc':datetime.datetime.fromtimestamp(int(obj['__REALTIME_TIMESTAMP'])/1e6,UTC).isoformat(),'client_matches':mine,'classes':matched or ['other_client_message'],'priority':obj.get('PRIORITY')})
print(json.dumps({'schema':1,'metadata':meta,'counts':dict(counts),'first_completion_utc':firsts,'last_completion_utc':lasts,'last_completion_before_reset_utc':last_before,'first_completion_at_or_after_reset_utc':first_after,'phases':{k:dict(v) for k,v in phases.items()},'completion_minute_buckets_utc':{k:dict(v) for k,v in sorted(minutes.items())},'groups':[{'kind':k[0],'endpoint_class':k[1],'status':int(k[2]),'protocol':k[3],'method':k[4],'count':v} for k,v in sorted(groups.items())],'error_status_completions':errors,'journal_query':{'argv':jargs,'exit':j.returncode,'unparsed_json_lines':journal_skipped,'stderr_present':bool(j.stderr),'events':journal},'limitations':['Access timestamps are request COMPLETION times, including SSE, not stream start times.','Combined records contain no request duration/upstream timing/connection id/request ordinal/h2 stream id/GOAWAY frame or active-incomplete stream history.','Only this client and the bounded incident interval are aggregated; raw URLs, query strings, referers, user names, user agents and session identifiers are not emitted.','sse_candidate class means URL ending events or stream; status/protocol are observed, Content-Type is not in access log.','Capture may precede requested interval end; no subsequent polling is performed.']},indent=2))
