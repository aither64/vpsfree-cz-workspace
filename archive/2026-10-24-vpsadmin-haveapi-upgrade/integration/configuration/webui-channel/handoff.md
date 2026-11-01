# Newadmin channel update ready for history disposition

One clean native-generated commit **64220e2877417f5a6669358b98660ae2b5649bae**, tree `b4f77e63f971859a03f8e89cb2b1973c45b75455`, on integrated master `9927bb70e07e9cb559f8988339619e4ab6e6b83d`. Ordinary `nix develop --command confctl inputs channel update --commit vpsadmin-webui vpsadmin-webui` exited0 in29.514s with normal precommit/commitmsg hooks. Full generated changelog/message is retained exactly; no handwritten source or documentation edit.

Authoritative pre-update SSH proved configuration master/own feature9927 and WebUI main exactlyf276, so this was a required update, not a no-op or selection of unreviewed upstream. `vpsadminWebui` changed606a02c→f2765d3fd778927f4cda3563f66615bfcf72b7cf; selected source `/nix/store/2x8shcz22d5k7qxprpr6nzd6m5vcqxbj-source`, measured NAR `sha256-gpWqK6RAI3WETK97O3f0QWqu3ReNLOwubdM+1l+A75E=`. WebUI tree is0f4949dc1c346bb4205940655f29965daeb16039.

The whole lock equals the base lock after changing only this node's locked rev/NAR/time. Only the semantic `vpsadminWebui` target changes among157 resolved paths (158 including root); its nixpkgsStable/vpsadminServices follows and every other raw JSON value remain exact. Services0f and entire upstreamc218 node are preserved. All474 other tracked mode/OID entries are equal9927, including Varnish, credential/logging, private-path and routing settings.

Complete one-commit base-to-head history/full binarydiff/full native message/expected wholelock and semantic graph are in [quick proof](quick-proof.json). NO MIGRATIONS in this configuration pin; no obsolete/repeated update/fixup stream. Already accepted WebUI review/20focusedcases/main all3CI retain their exactf276 scope and are not rerun or relabeled.

The only host consuming this channel/module/packages is `cz.vpsfree/vpsadmin/int.vpsadmin-webui1` (VPS30431,172.16.9.170), as declared by its module/config. Minimal postreview command is `nix develop -c confctl build --yes cz.vpsfree/vpsadmin/int.vpsadmin-webui1`, followed by actual selectedsource/frontend+BFF/system/input/config/closure/root/cleanembeddedrevision binding. Legacy PHP hosts use the unchanged services input. No suite or browser/API/runtime campaign is proposed.

STOPPED before build for lead final-history/mechanical-pin disposition. Original73861 ended0; source clean and writer idle. No feature publication, default mutation, claim, deployment, PR/registry/CI polling, lifecycle or cleanup occurred. All original9927/recoveries/roots/private/live/frozen249f paths remain.

[Quick proof](quick-proof.json) · [Full diff](full.diff) · [Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/)
