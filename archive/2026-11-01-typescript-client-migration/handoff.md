# TypeScript client migration handoff

Status: implementation, independent review and local verification complete;
PR#126 is open and exact-head remote CI observation is pending.

- [WebUI PR126](https://github.com/vpsfreecz/vpsadmin-webui/pull/126)
- [Stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/)

## Source and review

WebUI final feature head: `14cfdcb6d2a3bc337fd445932fd38916b3dcd9ab`, base/main
`63d484fc070dbee633d32624de545e834d483701`, branch
`dev/typescript-client-migration`. Nine logical commits, tree
`9ce3be45e8a8db79420c5ab40637f2f043fd77d6`;440files,+13903/-9286.
Complete pre-folda0fd tip is preserved. Lead and independent reviewer verified
all nine owner reconstructions, complete tree equality, authorship, one SDK input
stream and no obsolete delivered iterations or database migrations.

Generator foundation: HaveAPI `eea3ae5e82c3db23d5f5bc9f1a5e7784117c4e1b`.
Unpublished SDK: `99ee06654ef956a09b52749f4cd02d1435362087`, version0.3.0.
Normal JS runtime: HaveAPI0.32.0. Exact tracked archive337414bytes,
SHA256`f3bb42d0392fb738f5c70fe1415cc8742ab943a31c2ed2a85af5ccbd385d831f`.
These feature inputs remain unmerged; the SDK package remains unpublished.

Original full-source review found two Important and two Advisory issues, all
fixed and accepted with focused checks. Later packaging and readiness reviews,
and final whole-series/history review, each reported zero findings. See
webui-final-review-result.md, webui-packaging-review-result.md,
webui-readiness-review-result.md and webui-final-history-review-result.md.

## Verification

- Application2227tests/343files; BFF58tests; production Vite3566modules; affected
  script/type/lint/docs/catalog/structural/wire checks pass. Strict E2E104checked/
  178deferred with initial baseline unchanged. Final remote CI remains pending.
- BrowserA124desktop/mobile and B8selectedcs/en cases pass at1bfad6ce, both
  durableexit0 with exact22process/group/listener cleanup proof. Final source
  differs from this tested tree only in the dated work-log evidence append.
- Isolated SDK/API matrix:23calls, durableexit0/62.664s at API610a96f8, SDK99ee,
  runtime0.32.0. Exact owned Node/Ruby/DB processes, temporary database directory,
  listener and socket are absent. API097upstream documentation-hook change was
  source-assessed, not executed or deployed by this test.
- Literal final14cfd Nix five-output graph passes, durableexit0/53.328s. Both
  realized packages report schema1/exact14cfd/dirtyfalse/sourceenvironment.
  SourceNAR and complete1801-derivation input graph are in
  w-final-nix-evaluation-receipt.json; actualbuild in webui-final-nix-result.md.

Final Nix outputs:

- Frontend: `/nix/store/bicyxsc4phw6n82q55ssz9xfas0v238n-vpsadmin-webui-frontend-1.0.0`
- BFF: `/nix/store/a9rn1bkz0hz2kyc71kcy09hickd5j4gw-vpsadmin-webui-bff-0.1.0`
- Provenance: `/nix/store/p3vlsh9drr8mjjvahb4h4sy3r915n6sn-vpsadmin-webui-provenance`
- Source contents: `/nix/store/fc1yp9005gd21473li0sbzrfh67xwp5g-vpsadmin-webui-source-contents`
- Package contents: `/nix/store/500jbhwhsna2qqik6zr43pw62408zlca-vpsadmin-webui-package-contents`

## Actual visual evidence

Lead inspected implemented UI from synthetic local browser runs:
[captures-b611632f/capture-index.md](captures-b611632f/capture-index.md),
[captures-536a1c5c/capture-index.md](captures-536a1c5c/capture-index.md), and
[captures-1bfad6ce-bilingual/capture-index.md](captures-1bfad6ce-bilingual/capture-index.md).
They cover representative Czech/English VPS-first dialogs on desktop/mobile,
English HelpBox editors at actual wide/narrow widths, advisory actions and
Czech/English request detail/risk scenes on both projects, plus sampled user-data
editors. Indexes distinguish CSS viewports, dialog crops, full-page PNGs and
sampled trace frames. The English mobile editor has empty content at the captured
instant; it is not the populated Czech scene.

## Scope and remaining action

Review PR126 and the final CI outcome. The tracked archive makes WebUI builds
self-contained without publishing the SDK. Default-branch integration,
release/publication and deployment require explicit later instructions.
The session stays active/open and no machine deployment or lifecycle action
was performed. A frontend rollback does not undo API writes already accepted.

Evidence does not certify deployed OAuth/BFF integration, asynchronous worker
completion, other engines/physical devices or every unvisited language/date/
reset/filter scene. One earlier failed API attempt's deletion remains externally
unconfirmed because its exact ownership tuple was not captured; the later
successful run does not certify historical deletion. All current successful
runs have exact cleanup proof. Failed/abandoned attempts remain separate and
are not aggregated into passing counts.
