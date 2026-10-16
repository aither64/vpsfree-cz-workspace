# Affected-lane follow-up review

No Blocking or Important findings. The native instruction-shape adaptation is
accepted for the planned native rerun. This is not a claim that native isolation,
final consumer package builds or deployment acceptance have passed.

## Scope and conclusion

The same standalone reviewer, `/root/final_review`, reviewed general and
risk/compatibility concerns for codex-web
`8851f1c35e9424b1240705cb73d09d387d9276f0` to
`a0561fad8decb794117f8959fa2dd629547c5ba7`. Architecture and scope lanes were not
rerun. Assigned/catalog settings remain `gpt-6-astra` / `xhigh`; no additional
native model/effort metadata is exposed here.

The diff changes only the tagged native fixture and its reference explanation.
It does not change library behavior, policy, public APIs or model selection.
The strict predicate at `codex/ephemeral_integration_test.go:2163` preserves the
instruction proof against the realized exact candidate source:

- `core/src/client.rs:996` builds a `BaseInstructionsFragment` from the explicit
  base-instruction text and prepends it to model input. With Responses Lite
  disabled, the tool schemas remain top-level and this fragment is first.
- `core/src/context/base_instructions.rs` gives the fragment role `developer`,
  empty markers and the unchanged body. `context-fragments/src/fragment.rs`
  renders that body as input text; the protocol's tagged serialization produces
  a `message` containing `input_text`.
- `codex-api/src/common.rs:279` defines the native Responses request without a
  top-level `instructions` field. Rejecting that field, even if a correct prefix
  also appears, matches the selected release rather than accepting two forms.
- The predicate requires the first item's exact role/type, exactly one content
  item, its exact type and exact text. A user-message copy, later developer
  message, appended policy or predecessor field cannot satisfy it. Extra native
  metadata such as the generated message ID remains permitted as required.

The surrounding fixture still independently checks model/effort, tool schemas,
the absence of `additional_tools`, trusted global policy, excluded instruction
sentinels, persistence/streaming flags and actual dispatch/cancellation evidence.
Each utility provider request is checked; native source rebuilds the prefix on
each request. The new assertion therefore does not substitute user text for an
instruction or weaken the remaining isolation proof. The reference describes
the observed source behavior accurately.

## Verification and history

I independently ran the six cases in
`TestEphemeralIntegrationBaseInstructionShape`; all passed in 0.014 seconds:

```sh
nix shell --inputs-from . nixpkgs#go nixpkgs#gcc -c \
  go test -mod=readonly -tags=codex_integration ./codex \
  -run '^TestEphemeralIntegrationBaseInstructionShape$' -count=1 -timeout=20s -v
```

The first attempt supplied Go alone and failed before compilation because cgo
could not find GCC. Supplying GCC from the same pinned nixpkgs resolved the
environment issue. No native integration, long build or deployment was run.
The change passes `git diff --check`, and the worktree was clean at the reviewed
head.

The complete codex-web range remains
`523865195522ad6f4804613e6f54823ddf447924` to
`a0561fad8decb794117f8959fa2dd629547c5ba7`, with exactly two commits:
`4a091c94addf908e05f99d49f0432435845c4cda` and
`a0561fad8decb794117f8959fa2dd629547c5ba7`. The adaptation is folded into the
existing upgrade commit. No obsolete intermediate approach, extra update stream
or migration was introduced. **No migrations.** The original whole-branch
conclusion remains valid for this revised codex-web series.

## Original finding and remaining gates

Original **B1 is resolved** in the inspected runtime head `ca2ae0b`: the managed
fixture now expects 62680 bytes, matching the actual Luna catalog and SHA-256
`049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`. Its native
source prerequisite now matches the candidate's
`/nix/store/9is267xl3palxb615kk86qlli9nggkf9-source`. The source is realized, and
its complete catalog is byte-identical to the committed full fixture. This also
resolves the original report's missing-local-source reproduction gap.

The packet withdraws the earlier cached vendor-probe result as evidence for a
clean build. The observed vendor-hash correction is mechanical, but no current
clean final-package result is claimed here. Refresh codex-web consumer pins and
the corresponding generated vendor hash, consolidate each update stream, then
run clean checks/builds on those exact final inputs. Preserve the original
review's pending native isolation, managed naming, persisted-state and rollout
gates. A successful six-case shape test is not native isolation evidence.

Only this supplemental report was written. The original report is preserved.
