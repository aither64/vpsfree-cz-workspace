# Choosing unused addresses in network fixtures

A maximum row ID modulo a host range does not establish that an IP address is
unused. Explicitly supplying that derived address to a lower helper also skips
its automatic unused-address selection. vpsAdmin validates `ip_addr` globally,
so search occupied address values, preserving the requested network's prefix.

API38364190560 full foundation seed27013 exposed this in the inherited ownership
allocation fixture before any allocation assertions. The real register call
rejected a duplicate address. The native result does not identify the colliding
address or row; no local reproduction was run. Both owning helpers and the
failing ownership example were inherited unchanged from target7d911899.

The bounded correction searches the existing200-host fixture range in the
actual /24 and reports exhaustion. Keep real uniqueness, registration, charging
and allocation assertions. Corrected-helper verification remains pending.
See the source/native dispositions under
`work/2026-10-05-network-ipv4-left-counter/finish-api-fixture10-failure-source.json`
and `finish-api-render9-api-assessment1.json` in the same initiative.
