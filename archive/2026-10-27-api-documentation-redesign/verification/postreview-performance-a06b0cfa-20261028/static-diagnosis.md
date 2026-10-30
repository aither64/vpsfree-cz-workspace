# Static calibration-environment diagnosis

No new process loaded Ruby, made requests or performed a gate/pilot. This is
source/retained-artifact inspection after the failed CI evidence reconciliation.

## Exact mismatch and boundary

Expected environment.weekly versus actual baseline35c pilot environment has
exactly one difference: expected io-console0.9.4/platformruby is absent from
Gem.loaded_specs. The calibrated Ruby3.4.11 executable/engine/ABI/platform and
all other activated gem identities match exactly, including JSON2.21.2 and
sqlite3 platform. Frozen benchmark lock/Gemfile/shell match prepared local
bytes; io-console0.9.4 is present in that lock with its fixed gem checksum.
CI setup installed the locked70-gem bundle under its dedicated gem home and
Bundler4.0.23. The local protected io-console0.9.4 gemspec also exists with its
unchanged recorded hash. Evidence does not show changed installed versions or
an invalid reference/source/archive identity.

The strict comparison is a fixed calibration precondition, evaluated in the
neutral runner after each completed worker result. Worker#environment records
Gem.loaded_specs; CLI#verify_runtime checks merely availability of each exact
calibrated specification. Availability therefore passes while later activated
set equality fails. Both quick and weekly use environment.weekly. The failed
pilot belongs to baseline35c; it is not candidate activation or a source-version
normalization mismatch. No paired samples were produced.

## Source of load dependence

The neutral runner does not explicitly activate io-console. The pinned Ruby
stdlib pp.rb uses require 'io/console' inside PP.width_for; PP.pp's default width
calls that method. Framework Ruby/curl action-example helpers invoke PP.pp.
Historical complete documentation pages traverse action samples; current
version overviews intentionally omit those action bodies. This provides a
concrete source path for incidental activated-gem differences as page work
changes. The observed35c pilot did not activate io-console. Static evidence
cannot reconstruct the exact original calibration call order, so no such order
is invented. The structural cause is reliance on workload side effects to
activate a dependency that the unchanged policy requires in every worker.

The Nix <nixpkgs>/bashInteractive warning is separate: the command fell back to
an environment bash and executed the exact calibrated Ruby. There is no field
evidence tying that warning to the sole io-console activation difference.

## Shortest legitimate next step

The prepared local store already supplies the exact calibrated versions, but
an unmodified fresh local candidate worker still has this activation risk.
Do not assert the f6-to-final pair will work merely because local inputs match.
RUBYOPT/RUBYLIB/Bundler startup tricks cannot provide a supported workaround:
the pinned shell and fresh child environment explicitly clear them; the worker
command is fixed. Do not alter manifests, ignore missing activated specs,
subtract io-console from calibration, change budgets/reference or compose timing.

The minimal correction to propose is deterministic activation of the existing
exact frozen io-console0.9.4 in the single neutral worker bootstrap before
workload construction/timing, analogous to the existing explicit JSON version
activation. Both baseline and candidate then use the same complete required
graph; workload crypto/provider lookup, counters, loops and budgets remain.
This is a narrow runner source change and is NOT implemented or authorized by
this diagnosis grant. Lead should grant its original owner a focused fix/check/
commit/affected-review package if accepted. No new runner or dependency is needed.
After that and a new exact-final export binding, the existing direct f6-to-final
quick command should run once through the policy watcher on the prepared frozen
graph. Retain exact actual worker graphs and unchanged all-client-source/input
proof; never relabel the a06b all-client result as a CSS/runner successor without
an explicit affected-input equivalence receipt.

The successful CI all-client214/0 result (15×7×bothdetails plus roles/scaling)
remains valid at a06b and its recorded inputs. Automatic35c-to-a06b comparison
failed; required f6-to-final remains unexecuted. Any CI retry or local campaign
requires a later explicit run grant; no source/dependency/runtime/budget change
or run was performed here.
