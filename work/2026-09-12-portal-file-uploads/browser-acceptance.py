#!/usr/bin/env python3
"""Post-review browser upload acceptance against an isolated portal fixture."""
import hashlib,json,os,ssl,tempfile,time,urllib.request
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

root=Path(__file__).parent
info=json.loads(Path(os.environ['PORTAL_UPLOAD_BROWSER_FIXTURE']).read_text())
base=info['url']
tools=Path('/tmp/portal-uploads-browser-tools/bin')
opts=Options();opts.add_argument('-headless');opts.binary_location=str(tools/'firefox')
opts.accept_insecure_certs=True;opts.set_capability('webSocketUrl',True)
d=webdriver.Firefox(options=opts,service=Service(executable_path=str(tools/'geckodriver'),log_output='/tmp/portal-uploads-geckodriver.log'))
checks=[];metrics={};errors=[]
context=ssl._create_unverified_context()
def fixture(action):return urllib.request.urlopen(base+'/fixture/'+action,context=context).read()
def wait(fn,seconds=30):return WebDriverWait(d,seconds).until(fn)
def mark(label):checks.append(label);print('PASS '+label,flush=True)
def ready():return d.execute_script('return !document.querySelector("#message-send").disabled')
def cards():return d.find_elements(By.CSS_SELECTOR,'#message-uploads .codex-attachment')
def select(path):d.find_element(By.CSS_SELECTOR,'#message-uploads input[type=file]').send_keys(str(path))
def viewport(w,h):d.browsing_context.set_viewport(context=d.current_window_handle,viewport={'width':w,'height':h})
def digest_file(path):
 h=hashlib.sha256()
 with open(path,'rb') as f:
  for chunk in iter(lambda:f.read(4<<20),b''):h.update(chunk)
 return h.hexdigest()
