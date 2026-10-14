# Isolated proxy-addr patch preparation

Prepared commands only. No generator, install, application check, package build,
commit, push, PR, CI rerun or deployment has been executed by the implementer.
The network feature worktrees and their previous operation packet remain separate.

## Scope and source evidence

The maintenance worktree is
`worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin-webui-proxy-addr`, branch
`dev/proxy-addr-patch`, at exact clean main base
`02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51`. It has neither root nor BFF
`node_modules`. The original network CI audit failure is retained in
`fixture-final-w-ci-failure.log`; it precedes the nonbrowser quality/test gates.
Both the original main base and the network feature locked proxy-addr 2.0.7.

Express requests proxy-addr `~2.0.7` in the BFF lock. The root project and BFF
are independent npm projects. `packages/bff.nix` owns the BFF dependency hash,
currently `sha256-imijdRISN2eVBsYX79YBxl7zKM7Pjq3rixkKXJNDSvw=`. The root
lock and frontend hash remain unchanged. The package shell includes Node 24.21.0,
npm 11.19.0 and `prefetch-npm-deps`; `npm run env:locked` checks both versions.
No repository dependency-update wrapper or declared hook framework was found.

[GHSA-jqcg-44mw-7w3h](https://github.com/advisories/GHSA-jqcg-44mw-7w3h)
lists 2.0.8 as the patched version for trust-subnet misclassification. The
[official 2.0.8 manifest](https://github.com/jshttp/proxy-addr/blob/v2.0.8/package.json)
retains forwarded 0.2.0, ipaddr.js 1.9.1 and the existing Node requirement.
The BFF currently configures `trust proxy` as `loopback`; its existing server
tests cover forwarded IPv4/IPv6 addresses and invalid callback addresses.
These observations do not establish deployed exploitability.

The generator uses npm's
[targeted update command](https://docs.npmjs.com/cli/v11/commands/npm-update/),
without changing the Express constraint or adding a direct dependency/override.
It requires the resulting selected node to be exactly 2.0.8. Every other lock
node, root metadata, dependency constraint, package manifest and runtime source
must match the base. Selected tarball/integrity are checked against exact-version
registry metadata. Verified funding metadata for this selected package may be
added by npm; dependency/engine/license changes are rejected. A broader generated
diff stops the packet for inspection; there is no retry or manual lock repair.

## Generator and setup stage

The fresh watcher may execute this after root inspection and when its utility
slot is available. It verifies the session identity, both markers, exact clean
maintenance base and frozen helper inputs. It self-captures aggregate and per-step
logs/statuses, refuses overwrites and stops at the first failure.

Before selecting generator execution, root inspects the current relevant open PRs:

```sh
nix shell nixpkgs#gh --command gh pr list --repo vpsfreecz/vpsadmin-webui --state open --limit 100 --json number,title,headRefName,baseRefName
```

Do not treat an inventory at its limit as complete. Root owns overlap decisions;
this packet does not create or modify a PR. At execution, the generator repeats a
read-only SSH `git ls-remote` check and requires main still at the selected base
and the new maintenance branch unpublished. It does not update local refs. An
advanced main or existing feature publication stops for root reconciliation.

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/proxy-addr-maintenance-prep1.sh generate
```

Inside the locked Nix shell, the generator/setup commands are:

```sh
# Repository root
npm run env:locked
# bff/ (registry metadata is saved separately)
npm view proxy-addr@2.0.8 --json --registry=https://registry.npmjs.org --loglevel=error
npm update proxy-addr --package-lock-only --ignore-scripts --no-audit --no-fund --registry=https://registry.npmjs.org
# Guard the exact leaf delta before installing anything.
# Repository root, then bff/, respectively
npm ci --include=dev
npm ci --omit=dev
# bff/: verify Express actually resolves the installed 2.0.8; retain lineage.
npm explain proxy-addr
npm audit --omit=dev --audit-level=high --json
# Repository root
npm audit --omit=dev --audit-level=critical --json
prefetch-npm-deps bff/package-lock.json
prefetch-npm-deps package-lock.json
```

The wrapper routes every command to its explicit directory. Installs change
ignored `node_modules`; the targeted update changes the owned BFF lock. Audits,
lineage and prefetch do not edit product source, although network/cache access is
required. The unchanged root hash must reproduce its existing value. The new BFF
hash and exact generated-lock checksum are retained as separate receipts. This
stage stops before changing the Nix hash or project prose.

## Owner reconciliation and focused checks

After root reports the generator result, the implementer inspects the complete
lock delta and applies only the computed BFF `npmDepsHash` in `packages/bff.nix`.
Reconcile the current hash record in `docs/design/PACKAGING.md` and the inaccurate
historical sentence that the BFF lock did not change. Prepare a dated
`docs/work-log/2026-10-06-proxy-addr-patch.md` entry for root's direct final writing,
with actual evidence and unmerged/undeployed status. REQ-068 owns package/hash
consistency; REQ-064 owns the per-change record. No requirement, API, trust-policy,
UI text, locale, browser scenario, inventory or capture change is intended.

Only after that pause and the owner-applied hash may a fresh watcher run:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/proxy-addr-maintenance-prep1.sh quick
```

The second stage requires generator exit zero, unchanged generated lock bytes
and an exact hash-only Nix edit. It runs:

```sh
npm run test:bff
node --test scripts/check-package-source.test.mjs scripts/check-package-contents.test.mjs scripts/oauth-nginx-policy.test.mjs scripts/oauth-csp-contract.test.mjs
npm test -- src/app/runtimeBootstrap.test.ts src/app/runtimeBootstrap.required.test.ts src/lib/auth/oauth2Client.test.ts
npm run ci:quick
nixfmt --check packages/bff.nix
```

The eight existing BFF suites exercise the installed server dependency graph,
credentials, runtime settings, response pages and session concurrency. Script
fixtures cover packaging and existing response/forwarding policy; the React units
cover the BFF bootstrap/auth boundary. `ci:quick` includes the documentation audit,
quality gates and application/tooling/adopted-E2E/BFF-core type checks. It writes
ignored audit artifacts, without regenerating route/API inventory. No browser,
real login, VM, production service or network-feature check is launched.

## Later package verification and commit proposal

Package output verification needs a separate parent-selected watcher operation
after hash/docs reconciliation. These are the exact canonical targets; this
preparation wrapper does not launch them:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin-webui-proxy-addr
nix build --no-link --print-out-paths .#bff .#frontend .#checks.x86_64-linux.provenance .#checks.x86_64-linux.source-contents .#checks.x86_64-linux.package-contents
```

The installed-content check builds both packages and verifies paired provenance,
so the unchanged frontend output participates. The BFF dependency hash must be
validated by an actual Nix build. Do not claim clean release provenance from a
dirty worktree build; root selects the final exact candidate receipt and records
its state. A kernel build is unexpected for these targets: stop and report under
the workspace verification policy. No NixOS VM, configuration pin, deployment,
capture or lifecycle command is included.

Proposed commit: one focused maintenance commit containing the generated BFF
lock, its owning package hash, the package hash record and dated evidence entry.
Suggested subject: `bff: update proxy-addr to 2.0.8`. The eventual body describes
the advisory and exact leaf patch without claiming deployed exploitability or
including check transcripts. Root owns final prose/message approval and the later
normal commit/publication step. Inspect current main and relevant open PRs before
creating the separate maintenance PR; do not bundle, rebase or cherry-pick the
network branch as part of this operation.

The mandatory-review skill exempts genuinely mechanical dependency/generated
updates without substantive handwritten changes. This proposed lock/hash update
can fit that exemption. Any required new override, trust-policy change, runtime
edit or other behavior beyond the leaf patch is a deviation to report first.
No merge, deployment, ready-for-production or successful-check claim follows
from preparing this packet.
