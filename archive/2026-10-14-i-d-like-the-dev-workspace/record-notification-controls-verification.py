"""Bind completed exact-version checks; no execution, deployment or approval."""
from pathlib import Path
from datetime import datetime
import json,hashlib
root=Path(__file__).resolve().parent
rev='1038d4abdde8b115c21b5940b14be637cfa967b6'
def status(name):
 v=dict(line.split('=',1) for line in (root/name).read_text().splitlines())
 assert v['revision']==rev and v['exit_status']=='0',name
 v['elapsedSeconds']=(datetime.fromisoformat(v['finished'])-datetime.fromisoformat(v['started'])).total_seconds()
 return v
browser=status('notification-controls-1038-browser.status')
flake=status('notification-controls-1038-flake.status')
ci=json.loads((root/'notification-controls-1038-ci-result.json').read_text())
assert ci['headSha']==rev and ci['status']=='completed' and ci['conclusion']=='success'
artifacts=['notification-controls-1038-source-gate.json','notification-controls-composition-review.md','notification-controls-final-heads.json','notification-controls-lock-comparison.json','notification-controls-deployment-contract.log','notification-controls-1038-browser.log','notification-controls-1038-browser.status','notification-controls-1038-flake.log','notification-controls-1038-flake.status','notification-controls-1038-ci-result.json']
v={'schema':1,'runtimeRevision':rev,'applicableAutomatedChecks':'PASS','quickContracts':53,'sourceReview':'notification-controls-native-read-review.md','narrowRemedy':'notification-controls-review-dispositions.md','compositionReview':'notification-controls-composition-review.md','browser':browser,'fullFlake':flake,'ci':{'run':ci['databaseId'],'url':ci['url'],'headSha':ci['headSha'],'status':ci['status'],'conclusion':ci['conclusion'],'jobs':{j['name']:j['conclusion'] for j in ci['jobs']}},'browserScope':{'chromiumLifecycle':True,'firefoxLifecycle':True,'chromiumSyntheticSoundOptionsAndClick':True,'firefoxNativeRead':{'category':'AbortError','registrationSame':True,'identityVerified':False},'chromiumNativeRead':{'category':None,'registrationSame':True,'identityVerified':True}},'physicalNativeSoundOffVerified':False,'physicalMacOSExistingTabSelectionVerified':False,'keyboardSoundSaveFocusContinuityVerified':False,'priorOrdinaryFailureCauses':'unlocated','activationPerformed':False,'artifacts':{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in artifacts}}
with (root/'verification-notification-controls.json').open('x') as f:json.dump(v,f,indent=2);f.write('\n')
print('Completed exact1038 checks bound; no deployment performed.')
