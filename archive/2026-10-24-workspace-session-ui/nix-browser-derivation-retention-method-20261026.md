# Browser derivation instantiation and retention

Static method for lead review, 2026-10-26; no execution release. Architect0
verified current/envpair and ready Astra/xhigh/workspace_write roster32. Applicable
procedures remain read in this context. Only named own receipts and installed
manual files were read. No Nix, store query, source scan, Git or active utility
observation ran. The separate recursive inspect must still contain zero root,
realise, instantiation or build operations.

## Documented primitive and scope

Use ordinary **nix-instantiate --add-root**, returning a list of the three actual
derivation objects. Do not use --eval or its --strict/--json/--read-write-mode
companions for this operation. Normal nix-instantiate materializes derivations;
--eval selects a different evaluation-only mode. Do not pass a .drv to
nix-store --realise: that operation explicitly realizes its outputs.

The selected Nix2.34.9 manual's nix-instantiate Description states that a
top-level expression may be a derivation, list or set of derivations, and that
the command produces store derivations. Its --add-root documentation delegates
to the nix-store root option. The latter documents the requested symlink plus
a uniquely named registration symlink under `/nix/var/nix/gcroots/auto/`, and
multiple-result names `root`, `root-2`, `root-3`. Those are already indirect
roots; no additional --indirect flag is documented in the selected pages and
none is proposed. Registration uses this standard command, not a manual link
in the auto directory or store-database manipulation.

This is an explicit new metadata/retention phase: it can instantiate dependency
derivations, populate evaluation caches and register three persistent roots.
Their reachable dependencies are retained according to ordinary Nix policy;
this does not create or verify output bytes. IFD=false provides the documented
no-build evaluation boundary. substitute=false, empty builders and max-jobs0
remain supplemental limits; max-jobs0 alone does not override preferLocalBuild.

The existing legacy cache policy remains unchanged, including its honest limit:
there is no guessed legacy --offline flag and no network-denial claim. Missing
locked sources can require retrieval. A future release must expressly cover
only the same frozen URI and lock-selected source identities if retrieval is
needed, or hold this step pending that prerequisite. No moving-ref resolution,
lock update, output substitution/build, native/browser launch or policy widening
is proposed. Parent must separately accept and release the metadata/root writes.

## Small expression delta, no original-helper edit

The frozen helper SHA256
`52cb66707e0b00e51287f500591b08b193f743937f7e7ff0be63e7d70c444a2a` exports
`shell` as a derivation object. Its browser/review-assets values are only strings
inside `identities`; the underlying two objects are private let bindings.
Therefore the old JSON expression cannot simply be given --add-root. Use one
new owned projection, reproducing only those two exact constructor expressions,
and assert equality to the complete frozen identity result before returning
the list. Keep the original helper/JSON expression/receipts immutable.

Candidate expression, to be frozen by owner2 after method acceptance:

```nix
let
  uri = "github:aither64/dev-workspace/c31fdd9f6a86f2eb0e6b87001d6892b820bce2fe?narHash=sha256-30kKzkA7kulWE3eBXlaMgG1ym%2B9lLuU3jdsfMOT5erA%3D";
  e = import /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/runtime-final-c31-browser-preparation-v1/browser-environment.nix { runtimeFlakeURI = uri; };
  expected = builtins.fromJSON (builtins.readFile /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/runtime-final-c31-browser-preparation-v1/environment-evaluation-results-v1/identities.raw.json);
  f = builtins.getFlake uri;
  p = import f.inputs.nixpkgs { system = "x86_64-linux"; };
  browsers = p.playwright-driver.selectBrowsers {
    withChromium = true;
    withFirefox = true;
    withWebkit = false;
    withChromiumHeadlessShell = false;
  };
  reviewAssets = p.callPackage (f.outPath + "/nix/review-ui.nix") { };
in
assert { identities = e.identities; shell = { output = e.shell.outPath; derivation = e.shell.drvPath; }; } == expected;
assert f.outPath == expected.identities.runtimeSource;
assert browsers.drvPath == expected.identities.browserDerivation && toString browsers == expected.identities.browserOutput;
assert reviewAssets.drvPath == expected.identities.reviewAssetsDerivation && toString reviewAssets == expected.identities.reviewAssetsOutput;
[ e.shell browsers reviewAssets ]
```

The expected JSON must retain SHA256
`ad06dc09a47a98dbb71cd906f13c9d8c4d188060479ad6d387459333e96103d6`.
Assertions compare all nine identities and both shell fields, including exact
source, tool and output paths; no metadata identity may be refreshed to match
new output. Reproducing the two private expressions is bounded verification
glue, not a new package definition, .drv reconstruction or application edit.

## Candidate argv and root contract

One invocation, as an argument array, with the expression above as one argument:

```text
/run/current-system/sw/bin/nix-instantiate
--impure
--option allow-import-from-derivation false
--option substitute false
--option builders ""
--option max-jobs 0
--option accept-flake-config false
--option flake-registry ""
--option use-registries false
--option eval-cache false
--option tarball-ttl 4294967295
--add-root /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/runtime-final-c31-browser-metadata-retention-v1/roots/root
--expr <exact new projection as one argument>
```

