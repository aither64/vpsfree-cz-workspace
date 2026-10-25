# Integrated default-branch CI receipt

All eight retained automatic push runs completed successfully on attempt 1:

| Repository/head | Run | Workflow | Conclusion |
| --- | --- | --- | --- |
| vpsfreecz/haveapi / 090a188c | 40015973570 | clients/python | success |
| vpsfreecz/haveapi / 090a188c | 40015973636 | clients/rust | success |
| vpsfreecz/haveapi / 090a188c | 40015973720 | release | success |
| vpsfreecz/haveapi / 090a188c | 40015973728 | RuboCop | success |
| vpsfreecz/haveapi / 090a188c | 40015973732 | clients/js tests | success |
| vpsfreecz/haveapi / 090a188c | 40015973838 | servers/ruby RSpec | success |
| vpsfreecz/haveapi / 090a188c | 40015973916 | i18n health | success |
| vpsfreecz/vpsadmin-rust-client / ff876abe | 40016358629 | Rust client | success |

The HaveAPI release run40015973720 build job120627998096 passed; publishing job120630659905 was skipped because this is refs/heads/master, not a tag. Full build log: run-40015973720-archive-member-000.log (263519 bytes, 3053 lines, SHA256 51fc7c3071a334583ebd02e8d10c713b4554e6e41ddf80c6dba1c70c4dc54dba). All eight complete ZIPs, extracted raw logs and terminal jobs/steps remain byte-preserved. Artifact12529240712 (release-40015973720) metadata binds master090a; its payload was not downloaded or used as an official release.

The target Rollup circular/this-rewrite, JSDoc unknown-type, Fiddle default-gem and Rust naming warning patterns are absent from the whole release build log. Remaining release output includes eight Nix UID notices and four empty fixture repository warnings. Downstream output retains Bundler/RubyGems constant redefinitions, generated unused-field warnings and the excluded real-server package-test notice. Full diagnostic matches and exact line references are in warning-inventory.json, with interpretation separately in warning-interpretation.json; no raw log was filtered or changed.

Fresh policy watcher 01a16a7a-77e9-7931-9f82-51d1beb8f5e6 used Luna/low, explicit danger-full-access/never and parsed effective launch readiness. Operation exit0 in 22.966s; native CLI exit0. No local owned process remains; utility slot yielded. Both clean integration targets retain090a/ff876abe. Moving dependency source was not read/guarded, no CI was launched/retried/cancelled/dispatched, no refs/artifacts changed, no claims acquired. Release hold remains and sole Git owner returns to HOLD for source/prose/crosscheck yield.

These results validate the existing integrated source, not the new dependency refresh or0.30.1 release.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
