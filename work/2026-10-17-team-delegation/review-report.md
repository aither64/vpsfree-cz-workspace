# Independent final review

Review result: one Blocking and one Important finding. Resolve the Blocking
finding before long integration checks. Resolve or explicitly record the
decision on the Important finding before continuing.

## Findings

### R1 — Blocking: expanded presets can write creation journals that no reader accepts

Lanes: general, risk/compatibility. Introduced by
`ced922c533c7d51ff35d488780a0020162883e7f`.

Affected changes: `dev-workspace/portal/internal/teamruntime/runtime.go:425`
through the member expansion, and
`dev-workspace/portal/internal/agentteams/catalog.go:509`.
Relevant existing boundaries: `libexec/dev-session:3801`,
`libexec/dev-session:3481`, `portal/internal/agentteams/provenance.go:17`,
`portal/cmd/workspace-portal/main.go:566`.

The new count validation limits member count, but does not bound the expanded
snapshot's serialized size. A catalog with 16 implementers, each having the
allowed 4,096-byte instructions, passes Nix validation when its capacity and
max_open_agents are sufficient. The expanded preset already exceeds 64 KiB.
`valid_direct_team_preset?` accepts it, and CLI creation's
`write_creation_journal` writes the complete oversized journal without a size
check. The CLI's next read, the Go provenance reader, and workspace-host's
registration reader all retain a 64 KiB journal limit. The apply-preset file
reader also retains a 64 KiB limit. A package-owned valid selection therefore
leaves persistent creation evidence that ordinary recovery cannot read.
Browser creation similarly accepts the preset before its later bounded
`--team-preset` file read fails.

Concrete checks at the reviewed head:

- Nix evaluation of the site catalog with 16 implementers, 4,096-byte
  implementer instructions, and capacity/max_open_agents 32 returned
  `{"count":16,"valid":true}`.
- A minimal equivalent preset with 16 implementers and a reviewer returned
  `valid_direct_team_preset=true`. Its encoded size was 69,295 bytes.
- The actual Ruby writer successfully wrote its 69,570-byte creation journal;
  the actual bounded reader immediately refused it as
  `creation journal is not a private bounded regular file`.

Reject selections that cannot fit the existing serialized snapshot and journal
contracts before writing a receipt or starting a root. Include JSON escaping,
the journal envelope, and its newline in the bound, and protect the writer
from publishing an unreadable record. Add a focused regression showing refusal
without persistent partial creation and a fitting boundary case readable by
all recovery consumers. This does not require raising the existing limits.
The current five-person site preset is small enough; the defect is in the new
public count contract, which expressly accepts larger expanded selections.

### R2 — Important: an interrupted preceding unmanaged Full-team preset loses its retry path

Lanes: general, risk/compatibility. Introduced by
`ced922c533c7d51ff35d488780a0020162883e7f` at
`dev-workspace/portal/internal/teamruntime/runtime.go:463`; rejection occurs
in `ApplyPreset` at line 977.

The unmanaged `full` preset changed from three specialists to four, but
`ApplyPreset` reconstructs its expected lineup from the current preset on
every call. A preceding version can atomically reserve architect0,
implementer0, and reviewer0 and then stop during member creation. Retrying
`full` after the upgrade compares that saved three-member reservation against
the new four-member recipe and fails with
`a preset can only create an empty team`. This path is exposed by the unmanaged
portal preset action and `workspace-portal team preset`.

The isolated regression in `review-unmanaged-retry_test.go` constructs the exact
preceding complete reservation. It passes when the runtime implementation is
overlaid from base `9b50f357b40aeb4b3bd9715609815ebcdca57043`, and fails at the
reviewed head with the error above. No project source file was edited for this
check. Managed `ApplyPresetSpec` snapshots are unaffected. Individual member
retry remains available, so existing member identities are not lost, but the
promised unchanged-selection preset retry no longer works.

Preserve the accepted preceding unmanaged recipe when retrying its existing
complete reservation, while giving a fresh team the new lineup. Alternatively,
keep this unmanaged default outside the change and record that scope decision.
Retain the current refusal to append a new preset to an edited team. Cover an
interrupted old full preset across the upgrade as well as a new full preset.

## Scope and reviewed history

Reviewed all four requested lanes: general, architecture/repetition,
scope/proportionality, and risk/compatibility. Read the mandatory skill and lane
references, workspace and repository instructions, plan, design, packet, source,
tests, documentation, and complete commit series and final diffs. Risk is High
because this changes the catalog/package contract and persistent creation
recovery. The configured standalone reviewer policy is recorded in
`review-settings.json` as `gpt-6-astra` / `xhigh`.

Exact ranges:

- dev-workspace:
  `9b50f357b40aeb4b3bd9715609815ebcdca57043..732f3f382c6918319c211cc84e6ab434dff4a8b5`:
  `ced922c` (counts and creation) and `732f3f3` (fallback delegation policy).
- workspace:
  `a4aa81eb3a028b066ae11823dd11d5a3480ef1e8..7aefc9669ffcb1ecb13f484db957f2854bcf8dbc`:
  `7c6a037` (initial tracking), `b347b3f` (runtime input), and `7aefc96`
  (site roster and delegation policy).
- vpsfree-cz-configuration:
  `fbe190dc93e2d788aed561f367d049d2fe025b13..c9ed3e3169016eaece6955cfb716d3f75c6b142c`:
  `c9ed3e3` (generated devWorkspace channel pin).

The supplied bases are ancestors and the merge bases of their exact heads.
The commit split is coherent. No obsolete unmerged approach, corrective fixup
series, unused transitional implementation, or redundant repeated update stream
remains in these ranges. The superseded combined runtime commit `989c72c` is not
in the reviewed history; the packet records that no consumer pinned or deployed
it. There is one final workspace nested-runtime update and one matching
configuration-channel update; both select `732f3f3`, with the extension revision
and unrelated locked inputs preserved. These are two consumers of one final
runtime revision, not redundant successive updates to one stream.

**Migration lineage: no migrations.** There is no database or persisted-state
conversion migration in any reviewed range. Schema 4 is the preceding supported
catalog; the code retains its interpretation and validates its original raw
digest. Schema 5 is introduced directly, with no intermediate unapplied schema.
The packet records it as unmerged, unreleased, and undeployed. Intentional older
package rejection and forward-only recovery are documented. R1 and R2 remain
compatibility defects despite that sound schema lineage.

The generic runtime owns member counts and address expansion, while the site
owns the new composition and prompts. The unchanged extension passes teamConfig
through. The site and generic Nix fixtures exercise the schema-5 and schema-4
consumers respectively. The change does not add a scheduler, dispatcher,
permission mechanism, model change, or retained-prompt rewrite. No additional
architecture or proportionality findings arose beyond the bounded-acceptance
and retry issues above.

## Verification and remaining limits

Inspected the supplied focused Go/Ruby/instruction results in `quick-final.log`;
all reported checks pass. Independently checked the complete diffs with
`git diff --check`, evaluated the oversized-count catalog, exercised the actual
Ruby journal writer/reader, and ran the upgrade regression against the final
and preceding runtime implementations. The two reproductions expose gaps in
the passing focused suite.

No long integration, packaged runtime, CI, live App Server, or deployment check
was run in this review. Those remain necessary after findings are reconciled.
The changed prompts and static policy tests express the agreed delegation
behavior; an actual new Full-team creation and assignment smoke check is still
needed to establish operational behavior. Update the session phase/state from
its initial planning text when recording these results. No default-branch
integration was authorized or performed.
