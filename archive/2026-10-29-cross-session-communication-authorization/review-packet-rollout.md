# Final rollout pin/history review packet

The runtime implementation is unchanged4155d009, independently reviewed with no
findings, full actual-worker native idle/steer/reverse MCP and packaged CI passed.
New user directions authorize aitherdev deployment and, when deployed and verified,
feature integration into runtime/configuration/workspace master and machine release.
No activation or integration has occurred. No actual-session grants/private access
or lifecycle action is authorized. Session stays open.

## Exact completed ranges

Worktrees are under worktrees/2026-10-29-cross-session-communication-authorization/.

- Configuration vpsfree-cz-configuration: base
  b3b933bf6f9fc9f7f533b3f4e06775defd8879da -> head
  fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627. One generated confctl commit,
  `inputs: set devWorkspace to 4155d009`; flake.lock only3+/3-.
  Channel dev-workspace/role devWorkspace. All64 nodes/edges/originals unchanged
  except target locked lastModified/narHash/rev. Proper Nix pinned bundle bootstrap
  passed32.883s; Overcommit installed/trusted; Nixfmt/commit hooks passed, generated
  history width warnings retained per procedure. Fresh origin/master remains base.
- Workspace: base55a26f27e06d855176a8ae016a2f6bf23ece5f14 -> head
  8302996e0f7e0ad0ce0e62fa02f7cc1afec2bf9a. One commit, workspace nested runtime
  URL plus generated lock5+/5-. All35 node names/edges/follows unchanged;
  all34 other nodes equal. Published predecessor398dc7b..bedbf9cd was cleanly
  rebased over local tracking commits; range-diff is equal. Baseline adds a durable
  note outside work/archive; final package derivation changes source references,
  so do not claim complete derivation equality. Fresh exact-final build is pending.
- Runtime remains base08f3dbb92bc8585929edee85a824d44dfb3b0846 -> exact head
  4155d0099d03028b43d5f08d225a88156cb4155a, three reviewed commits A/B/C.
  Reuse original+affected reviews and narrow fixture followup; no new runtime review.

Both final pins select runtime4155d009 / NAR
sha256-hxhPj+obva7nETfnBTNZlmup+qqHERnZHI7zUdLcwkw=.
No migrations, obsolete approaches or repeated pin commits within either final
range. No pin deployment/release/external consumption occurred. Each repository's
single pin update is its own complete logical stream; no transitional pin retained.
Independently verify whole-series and migration conclusions, including the rebase.

## Checks and boundaries

Workspace deployment contract4runs19assertions passed; checker syntax/diff checks
passed. Real combined bin/check-dev-workspace-deployment passed both final locks.
Inherited unrelated agent-instructions check failed AGENTS16875bytes >16384;
AGENTS and test bytes identical to base. Do not expand pin work into instruction
rewrites. Full runtime CI40975812804 passed exact4155d009. Native fixture12.043s
passed exact4155d009; it executes production constructor/worker in test executable,
not installed portal binary. Candidate native output equals selected
/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0, same drv,
underlying executable SHA256647b0157e6472a793e0a0bd45bc44ef8ade673b6d8f3db4118260acda4976652.

See design.md rollout addendum and rollout.md for exact baseline systems/profile,
full source/input identities and physical machine aliases. Profile-only activation
is justified by unchanged nix/libexec/flakes/host/native contracts from deployed
5f4f1c1c to4155d009. Build/copy before machine claim; ordinary guarded switch only,
no system activation. No extra worker harness/provider campaign. Deployed proof
will combine exact installed artifact/source/native/tool-policy smoke, health,
naming availability and own continuity/settings with completed source-native test.
Only after verification integrate three approved defaults under separate short
claims; workspace tracking lock nonblocking; then release exact owned machine.
Forward recovery/immutable saved tuples and lifecycle exclusions remain intact.

## Assignment

Reviewer0 retained read_only, Sol/xhigh/codex-lb unchanged; verify same-session
identity. Risk High for deployment/authorization composition. Mechanical pin-only
content is eligible for the skill exemption; independently assess exemption,
whole-branch history/consolidation/no-migration conclusions and rollout contract
under general, scope and risk lanes. No handwritten logic/abstraction changed;
architecture content remains covered by original runtime reviews. Read applicable
skill references and repository procedures. Source/quick checks are complete; no
long build started. Owner evidence [D](rollout/config-pin-evidence.md) and
[E](rollout/workspace-pin-evidence.md) is complete.
Return report for lead persistence review-report-rollout.md; stay read-only,
no long tests/edits/mutations/nested agents. Explicitly distinguish review from
build/deployed usability, integration approval and machine release.
