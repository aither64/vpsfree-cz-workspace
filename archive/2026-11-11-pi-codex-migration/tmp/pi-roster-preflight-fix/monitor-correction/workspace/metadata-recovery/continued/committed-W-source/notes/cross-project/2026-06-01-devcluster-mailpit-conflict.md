# vpsAdmin devcluster Mailpit conflict

Related initiative: `work/2026-05-29-security-advisories`

## Symptom

Starting a vpsAdmin dev cluster failed during Nix evaluation with a conflicting
definition for:

```text
containers.mailer.systemd.services.mailpit.description
```

The two values were `Integration test mail capture service` and `Development
mail capture service`.

## Cause

The vpsAdmin test-services Nix module now enables Mailpit in the mailer
container by default. The dev-cluster module also defines a Mailpit service in
the same container so it can expose the capture UI through the dev-cluster
HTTPS proxy.

## Workaround

In the dev-cluster services machine config, set:

```nix
vpsadmin.test.mailpit.enable = false;
```

This disables the test module's Mailpit and leaves the dev-cluster Mailpit as
the single service definition.

## Verification

After the override, `devcluster start` reached `ready: yes`; the web UI loaded
through the local HTTPS proxy and Mailpit's `/api/v1/info` endpoint responded
with basic auth.
