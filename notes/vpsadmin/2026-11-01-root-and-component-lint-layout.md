# Root and API RuboCop can disagree on chained test layout

During published-advisory correction work, focused component RuboCop accepted a
multiline ActiveRecord .or chain in a spec helper, but root mandatory commit
RuboCop rejected its indentation. The two pinned contexts can select different
layout rules; passing component lint does not replace root hooks.

Use a conventional local relation variable followed by .or assignment when
both layouts cannot agree. This keeps query semantics clear without disabling a
rule. Reconcile the actual staged/rebase state after hook refusal; no commit may
have been created. Preserve the saved original refs/patch and resume the same
edit stop after the scoped fix. Normal root hooks still run.

Evidence: work/2026-11-01-published-advisory-corrections/package-a.md and state.md.
