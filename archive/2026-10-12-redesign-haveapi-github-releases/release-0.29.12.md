# HaveAPI 0.29.12: published and verified

Final status: published successfully and verified at all destinations. The user
approved the protected environment as aither64. Run39313082898 completed success;
[public Release](https://github.com/vpsfreecz/haveapi/releases/tag/v0.29.12).
The chronological preparation and approval checkpoints below are historical;
the final verification section records the completed result. Session stays open.

User authorization in lead conversation01a1309b-32dd-7863-93cf-c6134f412659:
"yes, merge and release", in reply to the explicit request to merge the fix into
haveapi/master, advance haveapi-0.29 and push v0.29.12. This authorizes those
mutations. The publishing job's protected-environment human approval remains
separate; no programmatic environment approval is authorized.

Reviewed candidates: master5266481..c58704a; release7fb218e..355c299. Full review
and history/no-migration conclusions: pending-tag-review.md; checks:
pending-tag-verification-summary.md; actual user-run pending-draft diagnostic:
pending-tag-live-draft-diagnostic.md. All quick/full/package and11safe CI checks
passed. No source edits after review. Both feature refs and worktrees retained.

Master integration uses selected i144xnc9 coordinator and frozen
pending-tag-integration-request.json. No machine deployment or reservation is
needed. The configured catalog covers canonical HaveAPI master, not the release
branch/tag target. The latter follows the documented SSH fast-forward/atomic
non-force push procedure using a fresh retained detached target worktree, with
normal Nix/Bundler hooks. No existing tags, drafts or artifacts may be changed.

Before tagging, recheck exact remote bases, new-version registry absence,
release enabled variable and required-reviewer/tag policy. Build the tag's own
original artifacts, retain them and validate source/version/run/hash bindings
before human approval. A source correction cannot replace an old tagged run.

Initial checkpoint: execution was pending. Source approval alone did not verify credentials;
registries/PHP and Packagist indexing remain to be exercised. Cross-registry
publication can be partial; preserve originals and diagnose before retrying.
Session remains open.

## Pre-release checks and master preparation

Final pre-merge inventory and clean heads/diff hashes match the independent
review exactly (pending-tag-premerge-inventory.json). Fresh SSH fetch confirmed
master5266481 and release7fb218e. New master coordinator run:
44265246-96eb-4791-a5be-bbc594dd8f4d, phaseprepare/needs_attention; no merge job
was submitted before isolated hook dependency failure. Eventcc74624f generation0
acknowledged. Existing dual-Ruby/JSON hook-cache repair runs under a fresh utility;
tracked application source and declared hooks remain unchanged.

Current environment API confirms required revieweraither64 and sole custom tag
policyv*. The development token's variable-read API returns403; it cannot read
HAVEAPI_RELEASE_ENABLED directly. Do not infer disabled setup from that result.
The tag workflow itself enforces the activation variable and current required
reviewers before building/publication. This does not weaken either guard.
Evidence: patch12-pretag-environment.json.

All three gem version0.29.12 endpoints and npm exact version returned404.
Fresh SSH checks find no v0.29.12 in HaveAPI or the PHP mirror. Evidence:
patch12-pretag-registry.json. Scriptpatch12-integrate-and-tag.sh guards the exact
release source/clean worktree, expected remote base and absent local/remote tag,
then uses Nix/Bundler hooks and an atomic non-force branch/tag push.

Hook dependency repair completed once in104seconds, exit0. Both Ruby3.3.10 and
3.4.9 probes pass with JSON2.9.1, and retained tracked source is still clean.
Original coordinator run resumed --background with continuationgeneration1.
No source changes, hook bypass or new integration request. Fresh utility observes
its result. Evidence: pending-tag-repair-hooks.log/status and
pending-tag-integration-resume.json.

## Master integrated

Coordinator run44265246-96eb-4791-a5be-bbc594dd8f4d generation1 completed;
merge job504e3a79-f801-4e9e-aedf-03b823b874e4 succeeded. Its exact head is
c58704a08451a231fdf6c6123437133422af46dc, independently confirmed over SSH.
No source edits or rebase occurred. Frozen review/check evidence remains valid.
Release target remains7fb218e with no v0.29.12 before the authorized atomic push.

## Release branch and tag pushed

patch12-integrate-and-tag.sh completed0. A fresh detached target checkout
fast-forwarded7fb218e ->355c299, then an atomic non-force SSH push updated
haveapi-0.29 and created annotated v0.29.12. Normal Nix/Bundler hooks remained
enabled. Prior tags and originals were not modified. Log/status:
patch12-integrate-and-tag.log and patch12-integrate-and-tag.status.

Fresh Luna/low utility patch12_tag_gate_watcher owns tag workflow observation
through its build/artifact/approval boundary. Seven ordinary component/lint/i18n
checks are included. Parent has not submitted a deployment approval. Source
worktrees, feature refs and detached target worktrees remain retained.

Independent post-push SSH proof confirms masterc58704a, release355c299,
v0.29.12 annotated objectd1867e0a1432cd29c00fad39805d0e475a872b76 peeling to355c299.
Both prior annotated tag objects and peeled sources match their saved identities.
Receipt: patch12-post-push-refs.json.

## Tag build and approval boundary

All seven ordinary tag checks and release build succeeded. Actions run39313082898
waits for human release-environment approval. Original artifact12217296363 was
downloaded once to patch12-tag-artifacts/ and verified with the actual run ID;
all seven retained-file hashes match. Manifest SHA256563ed9d468a5357a8a290a0e5ef6f6a973b844fd5b9b0db443b7ea732797a00c. See
[publication approval gate](patch12-tag-approval.md). Fresh utility observation
ended and the lead accepted ownership of the pending gate. No lead approval or
publication action was sent. Registry/PHP/Packagist success remains unverified.

## Publication and destination verification completed

Approval API receiptpatch12-approvals.json confirms aither64 approved the release
environment. Run39313082898 attempt1 /source355c299 completed successfully;
publishing job completed2026-10-19T19:50:21Z. Its draft retention, RubyGems trusted
credential configuration and package/PHP/finalization steps all passed. Fresh
Luna/low observation returned0 (patch12-publication-watch.status). No lead
programmatic environment approval or manual registry publication was performed.

A separate fresh Luna/low utility ran the read-only destination verification once
in8seconds and returned0. Parent inspected the complete receipt and bounded log:
patch12-publication-verification.json / .log / .status and
patch12-destination-helper-receipt.json. Actual downloaded registry bytes for
haveapi, haveapi-client and haveapi-go-client0.29.12 and the npm tarball match the
original manifest. npm repository is git+https://github.com/vpsfreecz/haveapi.git;
latest is0.29.12. Existing Publisher checks also confirm registry integrity.

Read-only PHP clone/preflight confirms v0.29.12 snapshot content and HaveAPI-Source
355c299 provenance, with master and tag at84c46343171d3839c5de011035d96a0f50425a86.
Packagist already indexes0.29.12 with that exact source/dist reference.

GitHub Release417680904 is public, finalized at2026-10-19T19:50:18Z. Its body
matches the retained release notes. All8publicly downloaded assets, including
release-manifest.json, match the retained originals byte for byte. Manifest
SHA256 remains563ed9d468a5357a8a290a0e5ef6f6a973b844fd5b9b0db443b7ea732797a00c.
No artifact was rebuilt or substituted after approval. Both failed earlier
source/tag/artifact boundaries remain preserved.

Actual OIDC publishers, scoped PHP deployment and Packagist integration have now
been exercised successfully. The requested release-process test is complete and
packages are ready for consumers. No release work/blocker or verification process
remains. Both source worktrees remain clean. Source compatibility, documented
non-atomic recovery and lifecycleactive/open policy remain unchanged. No archive,
delete, branch removal, cleanup or other session lifecycle action was performed.
