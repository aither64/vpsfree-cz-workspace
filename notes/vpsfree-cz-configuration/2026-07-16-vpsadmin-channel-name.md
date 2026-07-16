# vpsAdmin services input channel name

Related initiative: `work/2026-07-13-security-advisory-automation`

The flake input `vpsadminServices` is mapped by confctl channel `vpsadmin` with
role `vpsadmin`; there is no channel named `services`. Attempting
`confctl inputs channel set ... services vpsadmin ...` fails with
`no channels matched 'services'`.

Inspect the mapping with:

```sh
confctl inputs channel ls
```

Set the exact services revision with:

```sh
confctl inputs channel set --commit vpsadmin vpsadmin REV
```
