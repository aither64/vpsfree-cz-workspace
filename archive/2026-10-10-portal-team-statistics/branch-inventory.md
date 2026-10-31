# Final team-work notice branch inventory

## codex-web

Base: `c9878454f07da244c103b8a79340b92b6d5bf052`
Head: `7aff1632ee97c177e68c8bc45258abe055a087dd`

```text
4e0b9b29dde8aa342602014e384807275cfbac42 codex: count lifetime activity and recognize automatic waits
7aff1632ee97c177e68c8bc45258abe055a087dd codex: recover work observation after historical sleep
```

Final diff: `codex-web-final.diff`.

## dev-workspace

Base: `a756b2c6a3ec30efaf5fd25dccf1717c21a8efa8`
Head: `27ff7949944f79322b810fae7dd1a6e359d985c4`

```text
49ba4d65079e7aec0c0c94a8d3274427d1406c7f deps: select recovered activity reporting from codex-web
8aea65312193b0dab917000a334811886b17a290 portal: show retained team activity and lifetime statistics
40c8025805f047fac76b810d54f3c2bf87698409 portal: save model choices in active and stopped sessions
40abb17b4f9c626a22b7387260858c63375f0b5c portal: fit team metrics and settings into compact columns
27ff7949944f79322b810fae7dd1a6e359d985c4 portal: show ongoing work by other team members
```

Final diff: `dev-workspace-final.diff`.

## workspace

Base: `d68d8d8313f8acc5fc17a7b216f0c837b1276f88`
Head: `bb21a0f0a7d3a337ea4675dd703e4c535eeb22e8`

```text
0b2dd9dbf8a9696f2cbc7316118ab88088140960 workspace: select team statistics and activity notices
bb21a0f0a7d3a337ea4675dd703e4c535eeb22e8 instructions: route detailed branch readiness rules
```

Final diff: `workspace-final.diff`.

## vpsfree-cz-configuration

Base: `6e4947b52abe103c582bfab2d0b37a8f17a7c02d`
Head: `14cd296ad24cec0d62161f691c7d0374bda9e35c`

```text
14cd296ad24cec0d62161f691c7d0374bda9e35c inputs: set devWorkspace to 27ff7949
```

Final diff: `vpsfree-cz-configuration-final.diff`.

## Disposition

No migrations. Prior deployed source heads remain in v1/v2 tags and rollout.md.
All three pin streams have one final update; configuration generated from its
supported base using confctl and hooks. Workspace base is current master d68d8d83;
its original registration base is 1025d8c3. Review fixes and the later member API
fixture correction are folded into the owning notice commit. The latter changes
only test identity/routing; production assets are byte-identical to 2024a428.
Workspace instruction patch remains equivalent. No obsolete unapplied functional
approaches or new compatibility paths. Reviewer whole-branch conclusion and
narrowly verified corrections are in review.md. Two unused old go.sum checksums
are an accepted advisory; they do not select an older provider.
