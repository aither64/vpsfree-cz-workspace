# README CI watcher operation

Fresh utility verify_readme_ci, Luna/low, full_access/never. Verify bound session
2026-10-19-dynamic-python-api-client via dev-session current; environment identity
must both match or both absent+bound thread. Read dev-session-monitor SKILL.
Policy catalog digest ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376,
installed native verification_watcher-low full-access/never, retained identity
from same /nix/store/ad0s75irvrbj6pz6qk1zf7v9sy4l1qyp-dev-workspace-0.2.0.

Monitor existing GitHub vpsfreecz/haveapi runs ONLY at exact head
c1823f3d70365b0442d0e2171bdf83bd4c6dbe31:
Python39413502893,release39413502904,i18n39413502897.
CWD=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/haveapi
Evidence=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-dynamic-python-api-client/verification/readme-ci
Use installed gh, capture gh run view --repo vpsfreecz/haveapi --json
headSha,status,conclusion,jobs,url for each and assert expectedSHA. If incomplete,
wait with gh run watch --exit-status; retain output/status and final JSON. On
failure retain --log-failed evidence, no diagnosis/retry. No run launch/cancel/
approval/deploy/source edit/session lifecycle/nesting. Return compact result
all3 conclusions/exacthead/paths/elapsed, no outstanding operation. Normal
featurebranch release publication expected skipped; overall build success needed.
