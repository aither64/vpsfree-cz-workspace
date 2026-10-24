Result: **passed**. Both commands exited 0, and no operation remains running.

- `python3 backend-successor/loaded-root-retirement/run-affected-packaged-verification.py` — exit 0; build checks took 230.99 seconds. Session, source identity, derivations, closures, and source-after checks also passed.
- `python3 backend-successor/run-composed-final-verification.py` — exit 0; W checks took 458.45 seconds; system build took 99.56 seconds. W/C checks, profile build, system and rollback checks, closures, and final source status/head/tree checks all passed.
- Verified release heads: B `825c1d2ba34592d0c617c876cdb467829fd64385`; W `d5e6eb0ee09c7c96db431d1c108a54d0371e6635`; C `890df35c1c614c2ec45e4d693519da3dfac1573e`.
- No failure output. The command streams reported results; no separate log paths were provided.