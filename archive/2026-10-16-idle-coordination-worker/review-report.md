# Independent review report

Reviewer: /root/final_review, gpt-6-astra / xhigh, fresh standalone read-only fallback from installed default review-purpose policy. General, architecture/repetition, scope/proportionality, risk/compatibility lanes. Reviewed committed heads 4fd9128d, 2a03ea91 and 752edf11; not subsequent uncommitted lead fixes. No tests or live mutations performed by reviewer.

No Blocking findings; three Important and one Advisory:

1. Important (general/risk): workspace-integration-background.rb:112 classified all Error code 75 as waiting, while Engine#capture at workspace-coordination.rb:869 assigns 75 to any failed command, including nix build. Failed checks could retry indefinitely without waking the lead. Distinguish actual admission contention and persist needs_attention for failed commands/checks.
2. Important (general/architecture): background runner rescues WorkspaceCoordination::Error, while the real host callback at workspace-coordination-host.rb:173 calls prepare_profile, which raises DevWorkspaceHost::Error. Failed build/validation can escape without durable actionable state and be repeatedly restarted. Normalize errors at callback boundary or catch explicitly.
3. Important (architecture/risk): Collector#mark_live at workspace-coordination-gc.rb:292 accepts only schema 1. Every schema-2 journal, including complete, aborts collection globally. Use shared journal reader with pending/complete retention coverage.
4. Advisory (risk/general): background handover recognizes only resolved package changes, while current_generation! also checks profile token. Returning to the same package under a new token incorrectly requires agent action. Reuse complete predicate with token-only supersession coverage.

Acceptance gaps: the systemd test substitutes a fixture executable, bypasses real session admission, stubs tracking completion and simulates native delivery. Packaged worker execution, native wakeups with two contending sessions, deployment ordering and real generation handover remain unverified at review.

Whole-branch conclusions: complete histories match the packet; no superseded approaches or follow-up commits remain. Runtime coupled behavior, metadata, UI, docs and tests form one coherent feature commit. Pin streams are consolidated to one workspace runtime update and one configuration channel update selecting 4fd9128d with matching content hashes. Extension and unrelated inputs unchanged.

No database migrations. Schema-2 journals introduced directly, schema-1 manual compatibility retained. New format is unmerged, unreleased, undeployed and externally unconsumed; remote refs inspected contain it only on feature branch. Documented upgrade/drain and downgrade-refusal contracts reasonable subject to collector fix.

Lead dispositions and focused verification: review-remediation.md. Original review packet and three diffs remain retained separately. No claim that the reviewer evaluated later remediations.
