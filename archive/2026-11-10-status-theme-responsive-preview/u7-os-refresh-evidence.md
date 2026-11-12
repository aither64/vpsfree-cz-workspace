# U7: ordinary test-OS dependency refresh

Owner implementer0, retained Sol/xhigh/workspace_write, capacity accepted after
U5 completion. Identity/environment and live same-session roster verified.
Accepted C8 brief: [design.md](design.md). Base
`c4e11ec3f933de75f782b95bb3034ca31e3034d5`. Final separate head
`b589972c57a22fb806a643a1de9a683beca3a363`. No rejected C7 input split or
declaration override.

## Source and graph

Executed ordinary `nix flake update vpsadmin/vpsadminos`, with no manual JSON,
global update or override. Only three locked entries change:

| Input | Previous | Final | Final narHash |
| --- | --- | --- | --- |
| vpsAdminOS | `837baf04054c6ee0e71d288b8870ac42a6990c38` | `650170d699e3033c5279b911a2ef0a355439613c` | `sha256-5J/SysGaU9/12R6HGx1qxJI4WsK1Y1qKFM4fPKxVTqY=` |
| impermanence | `7b1d382faf603b6d264f58627330f9faa5cba149` | `fa627f4c8b8e92f58f58a73d99ee4e1304e64eb2` | `sha256-s0TeXWG5Ci75Y/Hzon0Z7NrN/fG773Rc54/z6oPFszQ=` |
| nixpkgsUnstable | `f13ff45afd1bb73e640eaa08a7066dbed07e3238` | `f4a03c008967841f2a0b3cb7c436fc6fc31671f6` | `sha256-ziZn2PvCJE5JEEpqTdxXwJpPB+L3YqoCpTAMCzyaP3U=` |

Exact semantic comparison verified all other nodes, source hashes and follows
unchanged. `flake.nix` matches the base byte-for-byte. vpsAdmin stays
`3f9b68adb97b7f43df929a85fc172d9d11e15211`; shared/root stable nixpkgs stays
`ac588ef1c914865dad517b337ea0eb9694a4021c` with Go 1.26. Source scope only
`flake.lock` and a short reusable test-baseline note in `tests/README.md`:
15 additions / 9 deletions. No Go, runtime API, schema/data, UI, kernel source,
suite assertions/resources/timeouts or production rollout changes.

The selected upstream OS changes the default test kernel from 6.12.95 to
6.12.113. Old vpsAdmin/new OS integration is unverified until the real full
suite runs; cache availability alone does not establish compatibility.

## No-build gate

The gate imports the selected runner's actual `evaluate-tests.nix` in complete
testJson and metadata modes, using ordinary no-update evaluation. Final policy
allows already-realized IFD reads while disabling local builds (`max-jobs=0`),
remote builders (`builders=""`) and substitution (`substitute=false`).
It collects the complete recursive config derivation graph. Both plain and
builtin-ZFS kernels must exactly match these published stable-baseline paths:

| Variant | out | dev |
| --- | --- | --- |
| Builtin ZFS | `/nix/store/b043pwyanxjfz22hbiibv5wipqqcl932-linux-6.12.113` | `/nix/store/5kahy705jlci2fhhwmjr3hjn1cad8264-linux-6.12.113-dev` |
| Plain | `/nix/store/6fknvi25ssxff96569ykjd0pnnvsyi5n-linux-6.12.113` | `/nix/store/8jpmywdph9hpjd7irr5jnfai8ir95r99-linux-6.12.113-dev` |

C8 baseline: upstream run `42803793083`, stable job `129787930399`, toplevel
`/nix/store/84j4bizm2y0slcl96xqaxjwacqyllwsh-vpsadminos-system-vpsadminos-26.05.git.650170d`.
After exact matching, all four outputs passed `nix store verify --store
https://cache.vpsadminos.org --no-contents PATH` (0.517s total). This confirms
available metadata/trusted signatures without downloading kernel contents.
No kernel/system build or VM occurred. Exact source-normalization prerequisite
was separately authorized and realized as recorded below.

Frozen source: `u7-eval-source`, base c4e11ec plus only the two U7 paths.
99-file receipt `u7-eval-inputs.json`, digest
`1e744494fcf2876ddcd31070c70878f11c7e6f408b0415e0f61c93c6dc392286`.
Framing is SHA256 of canonical JSON path-to-per-file-SHA256 mapping, sorted keys
and separators `(',', ':')`, not raw path/content NUL framing.
Final full-eval script `u7-eval-gate.py` SHA256
`8c62508db28be6141a35ae6649ade69dd473ca2cb555b518a375ef80ea432fb7`.
Lead-owned watcher v3 `654bf853-0997-4dd0-a416-20a5d0d90b28` completed actual
full evaluation, then failed in identity serialization handling. Its persisted
testJson/metadata result was reused; no repeated full evaluation followed.

