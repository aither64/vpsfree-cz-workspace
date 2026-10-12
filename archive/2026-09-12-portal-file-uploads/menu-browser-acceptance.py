#!/usr/bin/env python3
"""Focused attachment-menu acceptance in an isolated TLS portal fixture."""
import json,os,ssl,tempfile,urllib.request
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
root=Path(__file__).parent
info=json.loads(Path(os.environ['PORTAL_UPLOAD_BROWSER_FIXTURE']).read_text());base=info['url']
tools=Path('/tmp/portal-uploads-browser-tools/bin')
opts=Options();opts.add_argument('-headless');opts.binary_location=str(tools/'firefox');opts.accept_insecure_certs=True;opts.set_capability('webSocketUrl',True)
d=webdriver.Firefox(options=opts,service=Service(executable_path=str(tools/'geckodriver'),log_output='/tmp/portal-menu-geckodriver.log'))
checks=[];metrics={}
def wait(fn):return WebDriverWait(d,30).until(fn)
def js(code,*args):return d.execute_script(code,*args)
def el(selector):return d.find_element(By.CSS_SELECTOR,selector)
def fixture(action):return urllib.request.urlopen(base+"/fixture/"+action,context=ssl._create_unverified_context()).read()
def mark(label):checks.append(label);print('PASS '+label,flush=True)
def viewport(w,h):d.browsing_context.set_viewport(context=d.current_window_handle,viewport={'width':w,'height':h})
def open_menu(button):
 el(button).click();wait(lambda _:js('return document.querySelector(arguments[0]).getAttribute("aria-expanded")==="true"',button))
 return el('#'+el(button).get_attribute('aria-controls'))
def menu_checks(form,button,prefix):
 assert not el(form+' .codex-upload-composer').is_displayed()
 assert 'Up to 10 files' not in el(form).text
 before=js('return document.querySelector(arguments[0]).getBoundingClientRect().height',form)
 menu=open_menu(button)
 assert menu.text=='Attach files'
 rect=js('return arguments[0].getBoundingClientRect().toJSON()',menu)
 assert rect['left']>=0 and rect['right']<=js('return innerWidth') and rect['top']>=0 and rect['bottom']<=js('return innerHeight'),rect
 assert js('return document.querySelector(arguments[0]).getBoundingClientRect().height',form)==before
 assert js('return document.activeElement.getAttribute("role")')=='menuitem'
 d.switch_to.active_element.send_keys(Keys.ESCAPE)
 wait(lambda _:not menu.is_displayed());assert js('return document.activeElement===document.querySelector(arguments[0])',button)
 el(button).send_keys(Keys.ARROW_DOWN);wait(lambda _:menu.is_displayed())
 d.switch_to.active_element.send_keys(Keys.TAB);wait(lambda _:not menu.is_displayed())
 assert js('return document.activeElement===document.querySelector(arguments[0]+" button[type=submit]")',form)
 el(button).send_keys(Keys.SPACE);wait(lambda _:menu.is_displayed())
 point=js('const r=document.querySelector(arguments[0]+" textarea").getBoundingClientRect();return {x:r.right-8,y:Math.max(8,r.top+8)}',form)
 actions=ActionChains(d);actions.w3c_actions.pointer_action.move_to_location(point['x'],point['y']);actions.w3c_actions.pointer_action.click();actions.perform()
 wait(lambda _:not menu.is_displayed())
 el(button).send_keys(Keys.ENTER);wait(lambda _:menu.is_displayed())
 el(button).click();wait(lambda _:not menu.is_displayed())
 metrics[prefix]={'emptyHeight':before,'menu':rect}
 mark(prefix+' empty layout, bounds, toggle, keyboard and outside dismissal')
