import json, os, time, urllib.request
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

root=Path(os.environ['PORTAL_ACCEPT_EVIDENCE'])
base=json.loads(Path(os.environ['PORTAL_BROWSER_FIXTURE']).read_text())['url']
tools=os.environ.get('PORTAL_BROWSER_TOOLS','/nix/store/aklba75zn5fpld8y81ifqxx7j8vmj376-portal-browser-tools/bin')
options=Options();options.add_argument('-headless');options.binary_location=tools+'/firefox';options.set_capability('webSocketUrl',True)
driver=webdriver.Firefox(options=options,service=Service(executable_path=tools+'/geckodriver',log_output='/tmp/portal-review-browser-geckodriver.log'))
results=[]
def endpoint(name):
 with urllib.request.urlopen(base+'/fixture/'+name,timeout=5) as response:return json.load(response)
def wait(test):return WebDriverWait(driver,20).until(test)
def button(text):return next(e for e in driver.find_elements(By.CSS_SELECTOR,'.wizard-actions button') if e.text==text)
try:
 driver.browsing_context.set_viewport(context=driver.current_window_handle,viewport={'width':1440,'height':1000})
 driver.get(base+'/example/');wait(lambda d:len(d.find_elements(By.CSS_SELECTOR,'.message'))>=100)
 assert driver.find_element(By.CSS_SELECTOR,'[data-transcript-filter="messages"]').get_attribute('aria-selected')=='true'
 assert not driver.find_elements(By.CSS_SELECTOR,'.codex-typed-activity')
 driver.find_element(By.CSS_SELECTOR,'[data-transcript-filter="all"]').click();wait(lambda d:len(d.find_elements(By.CSS_SELECTOR,'.codex-typed-activity'))==2)
 assert driver.find_element(By.CSS_SELECTOR,'.codex-activity-links a').get_attribute('href')=='https://codemirror.net/'
 driver.find_element(By.CSS_SELECTOR,'.codex-activity-agents summary').click()
 assert driver.find_element(By.CSS_SELECTOR,'.codex-activity-agents pre').is_displayed()
 driver.find_element(By.CSS_SELECTOR,'[data-transcript-filter="messages"]').click()
 endpoint('approval');wait(lambda d:d.find_elements(By.CSS_SELECTOR,'.question-approval'))
 wait(lambda d:'3 messages' in d.find_element(By.ID,'codex-work-counts').text)
 assert '7 tool calls' in driver.find_element(By.ID,'codex-work-counts').text
 assert 'Working 1m 00s' in driver.find_element(By.ID,'codex-duration').text
 assert 'Waiting 2m 10s' in driver.find_element(By.ID,'codex-duration').text
 for name,width,height in [('desktop',1440,1000),('short',1280,720),('compact',1024,600),('mobile',390,844),('mobile-short',390,600),('zoom-equivalent',780,422)]:
  driver.browsing_context.set_viewport(context=driver.current_window_handle,viewport={'width':width,'height':height});time.sleep(.25)
  metrics=driver.execute_script('''return {width:innerWidth,height:innerHeight,documentWidth:document.documentElement.scrollWidth,...Object.fromEntries(['.question-approval','.wizard-content','.wizard-actions','#message-form'].map(s=>{const e=document.querySelector(s),r=e.getBoundingClientRect();return[s,{top:r.top,bottom:r.bottom,left:r.left,right:r.right,height:r.height,scrollHeight:e.scrollHeight,clientHeight:e.clientHeight}]}))}''')
  body=metrics['.wizard-content'];actions=metrics['.wizard-actions'];panel=metrics['.question-approval']
  assert metrics['documentWidth']<=width+1,metrics
  assert actions['top']>=body['bottom']-1 and actions['bottom']<=panel['bottom']+1,metrics
  assert actions['top']>=0 and actions['bottom']<=height,metrics
  assert metrics['#message-form']['bottom']<=height+1,metrics
  results.append({'viewport':name,'metrics':metrics})
  driver.save_screenshot(str(root/f'conversation-{name}.png'))
 driver.find_element(By.CSS_SELECTOR,'.wizard-content input[type="radio"]').click();button('Next').click()
 wait(lambda d:button('Submit answers'))
 driver.find_element(By.CSS_SELECTOR,'.wizard-content input[type="radio"]').click();button('Submit answers').click()
 wait(lambda d:not d.find_elements(By.CSS_SELECTOR,'.question-approval'))
 answers=endpoint('answers');assert set(answers)=={'choice','layout'},answers
 results.append({'messagesDefault':True,'typedSearchAndAgent':True,'counterAndTotals':True,'answersDelivered':sorted(answers)})
 driver.get(base+'/finished-example/');wait(lambda d:'Working 1m 00s' in d.find_element(By.ID,'codex-duration').text)
 time.sleep(16)
 reads=endpoint('activity-reads');assert reads.get('archived-thread')==1,reads
 assert 'Update unavailable' not in driver.find_element(By.ID,'codex-duration').text
 assert not driver.find_element(By.ID,'codex-work').is_displayed()
 driver.save_screenshot(str(root/'conversation-archived.png'))
 results.append({'archivedActivityReads':reads['archived-thread'],'archivedTimingFrozen':True})
 (root/'conversation-browser-results.json').write_text(json.dumps(results,indent=2)+'\n')
 print(json.dumps(results,indent=2))
finally:driver.quit()
