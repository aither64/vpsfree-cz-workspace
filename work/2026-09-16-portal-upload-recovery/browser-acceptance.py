#!/usr/bin/env python3
"""Real Firefox acceptance against the isolated, actual portal upload service."""
import json, os, ssl, urllib.request
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

root=Path(__file__).resolve().parent
info=json.loads((root/'browser-fixture.json').read_text());base=info['url']
opts=Options();opts.add_argument('-headless');opts.binary_location=str(root/'browser-tools/bin/firefox')
opts.accept_insecure_certs=True;opts.set_capability('webSocketUrl',True)
d=webdriver.Firefox(options=opts,service=Service(executable_path=str(root/'browser-tools/bin/geckodriver'),log_output=str(root/'geckodriver.log')))
checks=[]
context=ssl._create_unverified_context()
def request(path):
 return json.loads(urllib.request.urlopen(base+path,context=context).read())
def wait(fn):return WebDriverWait(d,30,ignored_exceptions=(StaleElementReferenceException,IndexError)).until(fn)
def mark(label):checks.append(label);print('PASS '+label,flush=True)
def cards(area):return d.find_elements(By.CSS_SELECTOR,area+' .codex-attachment')
def add(form,name,content='Synthetic email body\n'):
 d.execute_script('const dt=new DataTransfer();dt.items.add(new File([arguments[2]],arguments[1]));document.querySelector(arguments[0]).dispatchEvent(new DragEvent("drop",{bubbles:true,cancelable:true,dataTransfer:dt}));',form,name,content)
def remove(area,index=0):
 card=cards(area)[index]
 next(button for button in card.find_elements(By.TAG_NAME,'button') if button.text=='Remove').click()
def saved():return d.execute_script('return Object.entries(localStorage).filter(([k])=>k.startsWith("workspace-portal.upload-draft.")).flatMap(([k,v])=>JSON.parse(v).map(x=>({key:k,...x})))')
def fetch_json(path,method='GET'):
 result=d.execute_async_script('const done=arguments[arguments.length-1];fetch(arguments[0],{method:arguments[1]}).then(async r=>done({status:r.status,body:await r.text(),disposition:r.headers.get("Content-Disposition")})).catch(e=>done({error:String(e)}));',path,method)
 assert result.get('status') in (200,201),result
 return result
try:
 for path,form,area,submit in [('/example/','#message-form','#message-uploads','#message-send'),('/','#new-session-form','#creation-uploads','#new-session-form button[type=submit]')]:
  request('/fixture/baseline')
  d.get(base+path);wait(lambda _:d.find_elements(By.CSS_SELECTOR,'.codex-upload-toggle') and not d.find_element(By.CSS_SELECTOR,'.codex-upload-toggle').get_property('disabled'))
  add(form,'invalid\nsubject.eml')
  wait(lambda _:len(cards(area))==1 and 'control characters' in cards(area)[0].text)
  before=request('/fixture/stats')['creates'];remove(area)
  wait(lambda _:request('/fixture/stats')['creates']>before)
  assert len(cards(area))==1
  request('/fixture/current');d.refresh()
  wait(lambda _:len(cards(area))==1 and 'Choose file to retry' in cards(area)[0].text)
  remove(area);wait(lambda _:not cards(area));d.refresh();wait(lambda _:d.find_elements(By.CSS_SELECTOR,'.codex-upload-toggle') and not d.find_element(By.CSS_SELECTOR,'.codex-upload-toggle').get_property('disabled'))
  assert not cards(area);mark(path+' warmed baseline failed draft clears after upgrade and reload')

  for width,height in [(1280,900),(390,844)]:
   d.browsing_context.set_viewport(context=d.current_window_handle,viewport={'width':width,'height':height})
   good='Mail \\\' OR "1"=1; <img onerror=alert(1)> žluťoučký.eml'
   add(form,good)
   wait(lambda _:len(cards(area))==1 and 'Ready' in cards(area)[0].text)
   assert cards(area)[0].find_element(By.TAG_NAME,'span').text==good
   assert not cards(area)[0].find_elements(By.TAG_NAME,'img')
   entry=next(x for x in saved() if x['name']==good)
   data=fetch_json(entry['downloadUrl'])
   assert data['body']=='Synthetic email body\n'
   assert data['disposition'].startswith('attachment;')
   mark(path+f' {width}px special filename stays literal and downloaded bytes match')
   # The rejected card must not remove the ready neighbor or block later input.
   add(form,'rejected\tname.eml')
   wait(lambda _:len(cards(area))==2 and 'control characters' in cards(area)[1].text)
   assert d.find_element(By.CSS_SELECTOR,submit).get_property('disabled')
   before=request('/fixture/stats')['creates'];d.refresh()
   wait(lambda _:len(cards(area))==2 and 'control characters' in cards(area)[1].text)
   if width==390:d.save_screenshot(str(root/('uploads-conversation.png' if path!='/' else 'uploads-creation.png')))
   remove(area,1);wait(lambda _:len(cards(area))==1)
   assert request('/fixture/stats')['creates']==before
   assert not d.find_element(By.CSS_SELECTOR,submit).get_property('disabled')
   d.refresh();wait(lambda _:len(cards(area))==1 and 'Ready' in cards(area)[0].text)
   mark(path+f' {width}px rejected removal survives reload and preserves ready selection')
   # Delete bytes independently, then verify the stale local card is removable.
   fetch_json(entry['deleteUrl'],'DELETE');d.refresh()
   wait(lambda _:len(cards(area))==1 and 'expired or was removed' in cards(area)[0].text)
   remove(area);wait(lambda _:not cards(area));d.refresh();wait(lambda _:d.find_elements(By.CSS_SELECTOR,'.codex-upload-toggle') and not d.find_element(By.CSS_SELECTOR,'.codex-upload-toggle').get_property('disabled'))
   assert not cards(area);mark(path+f' {width}px expired file clears durably')
   assert d.execute_script('return document.documentElement.scrollWidth<=innerWidth'), 'horizontal overflow'
  # Older assets can still load and remove an acknowledged draft from new assets.
  add(form,'rollback\\subject.eml');wait(lambda _:len(cards(area))==1 and 'Ready' in cards(area)[0].text)
  request('/fixture/baseline');d.refresh();wait(lambda _:len(cards(area))==1 and 'Ready' in cards(area)[0].text)
  remove(area);wait(lambda _:not cards(area));request('/fixture/current');d.refresh()
  wait(lambda _:d.find_elements(By.CSS_SELECTOR,'.codex-upload-toggle') and not d.find_element(By.CSS_SELECTOR,'.codex-upload-toggle').get_property('disabled'));assert not cards(area)
  mark(path+' old browser assets read and remove acknowledged new draft')
 (root/'browser-results.json').write_text(json.dumps({'checks':checks,'count':len(checks)},indent=2)+'\n')
finally:
 d.quit()
