# Effective persistence committed review packet

Gate satisfied: final rebased quick batch18188 and every stage completed0.
See effective-mounts-final-quick/receipt.md, original logs/status and terminal
2092-second watcher receipt. All intended source is committed and clean.
This packet requests final source/history review before long runtime checks.

## Outcome and scope

The user requested independent GPT-6 Astra/xhigh review of the whole approach to
impermanence persistent mounts, then authorized implementation of the accepted
refinement. Ensure effective early mounts supplying /var/lib/nixos or /var/log
are established before real legacy user allocation, with explicit refusal after
a required mount failure. Preserve guest-owned layout, host-provided storage,
upstream global order, dynamic account IDs, saved maps and numeric ownership.

Session: 2026-10-12-streamline-vpsadminos-config-imports, explicitly selected by
the user. Workspace: /home/aither/workspace/ai/vpsfree.cz. Tracking is
work/2026-10-12-streamline-vpsadminos-config-imports; read plan.md, state.md and
the architect-owned design.md (current refinement begins at line179, SHA256
c80fea979d8fe48c48d98b78a81b21dd8ea596e31d0c45e8eda296abdb1382b9).
The original independent assessment is astra-whole-approach-review.md.

Reviewer selection: explicit user request for Astra/xhigh supersedes the saved
Sol reviewer0 choice without reconfiguring that member. The original standalone
reviewer cannot be re-addressed/validated through the current parent interface;
a fresh read-only codex exec session uses -m gpt-6-astra, xhigh and no nested
agents. Launch prompt/events/settings and final report are retained under
effective-mounts-review/.

Use all FOUR lanes in mandatory-change-review: general,
architecture/repetition, scope/proportionality, risk/compatibility. Overall risk
is HIGH: persisted numeric ownership can become detached from live account IDs.
Read the skill and all four references, applicable workspace procedures and
repository-local AGENTS/policy before inspecting the committed deliverable.
Review directly, read-only, without nested agents, edits, Nix/builds/tests,
runtime, ref changes, deployment or lifecycle operations. Existing receipts
provide verification evidence; independently inspect source and Git history.

## Exact repositories and complete history

All worktrees are below worktrees/2026-10-12-streamline-vpsadminos-config-imports
in the workspace. Live Git is authoritative.

Product vpsadminos, target staging:

- Base: 7fd09b9b1f87f0563d3ba0be47081bfe4342b9b8.
- Clean HEAD: bf74af0b76accdf844ad6ffbea75db6c409f386e.
- Tree: 822fe1de775fb57c592d8cef884ff016695a6ac2.
- Complete series: b2669ce00d440c1e05eb07b0e5bb4d201f3e5161 (selector v5),
  bf74af0b76accdf844ad6ffbea75db6c409f386e (baseline persistence correction v8).
- Inventory: 24 paths, 2990 additions, 189 deletions. Read
  effective-mounts-review/inventory.md, series.txt, paths.txt, complete.diff and
  technical-delta.diff, comparing them with actual Git.
- Complete diff SHA256:
  7ca9535062907e9ee03aed190b6f8298fd2191d55a2e502379005b17db51273c.
- Technical delta SHA256:
  a2dc5353ddef08b1f6e85980e06f50730952794e7d2c23741c726a49df71bf19.

The selector and independent baseline persistence defect are separately useful
logical changes. Tests, guide and caused fixture/harness refinements accompany
the behavior they deliver. All caused fixes are folded into their owners.
logical-patch-history.md records chronological versions and source/message
lineage under the restored permanent patch-series policy. Exact dated backup
refs retain earlier source. Both feature patches are byte-identical across the
final rebase; selector source patch equals original 6b187003. Upstream staging
changed stable nixpkgs and frozen kernel outputs; those are baseline changes,
not feature pin changes. Inspect the complete series and final tree yourself.

Instruction restoration, also explicitly requested by the user:

- workspace base=HEAD c0d19e269fe5d34d4680c0988711061eb0faf959,
  tree 6b06b7a1ed77edf59d05caf978c56050fe8c75c5; target master, empty feature range.
- vpsfree-dev-workspace base=HEAD 767dfd587e346168e1443e65ccdb67ce748f3fe3,
  tree 80181fb9f3805e99734b85edfdbcdd022f5e4b67; target master, empty feature range.
- instruction-restoration/receipt.md and its proof preserve all six removed
  instruction amendments and dated backups. No instruction owner remains.
- vpsfree-kb-contracts is unchanged clean 2d11b2cc8445a695e7862af18ca0a70598afb38b,
  tree dce630658c0f71f5b037bfec317763abf2c9315b, base ce2c8cd9358c3636e5d39343e595df813a0b197f.
  Its completed content/history review remains applicable; confirm identity and
  reuse unchanged conclusions rather than rerunning its content review.

NO MIGRATIONS: no schema, data, map or transitional conversion is introduced.
No repeated feature production dependency/channel/input/generated update stream
exists. Per-variant test closure metadata is test provisioning. Prior branch
publication and disposable CI are retained provenance, not a production release
or external state boundary requiring obsolete shipping commits. Explicitly
conclude on whole-branch history, repeated streams and migration lineage.

## Accepted boundaries and reviewer decisions

