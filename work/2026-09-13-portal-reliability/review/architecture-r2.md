# Architecture and repetition review rerun

Reviewed the targeted remediation series directly at the packet's exact
`codex-web`, `dev-workspace`, `vpsfree-dev-workspace`, and configuration heads.
The workspace-only commits were subsequently rebased without an implementation
change to `037bf6873b0d013afa1bf90aa31093ff1584647c` on
`7b00c831a3b6d171185885ccecab554f040a8d57`. The review covered the generic
provider contract, organization-owned shutdown budgets and packaging, the
matched dependency chain, complete server-rendered cluster refresh, and their
material interactions. Reviewer model/effort: `gpt-5.6-sol`, `xhigh`.

## Findings

### Important: an absent refresh leaves the prior provider status cached and a later start can resurrect it

Commit `4bc75a348c5b0fa6a134e615ee170e96d6d89429` makes a successful details
response authoritative for the browser's complete cluster section, but the
server does not make the same absence authoritative for its provider-status
cache. `sessionDetails` skips `InspectContext` when `MayExist` is false
(`dev-workspace/portal/internal/web/server.go:884-890`), while the only cache
deletion happens when `StatusCache.observe` receives `found == false`
(`dev-workspace/portal/internal/cluster/status.go:102-121,159-170`). A reset
removes the provider's cluster directory
(`vpsfree-dev-workspace/dev-clusters/lib/runtime.sh:577-585`), so the empty
HTML response clears the card but leaves the last running status, including
readiness, topology, commands, and credentials, in memory.

A later start creates that directory again while holding the same per-cluster
lock (`vpsfree-dev-workspace/dev-clusters/lib/runtime.sh:259-278`). Details can
then see `MayExist == true`; the provider promptly returns the reserved busy
result, and `StatusCache.observe` overlays the busy status with the stale entry.
The portal consequently renders the previous cluster's details again until the
new start finishes. The current transition test inserts a successful `stopped`
observation between busy and absence
(`dev-workspace/portal/internal/web/server_test.go:4015-4033`), which is not the
real running -> busy -> reset/absent sequence, and it does not exercise a later
busy start.

Make an authoritative absent details result evict the cached entries for that
session/providers, or route it through an equivalent `found == false` cache
observation. Cover running -> busy -> absent -> new-start busy and assert that
the old service data and secret do not return.

## Architecture assessment and residual validation

The new contract ownership otherwise resolves the original architecture
findings. The generic runtime owns and documents the reserved busy result and
release ceiling, exports the exact contract through its Nix library, and uses
the embedded values in Go. The organization provider owns one `shutdown.json`;
Ruby and shell read it, packaging installs it beside both consumers, and the
provider checks the aggregate budget against the generic ceiling. The
organization and workspace pins form one matched provider/portal dependency
chain, with no second hand-maintained provider catalog or timeout constants in
the reviewed path.

The shared cluster template also removes the former server/browser presentation
duplication, and event delegation keeps refreshed controls attached. The
planned browser exercise should still cover selected service-tab preservation
and delegated copy/reveal/release controls after replacement. The live cluster
test remains necessary to validate real QEMU shutdown, reaping, cleanup, and
the 180-second outer deadline; these are residual test gaps rather than
additional architecture findings.
