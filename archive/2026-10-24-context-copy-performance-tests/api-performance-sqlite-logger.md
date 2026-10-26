# SQLite performance worker logging boundary

Follow-up diagnosis, 2026-10-25. Prepared ActiveRecord8.1.4 and
sinatra-activerecord2.0.28; no production source/global logger mutation.

Loading ActiveRecord before HaveAPI without a selected test environment causes
Sinatra-ActiveRecord to install a stdout debug logger on ActiveRecord::Base.
`sinatra-activerecord/lib/sinatra/activerecord.rb:55-56` sets that logger outside
test/production (unless Rake was loaded). Schema and request SQL then prefix
worker JSON and add logging allocations/IO to measurements.

A proposed `logger=nil` on the scenario's own abstract AR base was insufficient:
`activerecord/lib/active_record/connection_adapters/abstract_adapter.rb:141`
initializes its logger directly from ActiveRecord::Base.logger, and
`activerecord/lib/active_record/log_subscriber.rb:121-122` reads the global logger
for SQL events. The new absent-RACK_ENV subprocess regression correctly failed;
the original17 SQLite specs remained sound. No claim that the local line fixed
SQL logging is retained.

C's worker sets RACK_ENV=test before requiring ActiveRecord/HaveAPI, matching the
original spec calibration. A fresh direct-fixture subprocess with that preload
policy passed1/1 (seed19327,2.52s), produced only JSON and retained actual
query1/auth1/exec1. It also confirmed the global logger identity was unchanged.
This diagnostic does not replace C's actual-worker subprocess regression.

Lead directed no broad fixture guard or global mutation; architect is assessing
the smallest boundary. Working preference is a C-owned actual-worker regression
and removal of the ineffective B-local line/test if redundant. B's temporary
followup is uncommitted; no Git/index mutation has occurred. Calibration's
RACK_ENV=test policy remains the valid selected environment; budgets are not
relaxed or recalibrated for noisy logging.

## Accepted disposition and equivalence

Architect/lead selected the worker's explicit pre-load RACK_ENV=test policy and
C-owned actual-worker subprocess regression. No fixture global-debug guard or
global logger mutation. Removed the ineffective local assignment/comment and
redundant B direct-fixture test; both B files match their original committed
`610da4e3212e66fac026eb94eedb55abf6d3c66a` contents, requiring no B fixup/rebase.

Bounded separate-process comparison evaluated both exact fixture variants under
that selected runtime policy. Two warmup batches, three trials of three requests
per quick case: with/without median total allocations are7319/7319 for page and
33796/33796 for nested includes. Every response identity and query/auth/execution
record is equal. These are equivalence observations for the assignment removal,
not replacements for C's actual worker budget measurements.

[Analysis](api-performance-sqlite-logger-equivalence.json),
[with assignment](api-performance-sqlite-logger-with.json),
[without assignment](api-performance-sqlite-logger-without.json) reconcile fixture
SHA256 `5cb0930b87e8ecb6731f5ea869bd189f77cdccfa6b8b5af7fcd3b1fd404baed7`
to final `faa5073996e7c666604080873c303d5ee6f8bd97ceaf7e33418342ceb83b6f0a`.
No budget relaxation or full recalibration. Final owned checks:17/17 focused
specs pass(seed65039,4.38s), two-file RuboCop clean, application diff clean.
