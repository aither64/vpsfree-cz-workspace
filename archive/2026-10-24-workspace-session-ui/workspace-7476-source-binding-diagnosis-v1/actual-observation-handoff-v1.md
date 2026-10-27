# Actual bounded tool observation handback

The one explicitly released observation exited0 in 0.122213s,
stderr empty. Raw stdout SHA256 `f627807d5a260c6610929d38eba1ee55128ffee4a888cf46fe4b847f968d9e5d` and all raw
stdout/stderr/exit/time/release bindings are in
[actual-mismatch-assessment-v1.json](actual-mismatch-assessment-v1.json), SHA `ff44008cf49265447dbbc028e3110acb486e1b34e958a4a9d729d77c99b77e16`.
Only dev-session resolution and SHA differ: fqaj/f2f07c46 -> fa7/579af04c;
selected entry remains /home/aither/bin/dev-session. Other five bindings match
exactly, including nix-store. Prior alias suspicion is falsified. No claim is made
about why the installed package changed or its compatibility.

The original sourcebinding attempt remains failed before imports/results/Nix and
current source guards. No retry or followup live query was performed. Source/Git
and all historical expectations remain frozen. Nested G.S/identity adaptation is
explicitly held pending architect/lead design disposition; no successor package
or copied-spec change was made.

[Raw URL static patch](raw-url-successor-unapplied.diff), SHA `6353e24ab2e48c735853de0e83d64302853ff2015e32c49856314aec551af6a3`, is UNAPPLIED:
parse/compile-object only, only main plus stdlib URL import changed. It validates
the actual metadata.url immutable GitHub7476 path and decoded narHash against
actual locked metadata, retains the raw URL verbatim, and replaces the formerly
synthesized narLockedURI with the observed value and explicit provenance. It does
not construct an observed URL or alter tool expectations. No new framework/test.

Lead owns next disposition/release and durable state. Session remains open.
[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/)
