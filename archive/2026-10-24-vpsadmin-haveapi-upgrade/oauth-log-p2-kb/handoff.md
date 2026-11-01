# P2 KB callback log package handoff

Source complete and focused quick checks pass; E2 releases its package writer
to E1 for assembly/ordinary whole-repository hooks and commit. No Git/index/ref
operation was performed by E2. Only packages/dokuwiki-oauth-log-protection/**
was edited in the new E1 worktree from exact249f2eb5896b0a2697ed94e44657294847b3e606.
No input update or migration, no runtime/deployment action.

## Interface

`pkgs.callPackage <package-dir> {}` returns a normal plugin named
`oauthlogprotection` with `$out/bootstrap.php` and passthru.callbackLogsPatch
pointing at the carried dokuwiki-callback-logs.patch. E1 adds the plugin to both
KB sites, appends callbackLogsPatch to each selected DokuWiki package's existing
patches, and wires per-site phpOptions.auto_prepend_file to bootstrap.php.
Existing source/pins/plugins/patches stay preserved. No redundant action filter.

The marker VPSFREE_DOKUWIKI_OAUTH_CALLBACK uses only PHP-parsed query-key
presence: code, oauth_token, state, error, error_description. Empty, array,
duplicate and malformed callback values remain unchanged. It neither validates
nor bypasses OAuth state/CSRF logic. It classifies any such key conservatively;
ordinary local-login requests without those keys retain native diagnostics.

E1 Matomo wiring uses its existing per-site js_tracking_code._raw PHP expression:
`(defined('VPSFREE_DOKUWIKI_OAUTH_CALLBACK') && VPSFREE_DOKUWIKI_OAUTH_CALLBACK)
? '' : trim(file_get_contents(<same immutable matomoCodeFile>))`.
This omits the whole JS+noscript injection server-side on sensitive documents;
clean navigation still gets the original string. Never insert PHP source inside
an already-rendered HTML string or rely on JS exact keys that miss code[].
E1 owns all shared config, allowdebug0, display_errors0, display_startup_errors0,
zend.exception_ignore_args1, PHP/Matomo/nginx/FPM settings and integration tests.

Bootstrap disables and verifies native log_errors only after a callback marker.
If that cannot be enforced it emits only oauth_callback_logging_unavailable,
sets HTTP500 and exits1 before app work. The request remains unchanged even in
that path. No error handler is replaced: user fatal/default engine termination
remains. A fixed shutdown category with basename+line retains early-fatal context
without raw message/trace/args. The five-line Logger entry patch replaces only
callback message/details before events or fallback formatting, preserving
facility/source location and the ordinary logger implementation.

## Focused verification

Normal `nix develop` shell batch completed0, original native handle33610 consumed:

```sh
nixfmt --check packages/dokuwiki-oauth-log-protection/default.nix
php -n -l packages/dokuwiki-oauth-log-protection/plugin/bootstrap.php
php -n -l packages/dokuwiki-oauth-log-protection/tests/request.php
python3 packages/dokuwiki-oauth-log-protection/tests/run.py \
  <retained-pinned-dokuwiki-source> <fresh-output-directory> \
  --php /nix/store/bic2hz2ga1qnhk7q730j8n48fqyd4n84-php-with-extensions-8.4.27/bin/php
```

Nix parse also passed. Exact quick results: quick-final/results.json; native
files, wiki files, stdout and request-preservation records remain beside it.
The patch applies with fuzz0 to original LoggerSHA256
1aa4c4feaad3e4be84cea0e7c4bb4b21bb9bb170c906359ae949bec0e5937a5d.
Ten cases pass: before-event logger, event visibility, empty/array/duplicate/
missing-state/provider-error keys, real core/native warning handlers, fatal
user errors and early exception exits255, fixed-category early fatal fallback,
normal benign wiki/native diagnostics, and failclosed disabled ini_set.
Public fixed sentinels are absent from actual wiki/native/stderr logs; serialized
GET/POST/Cookie/SERVER auth/CSRF/header/URI inputs and observed status survive.
These are input-preservation checks, not actual OAuth login/redirect acceptance.

Original quick-1 failure is retained: fixture observer incorrectly required an
unprefixed benign core warning; only that test assertion was corrected.
quick-2 passed; final adds shutdown observation proving inputs unchanged even
when native policy is unavailable. No hidden retry or lost failure evidence.
A temporary whitespace inspection also incorrectly treated unified-diff blank
context prefixes as trailing whitespace; the corrected check preserves diff
syntax and confirms added lines/other source have no trailing whitespace.

## Explicit limits

The boundary starts when auto_prepend executes. Engine/request-startup failures
before it remain outside this policy. CLI results do not prove installed FPM,
FastCGI/syslog/journal/worker-stderr transport behavior; that acceptance waits
for committed final independent review. Ordinary OAuth catches still display
rather than log; manual core fatal HTML can still contain a raw exception
message and is deliberately unchanged. No general error page or provider/auth
rewrite, global PHP/wiki logging disable, production/staging/login/network
operation, full stack, broad test campaign or new dependency was introduced.
No active owned command remains. Historical gate/failure evidence remains intact.

## Exact source inventory

- `packages/dokuwiki-oauth-log-protection/default.nix` SHA256 `4871b67747b8cc4236a08bbe9efa4740a2171943c4ed43ece849b24615a827dc`
- `packages/dokuwiki-oauth-log-protection/dokuwiki-callback-logs.patch` SHA256 `e480bda3564baac78f5d19946f1af9cac9d90c9fe65e9a8a296ba65e974e0acb`
- `packages/dokuwiki-oauth-log-protection/plugin/bootstrap.php` SHA256 `4c43f9f82da6fb11b14889bafe69945353efa855f3adc62a83d2493a1cec9118`
- `packages/dokuwiki-oauth-log-protection/plugin/plugin.info.txt` SHA256 `16c177d132f9175203955fa83938dcb76e99c316b31011a6fc6667d8df27d019`
- `packages/dokuwiki-oauth-log-protection/tests/request.php` SHA256 `54e6b38dbb4bfe04477f79689ffde7db1790168d46f7296fb24ee79f2665729f`
- `packages/dokuwiki-oauth-log-protection/tests/run.py` SHA256 `c2ecf9fc7b9c2fe20ab3a50e68576a94df195203f0c7dd7c66216a99eeabf034`
