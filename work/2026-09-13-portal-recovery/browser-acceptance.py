#!/usr/bin/env python3
"""Real Firefox/Chromium acceptance against an isolated production-handler fixture."""
import json,os,ssl,tempfile,time,urllib.request,urllib.parse
from pathlib import Path
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
root=Path(__file__).parent
base=json.loads(Path(os.environ['PORTAL_RECOVERY_FIXTURE']).read_text())['url']
browser=os.environ['PORTAL_BROWSER']
checks=json.loads((root/('browser-results-'+browser+'.json')).read_text())['checks'] if os.environ.get('PORTAL_PHASE')=='interfaces' else []
def fixture(action,**values):
 return json.loads(urllib.request.urlopen(base+'/fixture/'+action+'?'+urllib.parse.urlencode(values),context=ssl._create_unverified_context()).read())
fixture('recover')
if browser=='chromium':
 o=ChromeOptions();o.binary_location=os.environ['CHROMIUM'];o.add_argument('--headless=new');o.add_argument('--no-sandbox');o.add_argument('--ignore-certificate-errors');o.add_argument('--window-size=1280,1000')
 d=webdriver.Chrome(options=o,service=ChromeService(executable_path=os.environ['CHROMEDRIVER'],log_output='/tmp/portal-recovery-chromedriver.log'))
else:
 o=FirefoxOptions();o.binary_location=os.environ['FIREFOX'];o.add_argument('-headless');o.accept_insecure_certs=True;o.set_capability('webSocketUrl',True)
 d=webdriver.Firefox(options=o,service=FirefoxService(executable_path=os.environ['GECKODRIVER'],log_output='/tmp/portal-recovery-geckodriver.log'));d.set_window_size(1280,1000)
def el(selector):return d.find_element(By.CSS_SELECTOR,selector)
def js(code,*args):return d.execute_script(code,*args)
def wait(fn,seconds=30):return WebDriverWait(d,seconds,ignored_exceptions=(StaleElementReferenceException,)).until(fn)
def mark(label):
 if label not in checks:checks.append(label)
 print(browser+': PASS '+label,flush=True)
def connected():return not el('#conversation-connection').is_displayed()
def notice():return el('#conversation-connection').is_displayed()
def preserve():
 assert el('#message-form textarea').get_attribute('value')=='Preserved composer draft'
 assert el('#pending textarea').get_attribute('value')=='Preserved pending answer'
 assert abs(js('return document.querySelector("#transcript").scrollTop')-scroll)<4, {'expected':scroll,'actual':js('return document.querySelector("#transcript").scrollTop')}
 assert 'preserved.txt' in el('#message-uploads').text
 assert el('#message-form button[type=submit]').is_enabled()
