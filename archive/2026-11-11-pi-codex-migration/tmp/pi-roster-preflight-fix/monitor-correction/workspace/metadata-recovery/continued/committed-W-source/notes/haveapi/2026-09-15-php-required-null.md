# PHP client rejects explicit null for required input

Related initiative: `work/2026-09-09-ip-release-mechanism/`.

The WebUI bulk exemption removal sent `reason: null` to a required, nullable
API parameter. haveapi/client 0.29.6 raised local ValidationError before HTTP;
the API's direct JSON request tests passed. The same required-input check is
present in upstream 0.29.8 (`clients/php/src/Client.php`,
`coerceAndValidateInput`): it rejects null without consulting nullable metadata.

The new, unmerged bulk campaign action now uses an explicit remove flag, with
nonblank reason validation for setting exemptions. The single-address HTTP
contract remains unchanged. This avoids a framework release for the feature,
but does not fix the generic client's required/null handling. When testing PHP
callers, include the real client and nullable operations; server request specs
alone do not establish that the WebUI can encode the operation.
