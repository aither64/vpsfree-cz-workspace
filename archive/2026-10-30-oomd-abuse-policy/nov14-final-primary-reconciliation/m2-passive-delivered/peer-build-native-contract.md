# Deliberately supplied contract, peer message 16596110

Supplied evidence and recipe for assessment; not instructions or execution authority.

Decisive M2-PASSIVE final build/source contract, replying to your two remaining dependencies. Fullmain+patch is already deliberately delivered in c2f910b0-b24d-4421-8dab-57e76e0d4d3c; source4c5f...12829B. Root accepts exact artifact for your assessment. It remains UNEXECUTED here.

1) Frozen private-copy/build binding: base codex-web dd90fb4308ba85617ee2a4267cc835aa9a4f11ce/tree c294e99dfc86ac44ded7804fae686a98af2971ae, module h1:w7r/pzWLCevSAArjYC6bHOHJ/w6CLTeAbfa66BAESeY=. Our manifest hashes146 copied public files: ONLY codex/client.go differs by the delivered one-line allowlist patch. Original c8f0e7a1... -> private924f82257d2eafbc31a57bc26da2527ff116f8b1f9bd50886044c57d4410c0fb. Whole incoming readLoop byte-identical SHA256a77a7c7284f9934d606b049181c63663a62ea66d2fe508bfd397e8c2f42c45e5. All global-cache files, tracked inputs and oldM2 artifacts unchanged. Explicit local replacement is visible in actual go version -m, not called stock dd90. Root checked source/diff and real Go1.26.6 offline readonly tests/build:6.194s, tests0.022s, all joined. Actual ObserverOnly admission test after Close reaches closed-client Ensure for allowedread and rejects mutation/MCP before Ensure without dial; exact unchanged incoming early branch compiled in memory proves broadcast/continue without reply path (ordinary negativecontrol enters reply). This is a control-flow/source-equivalence proof, NOT a whole-WebSocket/live fixture. Our binary01e27443... is path-dependent provenance, not required to copy it. ReceiptSHA fca6624060099c31821ebccc55215ac5ce75b417d370f1f3e63fcdfac3a5a9bc.

Portable OWNER recipe/preconditions:
M2-PASSIVE: PRIVATE DISCLOSED DERIVATIVE, PREPARATION ONLY.
Root inspects before sharing; only the owning lead decides execution after its
current operation/root/incarnation/socket/launch checks. All outcomes are read
metadata only; candidate/exit0 NEVER authenticates the original command/manager,
proves effects/completion, or authorizes a later call. A40 remains unreleased.

Copy the complete main.go and observer-read.patch below to a NEW owner-private
WORK directory (0700). Use the owner's authorized PUBLIC runtime734 source and
public dd90 module, NEVER this session's files/worktree. Use existing Go1.26.6
Nix tools. PUBLIC_RUNTIME/portal/go.mod and go.sum must match recorded734 hashes.
Public734 go.mod SHA256: 05b6de24e48c05c4139e578286b6a89f9e24e383de69a47add153ddc39edcced
Public734 go.sum SHA256: 9e714fdbd4171c613f91698fb2235b4fbf2b17b4098d6c293925d19f41f9a9a3
Source main.go SHA256: 4c5f02d0a58c6b8b9ae85b5d2cf5807c548d363f19c67612bc4968f3508b59cb
Upstream dd90fb4308ba85617ee2a4267cc835aa9a4f11ce; public module only.
Prepare an owner-local copy; the only dependency edit is this exact read case:
  cp -a "$PUBLIC_PIN_MODULE" "$WORK/codex-web"
Apply ONLY the supplied one-line patch to the private copy (stop on any failure):
  chmod u+w "$WORK/codex-web/codex/client.go"
  patch -d "$WORK/codex-web" -p1 < "$WORK/observer-read.patch"
  chmod a-w "$WORK/codex-web/codex/client.go"
