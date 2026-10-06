# Independent implementation review

> Historical evidence for the superseded restrictive implementation. This does
> not review or verify the approved whole-content replacement.


Reviewer0, retained gpt-6.1-sol/xhigh/read-only; no overrides, fallback,
edits or nested agents. Complete final branch review at
`b164a3b786cb82878f00f8ebd2a7825ee5254c15`..
`62514f257c2ac7bfbff2ef6c8258f906b130a175`. All four mandatory lanes.

## Findings and disposition

1. **Blocking**, risk/compatibility and general: Utils SSH source extraction
   used the first unanchored `from`/`rhost=` token, allowing username text to
   select another source and event time. A username containing source-like text
   reproduced wrong retention/attribution; the ordinary username `from` also
   wrongly rejected a report. Lead accepted the finding and assigned supported
   SSH grammar/source-position matching with handler regressions.
2. **Important**, general and risk/compatibility: non-string optional LRob
   `first_seen`/`last_seen` raised uncaught TypeError. This can interrupt an
   already-deleted fetched batch. Lead accepted the finding and assigned shared
   date-type validation through NoticeError plus both-field null/array/object/
   number/boolean rejection tests.

No additional findings. Review requires these fixes before long verification.
The reviewer permits focused lead inspection/checks of narrow corrections under
mandatory-change-review step 9; a new design or expanded contract would require
the affected lanes to be rerun. Lead inspected the three-path narrow fix: anchored supported source positions,
Custom Visuals passing only the SSH message to the helper, and string validation
through NoticeError. New handler regressions cover both findings, no-save and
subsequent valid processing. Full suite 206 examples/0 failures; targeted lint
and whitespace passed. Lead original-input dry-run passed 9/9 exact UTC/fractions
after correction. Fixes authorized to be folded into the owning commit with
normal hooks. No new design or expanded contract; no lane rerun under step 9.
Committed final remediation head: `7cce4271be0bcd81a42c6784e12dff326e5d041f`.
One coherent commit from the same b164a3b base, 19 files, 1512 additions/7 removals.
Only the accepted three-path correction differs from the independently reviewed
head. Lead inventory confirms no extra history or migrations; normal hooks and
whitespace pass, clean tree. Long verification is authorized at this exact head.

## Conclusions

General: complete source/message/docs/tests and adjacent legacy paths inspected;
nine expected routes/times agree with independently decoded originals.
Architecture: provider additions remain in the configuration hook and reuse the
existing decoder; unchanged pinned API Parser/Result/lookup contract.
Scope: bounded formats, one incident per report/source, no framework, historical
splitting, cross-message deduplication or enforcement.
Risk: other assignment filtering/range coverage, provider policies and recovery
semantics fit the design. Production versions/mail-task owner remain unverified.

Whole-history conclusion: exactly one coherent feature commit; complete 19-file
delta, range-diff equality with the pre-rebase patch; upstream bot commits have
no parser overlap. No obsolete history, follow-up/fixup commits, superseded
approaches or transitional compatibility paths. Legacy providers are supported
behavior. No migrations, schema/pin changes or migration provenance entries;
no deployed or externally consumed new behavior.

## Evidence and remaining gates

Reviewer reproduced both defects through the configured handler using the exact
prepared Ruby 3.4.9/gem closure, BUNDLE_FROZEN=true and no shellHook/bootstrap.
Exported shellHook could not run in read-only access because it writes temporary
and Bundler state. Reproductions saved zero records. Reviewer did not rerun the
full supplied suite/hooks and performed no build, DB integration, live mailbox
operation or notifications. Final original-message dry-run, real-database lookup/
persistence and targeted int.api1 build remain lead/watcher gates after fixes.