Keep the accepted cwd/public environment/tool checks from materializationv2;
preserve nix-instantiate basename dispatch to selected z4w Nix2.34.9 and
executable SHA256 `6b20a492de8d0b2cf67e68d4cad1773a132753aa2909d8ddcdd44345c869e171`.
The proposed directory is a future name, not an observed absent destination.
Owner2 must freeze exact argv, expression hash, policy and fresh result paths
for parent acceptance before any execution.

Preparation/launch must refuse any existing destination, including dangling
symlinks. Create only the fresh session-owned root directory, exclusively, and
require `root`, `root-2` and `root-3` absent. Preserve every existing root and
original packet. Use the existing bounded watcher envelope, source609/client137,
complete locks, inherited3937/current4583 plus additive packet/tool guards,
mandatory finalization and finite group settlement. No blanket guard refresh:
known missing derivation metadata is the explicit repair target; unchanged
source/tool/lock guards remain preconditions, and all three original raw-file
expectations are mandatory postconditions. Do not reuse the failed inspect
runner to perform these mutations.

Require actual exit0 without ignored-option/settings warnings, complete retained
stdout/stderr and settled groups. Inspect only the three new own symlinks and
their exact targets immediately. The target set must be precisely the following,
once each; record actual numbering-to-target mapping rather than assuming list
traversal order. Retain stdout verbatim; any printed own-root paths must resolve
through this recorded mapping, not be mistaken for output paths. Unexpected
reported paths or extra results refuse admission.

| Exact derivation target | Regular file mode/bytes | Raw SHA256 |
| --- | --- | --- |
| `/nix/store/za8m52vzbdn32yxiagkdjxi4n84gbr8r-nix-shell.drv` | 0444 / 4680 | `29f33a38d1297d3b58c3311d0c62b385f1f7462c1ff7f6c44e19816edf712824` |
| `/nix/store/d0jjibskvbdiyg0wad1510f4iggzicll-playwright-browsers.drv` | 0444 / 2184 | `95cc590be7ab365980b493dda29a8219a1108b5073ce3b3a340a46e1854b0574` |
| `/nix/store/8q2z94mf32mv0j8wxlsshm805xlfysi9-workspace-repository-review-assets-1.0.0.drv` | 0444 / 3120 | `17e5058c9d5b36cb41e590c538e5ab3a79de614aae13f8cdd85802ad72bd9927` |

Standard command success, bound tool/argv evidence and the exact own symlink
targets establish registration according to the documented interface. Do not
globally query roots, enumerate auto links or invent their names. Retention
depends on keeping these links at their registered locations; do not move,
replace or remove them. It is not a continuous availability observation or an
explanation for the earlier disappearance. Rooting the .drv retains its metadata
dependency graph; it does not certify required output closure availability.

Retain the existing exact-three, nonrecursive `nix derivation show` command as a
separately recorded postcondition in this new phase, with its unchanged bounded
no-build options. Require readable complete metadata matching retained JSON
SHA256 `3206262ee0e0eca4fa20d0b2d2612e026402af3b4f89ca0b67ce4566c7ffa600`
semantically, all three expected outputs, raw hashes above and final guards.
Presence alone is not validity/build proof. Parent accepts this phase before a
fresh **separate read-only recursive inspection**; that inspector retains zero
GC-root/realise/build/materialization commands and rechecks these input bindings.
No output build follows automatically.

On any failure, preserve actual status and partial derivations/roots/results;
stop and report. A new root can exist even after aggregate failure. Do not delete,
unregister, replace, repeat or hide partial effects. Future reconciliation is
limited to exact owned objects and needs lead disposition.

## Evidence and limits

Owner2 observations `b1b34965…`, bindings `88d03124…` and SHA256SUMS `4549629f…`
were independently hash-matched. Earlier materializationv2's actual command0,
top-level read0 and delayed05:53 raw equality remain historical; the later single
lstat observations establish za8/d0jj absence and exact8q2 only at their times.
No DB, cache, GC, deletion or source-defect cause has been established.

Selected local manual root:
`/nix/store/addg4icdw1xadiwh6bk4lql8bxbvf11i-nix-manual-2.34.9/share/doc/nix/manual/`.

- `command-ref/nix-instantiate.html:213–225`, SHA256
  `9c26805c4aa500cf54ee96fb0cef605cdbdaf0e9c63af4dd3de10ea0b438fbb6`:
  normal instantiation, accepted top-level values and --add-root cross-reference.
- `command-ref/nix-store/realise.html:205–229,293–319`, SHA256
  `23852541db94cc60a2597293463084dc9f2b646c0046bce593fac529e1fefa5e`:
  .drv realization builds outputs; root registration, indirect link, numbering,
  and prohibition on moving registered roots.
- `package-management/garbage-collector-roots.html:201–212`, SHA256
  `d3f575e7ae81cde0810480854cf4d3b88c5aa2e3d96aa9c690e8f99dcc51bed8`:
  roots retain store objects/dependencies and the symlink indirection rule.
- `command-ref/conf-file.html`, SHA256
  `4426648e44da36d28e8bf588838a7192f16d35aa6959addf20e344cc75144b49`:
  IFD prohibition, cache/substitute/registry settings and max-jobs limitation.

No application design change, consumer repin or source correction follows from
this method. Keep design497769/6bcf and the naming/system packages unchanged.
Owner2 prepares only after parent acceptance; a fresh parent-released utility
owns execution after the active system operation settles. Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