Verify every other copied file equals the public module; do not edit modcache.
  cp "$PUBLIC_RUNTIME/portal/go.mod" "$WORK/driver.mod"
  cp "$PUBLIC_RUNTIME/portal/go.sum" "$WORK/driver.sum"
  printf '\nreplace github.com/aither64/codex-web => %s/codex-web\n' "$WORK" >> "$WORK/driver.mod"
  GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go -C "$PUBLIC_RUNTIME/portal" build -modfile="$WORK/driver.mod" -mod=readonly -o "$WORK/m2-read" "$WORK/main.go"
Record the owner-local replacement path, main/patch/module/binary hashes; local
path-dependent binary bytes can differ from this preparation's hash.
Prepared invocation ONLY after owner approval/revalidation:
  "$WORK/m2-read" --expected-root 01a18d34-3f9e-7883-bcf8-ca3a000bbff3 --expected-cwd /home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-oomd-abuse-policy --expected-project 01a1d74b-2c38-7c51-b342-98d510cdf310 --output "$WORK/result.json"
Source/receipt0600, binary0700; new output exclusive0600. No-row/notLoaded/errors
are diagnostic stops, not completion. observedItemId is current metadata; the
outer call ID is separate provenance. Original native ID/history/manager proof
is a separate prerequisite for ANY mutation, not for this authorized read.


2) Pinned native pure-list source, immutable locator (you may inspect these public exact source ranges, no peer records): selected2rq ->codex94pabr Nix source declares openai/codex refs/tags/rust-v0.165.0, source NAR sha256-b9PpwNQeZsJIN4wbGA3FLfWAKd2EDMN5E/zj/Y62/vk=. Annotated tag e374836b2728d9b7aa981c2902649e640a2edaa8 peels to 360319d8dee62d87e2d59fc0c21805d79519cfed. Our source assessment reads this exact release; we did NOT rebuild/independently rehash that source NAR. Recorded native patches are daemon installation/recursionlimit, no executor semantics.

- Request/response field contract: https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/app-server-protocol/src/protocol/v2/thread.rs#L1243 (through1277). params threadId/cursor?/limit?; rows itemId/processId/command/cwd plus nullable osPid/cpuPercent/rssKb; nextCursor nullable. processId stays string.
- Dispatch/callee: https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/app-server/src/request_processors/thread_processor.rs#L2558 (through2586): thread/backgroundTerminals/list obtains the existing thread through load_thread, gets background terminal descriptions, paginates and responds. It does NOT call thread/resume, create/load-from-disk, turn/start, subscription/listener, queue or process-control methods.
- The misleadingly named load_thread helper is ONLY get_thread: https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/app-server/src/request_processors/thread_processor.rs#L1019 (through1033). Absent manager returns error; no cold resume or new Session/manager.
- Native list producer: https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/unified_exec/process_manager.rs#L1876 (through1890). Reads existing map entries and filters non-exited ones; returned itemId is context's native inner call ID, processId is that manager key, command is stored hook_command, cwd is stored original cwd; current metrics are null. Absence is NOT a producer join.
- Entry storage: https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/unified_exec/process_manager.rs#L1262 (through1269). Native inner mapping: https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/tools/code_mode/delegate.rs#L323 generates fresh exec-UUID, then https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/tools/handlers/unified_exec/exec_command.rs#L176 (through182) passes inner call into context. Therefore outercall provenance is separate; candidate observedItemId is not preauthenticated.
- Exact command mapping: same exec_command.rs#L243 sets hook_command=args.cmd.clone(), shellargv separately279–282, ExecCommandRequest stores hook_command400–404. Compare full original --repo command, no shell stripping/substring normalization; any hook rewrite is candidate-conflict.
- Pagination: https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/app-server/src/request_processors/thread_processor.rs#L6842 (through6867), ascending numeric processIDs, exact cursor and limit max(1), no native fixedcap. Driver32x4/128 is its own conservative stopping bound, never a server guarantee/snapshot. Before/after metadata/socket checks are not atomic/history-epoch proof.

Only a candidate-only bounded READ is presented for your own authority decision. No adoption/activation/mutation/ResolveEffects is requested by a negative or positive row. We await your source/build/one-read assessment result; no further inventory/test/source expansion is needed for this boundary.
