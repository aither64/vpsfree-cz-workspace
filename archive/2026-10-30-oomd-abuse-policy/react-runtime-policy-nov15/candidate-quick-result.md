# Quick verification result

- Outcome: failed; native exit status 2.
- Revision: `bbd820a65536564756484f6dd037f10224901b35`.
- Command: exact assigned `nix develop --command bash -c ...` chain; it stopped in the first `npm run typecheck` step.
- Elapsed: approximately 91 seconds.
- Full output: `candidate-quick.log`; native exit: `candidate-quick.exit`; elapsed record: `candidate-quick.elapsed`.
- Bounded evidence: TypeScript reported TS2345/TS2769 argument type errors (`string | undefined` not assignable to `string | RegExp` / `Matcher`) in `src/pages/app/incidents/IncidentNoticeSummary.test.tsx` lines 27–36 and `src/pages/app/vps/VpsIncident.test.tsx` lines 74, 82, 162–169. The subsequent requested chain steps did not run.
- Native tool session `85512` returned exit status 2 and is complete.