try:
 with tempfile.TemporaryDirectory(prefix='portal-menu-inputs-',dir='/tmp') as directory:
  small=Path(directory)/'evidence.txt';small.write_text('Attachment menu acceptance.\n')
  viewport(1280,900)
  fixture('baseline');d.get(base+'/');wait(lambda _:el('#creation-uploads > button').is_enabled())
  assert el('#creation-uploads > button').is_displayed()
  d.get(base+'/example/');wait(lambda _:el('#message-uploads > button').is_enabled())
  assert el('#message-uploads > button').is_displayed()
  fixture('current');d.refresh();wait(lambda _:el('#message-upload-controls button').is_enabled())
  d.get(base+'/');wait(lambda _:el('#creation-upload-controls button').is_enabled())
  fixture('baseline');d.refresh();wait(lambda _:el('#creation-uploads > button').is_enabled())
  assert el('#creation-uploads > button').is_displayed()
  d.get(base+'/example/');wait(lambda _:el('#message-uploads > button').is_enabled())
  assert el('#message-uploads > button').is_displayed()
  mark('warm-cache forward/rollback keeps both forms usable with baseline and current assets')
  fixture('current');d.refresh();wait(lambda _:el('#message-upload-controls button').is_enabled())
  button='#message-upload-controls .codex-upload-toggle'
  menu_checks('#message-form',button,'desktop session')
  js('window.pickerClicks=0;document.querySelector("#message-upload-controls input").addEventListener("click",e=>{e.preventDefault();window.pickerClicks++;});')
  menu=open_menu(button);menu.find_element(By.TAG_NAME,'button').click()
  assert js('return window.pickerClicks')==1 and not menu.is_displayed()
  el('#message-upload-controls input[type=file]').send_keys(str(small))
  wait(lambda _:'Ready' in el('#message-uploads').text)
  js('const dt=new DataTransfer();dt.items.add(new File(["Drop acceptance"],"dropped.txt"));document.querySelector("#message-form").dispatchEvent(new DragEvent("drop",{bubbles:true,cancelable:true,dataTransfer:dt}));')
  wait(lambda _:len(d.find_elements(By.CSS_SELECTOR,'#message-uploads .codex-attachment'))==2 and el('#message-send').is_enabled())
  mark('menu invokes picker synchronously; picker and drop retain ready cards')
  d.find_elements(By.CSS_SELECTOR,'#message-uploads .codex-attachment button')[-1].click()
  wait(lambda _:len(d.find_elements(By.CSS_SELECTOR,'#message-uploads .codex-attachment'))==1)
  viewport(390,844);menu=open_menu(button)
  assert js('return document.documentElement.scrollWidth')==390
  d.save_screenshot(str(root/'menu-session-narrow.png'));menu.find_element(By.TAG_NAME,'button').send_keys(Keys.ESCAPE)
  el('#message-send').click();wait(lambda _:not el('#message-uploads').is_displayed())
  wait(lambda _:len(d.find_elements(By.CSS_SELECTOR,'#transcript .codex-attachment a'))==1)
  link=el('#transcript .codex-attachment a').get_attribute('href')
  assert urllib.request.urlopen(link,context=ssl._create_unverified_context()).read()==small.read_bytes()
  mark('attachment-only Send carries exact bytes and collapses cleared cards')
  menu_checks('#message-form',button,'narrow session')
  viewport(1280,900);d.get(base+'/');wait(lambda _:el('#creation-upload-controls button').is_enabled())
  button='#creation-upload-controls .codex-upload-toggle'
  menu_checks('#new-session-form',button,'desktop creation')
  viewport(390,844);el(button).location_once_scrolled_into_view
  menu_checks('#new-session-form',button,'narrow creation')
  menu=open_menu(button);d.save_screenshot(str(root/'menu-creation-narrow.png'));menu.find_element(By.TAG_NAME,'button').send_keys(Keys.ESCAPE)
  el('#creation-upload-controls input[type=file]').send_keys(str(small));wait(lambda _:'Ready' in el('#creation-uploads').text)
  el('#creation-uploads .codex-attachment button').click();wait(lambda _:not el('#creation-uploads').is_displayed())
  mark('creation picker upload and removal collapse cards')
  # Real DOM coverage of the provider's optional slot and legacy single-root API.
  result=d.execute_async_script('''const done=arguments[0];(async()=>{
    const {mountUploads}=await import('/codex/assets/uploads.js?v=2');
    const host=document.createElement('div');host.style.cssText='position:fixed;top:12px;right:8px;z-index:1000';document.body.append(host);
    const action=document.createElement('button');action.textContent='Host action';host.append(action);
    const cards=document.createElement('div');document.body.append(cards);
    const store=new Map();const storage={getItem:k=>store.get(k),setItem:(k,v)=>store.set(k,v)};
    const client={list:async()=>({limits:{fileBytes:3,promptBytes:3,files:1,chunkBytes:3},files:[]})};
    const uploads=mountUploads(cards,{controlsRoot:host,client,storage,storageKey:'slot'});await uploads.initialized;
    const toggle=host.querySelector('.codex-upload-toggle');toggle.click();
    const menu=host.querySelector('.codex-upload-menu');const rect=menu.getBoundingClientRect();
    const flipped=rect.top>toggle.getBoundingClientRect().bottom && rect.right<=innerWidth;
    uploads.lock(true);const closed=!menu.matches(':popover-open') && toggle.disabled;
    uploads.lock(false);const dt=new DataTransfer();dt.items.add(new File(['1234'],'oversized.txt'));
    cards.dispatchEvent(new DragEvent('drop',{bubbles:true,cancelable:true,dataTransfer:dt}));
    const rejected=!cards.hidden && cards.textContent.includes('exceeds the file or prompt upload limit');
    uploads.destroy();const preserved=host.children.length===1 && host.firstChild===action && !cards.children.length;
    const legacy=mountUploads(cards,{client,storage,storageKey:'legacy'});await legacy.initialized;
    cards.querySelector('.codex-upload-toggle').click();const fallback=!cards.hidden && cards.querySelector('.codex-upload-menu').matches(':popover-open');
    legacy.destroy();host.remove();cards.remove();done({flipped,closed,rejected,preserved,fallback});
  })().catch(e=>done({error:String(e)}));''')
  assert all(result.values()) and 'error' not in result,result
  metrics['provider']=result;mark('provider flips/clamps menu, locks, shows limit errors, preserves host actions and supports legacy root')
  js("const script=document.createElement('script');script.type='module';script.src='/fixture/shared-composer.js';document.body.append(script);")
  wait(lambda _:el('#shared-acceptance .codex-upload-toggle').is_enabled())
  assert js('return !!document.querySelector("#shared-acceptance .codex-upload-toggle").closest(".codex-conversation-actions")')
  assert not el('#shared-acceptance .codex-upload-composer').is_displayed()
  js('window.destroySharedAcceptance();document.querySelector("#shared-acceptance").remove()')
  mark('shared conversation composer places the menu in its action row')
  el('#creation-upload-controls input[type=file]').send_keys(str(small));wait(lambda _:'Ready' in el('#creation-uploads').text)
  el('#new-session-form input[name=name]').send_keys('menu-acceptance')
  js('document.querySelector("#new-session-form").addEventListener("submit",e=>{e.preventDefault();window.initialForm=[...new FormData(e.target).entries()];});')
  el('#new-session-form button[type=submit]').click();form=wait(lambda _:js('return window.initialForm'))
  assert len([v for k,v in form if k=='attachmentIds'])==1 and any(k=='uploadScope' and v for k,v in form)
  assert not el('#creation-upload-controls .codex-upload-toggle').is_enabled()
  mark('attachment-only initial prompt retains file IDs and locks the menu on submit')

except BaseException:
 d.save_screenshot(str(root/'menu-browser-failure.png'))
 (root/'menu-browser-failure.html').write_text(d.page_source)
 raise
finally:
 d.quit();(root/'menu-browser-results.json').write_text(json.dumps({'checks':checks,'metrics':metrics},indent=2)+'\n')