try:
 with tempfile.TemporaryDirectory(prefix='portal-upload-inputs-',dir='/tmp') as directory:
  files=Path(directory);small=files/'evidence.txt';small.write_text('Known upload content.\n')
  medium=files/'resume.bin'
  with medium.open('wb') as f:f.write(b'A'*(4<<20));f.write(b'B'*(4<<20));f.write(b'C'*(4<<20))
  large=files/'one-gib.bin'
  with large.open('wb') as f:f.write(b'Upload acceptance\n');f.seek((1<<30)-1);f.write(b'Z')
  viewport(1280,900);d.get(base+'/example/');wait(lambda _:ready())
  select(small);wait(lambda _:len(cards())==1 and ready());mark('picker upload becomes ready')
  d.execute_script('const dt=new DataTransfer();dt.items.add(new File(["Dropped content"],"dropped.txt"));document.querySelector("#message-form").dispatchEvent(new DragEvent("drop",{bubbles:true,cancelable:true,dataTransfer:dt}));')
  wait(lambda _:len(cards())==2 and ready());mark('drag and drop adds another file')
  cards()[1].find_element(By.TAG_NAME,'button').click();wait(lambda _:len(cards())==1 and ready());mark('draft removal reclaims selection')
  d.find_element(By.ID,'message-send').click();wait(lambda _:not cards())
  wait(lambda _:len(d.find_elements(By.CSS_SELECTOR,'#transcript .codex-attachment'))==1)
  sent=d.find_element(By.CSS_SELECTOR,'#transcript .codex-attachment')
  link=sent.find_element(By.TAG_NAME,'a').get_attribute('href')
  assert urllib.request.urlopen(link,context=context).read()==small.read_bytes();mark('attachment-only send and exact downloaded bytes')
  assert 'Attached local files' not in d.find_element(By.ID,'transcript').text
  wait(lambda _:not d.find_element(By.ID,'message-receipts').is_displayed());mark('attachment receipt resolves without exposing generated path prose')
  fixture('slow');select(medium);wait(lambda _:len(cards())==1)
  wait(lambda _:'%' in cards()[0].text and cards()[0].find_element(By.TAG_NAME,'progress').get_attribute('value')!='0')
  d.refresh();wait(lambda _:len(cards())==1 and 'Choose file to resume' in cards()[0].text)
  assert not ready();fixture('fast')
  cards()[0].find_element(By.TAG_NAME,'button').click();select(medium)
  wait(lambda _:ready(),60);mark('reload pauses and reselect resumes verified upload')
  fixture('busy');wait(lambda _:d.find_element(By.ID,'message-queue').is_displayed())
  d.find_element(By.CSS_SELECTOR,'#message-form textarea').send_keys('Use this file next')
  d.find_element(By.ID,'message-queue').click();wait(lambda _:not cards())
  wait(lambda _:len(d.find_elements(By.CSS_SELECTOR,'#queue-list .codex-attachment'))==1);mark('queue shows attached file')
  d.find_element(By.CSS_SELECTOR,'#queue-list .queue-remove').click();wait(lambda _:not d.find_elements(By.CSS_SELECTOR,'#queue-list li'));fixture('idle')
  select(small);wait(lambda _:ready())
  fixture('busy');wait(lambda _:d.find_element(By.ID,'message-queue').is_displayed())
  d.find_element(By.CSS_SELECTOR,'#message-form textarea').send_keys('Read while working')
  d.find_element(By.ID,'message-send').click();wait(lambda _:not cards())
  wait(lambda _:len(d.find_elements(By.CSS_SELECTOR,'#transcript .codex-attachment'))==2);mark('active-turn steering carries file')
  d.execute_script('window.acceptanceConfirmations=[];window.confirm=message=>{window.acceptanceConfirmations.push(message);return true;}')
  first=d.find_elements(By.CSS_SELECTOR,'#transcript .codex-attachment')[0]
  d.execute_script('document.querySelector("#transcript .codex-attachment button").click()')
  wait(lambda _:'idle' in d.find_elements(By.CSS_SELECTOR,'#transcript .codex-attachment')[0].text);mark('sent deletion refuses a busy session')
  fixture('idle');time.sleep(1)
  first=d.find_elements(By.CSS_SELECTOR,'#transcript .codex-attachment')[0]
  d.execute_script('document.querySelector("#transcript .codex-attachment button").click()')
  wait(lambda _:'File removed' in d.find_elements(By.CSS_SELECTOR,'#transcript .codex-attachment')[0].text);mark('confirmed idle deletion retains removed-file card')
  assert len(d.execute_script('return window.acceptanceConfirmations'))==2
  before=json.loads(fixture('stats'));started=time.monotonic();select(large)
  max_rss=0
  wait(lambda _:any('one-gib.bin' in card.text for card in cards()))
  while not ready():
   status=Path(f'/proc/{before["pid"]}/status').read_text()
   rss=int(next(line.split()[1] for line in status.splitlines() if line.startswith('VmRSS:')))*1024
   max_rss=max(max_rss,rss)
   if time.monotonic()-started>240:raise TimeoutError('1 GiB upload')
   time.sleep(.3)
  elapsed=time.monotonic()-started;after=json.loads(fixture('stats'))
  catalog=json.loads((Path(info['uploads'])/'catalog.json').read_text())
  record=next(record for record in catalog['files'].values() if record['name']=='one-gib.bin')
  stored=Path(info['uploads'])/'files'/record['id']/'file.bin'
  assert stored.stat().st_size==1<<30
  assert digest_file(stored)==digest_file(large)
  assert max_rss<400<<20,(max_rss,before,after)
  metrics['largeUpload']={'bytes':1<<30,'seconds':elapsed,'peakServerRSS':max_rss,'before':before,'after':after}
  mark('1 GiB transfer preserves SHA-256 with bounded server memory')
  viewport(390,844);time.sleep(.2)
  layout=d.execute_script('return {width:innerWidth,scrollWidth:document.documentElement.scrollWidth,form:document.querySelector("#message-form").getBoundingClientRect().toJSON()}')
  assert layout['scrollWidth']<=390,layout
  assert layout['form']['bottom']<=844+1,layout
  metrics['narrow']=layout;d.save_screenshot(str(root/'uploads-narrow.png'));mark('narrow layout retains prompt actions')
  cards()[0].find_element(By.TAG_NAME,'button').click();wait(lambda _:not cards());assert not stored.exists()
  d.get(base+'/');wait(lambda _:len(d.find_elements(By.CSS_SELECTOR,'#creation-uploads input[type=file]'))==1)
  d.find_element(By.CSS_SELECTOR,'#creation-uploads input[type=file]').send_keys(str(small))
  wait(lambda _:'Ready' in d.find_element(By.ID,'creation-uploads').text)
  assert not d.find_element(By.CSS_SELECTOR,'#new-session-form textarea').get_attribute('required')
  d.execute_script('document.querySelector("#new-session-form").addEventListener("submit",event=>{event.preventDefault();window.acceptanceForm=[...new FormData(event.target).entries()];});')
  d.find_element(By.CSS_SELECTOR,'#new-session-form input[name=name]').send_keys('browser-upload')
  d.find_element(By.CSS_SELECTOR,'#new-session-form button[type=submit]').click()
  form=wait(lambda _:d.execute_script('return window.acceptanceForm'))
  assert len([value for key,value in form if key=='attachmentIds'])==1,form
  assert any(key=='uploadScope' and value for key,value in form),form
  mark('initial attachment-only form submits scope and opaque file IDs')
  d.save_screenshot(str(root/'uploads-initial.png'))
except BaseException:
 d.save_screenshot(str(root/"browser-failure.png"))
 (root/"browser-failure.html").write_text(d.page_source)
 raise
finally:
 d.quit()
 (root/'browser-results.json').write_text(json.dumps({'checks':checks,'metrics':metrics},indent=2)+'\n')