- Select effective enabled boot.specialFileSystems, non-root component-aware
  ancestors of state/log paths. Include /var, /var/lib and direct fileSystems or
  specialFileSystems declarations and overrides. Root alone, pseudo mounts,
  disabled and near-prefix paths do not trigger the adapter.
- Use existing utils.fsBefore only for finite required-predecessor membership.
  Keep upstream global order/cycle handling and source earlyMountScript once.
  No sorter, replay, second phase or runtime registry is authorized.
- Dispatch the actual effective type/device/target/options. Bind/rbind options
  select directory identity checks and source preparation. Required predecessor
  bind sources are never created. Non-bind device/network strings are not
  directories and are not compared with -ef. Required mount/remount failures
  explicitly exit activation; unrelated callbacks retain upstream behavior.
- Preserve matching binds/no stacking, declared backing checks, metadata, dry
  activation, guest mkForce, priority90, legacy-only dependency and alternative
  backend behavior. Root-backed sources remain supported. Undeclared host
  storage retains its existing host contract; arbitrary non-bind source-device
  identity or durability is not promised by exact mountpoint presence.
- User chose fixed root/0755 defaults for missing selected bind sources. BOTH
  custom owner and custom mode require pre-provisioning. Impermanence does not
  later apply metadata to an existing source. Preserve existing metadata.
- Retain recursive helper: the suggested single mkdir-p form differs for
  missing-parent modes under inherited default ACLs. The earlier advisory was
  conditional on equivalence and is accepted with this explicit rationale.
- Four raw modules stay self-contained, latest stable byte-equal26.05. No raw
  import dependency, new option, allocator/backend forcing, account/map/ID/data
  repair, host/daemon/API/protocol or stateVersion/pin change is introduced.

The owner is guest NixOS compatibility. Consumers are flake module exports,
self-contained raw downloads, stable guest image templates and existing guest
configurations; inspect actual imports/exports/templates and representative
pinned25.11/26.05/unstable consumers. No test-runner/daemon public API changes.
The inert selector mock only gains boot.specialFileSystems={}.

## Documentation, compatibility and acceptance

Owning product guide: docs/containers/nixos.md, linked by existing docs index.
It explains ordering/failure limits, fresh metadata, custom pre-provisioning and
healthy source-only adoption. Main agent applied user-facing writing directly.
Session design/causal/attempt records retain rollout history and temporary
verification. No product guide should depend on session-specific paths.

Guests adopt independently by changing only module source with their existing
nixpkgs/accounts/storage/stateVersion. Existing maps/data remain readable to
older generations; rollback can restore the old ordering defect. Required
failures formerly hidden now stop allocation deliberately. Already-drifted IDs
need separately authorized recovery. No coordinated host update, production
integration/deployment, KB publication or lifecycle closure is authorized.

Quick checks and development failure reconciliation:

- Final rebased evidence: effective-mounts-final-quick/receipt.md and individual
  original logs/status. Batch uses rooted native nix-instantiate/nix-store,
  standard tests/nixos-container-eval.sh, actual registered12-script JSON and
  Ruby-c, declared overcommit and normal ci discovery. Final gate above is satisfied.
- Pre-rebase evidence: effective-mounts-quick/receipt.md, diagnosis.md and
  post-generated-wrapper.status0; all three-release assertions, all 30 generated
  fixtures/483 scenarios, template/standalone/negative evaluator, actual 12 Ruby
  scripts, docs/hooks/discovery passed. Retain original failed attempts.
- Diagnosed test-only mismatches: partial effective options, Bash dynamic-scope
  collisions, bare-target rewrite and unstable dependency-locator rewrite.
  Production raw bytes stayed unchanged during those corrections. GC removed
  unrooted diagnostic outputs; normal derivation/output roots now retain them.
  A prior successful evaluation had a warning prefix mixed with JSON; exact
  extraction retained original bytes/hash without re-evaluation. Final wrapper
  now separates stdout/stderr. See diagnosis.md and prepared static receipt.
- Four new runtime operation faults require anchored executed type/source/target
  and option tokens before executed refusal. This closes the evidence gap where
  an earlier mount failure could satisfy a generic operation assertion.

Runtime is pending and follows this source/history gate. Exactly 12 registered
cases retain old->new adoption, repeated switch/restart, actual release inputs,
root/declared/dependent backing and real allocator failure controls, adding
ancestor-var, ancestor-var-lib, direct-filesystem-bind and fresh-ancestor26.05.
Ancestor layouts omit both exact state/log declarations. Snapshots compare
independent live IDs/maps/payload bytes/numeric owners/machine-id, actual backing
identity/count/options, restrictive existing0710, fresh root0755 and payload0750.
Non-bind and still-present failed required remounts use real private-namespace
mounts and complete activation, with no Perl allocator after refusal and no
changed saved accounts/maps/data. Shell markers alone cannot establish this.

Earlier exact 20b eight-case and six-image passes are useful prior evidence only.
Broader 20b CI has diagnosed unrelated kernel identity/expectation and older-guest
cgroup failures (prior-20b-ci-failures/diagnosis.md); no overall-green claim.
Do not run duplicate tests during review. Report findings by severity/lane with
source/commit evidence and explicit residual runtime gaps. The lead reconciles
findings and records any runtime-phase clearance only after the final report.
