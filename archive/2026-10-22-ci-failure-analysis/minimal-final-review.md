# Independent final review: minimal five-commit branch

Reviewer0, retained gpt-6.1-sol/xhigh/read_only, verified session binding and
roster32. All four review lanes, overall High risk due persisted-state import
and host dataset retirement. No settings overrides or nested agents. Reviewer
returned this report for lead to save; review performed read-only source/Git
object/receipt inspection, no tests/Nix/builds/probes/scans/fetch/mutations.

**No findings:** no Blocking, Important or Advisory source/history issue in
the complete intended deliverable. Independent mandatory final review complete.
Native verification remains deferred; no runtime/publication/integration approval.

Checkout: worktrees/2026-10-22-ci-failure-analysis/vpsadminos-final-series.
Base `e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854`.
Head `04a2d2696bb4bcc7602221008a5c5096ede98046`.
Tree `43c15f40ce94be0a2cbd9bae21aa96e2cff3e7b8`.
HEAD/tree match; checkout/index clean. Current slug matched trusted binding;
both session environment markers absent, consistent with the binding.

Reviewer read skill/all four references, local AGENTS/patch-series policy,
selected design/plan/state, complete final series/diff, specs, lasting docs and
relevant adjacent consumers.

## Source conclusions

- Writer start.rb:327 persists final temporary-root selection after preparation,
  before startup and independently of CPU scheduling. Failure/custom-boot
  boundaries retained.
- Legacy run_configuration.rb:197/450 requires complete metadata, one exact GC
  owner without competing ancestor/descendant ownership, and authenticated
  retained init/root. Birth, namespace PID1, cgroup, mount/ZFS, private-root
  inode/device, saved bytes and GC ownership are rechecked before selection-only
  repair/publication. Descriptor duplication preserves lease ownership without
  reopening a PID.
- Pool.rb:692 and garbage_collector.rb:116/255 protect publication under
  manipulation exclusion and reconcile event failure using exact object
  identity. Prepublication refusal omits container and inhibits retirement;
  postpublication attachment failure retains managed ownership and inhibits
  retirement. Trash sink covers periodic/manual pruning and queued frees.
  Registered records retained; unregistered refused frees have no durable retry
  promise. No additional reader/GC defect found.
- Focused regression requires genuine old-writer stale state, live run/root/
  payload continuity, selection-only repair, reload without rewriting,
  immediate new-writer persistence and ordinary retirement in both cgroup modes.
  Missing stale-state coverage fails without synthetic YAML or retries. Full2ab
  source is distinct from live inventory.
- Health checks retain original cumulative dmesg and workload/recovery rules.
  No recorder ships.
- Catalog/rename/removals/policy coherent; shared framework/runner contracts and
  consumers unchanged. Dataset/updates/testing docs describe owning behavior,
  refusal/rollback and lifecycle without claiming deployment. Retirement is
  explicit scope/support decision against configured production, not evidence
  that old saved state disappeared.

## Whole-history conclusion

Exactly five coherent, independently meaningful owners:

1. `0d649b80f67a262830682d1651cc748d752e1d42` writer persistence and units.
2. `e83a18ef8e4c52580f0298eb3758cdab5168629e` authenticated recovery/import/GC,
   units and compatibility docs.
3. `5af40521f48b66d4a9b994c5c6f69c97c54d2625` health assertions/explanation.
4. `2868fbbe19da9d7e9634ca24c887ab1ad5e1adcf` production transition at final name.
5. `04a2d2696bb4bcc7602221008a5c5096ede98046` historical retirement/policy.

No obsolete implementation, diagnostic add/delete cycle, intermediate opt-in,
recorder or fixup residue. Rename/header and health prose folded into owners.
Messages truthfully separate prior checks from unrun runtime; earlier provenance
findings resolved. Recorder exclusion does not certify it.

Independent committed-object checks: dated old07 backup binds original07;
pure1652d702 equals original tree70e412. Original-base30b7 tree removes only
four recorder files/28 doc lines. Five range-diff entries all '='. Final tree
differs only by upstream flake.lock, exact fetched base. Original authors/dates
preserved. Final diff42files/+1690/-3952 SHA256
`fb5efe1a96e2e2be5607d6fec34808750c2d39c3f7b3900e67a2c6109988aa25`.

## Migration and repeated-stream conclusions

No migrations: no database/schema/API/run-ID versions or intermediate branch
migrations. YAML old-reader-loadable. Supported real old saved/running state and
rollback/restoration compatibility intentionally retained. Rollback loses new
authentication/GC protections as documented. No coordinated fleet update needed;
no migration merge/release/deployment/external-consumption lineage exists.

No repeated dependency/channel/input/kernel/gem/generated update streams in the
five commits. Upstream impermanence lock update belongs to base and is preserved,
not a feature repin stream.

## Verification limits

Normal hooks and scoped format/parse/Ruby-syntax receipts support committed
package. Width-preference warnings unsuppressed; messages satisfy80columns.
Earlier23/177 units and38/41 assertion/static checks remain prior environment-
bound evidence, not final-head reruns. Full testScript byte-exact16,955B SHA256
`b949f3fc408e31daa78fcf15d46016fe424ccceafb33096c9e821579be9e78e4`.

Final native catalogs, realized packaged-source bytes, production-originv1/v2
VMs and qualification/hotplug runtime remain unproven. Original warning/denial
is not resolved by static review. These deferred gates are not speculative
source findings. No source/history blocker to selected focused native checks.
Branch/runtime readiness and integration remain unclaimed.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/
