# Actual build verification — incomplete, staging failed

User reports all eight targets deployed. Read-only actual-artifact checks found
that the build selected by aitherdev does not contain the staging mitigation.
This is distinct from earlier exact-merged-head Nix option evaluation, which
passed for all 11 pools; no actual worker value is claimed here.

## Aitherdev staging: FAIL

Selected host system:
`/nix/store/vq63sg427gay6wb9w41ixnv6hza88izk-nixos-system-aitherdev-26.05.20261019.f3a73bc`.
Its nested build:
`/nix/store/7psqfgnz602qlhg935fy5rbc6il8jqkw-nixos-system-kb-staging-26.05pre-git`.
Both real generated pool units/configurations were read. The shared `-c` INI
`/nix/store/6a856s7i2cgn3wkaaylm6l8nl9rasn7q-php.ini` has only the commented
`;session.upload_progress.enabled = On` at line 1443. Neither pool FPM config
has the administrative flag or includes. Actual executable wrapper/sole scanned
INI have no active upload-progress assignment; units have no relevant environment
overrides, EnvironmentFile or drop-ins. Both selected built staging pools lack
the new configuration. Container was already active and was left untouched.

Details: [staging/WebUI report](deployed-php-webui-staging.md).

## Other seven machines: UNVERIFIED

Public four and three WebUI hosts reject SSH host-key verification for the
available targets. No keys accepted or checks weakened. Exact-merged-snapshot
INI/FPM output paths are absent from this workspace's local Nix store; expected
builder inputs/evaluation values cannot substitute for actual built file reads.
Foto actual package/config remains unverified. No additional build, deployment,
source/Git change, service restart, HTTP request or PHP probe performed.

Details: [public services report](deployed-php-public-services.md) and
[WebUI/staging report](deployed-php-webui-staging.md).

## Next action

Need the machine and checkout path where user ran deployment, or an existing
trusted access path to its actual output artifacts. User was asked asynchronously;
do not infer deployed revision from previous branch merge. No rollout success
claim until actual generated artifacts are verified. No deployment mutation
is authorized by this inspection request.

## Accepted scope exception

User accepts the selected staging build's missing setting because aitherdev is
not publicly reachable. Aitherdev is excluded from further public-rollout
verification; no staging activation or deployment is requested. The seven
public service machines remain unverified pending build artifact access.
