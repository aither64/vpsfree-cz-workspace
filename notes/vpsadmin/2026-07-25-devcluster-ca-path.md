# Dev-cluster URL output can report the wrong CA path

## Symptom

`bin/devcluster urls <slug>` printed the CA under
`dev-clusters/vpsadmin/certs/default/vpsadmin-ca.crt`, and `curl --cacert`
failed because that file did not exist.

## Cause

The generated development-cluster state and certificates live below the hidden
top-level `.dev-clusters/` directory. The URL output omitted the leading dot in
the certificate path.

## Workaround and verification

Use:

```sh
curl --cacert \
  /home/aither/workspace/ai/vpsfree.cz/.dev-clusters/vpsadmin/certs/default/vpsadmin-ca.crt \
  https://webui.aitherdev.int.vpsfree.cz/
```

The corrected path returned HTTP 200 for initiative
`work/2026-06-15-vpsadmin-events`.
