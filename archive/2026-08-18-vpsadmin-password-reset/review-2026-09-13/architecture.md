# Architecture and repetition review

Reviewer: fresh gpt-5.6-sol / xhigh, architecture-and-repetition lane. Reviewed
the complete committed series and current consumers directly. No nested agents.

## Findings

### Blocking

1. **Password recovery expands the password-acceptance contract to a fourth
   independent runtime implementation.** Commit
   `ee70a09ca67026f1724f5583905787babbbb92de` added the recovery check at
   `vpsadmin/api/lib/vpsadmin/api/authentication/password_recovery.rb:343-350`;
   commit `dd930d8f11889f57d3718fa9337339082b27e021` separately put the same value
   into the recovery form at
   `vpsadmin/api/lib/vpsadmin/api/authentication/password_recovery.erb:240-259`.
   The final tree currently implements the same minimum of eight in OAuth reset
   at `vpsadmin/api/lib/vpsadmin/api/authentication/oauth2_config.rb:741-746`,
   token reset at
   `vpsadmin/api/lib/vpsadmin/api/authentication/token_config.rb:159-165`, and
   authenticated/admin update at
   `vpsadmin/api/lib/vpsadmin/api/resources/user.rb:387-392`; OAuth form metadata
   repeats it at
   `vpsadmin/api/lib/vpsadmin/api/authentication/oauth2_authorize.erb:264-281`.
   There is no current behavioral mismatch: all four server paths reject fewer
   than eight characters. The
   maintenance failure is the next policy edit: raising the minimum or adding a
   common acceptance rule in three established change/reset paths can leave the
   recovery path accepting a weaker password, while changing recovery alone can
   make the public flows disagree. Because this series expands independently
   maintained security-sensitive public-contract logic, this is Blocking under
   the lane rubric. The smallest remediation is for the existing narrow
   `VpsAdmin::API::PasswordChanges` owner to expose the minimum and one
   `too_short?`/acceptance predicate, use it from these four runtime sites, and
   derive both password forms' `minlength` and formatted error text from that
   value. Add a focused test at that shared boundary plus representative route
   assertions. This does not require a generalized password-policy framework.

### Important

No findings.

### Advisory

No findings.

## Review coverage

Reviewed the exact ranges from the packet:

- `vpsadmin` `61d2ef6e712345200daddff3abcb4697c028d176..a2e6d8037c737c61c15bfd845c1b3c57d894f310`
- `vpsfree-mail-templates` `9e1ddbd973703cf48a43f0e5afc2bfb392a8b676..f944ba03eba5d0d6b58b7eb856f251d1c96f2c11`
- `vpsfree-kb-contracts` `81d6d7dfe530884aff3e1d2634e02e4b12fe28e8..6d8ab17db3ce8ffc41216feeb90bff8468b4d39d`
- `vpsfree-cz-configuration` `b4e120294696578c3871124259f266205bad4393..8928b2aba9230202e805aa5489dc9f7369650ac7`

The review traced WebUI password-change-log consumption, API resource/model and
operation ownership, OAuth and token reset callers, the notification-template
provider declarations and branded external templates, production replacement
mode and exact application/template pins, monitoring's use of the exported
queue-limit metric, and the KB source/navigation/capture pins. The recovery
policy, MFA verification and factor-change locking, OAuth default/deletion
invariants, queue serialization, lifecycle gates, event catalogs, and
cross-project pins otherwise have localized owners and matching consumers.

## Residual gaps

Production `replace` mode makes the branded external mail bodies independently
maintained from the generic built-in bodies. Their declared variable contracts
match and I found no current semantic contradiction at the pinned heads. The
reported checker passes 71 templates and 349 files, but it validates template
structure and variables rather than future prose parity; later security-mail
wording changes still need a coordinated provider/consumer review.

No tests or integration commands were run in this read-only lane. I used the
packet's quick result of 16 tests / 55 assertions and the coordinator's report
that every current-head workflow passed and the full integration run completed
118 tests successfully. Those results support current-head stability but do not
remove the prospective policy-drift finding above.
