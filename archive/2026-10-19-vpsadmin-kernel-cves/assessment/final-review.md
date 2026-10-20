# Independent final whole-branch review

Reviewer0, retained gpt-6.1-sol/xhigh/read_only, thread
01a155a2-b52d-7b43-b92c-80ad1d45c16f. Exact reviewed range:
ea6247687fd02417f87e1e5593fecd8b9055925d..34ad7d5785382215cbe00b5140174cad5661a132.
All four lanes: general, architecture, scope, risk/compatibility. Verified exact
session/thread binding and roster; no fallback, overrides or nested reviewers.
Full report delivered through team message in this conversation; this durable
record preserves its findings and acceptance evidence.

No Blocking findings. One Important and one Advisory; lead elected to fix both
before longer checks and guarded draft writes. Worktree/index clean and reviewed
HEAD unchanged at report time. No source/Git/API/lifecycle mutations by reviewer.

## Important: wrong primary-source provider

All20 owner0 analyses have40 raw GitHub CVEProject/cvelistV5 links using Linux
security/vulns revision56fdb3; all20 owner1 analyses have20 analogous GitHub blob
links. Examples:98858 analysis lines5/64,74668 line73,74753 lines5/65. The revision
belongs to a different repository, so links do not reproduce the claimed pinned
primary record. Sample raw URL independently404. Retained primary evidence and
ranges are not disproved. Owner2's20 use the actual Linux CNA provider.

Correct to immutable same-revision Linux CNA provider URLs and verify decoded
record bytes against retained hashes. Regenerate digest-consistent normal-tool
evaluations and prove no source/fact/conclusion change. Owner0 prepared20 old404 /
20 counterpart200/exactbyte matches; owner1 prepared20 browser/TEXT200/exactbyte
matches. Reviewer did not repeat all network requests. Requested narrow remedy,
lead may verify under mandatory review step9 without automatic whole rerun.

## Advisory: KVM protection credit

98720 analysis line56 and89929/89930/89932 line62 share allocator randomization,
zeroing, stack protection, KASLR and FORTIFY credit. Those primitives are direct
L0 TPR access or stale tagged memory translations; no heap/stack/layout-dependent
exploit step is established. Replace with primitive-specific limits stating that
these controls do not address the demonstrated effect. Public EN/CS/evaluations
do not depend on this paragraph. Lead elected to fix rather than accept it.

## Independent substantive evidence

- Inspected all60 bilingual dossiers, source/range/prerequisite/role/negative
  claims and evaluations, especially64387/74753 and cumulative-v6 targets/content.
- Direct primary join covers393 Git intervals; declared semantic fixes agree,
  apart from three documented64387 ineffective-backport exceptions.
- All53 supplied CVSS vectors/scores traceable in analyses. Archived config hash
  matches c10922...; MPTCP/RT exclusions and built-in tunnel/modular MIP6 match.
- Independent configuration Git history confirms126 production-hypervisor
  addition and absence in parent; scope is not an exact deployment timestamp.
-64387 stable patch modifies send_set_info; rejection of nominal.96 safety is
  supported. Exact v6 payload b8ba1b... includes perf DETACH_GROUP introduction and
  lacks EXIT checks. Accepted correction coverage and helper-fanout withholding
  agree with payload/target evidence.
- Reproduced all60 evaluations exactly against frozen schema8 snapshot with
  Reconciler.evaluate(persist:false), excluding only evaluated_at. Aggregate780:
  696mitigated/58not_affected/14unknown/12vulnerable.
- All110 schema1 dossiers produce identical evaluation objects using base versus
  final evaluator (0differences). Isolated comparison first needed unchanged
  SysctlEvidence dependency alias, then passed. No evaluation file written.
- gitdiffcheck and40local analysis links pass. Owner113 focusedRSpec/lint/hooks
  and mechanical gate are supplied evidence, not independently repeated fullsuite.

## Architecture, scope, history and compatibility

Demonstrated74753 consumer justifies exact affected_livepatches rules; identity
validation shared with protection rules and existing sparse/timeline engine
reused. No duplicated atomic inference, generic predicate framework, collector
or API expansion. Safe-release override ordering and ambiguous evidence remain
conservative. Schema2 fails closed on old tools, schema1 behavior preserved.
Exactapproved60 only; no unapproved publication/mail/deploy/service work.
Prepared single-writer operations use existing guards, frozen evidence, exact
readback and one submission commit before next write.

Independently reviewed complete six-commit/189-file series: coherent selection
procedure;network20;core19;supportmodel;dependent74753;filesystem20. No obsolete
unmerged design, fixup/transitional history, repeated dependency/channel/input/
generated update stream, database migration or transitional migration. No merged,
released,deployed or externally consumed migration lineage. Evidence/evaluation/
submission schemas unchanged; dossier2 introduced directly. No external draft
source_commit recovery boundaries at review time. Subsequent remediation needs
normal final history/digest verification.

## Residual limits and authorization

Review is source/frozen-observation reasoning, not exploit reproduction or proof
of no production exploitation. Unmodeled mounts/programs/device/CPU/LSM facts
remain qualified; archived config cannot prove fleet history.74753 keeps12
historical unknowns;RTpair each one storage unknown;64387 has12conservative
vulnerable conclusions without proof of an actual hostile mount. Later refresh
must reapply prerelease/custom-source gate; no affectedRC occurs in frozen data.
No fullsuite,CI,remote duplicate refresh or guarded draft write by reviewer.
Remote target freshness not fetched. Review grants no publication,email,merge,
deployment or lifecycle approval. Session remains open.
