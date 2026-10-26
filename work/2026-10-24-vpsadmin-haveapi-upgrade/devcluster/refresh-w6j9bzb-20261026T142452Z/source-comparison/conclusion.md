# API path-input comparison and prepared generation rebind

Preparation only. No source graph acceptance or activation is implied.

## Exact source difference

The old rooted `/nix/store/s2cgrahgwq60ngfj230fv5gn912cdr0k-source` has NAR
`sha256-4l9c0i/1a3ia7r9ylbZeOv0IzYC6Q9PUUpXEg6+c4EU=` (167,459,072 bytes).
The exact new locked source resolves to
`/nix/store/cwrqv2vbg7rj1wf29a1inr84ppgvaz57-source`, NAR
`sha256-7+95mErWohWFPhKV1g7NkUP7k0ftftDIXS1q+hMnQQA=` (167,459,648 bytes).
Resolution used one offline `builtins.fetchTree` evaluation with the full
locked path/NAR/lastModified, IFD=false and max-jobs=0; exit 0 in 9.19 seconds.
No second full metadata evaluation or build was needed.

All 22,526 entries in each snapshot were compared by type, store permission
mode, regular-file content SHA-256 and Git blob ID, executable bit, and symlink
target hash. Only `api/Gemfile.lock` differs. It is ignored, nonexecutable,
mode 0444 in both immutable store snapshots:

| | Size | SHA-256 |
| --- | --- | --- |
| Old | 18,519 | `a927d1da4744012cd8ca987e7e06cb4cbe1de11543c0ab60533f436fa1cd6396` |
| New | 19,094 | `d9e69553a7a705ed64751e742bcd345de5147d85301f6397db378c12a3055202` |

Both snapshots match all 3,161 tracked paths' blobs and executable/symlink
modes at `70a2ed54b98d0c2f359a9cc4484452a257a9807b`. The other 22,525
entries, including Git pointer, configuration and cache entries, are identical.
Of 186 lock/version paths, only this ignored lock differs. No configuration
values or raw ignored configuration were printed. Snapshot hashes establish
the byte cause of the NAR change; the process that rewrote the lock was not
independently established and is not attributed here.

The new lock adds four specs and their checksums: `fio_api 0.0.11`,
`httparty 0.24.3`, `csv 3.3.6`, `multi_xml 0.9.1`; their declared dependencies
and the top-level `fio_api!` entry are the only other added lines. No lines,
specs or dependencies were removed or changed. Source headers and Bundler
4.0.23 are unchanged. HaveAPI server/client/Go-generator/Rust-generator gems
remain 0.30.2 with identical declared dependencies.

## Consumer relevance and recommendation

This ignored lock is **not excluded** by `packages/source/default.nix:8`:
the filter excludes `.gems`, `.git`, `result` and `tests` directories, then
copies the remaining source. Thus the source package really includes different
lock bytes; derivative source/package/toplevel identities may change. This is
not a claim of equal build outputs or reuse of prior cluster artifacts.

Native API/database/supervisor commands select `${package}/ruby-env/bin/bundle`
through `nixos/modules/vpsadmin/api-app.nix:40` and the provider's seed commands.
`packages/api/common.nix:13` constructs that bundler environment from the
separate `packages/api/` gemdir. Its `Gemfile`, `Gemfile.lock` and `gemset.nix`
are byte-identical in both snapshots and already contain the same four versions.
Nixpkgs `bundled-common/functions.nix:14` selects those files;
`bundled-common/default.nix:117` copies them into its configuration output.
`bundled-common/gen-bin-stubs.rb:35` forces `BUNDLE_GEMFILE` to that packaged
Gemfile, frozen mode and ignored Bundler configuration before setup. The wrapped
Ruby likewise sets that packaged Gemfile (`default.nix:194`). The copied
`api/Gemfile.lock` therefore does not select gems for these native startup
commands. No substantive API/runtime contract change is established by this
delta. Actual built/runtime proof remains outstanding.

Recommendation to lead: accept the new exact path-input NAR for Package E as
an explained ignored-lock payload difference, preserving its identity and this
scope limitation. Do not clean/reset/rewrite the ignored file, change a ref,
pin a workaround or claim source/artifact equality. The new graph remains
unaccepted until lead disposition; immediate pre-start checks still apply.

## Bounded driver identity update

Per lead acceptance, only the driver's `RUNTIME` and `PROVIDER` assignments
were rebound to selected `w6j9bzb...` / `q19s1vj...`. Prior accepted driver,
command and static-check bytes/hashes are retained at
`devcluster/history/fa7zlb-accepted-activation/`. The command document adds
only the selected identity note. No driver behavior or resource policy changed.

AST comparison confirms exactly those two changed assignments, Python parsing
passes, both shell blocks parse, four synthetic output-filter checks pass, and
both installed public command realpaths match the new runtime guard. No driver,
scope, native startup or guest was executed for these checks.

- Current driver SHA-256: `2473cac0fa3ca6b97d8e97d7c3755dfc5e18e79e87fc68e9d9f5be3572a358bf`.
- Current command SHA-256: `1635cf1a0d57e3655e89c7223794db2c247a8f15e20b2437abe13344f209e5be`.

Exact evidence: [comparison](comparison.json), [lock semantics](lock-semantic-delta.json),
[resolution](resolve.json), and local old/new content manifests. No source,
ignored lock, Git state, host/foreign hold, lifecycle, KB or staging mutation
occurred. Activation remains unreleased pending the lead's final VPS-ops and
guest/process clearance plus fresh immediate graph/native/IP/capacity checks.
