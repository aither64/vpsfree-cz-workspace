# Affected-container build result

PASSED exit0 at exact configuration9c8e73511eededc6ffe5aa57bd1b725ade0220b0,
selecting bot263ddbc0b541b5df2d025a73f1759d33db3f30b2 and hash
sha256-krNNqpHqOQ199uwVOyI1Efh2w8xX0tgzhyEnL6W0m78=.

Command: nix develop -c confctl build --yes 'cz.vpsfree/containers/int.vpsfbot'.
Complete transcript config-build-final.log; exact status config-build-final.exit.
Parent monitored with explicit visible fallback because the one permitted utility
was occupied by VM/CI; no second utility or capacity wait. No unexpected kernel
build, no activation/deployment/restart. No source changes.

Singleton generation2026-10-19--23-05-52 built. Metadata copied verbatim as
config-built-generation.json from the repository's ignored .confctl output.
Toplevel: /nix/store/p7xi9fmn21d2k2k6crc78bflwxk51qr3-nixos-system-vpsfbot-26.05.20261018.8ce7336.
Full log reaches101/101 derivations and confirms this machine only. Earlier
prompt/EOF attempt did not build and remains disclosed; corrected documented
--yes used, never a deployment permission bypass.

Independent final review/narrow findings acceptance and quick150 specs/lint/
format/evaluation evidence remain in final-review.md/quick-results.md. VM/CI
runtime verification still gates both authorized master integrations.

## Final readiness-corrected revision build

Exact configuration cdaa14c8af445fb921c62bc0a1b2fc8fdb54666d selecting
bot94ac4eb5a7caf0456fff7df86a44cae198463276/hash
sha256-v7m4mhpYs/P23cjiPm6XESAG5jIkoMBq5P1nTs0Lr6g= also PASSED exit0
with the same scoped --yes command. New transcript/status config-build-ready.log/
exit. Final generation2026-10-19--23-18-24, metadata config-built-ready-generation.json.
11/11 changed derivations built. No activation/restart/deployment/source changes.
Final generated-config evaluation config-eval-ready-result.json passed exact
summary/3600/#vpsfree/package identity. Prior build evidence retained separately.

## Clean upstream refresh build

Configuration7ffa98a5761e001ed22b70fa24eecc21ff8c58ca after unrelated upstream
master refresh also PASSED exit0. Same scoped noninteractive build, generation
2026-10-19--23-43-09, 9/9 derivations. config-build-merge.log/.exit retained;
config-eval-merge-parsed.json confirms unchanged94ac source and summary/3600.
No unexpected kernel build or activation/deployment/service restart. The single
Luna utility owned CI, so parent monitoring fallback was disclosed before launch.
