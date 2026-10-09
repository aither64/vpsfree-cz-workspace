# Final branch inventory

Initial independent whole-branch review and focused reset-lock review are recorded in [review.md](review.md). Later changes are three bounded browser fixture corrections, directly verified under the narrow-fix rule; application code is unchanged from reviewed runtime26640fb5. All corrections and repeated pins are folded into their owning unmerged commits. Eight focused commits; no obsolete approaches, unused compatibility paths or migrations. No branch was merged, released or deployed during history consolidation. Configuration and workspace select the same runtime; extension source remains unchanged. Default-branch integration is not authorized.

## codex-web

Base `3d07cf60cfde5d117a181a9bdb6d90a5860f6f0c`; head `860d515d0aa5d2f7ad68893db41f0969c78e00a7`.

```
dd13156b051c1ae32bc9bc409b622b5eb5d58e18 codex: expose account credits and idempotent limit resets
8263ccd44587a50148242d4e94d2e582d6bda759 conversation: attach binary clipboard files from the composer
860d515d0aa5d2f7ad68893db41f0969c78e00a7 conversation: keep refresh quiet and edit settings in a dialog
```

Final diff: [codex-web-final.diff](codex-web-final.diff).

## dev-workspace

Base `c51ba3c0ca0d41d237ef71c56accd564beb70a33`; head `675504f638d21578e87a94f460cc9cbf9e0df395`.

```
f824e6900298d0a3f149db1e7abb366aa7eda2f2 portal: keep refresh values visible and compact model controls
c93cb06c1894764ebb670e2a0e563673c7d74bab portal: show credits and confirm banked reset use
675504f638d21578e87a94f460cc9cbf9e0df395 inputs: select the updated Codex web integration
```

Final diff: [dev-workspace-final.diff](dev-workspace-final.diff).

## workspace

Base `747e9a875c23a7a760fcb3ce18d7d7a51f3015e5`; head `5448392af308b64cd28af4c0c665d68cf81e18a7`.

```
5448392af308b64cd28af4c0c665d68cf81e18a7 inputs: select the portal usability runtime
```

Final diff: [workspace-final.diff](workspace-final.diff).

## vpsfree-cz-configuration

Base `ae670dc0d4a5d43adf9560da1a6a0a35925cd2e5`; head `081ac7cc6098f79b004f7ff349e71c85257b518f`.

```
081ac7cc6098f79b004f7ff349e71c85257b518f inputs: set devWorkspace to 675504f6
```

Final diff: [vpsfree-cz-configuration-final.diff](vpsfree-cz-configuration-final.diff).
