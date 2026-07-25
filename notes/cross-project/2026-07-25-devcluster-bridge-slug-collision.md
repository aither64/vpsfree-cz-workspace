# Same-slug bridge devclusters share deterministic addresses

Related initiative: `work/2026-06-15-vpsadmin-events`

## Symptom

A general vpsAdmin development cluster and the independent KB capture cluster
could not run at the same time when both used slug
`2026-06-15-vpsadmin-events` on the bridge network.

## Cause

Bridge addresses are derived deterministically from the slug. Independent
cluster implementations using the same slug therefore attempt to own the same
services address.

## Fix and verification

Stop one cluster before starting the other. Use the capture-repository cluster
while generating screenshots, then stop it before starting the general-purpose
vpsAdmin cluster for final runtime verification. Do not switch to local
networking merely to bypass this conflict.
