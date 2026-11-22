# Reproduce vpsfree-client gem checksums with the release epoch

Initiative:
`work/2026-07-24-vpsfreectl-snapshot-download-fix/`

## Symptom

Building the same vpsfree-client source tree with ambient `gem build`
produced a different SHA-256 than the reviewed artifact. File lists, versions,
and dependencies were identical.

## Cause

The repository's Nix shell exports:

```text
SOURCE_DATE_EPOCH=315532800
```

RubyGems therefore dates the package and its internal archives as 1980-01-01.
Without that environment variable, RubyGems 3.7.2 uses 1980-01-02. The gzip
headers and gemspec date change the archive checksum.

## Reproducible build

Use the release epoch when rebuilding outside the repository shell:

```sh
SOURCE_DATE_EPOCH=315532800 gem build vpsfree-client.gemspec
```

For version 0.20.0 this reproduced the reviewed artifact byte-for-byte with
SHA-256
`325751cfc215358d7cc05fcd494356ee4840dc4dd111867217bebd2c036126aa`.
