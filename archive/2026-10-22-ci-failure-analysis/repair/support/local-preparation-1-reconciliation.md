# Preparation1 reconciliation and bounded preparation2 correction

Preparation1 stopped before config realization. Kernel substitution/hash and
config dry-run all exited0; the fetch allowlist then refused the one extra
`fbrmzbsak0m5kx8is8i71igsnwmhxs9q-stdenv-linux` output. Duration6.951s;
11439retained log bytes. Recorded clients3683129,3683452,3683474 were reaped,
and a later exact-PID observation found all absent. No VM, config JSON output
root or closure-info output root was created. Kernel/config/original-config
derivation roots remain intact. No signal, root removal or cleanup was needed.

The added output is the existing frozen5794-node graph's exact
`jfk5cr6f6ry3hlb9lpa5hyzh17m73i37-stdenv-linux.drv` output. There is no recipe,
source or graph expansion. Its omission from the initial required-fetch list
and later required fetch are consistent with shared store reclamation; collector
identity/timing are not proved. The later local-path scan also lacks it, so that
scan does not date the change.

[Cache metadata](attempt2-stdenv-metadata.json) and [native narinfo](attempt2-stdenv.narinfo)
bind exactly that output/deriver to19106compressed bytes and61296NAR bytes,
expected hash `sha256:1wx2jc861l8lpriwakin5nmc5vgdmqpxh21c68njbvnw867l2iz0`.
All30direct reference paths existed at inspection. Preparation2 approves only
this explicit additional output; an unknown missing transitive dependency still
refuses. It first substitutes/roots the output with max-jobs0, empty remote
builders and fallbackfalse, then checks the NAR hash before continuing.

Lead accepted this finite correction and inspected its exact diff/hash.
[run-local-preparation-2.py](run-local-preparation-2.py), SHA256
`f4d42cce87e0658a3f026be513426bedcced08ba901e4ef15a70b4da7fe5adbc`,
uses fresh local-preparation-2 receipts, reuses only the existing exact kernel
root, and adds the stdenv-closure-info output root. All other216-builder and
budget/deadline/cancellation guards remain. The original preparation1 script and
receipts are unchanged. Lead selected a fresh watcher for2; implementer3 did not
launch/retry or observe its active execution. Source remains frozen.

One readiness report incorrectly supplied an unverified hash before reading
tool output. A separate immediate correction supplied the f4d42... hash above;
the lead independently verified and selected that actual hash. The incorrect
fe22... report is not a source identity.
