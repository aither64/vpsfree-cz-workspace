# Hosted visual inspection at Wa9

Source a9d0b5e9402faafef937894f50463da3c27e8935, hosted smoke37752175398.
Images are implemented React with synthetic HTTP fixtures, not a live cluster.

Root viewed EN/CS desktop/mobile admin-ip-flags images. The three cases retain
assigned/routed context and actions; only the explicit disabled network has a
localized warning. On mobile, focus reveals the description. No enabled-state
flag noise is shown. The desktop captures do not show the focused description:
reviewer0 confirms the same table-clipping boundary for the disabled row tooltip
at IpAddressesListTable:182. The final-row case is included in the remediation.

Root viewed EN desktop and CS mobile network-counts images. Counter labels and
owned-detached value are present, but the absolute positioned available tooltip
is clipped by the table's overflow boundaries. Its important description cannot
be fully read. This is a concrete visual finding despite the passing browser
suite. Implementer is assigned bounded inventory-description placement and real browser
geometry/clipping assertions. Architect0 reconciles one shared owner for count
hints and these new disabled-only badges, with no copy/counter/layout redesign
or global Badge changes.

All four exact network-counts screenshots remain historical failed-appearance
evidence for this head. Do not publish them as approved final visuals. Corrected
same-selector hosted screenshots must be inspected after the fix.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/)
