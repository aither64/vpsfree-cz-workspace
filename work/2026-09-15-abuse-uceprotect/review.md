# Mandatory change review

## Scope

High risk: incident ownership and evidence isolation across members. All four
required lanes used gpt-6-astra with xhigh reasoning and fresh context
(fork_context=false, current tool equivalent of fork_turns=none). Review packet:
[review-packet.md](review-packet.md). Reviewed base
713fb3ba48ae31c87519e75892d1413a48a22fb0 through
81d827c269c09db55a7dc97783696ec803cfb37c.

| Lane | Agent | Findings |
| --- | --- | --- |
| General | 01a0a4f0-12ec-76f3-b075-fbd5198b515e | None; independently confirmed 115-example full suite |
| Architecture | 01a0a4f0-14a5-7f93-8aec-b57b556be0e4 | None; independently ran focused 48-example suite |
| Scope | 01a0a4f0-1590-73e3-b39b-8bc6a7bc86b5 | None |
| Risk | 01a0a4f0-1682-7a81-b43d-a471dcad6564 | One Important finding, fixed below |

## Important: padded subject list exposed another IP

Risk reviewer reproduced a subject ending in `( 192.0.2.10, 192.0.2.20 )`
with a body reporting only the first IP. Whitespace after the opening parenthesis
made the subject matcher return no match without a rejection. The original
subject was then retained for the single valid body entry, exposing the second
IP to that member.

Remediation: distinguish an absent subject suffix from an unparseable one.
Validate the complete suffix against a single-IP form, allowing surrounding
whitespace. Unknown/malformed suffixes log a rejection and prevent reuse of the
original content. Valid body reports remain eligible under the user's
partial-success policy. Added tests for the exact serialized Mail reproduction,
an unknown suffix containing another IP, and a padded valid single-IP subject.

Focused checks: 51 examples passed, Ruby lint clean. The fix narrows existing
original-content reuse and completes the already-reviewed subject validation
boundary; it introduces no new interface or design. Per the skill's direct-fix
rule, no reviewer rerun is required. Changes are folded into final functional commit
b6e650ad902482b4c4e66b5a89a4275bed92419e. No Blocking, Important, or Advisory findings remain open.

## Residual limits

No live database, historical assignment query execution, SMTP delivery, production
mail processing or deployment was performed. Tests use controlled assignments
and in-memory incident records. Partial processing and manual RT recovery are
explicitly accepted. No automatic retry or cross-message idempotency was added.
After review, the offline check using pinned vpsAdmin Handler/Result/Send/Reply
and the real notification template passed with fake persistence/delivery: two
owner-specific rendered notifications and one RT summary. Final full config
suite: 118 examples passed; full Ruby lint: 34 files clean.
