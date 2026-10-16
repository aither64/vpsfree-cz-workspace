"""Bind completed exact-version checks; no execution, deployment or approval."""
from pathlib import Path
from datetime import datetime
import json,hashlib
root=Path(__file__).resolve().parent
rev='8cb1c0e545e1343d311f7cb9405eee83c468b4a6'
def status(name):
 v=dict(line.split('=',1) for line in (root/name).read_text().splitlines())
 assert v['revision']==rev and v['exit_status']=='0',name
 v['elapsedSeconds']=(datetime.fromisoformat(v['finished'])-datetime.fromisoformat(v['started'])).total_seconds()
 return v
browser=status('notification-compact-8cb1c0e5-browser.status')
flake=status('notification-compact-8cb1c0e5-flake.status')
ci=json.loads((root/'notification-compact-8cb1c0e5-ci-result.json').read_text())
assert ci['headSha']==rev and ci['status']=='completed' and ci['conclusion']=='success'
artifacts=['notification-compact-source-gate.json','notification-compact-composition-review.md','notification-compact-final-heads.json','notification-compact-remedy-final-freeze.json','notification-compact-composition-check.log','notification-compact-8cb1c0e5-browser.log','notification-compact-8cb1c0e5-browser.status','notification-compact-8cb1c0e5-flake.log','notification-compact-8cb1c0e5-flake.status','notification-compact-8cb1c0e5-ci-result.json']
v={'schema':1,'runtimeRevision':rev,'applicableAutomatedChecks':'PASS','quickContracts':62,'sourceReview':'notification-compact-review.md','narrowRemedy':'notification-compact-review-dispositions.md','compositionReview':'notification-compact-composition-review.md','browser':browser,'fullFlake':flake,'ci':{'run':ci['databaseId'],'url':ci['url'],'headSha':ci['headSha'],'status':ci['status'],'conclusion':ci['conclusion'],'jobs':{j['name']:j['conclusion'] for j in ci['jobs']}},'browserScope':{'chromiumLifecycle':True,'firefoxLifecycle':True,'chromiumSyntheticSoundOptionsAndClick':True,'firefoxNativeRead':{'category':'AbortError','registrationSame':True,'identityVerified':False},'chromiumNativeRead':{'category':None,'registrationSame':True,'identityVerified':True}},'physicalNativeSoundOffVerified':False,'physicalMacOSExistingTabSelectionVerified':False,'keyboardSoundSaveFocusContinuityVerified':False,'priorOrdinaryFailureCauses':'unlocated','activationPerformed':False,'artifacts':{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in artifacts}}
with (root/'verification-notification-compact.json').open('x') as f:json.dump(v,f,indent=2);f.write('\n')
print('Completed exact8cb1c0e5 checks bound; no deployment performed.')
