# Maintenance commit, package and publication proposal

Prepared for root inspection only. The implementer has not executed these
operations or changed the held source, original generator/helpers, network
branches or configuration pins. All commands below are proposals for later
root-selected execution.

## Candidate and evidence

- Worktree: `worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin-webui-proxy-addr`.
- Branch: `dev/proxy-addr-patch`; remote `git@github.com:vpsfreecz/vpsadmin-webui.git`.
- Exact base/current uncommitted HEAD: `02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51`.
- Intended commit contains exactly `bff/package-lock.json`, `packages/bff.nix`,
  `docs/design/PACKAGING.md` and `docs/work-log/2026-10-06-proxy-addr-patch.md`.
- BFF hash: `sha256-m6CayVcO1z+Xuy+XlAEqVLoRFRACSNjdcn4pae1T+Dc=`.
- No migrations. Generated leaf dependency, corresponding hash and documentation
  metadata only; no handwritten runtime, trust-policy or public-contract change.
- Parent quick stage: all steps exited zero; 57 BFF tests, 14 package/policy
  cases, 43 units in three files, complete `ci:quick`, Nixfmt and scope guards.
- The parent final evidence-only documentation audit is a separate required
  `proxy-addr-maintenance-final-docs.exit` zero receipt (68 docs/70 requirement IDs).

Root owns the final diff and mandatory-review exemption rationale. The skill's
mechanical dependency/generated/metadata exemption applies only while this
exact accepted scope remains intact. A runtime, trust-policy, public-contract
or other substantive change requires separate reconciliation; the packet does
not invent an exemption for it.

The owning dated log records quick evidence and package checks pending at this
checkpoint. It links the stable portal for later final exact-source receipts.
Do not amend source solely to insert a later package success: preserve the
clean candidate that actually ran. Root may update the tracking PR draft after
actual package evidence without changing application source.

## Frozen operation entry points

The packet freezes the actual current four source files, its scripts/message,
unchanged generator packet and passed receipts. It verifies the bound identity
and both markers and runs in this worktree's declared Nix shell. Aggregate and
per-step logs/exits use `proxy-addr-maintenance-final-*`, without overwriting
earlier evidence. Each invocation refuses existing outputs, stops on its first
failure and does not retry or clean up.

Root selects a fresh watcher for uncertain duration or uses the monitor skill's
visible fallback while the utility slot is unavailable. No operation runs as
part of preparing this proposal.

```sh
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
bash "$tracking/proxy-addr-maintenance-final.sh" commit
# Use the exact new SHA written by the completed commit, never an inferred tip.
maintenance_sha=$(cat "$tracking/proxy-addr-maintenance-final-committed.sha")
bash "$tracking/proxy-addr-maintenance-final.sh" packages "$maintenance_sha"
bash "$tracking/proxy-addr-maintenance-final.sh" publish "$maintenance_sha"
```

`packages` and `publish` both require the exact recorded clean committed SHA.
Their order is selected by root; the list above puts package proof first. Neither
operation edits the owning dated log or records speculative package success.

## Normal commit and feature-only publication

Commit requires the base HEAD, exact branch/SSH remote, clean index and only the
four frozen source paths. It reuses the successful original leaf/hash scope
guard. It verifies that the known repository still declares no hook framework,
custom hook path or active undeclared hook; a changed declaration stops for
normal hook setup/inspection. It refuses hook-bypass variables. Normal
`git commit -F proxy-addr-maintenance-final.message` runs with no bypass.

Before committing, it fetches only main's remote-tracking ref and requires main
still equal to the selected base with proven ancestry. It refuses an existing
published maintenance branch. It stages only the four paths, verifies the exact
staged list and whitespace, then saves the one-commit head/tree/history/diff.
Commit failure leaves its actual index/state for root; no unstage/reset is hidden.

Publication rechecks the exact clean one-commit candidate, hook state and freshly
fetched main/base ancestry. It requires the remote maintenance branch absent,
then uses normal SSH `git push origin EXACT_SHA:refs/heads/dev/proxy-addr-patch`.
It proves the new remote head before explicitly fetching only that owned feature
tracking ref with leading `+`, accommodating the bare remote's absent fetch
refspec. It saves `proxy-addr-maintenance-final-published.sha`.
No network feature ref, default branch, configuration pin or existing CI run is modified.
Creating the separate PR may start ordinary CI; no wait, rerun or cancellation
is included here.

## Exact committed package proof

The package stage builds only these attributes, with `--no-link`,
`--print-out-paths` and `--no-update-lock-file`:

```sh
nix build --no-link --print-out-paths --no-update-lock-file .#bff
nix build --no-link --print-out-paths --no-update-lock-file .#frontend
nix build --no-link --print-out-paths --no-update-lock-file .#checks.x86_64-linux.provenance
nix build --no-link --print-out-paths --no-update-lock-file .#checks.x86_64-linux.source-contents
nix build --no-link --print-out-paths --no-update-lock-file .#checks.x86_64-linux.package-contents
```

It requires unchanged clean HEAD before/after builds and zero receipts for both
packages and all three exact checks. It reads actual output files
`frontend/build-info.json` and `bff/share/vpsadmin-webui-bff/build-info.json`.
Both must have the selected full 40-character SHA, its correct short SHA,
schema 1, `dirty: false` and `source: environment`, with identical fields.
The BFF output must contain installed proxy-addr 2.0.8. The evidence JSON records
all five output paths and both actual metadata records. This supplements the
canonical installed-content check and does not substitute a fixture for it.

These targets include no Linux kernel. If a kernel build appears, stop the owned
verification command and report it under workspace policy. No local fallback
kernel build, browser, VM, network/configuration check, service activation,
cluster action, lifecycle helper, merge or deployment is authorized by this packet.

## Separate PR and message draft

The commit subject is `bff: update proxy-addr to 2.0.8`. Its proposed body is in
`proxy-addr-maintenance-final.message` and contains rationale without check
transcripts. Root owns final wording before selecting execution.

PR title/body drafts are in `proxy-addr-maintenance-final-pr-title.txt` and
`proxy-addr-maintenance-final-pr-draft.md`. Their current wording records actual
quick results and package checks pending. They are intentionally outside the
operation freeze so root can reconcile final evidence before a separate PR
without rewriting source. No PR-creating action is in the executable packet.

After exact publication and root's final prose, inspect the current relevant PRs:

```sh
nix shell nixpkgs#gh --command gh pr list --repo vpsfreecz/vpsadmin-webui --state open --limit 100 --json number,title,headRefName,baseRefName
```

Refuse to treat a saturated inventory as complete. Root previously found only
network PR19; check again before creating a maintenance PR. Reuse a relevant
existing PR instead of duplicating one. If none exists, the proposed command is:

```sh
nix shell nixpkgs#gh --command gh pr create --repo vpsfreecz/vpsadmin-webui --draft --base main --head dev/proxy-addr-patch --title "Patch the BFF proxy-addr dependency" --body-file "$tracking/proxy-addr-maintenance-final-pr-draft.md"
```

Verify the resulting PR head equals the exact published receipt and keep it
separate from network PR19. Maintainer review, passing checks and preparation
do not authorize merging or deploying it.
