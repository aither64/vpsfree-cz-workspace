# HaveAPI 0.29.9 final review and publication

Independent retained reviewer0, GPT-6 Astra/xhigh/read-only, reviewed the full
22fae158..784e113 release series across all four lanes. No findings. Runtime
and test changes match master; only developer guidance placement differs.
History has three coherent commits, no obsolete approaches or repeated streams,
and no migrations or persisted-state changes. Prior I1 is resolved.

Release verification:20 focused examples and365 full server examples passed;
Ruby syntax/lint/hooks and all seven exact-head CI workflows passed. Normal
make release built three Ruby gems and the JS artifact with clean tracked diff.
Built and downloaded server gems were independently extracted and exercised:
five nonempty shared documents, extracted framework source assertion, and
three HTTP200 documentation responses with expected content.

Master ed88e2a and release784e113 were integrated by authorized fast-forward;
v0.29.9 tag pushed. RubyGems published all three Ruby packages. Published server
SHA256:a0797067cf871a42402f917f1919a3db624d8e1e9cfb632daf7e64c2ae0061a4.

The normal publish recipe failed at npm with404; whoami/access checks show401.
After the user refreshed login, only npm publication was retried from the
reviewed staging package. It exited 1 with EOTP, requiring a publishing
one-time password; the retry did not publish a version. The user then completed
interactive publication. npm haveapi-client 0.29.9 is now available; its
downloaded tarball passes registry integrity checks and its JavaScript matches
the reviewed release build. See [artifact evidence](npm-published-artifact.json)
and [the automation recommendation](delivery.md).
PHP mirror metadata was separately prepared and reviewed, then approved and
fast-forwarded into its master. Annotated v0.29.9 was pushed; Packagist lists
haveapi/client 0.29.9 at the reviewed commit and its archive matches all 35 tracked
files. All components of this patch release are now published and verified.
See [PHP publication evidence](php-published-artifact.json).

[Release packet](release-review-packet.md), [CI evidence](release-ci-result.json).
No deployment, session closure or branch removal occurred.
