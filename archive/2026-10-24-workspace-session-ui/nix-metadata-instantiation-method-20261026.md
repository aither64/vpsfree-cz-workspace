# Explicit derivation metadata instantiation

Status: static method proposal for lead assignment2633346a, not an execution
release. Owner2 prepares the successor after lead acceptance; the parent owns
the fresh policy-selected watcher/max1 launch. Architect read only the selected
installed manuals and named frozen receipts. No Nix/help/query/eval/build,
network access, store inventory or source/Git mutation ran. Existing
design3952/6bcf3717 and all original packets remain unchanged.

## Disposition

Use the selected Nix2.34.9 **legacy explicit read/write evaluation** for the one
metadata operation. It can preserve the exact frozen JSON expression while
instantiating evaluated derivations. Do not invent `--read-write-mode` for
modern `nix eval`, or `--offline` for the legacy command. Retain explicit
no-build settings and use the documented cache settings below, recording their
limits rather than calling them a network prohibition.

Modern `nix eval` documents `--read-only` as “Do not instantiate each evaluated
derivation.” The original argv did not select it. This does not explain why two
files were absent at the later observation. The local documentation supplies no
evidence that evaluation caching, string context, GC or deletion caused this
case. Disabling the eval cache below removes that option from the new invocation;
it is not a diagnosis or a claimed fix for the old result. There is no accepted
selected implementation-source pointer, and none was searched for or fetched.

Legacy `nix-instantiate --eval` alone explicitly hashes/discards store
derivations. Its `--read-write-mode` documentation expressly says evaluation
then instantiates every evaluated derivation. `--strict` recursively forces
the finite JSON object's attributes; `--json` retains the existing output
shape. No expression rewrite, context manipulation, derivation reconstruction,
manual store import or output realization is needed.

## Exact proposed command construction

Read `argv[-1]` verbatim from
`runtime-final-c31-browser-preparation-v1/environment-evaluation.json`.
Verify plan SHA256
`6bbb1b78ab685036b39bd68202da07dba6757c2b735105248f8b9e1236629591` and UTF-8
expression SHA256
`80f68639955bb4ad750093fa509a82b28a286e2526bc52ffe3f8206e277a566d`.
Keep the original cwd and environment/tool guards. The successor argv is:

```text
<verified nix-instantiate launcher from selected z4w... Nix2.34.9 output>
--eval --strict --json --read-write-mode --impure
--option allow-import-from-derivation false
--option substitute false
--option builders ""
--option max-jobs 0
--option accept-flake-config false
--option flake-registry ""
--option use-registries false
--option eval-cache false
--option tarball-ttl 4294967295
--expr <the exact original argv[-1] as one argument>
```

Construct an argument array, not a shell-interpolated expression. The launcher
must be verified by owner2's preparation against the selected immutable Nix
output `/nix/store/z4wkkj3ncr69vgrb3020saqx1c8mfsjj-nix-2.34.9`; the expected
sibling entry is `bin/nix-instantiate`. Its existence/link/invocation identity
has not been observed by architect. Do not substitute ambient PATH or pretend
the modern executable receipt proves the legacy launcher. Bind its real target,
hash and actual future process identity; if it is absent or differs from the
selected release, stop and report. No new Nix installation is proposed.

All flags/settings above are documented by the selected manuals. In particular,
`--impure` retains access to the exact guarded local helper; it does not permit
changing its frozen source or URI. Keep the original locked c31 URI/revision/NAR,
all locked input identities and helper SHA256
`52cb66707e0b00e51287f500591b08b193f743937f7e7ff0be63e7d70c444a2a`.
Retain the original experimental-feature configuration; no new feature is
required for legacy evaluation of the existing `builtins.getFlake` expression.

`allow-import-from-derivation=false` is the documented no-build boundary:
Nix errors on IFD even when its output already exists, so evaluation does not
require builds. Empty builders, substitute=false and max-jobs0 add the requested
execution limits. max-jobs0 alone is insufficient for preferLocalBuild
derivations; it is not the basis of the no-build claim. Do not add `--repair`,
build, realise, import, deletion or root operations to this command.

## Offline scope and necessary release

The modern manual defines `--offline` as disabling substituters and considering
previously downloaded files up-to-date. It does **not** document a general
network denial or a guarantee that every source cache miss refuses.

Legacy's supported `--option` interface supplies the explicit settings above.
substitute=false disables binary substitutes; the long finite tarball TTL
keeps retained cached downloads fresh for this bounded operation. The selected
manual says the TTL governs NIX_PATH, fetchGit, fetchMercurial, fetchTarball and
fetchurl. This is an explicit documented cache policy, not a claim that it is
identical to every implementation detail of modern `--offline` or covers every
fetcher cache. Empty registry/use-registries=false excludes registry resolution;
it does not disable the frozen explicit GitHub source reference.

The new release therefore authorizes **metadata/cache writes from explicit
instantiation**. It must not promise “no network under all circumstances.” If
required locked-source retrieval is not already permitted, keep that as a
separate lead-released evaluation prerequisite: retrieve only the exact frozen
URI and lock-selected sources, verify their existing revision/NAR/source
identities, then continue. Do not infer that setting a TTL makes absent sources
available, or that all source retrieval is deferred until a later build. The
metadata evaluator may fetch a missing source; preparation must disclose this
potential and the lead must include the exact-source permission or keep the
operation held. No moving ref, lock update, input override, source replacement,
toolchain download/build or automatic retry follows a cache failure.

