# Review remediation packet

Same independent reviewer; rerun the general, architecture, scope and risk lanes affected by the new cross-tab reset coordination. Do not repeat unaffected full-branch review. See review.md for the initial four findings and fixes. No migrations; all follow-up corrections folded into their owning unmerged commits. User decisions and scope remain in review-packet.md and design.md.

Quick checks: 59 provider Node tests (including automatic repair hide/resume), five mocked reset controller tests (including two stale tabs and no lock), focused Go limits/reset/browser contracts and corrected source assertion pass. Provider exact-head CI success. The previous runtime CI failure was the old literal polling assertion; full failed logs inspected. Cancellation of obsolete run 37943731262 was refused by GitHub token permissions (403), recorded rather than bypassed.

## codex-web

Base `3d07cf60cfde5d117a181a9bdb6d90a5860f6f0c`; head `860d515d0aa5d2f7ad68893db41f0969c78e00a7`.

```
dd13156b051c1ae32bc9bc409b622b5eb5d58e18 codex: expose account credits and idempotent limit resets
8263ccd44587a50148242d4e94d2e582d6bda759 conversation: attach binary clipboard files from the composer
860d515d0aa5d2f7ad68893db41f0969c78e00a7 conversation: keep refresh quiet and edit settings in a dialog
```

## dev-workspace

Base `c51ba3c0ca0d41d237ef71c56accd564beb70a33`; head `26640fb5505d92c976d52cf7d58336653876f7ed`.

```
14dfc5e8ec82ef29a1057aa46223c8499372350c portal: keep refresh values visible and compact model controls
3ec3626527758a735e99c800a709bb051fb7602d portal: show credits and confirm banked reset use
26640fb5505d92c976d52cf7d58336653876f7ed inputs: select the updated Codex web integration
```

## workspace

Base `747e9a875c23a7a760fcb3ce18d7d7a51f3015e5`; head `0957e7c3c76af50e0cd919e54c77b9af2f7887c0`.

```
0957e7c3c76af50e0cd919e54c77b9af2f7887c0 inputs: select the portal usability runtime
```

Configuration mechanical final pin and composed-lock check agree on runtime 26640fb5505d92c976d52cf7d58336653876f7ed; extension unchanged. Account locks are only browser redemption coordination, not a new server contract or schema. Web Locks unavailable disables reset actions. Both Use and Retry reload and act under the lock; storage events update other tabs without automatically consuming. Please assess actual implementation and tests, report concrete findings, and read the applicable skill lane references. No live resets, code edits, deployment, long checks or nested delegation.
