# Override inherited HaveAPI parameter descriptions with the action DSL

Related initiative: `work/2026-09-09-vpsadmin-pr-43`.

HaveAPI 0.29.8's inherited Index parameters use LocalizedMessage values.
Adding application locale keys alone does not replace those messages: the
parameter metadata fallback keeps their HaveAPI ownership.

For an action with different cursor semantics, use `patch :from_id, desc:`
with a plain English literal in that action's input block. This preserves
the label, type and validation while enabling application metadata lookup.
Run `bundle exec rake vpsadmin:i18n:update` in the API Nix shell, translate
the generated Czech TODO, regenerate, and run `vpsadmin:i18n:health`.

The generator can compact a single application-owned description under
`vpsadmin.attributes.from_id`; do not manually invent a parameters namespace
or force an action-specific locale tree. Other actions with inherited
LocalizedMessage values keep their framework descriptions. Bilingual OPTIONS
requests for UserPayment::Index and User::Index verified this distinction and
confirmed that their other cursor metadata remains identical.
