# Dev-cluster SSH command argument forwarding

Initiative: `work/2026-07-13-security-advisory-automation`

## Symptom

Passing a nested `sh -lc '...'` command through `devcluster ssh ... --` lost
the intended quoting. A later attempt to use `vpsadmin-api-ruby -e` also failed
because that wrapper accepts a script path, not Ruby interpreter options.

## Cause and workaround

`devcluster ssh` forwards remote arguments to SSH, where another shell parsing
layer is involved. Prefer simple commands with one argument per local shell
word. For API model inspection, run `vpsadmin-api-shell` interactively and
send the wrapped Ruby command through its standard input, or copy a prepared
script and give its path to `vpsadmin-api-ruby`.

The Ruby runner adds the packaged API `lib` directory to the load path but does
not load the application. A prepared model-inspection script must start with
`require 'vpsadmin'` before it uses model constants such as `User`.

Do not assume convenience tools such as `jq` are installed on a vpsAdminOS
Node. Read small evidence files directly or process them on the host.

## Verification

Simple `readlink`, `head`, and service-status commands worked reliably. The
interactive API shell successfully inspected the persisted Node evidence and
service-Node suppression state.
