# Missing nginx Basic password files return 403

Pinned nginx1.30.6 auth-basic maps ENOENT opening auth_basic_user_file to HTTP403;
other file-open errors may map500. The query-interface fixture originally expected
500 and failed only at its last assertion. An exact-binary bounded reproduction
returned403 and confirmed zero requests to a permissive backend. Correct the
precise expected status while preserving the backend-unreached check.

Evidence: work/2026-10-21-aitherdev-observability-access/verification-retry-02.log
and verification-status-fix.diff. No production authentication policy changed.
