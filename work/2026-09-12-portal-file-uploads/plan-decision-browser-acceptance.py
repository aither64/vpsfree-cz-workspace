#!/usr/bin/env python3
"""Exercise current-plan selection and composer replacement in the real browser."""
import hashlib,json,os,ssl,tempfile,urllib.request
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
root=Path(__file__).parent
base=json.loads(Path(os.environ['PORTAL_PLAN_BROWSER_FIXTURE']).read_text())['url']
tools=Path('/tmp/portal-uploads-browser-tools/bin')
opts=Options();opts.add_argument('-headless');opts.binary_location=str(tools/'firefox');opts.accept_insecure_certs=True;opts.set_capability('webSocketUrl',True)
d=webdriver.Firefox(options=opts,service=Service(executable_path=str(tools/'geckodriver'),log_output='/tmp/portal-plan-geckodriver.log'))
checks=[];metrics={}
def wait(fn):return WebDriverWait(d,30).until(fn)
def js(code,*args):return d.execute_script(code,*args)
def el(selector):return d.find_element(By.CSS_SELECTOR,selector)
def fixture(action):return urllib.request.urlopen(base+'/fixture/'+action,context=ssl._create_unverified_context()).read()
def mark(label):checks.append(label);print('PASS '+label,flush=True)
def visible(selector):return el(selector).is_displayed()
def viewport(w,h):d.browsing_context.set_viewport(context=d.current_window_handle,viewport={'width':w,'height':h})
def composer():return visible('#message-form') and not visible('#plan-actions')
def decision():return visible('#plan-actions') and not visible('#message-form')
def height(selector):return js('return document.querySelector(arguments[0]).getBoundingClientRect().height',selector)
try:
 with tempfile.TemporaryDirectory(prefix='portal-plan-inputs-',dir='/tmp') as directory:
  upload=Path(directory)/'preserved.bin';upload.write_bytes(b'preserved upload\n'*524288)
  viewport(1280,900);d.get(base+'/example/');wait(lambda _:el('#message-upload-controls button').is_enabled())
  wait(lambda _:composer())
  legacy_id='00000000-0000-4000-8000-000000000099'
  legacy_key='workspace-portal.send-attempt.example.thread-1.'+legacy_id
  plan_text='1. Inspect the code.\n2. Implement the change.\n3. Verify the result.'
  legacy={'message':'Implement the plan.','steered':False,'context':'plan:'+hashlib.sha256(plan_text.encode()).hexdigest()}
  fixture('legacy-prepared');js('sessionStorage.setItem(arguments[0],arguments[1])',legacy_key,json.dumps(legacy))
  d.refresh();wait(lambda _:el('#message-upload-controls button').is_enabled())
  wait(lambda _:js('return sessionStorage.getItem(arguments[0])===null',legacy_key))
  assert composer() and 'Implement the plan.' not in el('#transcript').text
  mark('reload retires an unsent legacy retry without approving a plan or changing mode')
  js('sessionStorage.setItem(arguments[0],arguments[1])',legacy_key,json.dumps(legacy))
  fixture('legacy-submitted')
  wait(lambda _:json.loads(fixture('recovery-status'))['waiting'])
  wait(lambda _:'Implement the plan.' in el('#transcript').text)
  wait(lambda _:json.loads(js('return sessionStorage.getItem(arguments[0])',legacy_key)).get('state')=='observed')
  fixture('release-recovery')
  wait(lambda _:js('return sessionStorage.getItem(arguments[0])===null',legacy_key))
  mark('held submitted recovery acknowledges the observed receipt without a later event')
  fixture('legacy-reset');wait(lambda _:'Implement the plan.' not in el('#transcript').text)
  el('#codex-mode button[data-codex-mode="plan"]').click()
  wait(lambda _:el('#codex-mode button[data-codex-mode="plan"]').get_attribute('aria-pressed')=='true')
  assert composer()
  mark('enabling Plan mode after an ordinary reply does not revive an earlier plan')
  el('#message-form textarea').send_keys('Preserved draft text')
  fixture('slow');el('#message-upload-controls input[type=file]').send_keys(str(upload))
  wait(lambda _:'preserved.bin' in el('#message-uploads').text)
  wait(lambda _:visible('#codex-work'))
  before=height('#transcript');fixture('plan');wait(lambda _:decision())
  assert not visible('#codex-work')
  assert not visible('#message-upload-controls') and not visible('#codex-mode')
  assert height('#transcript')>before,(before,height('#transcript'))
  metrics['desktop']={'before':before,'decision':height('#transcript')}
  # Wait for the upload to finish while its form stays hidden.
  fixture('fast');wait(lambda _:'Ready' in el('#message-uploads').get_attribute('textContent'))
  assert decision()
  d.save_screenshot(str(root/'plan-decision-desktop.png'))
  mark('desktop decision replaces the full composer, hides waiting, and upload completes while hidden')
  fixture('queue');wait(lambda _:visible('#queue-panel'))
  el('#plan-implement-new').click();wait(lambda _:visible('#plan-session-dialog'))
  el('#plan-session-dialog [data-dialog-close]').click();wait(lambda _:not visible('#plan-session-dialog'))
  assert decision() and visible('#queue-panel')
  mark('canceling new-session dialog retains the decision and queued messages')
  el('#plan-keep-planning').click();wait(lambda _:composer())
  assert js('return document.activeElement===document.querySelector("#message-form textarea")')
  assert el('#message-form textarea').get_attribute('value')=='Preserved draft text'
  assert 'preserved.bin' in el('#message-uploads').text and 'Ready' in el('#message-uploads').text
  fixture('queue');assert composer()
  mark('Keep planning restores focus, exact draft, ready upload, and survives refresh events')
  viewport(390,844)
  # A later turn with identical plan text must be offered again.
  before=height('#transcript');fixture('plan-again');wait(lambda _:decision())
  assert not visible('#codex-work') and visible('#queue-panel')
  assert js('return document.documentElement.scrollWidth')==390
  assert height('#transcript')>before,(before,height('#transcript'))
  metrics['narrow']={'before':before,'decision':height('#transcript')}
  d.save_screenshot(str(root/'plan-decision-narrow.png'))
  mark('identical plan in a newer turn reappears and gives more transcript room at 390px')
  for action in ['empty','failed','interrupted','missing','ordinary']:
   fixture(action);wait(lambda _:composer())
  mark('new empty, failed, interrupted, missing-identity and ordinary turns hide historical decisions')
  # Reload resets page-local dismissal; it must preserve composer behavior for current data.
  d.refresh();wait(lambda _:el('#message-upload-controls button').is_enabled());assert composer()
  fixture('plan');wait(lambda _:decision())
  el('#plan-implement-same').click();wait(lambda _:composer())
  wait(lambda _:'Implement the plan.' in el('#transcript').text)
  assert el('#codex-mode button[data-codex-mode="default"]').get_attribute('aria-pressed')=='true'
  assert visible('#queue-panel')
  mark('Implement here restores composer in Default mode when work starts')
  wait(lambda _:visible('#message-receipts'))
  fixture('plan-again');wait(lambda _:decision())
  assert el('#plan-implement-same').text=='Implement here'
  assert visible('#message-receipts') and visible('#queue-panel')
  el('#plan-implement-same').click();wait(lambda _:composer())
  wait(lambda _:el('#transcript').text.count('Implement the plan.')==2)
  mark('identical later plan starts a distinct request while the earlier receipt remains unacknowledged')
finally:
 (root/'plan-decision-browser-results.json').write_text(json.dumps({'checks':checks,'metrics':metrics},indent=2)+'\n')
 d.quit()