try:
 with tempfile.TemporaryDirectory(prefix='portal-recovery-input-') as temp:
  upload=Path(temp)/'preserved.txt';upload.write_text('Browser recovery attachment\n')
  d.get(base+'/example/');wait(lambda _:connected());wait(lambda _:el('#pending textarea').is_displayed())
  el('#message-form textarea').send_keys('Preserved composer draft')
  el('#pending textarea').send_keys('Preserved pending answer')
  el('#message-upload-controls input[type=file]').send_keys(str(upload));wait(lambda _:'Ready' in el('#message-uploads').text)
  js('const t=document.querySelector("#transcript");t.dispatchEvent(new WheelEvent("wheel",{deltaY:-100}));t.scrollTop=200;t.dispatchEvent(new Event("scroll"));window.savedAnswer=document.querySelector("#pending textarea");window.savedComposer=document.querySelector("#message-form textarea")')
  time.sleep(0.3)
  scroll=js('return document.querySelector("#transcript").scrollTop')
  if os.environ.get('PORTAL_PHASE')!='interfaces':
   fixture('failure');fixture('hint');wait(lambda _:notice() and 'Fixture service unavailable' in el('#conversation-connection').text)
   preserve();assert 'Last refreshed at' in el('#conversation-connection').text
   missed=browser+' final reply after outage';fixture('reply',text=missed);fixture('recover')
   wait(lambda _:connected() and missed in el('#transcript').text,40);preserve()
   assert js('return window.savedAnswer===document.querySelector("#pending textarea") && window.savedComposer===document.querySelector("#message-form textarea")')
   mark('service failure shows stale notice and silently recovers missed reply without changing drafts, attachment or scroll')
   # Hold an actual fetch response indefinitely. Deadline must release the old read.
   fixture('stall');fixture('hint');before=fixture('stats')['reads'];wait(lambda _:fixture('stats')['reads']>before)
   wait(lambda _:notice() and 'timed out' in el('#conversation-connection').text,42);preserve()
   missed=browser+' reply after stalled fetch';fixture('reply',text=missed);fixture('recover')
   el('#conversation-connection button').click();wait(lambda _:connected() and missed in el('#transcript').text);preserve()
   mark('35-second deadline releases hung request; Retry now restores a fresh snapshot')
   # Suppress writes while keeping the actual EventSource and server alive.
   fixture('silent');before=fixture('stats')['streams'];fixture('reply',text=browser+' silent final reply')
   wait(lambda _:notice(),55);preserve();wait(lambda _:fixture('stats')['streams']>before,35)
   fixture('recover');wait(lambda _:connected() and browser+' silent final reply' in el('#transcript').text,55);preserve()
   mark('missing visible SSE heartbeats detects a silent connection and replaces the stream')
   # Browser wake signals supersede the hung request and coalesce.
   fixture('stall');fixture('hint');before=fixture('stats')['reads'];wait(lambda _:fixture('stats')['reads']>before)
   fixture('reply',text=browser+' resumed reply');fixture('recover')
   before=fixture('stats');js('window.dispatchEvent(new Event("online"));window.dispatchEvent(new Event("focus"));document.dispatchEvent(new Event("visibilitychange"))')
   wait(lambda _:connected() and browser+' resumed reply' in el('#transcript').text);preserve()
   after=fixture('stats');assert after['streams']-before['streams']<=1 and after['reads']-before['reads']<=2,(before,after)
   mark('wake signals replace pending work and coalesce into one reconnect')
   # Exercise offline event and actual Chromium network emulation where available.
   if browser=='chromium':d.execute_cdp_cmd('Network.enable',{});d.execute_cdp_cmd('Network.emulateNetworkConditions',{'offline':True,'latency':0,'downloadThroughput':-1,'uploadThroughput':-1})
   else:js('window.dispatchEvent(new Event("offline"))')
   wait(lambda _:notice());preserve();fixture('reply',text=browser+' online reply')
   if browser=='chromium':d.execute_cdp_cmd('Network.emulateNetworkConditions',{'offline':False,'latency':0,'downloadThroughput':-1,'uploadThroughput':-1})
   js('window.dispatchEvent(new Event("online"))');wait(lambda _:connected() and browser+' online reply' in el('#transcript').text);preserve()
   mark('offline/online resumes the conversation and keeps message controls usable')
  # Mount the provider's reusable UI using the same actual HTTP endpoints.
  js("const script=document.createElement('script');script.type='module';script.src='/fixture/shared.js';document.body.append(script)")
  wait(lambda _:len(d.find_elements(By.CSS_SELECTOR,'#shared-check .codex-prompt textarea'))>0)
  wait(lambda _:not el('#shared-check .codex-connection-status').is_displayed())
  el('#shared-check .codex-conversation-form textarea').send_keys('Shared draft')
  el('#shared-check .codex-prompt textarea').send_keys('{"q1":{"answers":["Shared answer"]}}')
  js('document.querySelector("#shared-check .codex-conversation-transcript").scrollTop=100')
  fixture('failure');js('window.dispatchEvent(new Event("pageshow"))');wait(lambda _:el('#shared-check .codex-connection-status').is_displayed())
  fixture('reply',text='Shared restored reply');fixture('recover')
  wait(lambda _:not el('#shared-check .codex-connection-status').is_displayed() and 'Shared restored reply' in el('#shared-check .codex-conversation-transcript').text,40)
  assert el('#shared-check .codex-conversation-form textarea').get_attribute('value')=='Shared draft'
  assert el('#shared-check .codex-prompt textarea').get_attribute('value')=='{"q1":{"answers":["Shared answer"]}}'
  assert js('return document.querySelector("#shared-check .codex-conversation-transcript").scrollTop')==100
  js('window.destroyShared();document.querySelector("#shared-check").remove()')
  mark('shared mounted conversation recovers with its composer, answer and scroll intact, then disposes')
  el('#session-tab-repositories').click();wait(lambda _:el('.repository-history-summary').is_displayed())
  # Each browser has its own fresh fixture, initially one commit.
  assert '1 commit' in el('.repository-history-summary').text
  assert len(d.find_elements(By.CSS_SELECTOR,'.repository-pagination'))==0
  assert '+1' in el('.repository-history-summary').text and '−1' in el('.repository-history-summary').text
  mark('one commit shows full net totals without pagination')
  fixture('commits',count=49);el('[data-review-refresh]').click();wait(lambda _:el('.repository-history-summary').text.startswith('50 commits'))
  assert len(d.find_elements(By.CSS_SELECTOR,'.repository-pagination'))==0
  fixture('commits',count=1);el('[data-review-refresh]').click();wait(lambda _:el('.repository-history-summary').text.startswith('51 commits'))
  summary=el('.repository-history-summary').text
  buttons=d.find_elements(By.CSS_SELECTOR,'.repository-pagination button');assert not buttons[0].is_enabled() and buttons[1].is_enabled();buttons[1].click()
  wait(lambda _:el('.repository-pagination span').text=='Page 2');assert len(d.find_elements(By.CSS_SELECTOR,'.repository-commit'))==1
  buttons=d.find_elements(By.CSS_SELECTOR,'.repository-pagination button');assert buttons[0].is_enabled() and not buttons[1].is_enabled()
  assert el('.repository-history-summary').text==summary
  buttons[0].click();wait(lambda _:el('.repository-pagination span').text=='Page 1')
  mark('50 commits hide controls; 51 paginate with stable totals and Previous on final page')
  if browser=='firefox':d.browsing_context.set_viewport(context=d.current_window_handle,viewport={'width':390,'height':844})
  else:d.execute_cdp_cmd('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':False})
  assert js('return document.documentElement.scrollWidth<=window.innerWidth')
  d.save_screenshot(str(root/('repositories-'+browser+'.png')))
  mark('repository summary and pagination fit a 390px viewport')
finally:
 d.save_screenshot(str(root/('last-browser-'+browser+'.png')))
 fixture('recover')
 (root/('browser-results-'+browser+'.json')).write_text(json.dumps({'browser':browser,'checks':checks},indent=2)+'\n')
 d.quit()