### Gate result and bounded harness corrections

- Complete actual selected test config:
  `/nix/store/i3zn05pf87z14bwgqzvqq05ykn75ybs3-os-test-status-page.json.drv`.
  App package in this frozen path snapshot:
  `/nix/store/79rg9s1xkih65p5fx4rlfpnj2v9psfd9-vpsf-status-dirty.drv`.
  The snapshot is a path flake, so package version is `dirty`; final-head
  package version identity is left to the actual full run. Source bytes match.
- Full recursive graph in `u7-eval-gate-v3/derivations.stdout`: 6,658 derivations,
  26,707,709 bytes. Both kernel derivations and all four outputs match C8 exactly:
  builtin `/nix/store/avd0kbbv96nvfkjjnm6gmldbl1rqfrh9-linux-6.12.113.drv`;
  plain `/nix/store/md61flvfj3zp6k2a06kk5w3n2wbllm9h-linux-6.12.113.drv`.
- Metadata retains three VMs, 14 CPUs and 17,920 MiB memory/shared memory. Go is
  1.26.10. No test/resource/assertion changes or mixed-version success claimed.
- Initial harness passed a contextful `flake.outPath` string rather than the
  actual CLI's path argument. Corrected to a literal snapshot path. Installed
  Nix 2.34.9 derivation JSON is schema 4 with `derivations` envelope, relative
  names and `inputs`; the reader was checked against one actual derivation.
- Required generated vpsAdmin source was missing. Lead authorized only
  `/nix/store/hcxvnrfjxj9kzskkvvlgbb0nvqnvpp49-vpsadmin-source-unknown.drv`.
  Its initial unrooted output disappeared before retry. Rooted realization then
  completed at `/nix/store/bs71zq9jd3v9bpqch69f7k8z1qfjx2b8-vpsadmin-source-unknown`,
  retained by `u7-vpsadmin-source-root`. It copies source/inserts revision files
  and normalizes shebangs; no kernel/system compilation. Keep this root through
  full integration; no cleanup/lifecycle action authorized.
- Tiny real prerequisite reads succeeded under the final no-build/no-substitute
  settings. A missing derivation probe failed closed with local builds disabled.
- Nix coerced identity attrsets containing `outPath` to strings after complete
  eval. Renaming only that field to `sourcePath` fixed the identity-only check
  (0.268s); saved as `u7-eval-gate-v3/input-identities.json`. Root/OS ac588,
  old vpsAdmin3f9/new OS650 and their content hashes match. Reused the persisted
  full config, read its graph once, then performed four fast trusted-cache
  signature checks. No generic resume framework or repeated cold full eval.
- Final signatures saved in `u7-eval-gate-v3/signature-verification.json`.
  All four exit 0. C8 HTTP200 narinfo/run provenance remains linked above.

## Verification and delivery

- Semantic lock graph/source comparison, lock JSON parse, `git diff --check`:
  passed.
- App source/stable package input unchanged; existing Go/UI evidence reusable
  within its scope, not a substitute for complete config and integration checks.
- Lead directly approved the actual reusable README paragraph unchanged.
- Complete config/kernel/cache gate passed through the reconciled evidence
  above. Required Nix/Lefthook 2.1.5 i18n hook passed 0.36s (0.38s total), gofmt
  skipped without Go files; commit used the required temporary message file.
- All 99 compiled/logical source inputs still match the frozen receipt after
  hooks, final head bound in `u7-final-inputs.json`. Worktree/index clean and
  exclusive commit window released. No unexpected hook effects.
- Independent exact-head final review and real old-vpsAdmin/new-OS full suite
  remain lead-owned. No broad Go repeat, kernel compilation, duplicate full
  test invocation or product source changes for harness repairs.

One separate logical dependency correction is committed after U5. No migrations,
transitional schema history or production state boundary. Coherent revert of
this lock update restores the original known cache mismatch, without data
conversion. Use fresh isolated test state for the refreshed runner/OS rather
than resuming C5's interrupted run. No push, integration, services or lifecycle
actions by this package.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-status-theme-responsive-preview/)
