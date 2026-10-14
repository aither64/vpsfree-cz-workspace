Source-only D fixture repair at b1ec1bf. One generated-provider helper
closes a complete literal EOF payload at a sibling temporary path before
rename. Exactly three existing producers call it, after their original
stdin EOF. All consumers, assertions, timing bounds, release barrier, PID
marker, child reaping and generation guard remain byte-identical.

E38083114582 reported expected EOF / actual empty at the abrupt dispatcher
loss assertion. File creation before payload completion supports the race
diagnosis; the native log does not prove that scheduling interleaving or a
production defect. No repaired test was executed. Existing owning portal
documentation already states the unchanged contract, so no prose change
is useful. Root owns normal consolidation, exact hosted D/E and review.
The earlier K fixture source/control packet remains held and immutable.
