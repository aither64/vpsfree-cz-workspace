# C0312 postreview proposal — accepted and released

Lead accepted reviewer0 final review with no findings at the exact range and
released this complete check plus conditional own-publication package. Actual
commands/results are recorded separately; the scope below remains unchanged.
Candidate `2e32c814d3af70ac39257f2542075bd580ee38d4`, accepted base9113caa0,
clean own `vpsadmin-webui-0312` / `dev/vpsadmin-haveapi-0312`. Main40653 remains
intentionally excluded. No source/test change after the committed quick packet.

The actual JS delta is Version-only; declarations and complete app/BFF/fixture/
tooling/Node/flake/security inputs equal reviewed e468. Quick123 actual-library
cases, six source guards and full ci:quick passed. Those are retained at their
actual input identity; no repeated quick gate or focused fixture run is proposed.

## Smallest batch respecting current repository wording

AGENTS requires `npm test`, build and relevant checks. The current
`docs/design/HAVEAPI_CLIENT.md` additionally says: **“Run full unit/build and Nix
frontend/source/package checks after committed-deliverable review.”** Therefore
propose full `npm test` once, solely to honor this explicit guidance, then normal
production build. The package defines `ci:tests` but does not require that whole
aggregate for this patch; omit it and its extra script/BFF suites. This is not a
new semantic need inferred from the version constant. Lead can explicitly select
scoped patch verification if superseding that general full-unit instruction.

From the own worktree, with `NIX_CONFIG` max-jobs1/cores2:

```sh
taskset -c 60-63 nice -n 5 nix develop \
  --profile <C0312-records>/toolchain-profile \
  -c bash -ec 'npm test; npm run build'
```

Expected4–7minutes based on e468's unit237.5s/build21s at the same resource cap;
estimate only, no timeout. Bash-e prevents build after test failure. Keep full
log/status/time/counts and truthful exact2e32/dirtyfalse normal build metadata.
No BFF install/test57, script228, browser/expiry/SDK, API or VM campaign.

Only after pass, build the affected outputs/checks normally:

```sh
taskset -c 60-63 nice -n 5 nix build --max-jobs 1 --cores 2 \
  --print-build-logs --json --out-link <C0312-records>/nix-result \
  .#frontend .#bff .#checks.x86_64-linux.provenance \
  .#checks.x86_64-linux.source-contents \
  .#checks.x86_64-linux.package-contents
```

Expected1–3minutes with normal cached dependencies. New frontend and BFF outputs
must bind exact2e32 even though BFF implementation/dependencies are unchanged.
Retain all five ordinary persistent out-links, source root and toolchain profile.
Record actual derivations/outputs/NARs/references, full locked metadata, complete
recursive derivation/input graph and recursive output closure; verify both build
metadata files agree at exact2e32/dirtyfalse. No old-path/output equality claim.

## Ownership, stop and handoff

Fresh current/environment/head/clean/tested-hash/locks/capacity preflight before
launch. CPU60–63/nice5/Nix1job2cores, explicit bash/loginfalse, no host policy
change. Fresh pinned Luna/low for a free released utility slot, with actual
policy verified; visible parent fallback if unavailable/mismatched/busy, without
waiting or competing. Each owner retains its command handle/log/exit until
reconciled; waits at most50s and progress at safe boundaries.

Stop and diagnose any actual failure before retry/source repair or dependent
execution. Source/input mismatch stops before build; stop only an owned
unexpected actual kernel compile under the existing guard, not modules/initrd.
No arbitrary quiet timeout, foreign signals or automatic new campaign.

After pass, reconcile exact source/hash/locks/roots/process effects and report
artifact identities/no active source writer. Publication remains separately
conditional on lead's release, fresh canonical SSH own-ref/default boundaries,
normal hooks and an explicit one-ref no-force push; no PR74/default/native move.
Old browser failure/paired-pass and native unknown-metadata limits remain scoped
as recorded. E3 owns later actual native outputs, Go panel and deployed TLS/login;
this proposal adds no provider fix or cluster action.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