This matches the lead's clarified requirement for documented offline/cache
semantics, rather than a stronger unrequested network isolation mechanism.
No namespace wrapper, credential/cache manipulation or new runner framework
is introduced. If strict network denial becomes required, this argv does not
establish it and needs a separate bounded disposition.

## Postconditions before the separate recursive inspect

Use a new absent result directory; refuse collisions. Preserve actual argv,
cwd, environment/tool identities, stdout, stderr, exit, timing and joined/group-
empty result. Keep the original180-second command/240-second outer bounds and
record interruption/partial effects honestly; no implicit retry or cleanup.

1. Actual exit0, complete JSON and no ignored option/setting warnings. Parsed
   JSON must equal the original identities.raw.json (SHA256
   `ad06dc09a47a98dbb71cd906f13c9d8c4d188060479ad6d387459333e96103d6`), including
   all nine identities and both shell fields. JSON whitespace need not match.
2. Immediately check only these three roots as regular non-symlink files and
   record fresh mode/size/raw SHA256, followed by the selected modern
   `nix derivation show` on exactly these three paths, without `--recursive`.
   Preserve `--offline` and the same no-build/registry settings; bind its full
   argv before release. Require actual exit0 and complete parseable metadata
   identifying all three roots. This proves Nix can read their metadata at that
   observation, without inspecting the recursive graph yet:

   ```text
   /nix/store/za8m52vzbdn32yxiagkdjxi4n84gbr8r-nix-shell.drv
   /nix/store/d0jjibskvbdiyg0wad1510f4iggzicll-playwright-browsers.drv
   /nix/store/8q2z94mf32mv0j8wxlsshm805xlfysi9-workspace-repository-review-assets-1.0.0.drv
   ```

   The retained8q2 size3120/mode0444 is historical. Compare any earlier retained
   raw hash if available; do not invent one for previously absent roots.
   File presence alone is not store validity, and either alone is not a build.
3. All original source/helper/tool/lock guards pass. A changed JSON field,
   missing/invalid derivation, refused option, unexpected source identity or
   unfinished process stops. Preserve partial metadata; no repair/delete/root
   mutation is implied by failure.
4. Parent accepts materialization, then separately releases the existing exact
   recursive metadata inspection under a fresh no-clobber packet. Successful
   materialization does not authorize the browser/environment output build.

No new retention primitive is necessary for this disposition. Do not pass a
`.drv` to the output-only NON_DRV realise method. An output root does not prove
producer retention, and instantiation alone is not a durable GC root. If the
roots disappear again before inspection, preserve the new evidence and report
it; do not invent an auto-root, repeat a global roots query or retry implicitly.
Any standard `.drv` retention action needs its own exact documented command and
explicit release outside this package.

## Naming and system selectors

The same **acceptance postcondition** applies to owner3's frozen naming
evaluation and owner1's frozen system selector: an evaluated `.drv` string is
not proof of current file/store availability. Their own exact selected roots
need immediate presence/raw identity and store-validity evidence before
recursive metadata inspection, then separate graph/build admission.

Do not mechanically rewrite those argv or switch them to legacy evaluation.
The explicit read/write recipe is applicable only if their frozen expression
is compatible with legacy JSON evaluation, and their exact selected inputs,
tool identity and metadata/source-write scope remain bound. Their owner prepares
any concrete delta for lead acceptance. This answer neither inspected their
mutable source nor attributes the browser failure's unknown cause to them.

## Evidence read

- Owner2's named diagnosis: `runtime-final-c31-browser-instantiation-diagnosis-v1/`
  `facts.json` SHA256
  `4e103f9f8ed7abe64604c30877cc6629a93111f05cee7c4c08e73a3fec8bba77`,
  plus `manual-excerpts.md`. Original failed-inspect assessmentfb72 remains
  untouched; original modern eval receipt records exit0/14.444 seconds.
- Selected legacy manual:
  `/nix/store/hfgddkr6rmz6xxkmvw5fr88wx9fn7znw-nix-manual-2.34.9-man/share/man/man1/nix-instantiate.1.gz`,
  compressed SHA256
  `cbb1c61831a79c2fb7823a861c82242d3b6e36cc5692494d236acc021ffd8bb2`.
  Read Description, eval/strict/json/read-write-mode, and common options.
- Selected HTML manual root:
  `/nix/store/addg4icdw1xadiwh6bk4lql8bxbvf11i-nix-manual-2.34.9/share/doc/nix/manual`.
  `command-ref/new-cli/nix3-eval.html` SHA256
  `0875f6132161ad7cad377041447c22f38b391b6f35206644710b75c7a8821a66`;
  `command-ref/conf-file.html` SHA256
  `4426648e44da36d28e8bf588838a7192f16d35aa6959addf20e344cc75144b49`.
  Read read-only/offline/eval-store and the cited configuration settings.
- Same HTML root, `command-ref/new-cli/nix3-derivation-show.html`, SHA256
  `2103ef34511f4eb1502e0bbaa67b2ed2fc1453ee91f4249bab6e88d458bed7ca`:
  documents JSON store-derivation contents, top-level-only default and
  `--recursive` as the separate dependency-graph option.

Session remains open. This is a verification-method clarification, not an
application design change; no amendment to accepted design6bcf is necessary.
