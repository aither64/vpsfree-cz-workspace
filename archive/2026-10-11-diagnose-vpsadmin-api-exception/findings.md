# Missing HaveAPI documentation in the published gem

The exception is caused by a missing generated documentation file in the
published HaveAPI 0.29.8 package. The request is for the human-readable
documentation page, not an API action involving VPS state.

## Evidence

The attached email reports `Errno::ENOENT` for `GET /doc/json-schema` on
2026-10-11 at 21:12:14 +0200. The user agent identifies itself as PetalBot.
This identifies the triggering request, not authenticated crawler identity.

The first application frame is the installed HaveAPI `server.rb:536`:

```ruby
@content = File.read(File.join(settings.root, '../../doc/json-schema.html'))
```

The exact Nix package from the email is available locally:

```text
/nix/store/v36zkvq35m3026pijh3n011gjjc8ch3k-ruby3.4-haveapi-0.29.8
```

Its installed gem's `doc/` directory contains only `hooks.erb` and `index.md`.
The expected path resolves to the correct gem documentation directory, where
`json-schema.html` is absent. The observed problem is package content.

The original [published gem](https://rubygems.org/downloads/haveapi-0.29.8.gem)
was downloaded into memory and its `data.tar.gz` inspected. It also contains
only those two documentation files. SHA256:

```text
8e362aef9e6b1c77233ee53bb1237056b2e15abcba9b2ef5b3d188a1dd9ec1e7
```

Thus the omission precedes Nix installation. vpsAdmin's referenced API gemset
selects this published gem version. `doc/protocol.md` and `doc/create-client.md`
are missing too, although this email only proves the JSON schema route failed.

## Release-process cause

At [tag v0.29.8](https://github.com/vpsfreecz/haveapi/tree/v0.29.8):

- [utils/copydoc.sh](https://github.com/vpsfreecz/haveapi/blob/v0.29.8/utils/copydoc.sh)
  renders the shared JSON schema ERB into `servers/ruby/doc/json-schema.html`
  and copies shared Markdown/image documentation into the server directory.
- [Makefile](https://github.com/vpsfreecz/haveapi/blob/v0.29.8/Makefile)
  runs this script through `make doc`. Its `release` target does not depend on
  or call `doc` before building the Ruby gem.
- The generated files are Git-ignored.
- [haveapi.gemspec](https://github.com/vpsfreecz/haveapi/blob/v0.29.8/servers/ruby/haveapi.gemspec)
  adds `Dir.glob('doc/*')` to tracked files. This includes generated files when
  present, but neither generates them nor rejects missing documentation.

A clean-source release can therefore build successfully without these files.
The published artifact proves that they were omitted; the individual release
operator's exact commands are not known.

## Why a documentation request sends exception mail

The [documentation index](https://github.com/vpsfreecz/haveapi/blob/v0.29.8/servers/ruby/doc/index.md)
advertises the JSON schema link, so ordinary crawlers or readers can reach it.
The [dedicated route](https://github.com/vpsfreecz/haveapi/blob/v0.29.8/servers/ruby/lib/haveapi/server.rb#L533)
reads the HTML without handling a missing file. The adjacent generic
documentation route has a missing-file handler, but the dedicated route wins
for this URL. HaveAPI's ExceptionMailer hooks request exceptions, turning the
uncaught filesystem error into the received notification.

The inspected [documentation specs](https://github.com/vpsfreecz/haveapi/blob/v0.29.8/servers/ruby/spec/documentation_spec.rb)
exercise `/doc`, `/doc/index` and API version pages, but not `/doc/json-schema`
or the generated shared-document pages. Existing successful checks therefore
do not establish packaged documentation completeness.

## Proposed solution

1. Make shared-document generation mandatory for release packaging, for example
   change the Makefile target to `release: doc`. If direct `rake build` remains
   a supported release entry point, give it the same requirement or reject a
   build missing required files.
2. Verify the built gem contains the generated JSON schema and shared
   documentation. Exercise `/doc/json-schema`, `/doc/protocol.md` and
   `/doc/create-client.md` using an installed artifact rather than relying only
   on a prepared source checkout. The repaired pages should return HTTP 200.
3. Add a narrow missing-file handler to `/doc/json-schema` that returns HTTP 404
   consistently with the generic documentation route. Test the missing-file
   response and verify it does not invoke exception mail. This limits the
   consequence of a packaging failure; shipping the documentation remains the
   primary repair.
4. Publish a new HaveAPI patch release through the normal approval workflow,
   update vpsAdmin's dependency lock/gemset, and rebuild/deploy the API package.

No fix, publication or deployment was executed. This proposal changes no
database schema, stored VPS state, API action contract or daemon protocol and
needs no coordinated node update. API rollback needs no state conversion.
Avoid modifying Nix store files or disabling the exception mailer globally.

As a temporary operational mitigation, an exact reverse-proxy rule could return
404 for `/doc/json-schema` until the repaired package is deployed. This prevents
the triggering request from reaching the broken route but leaves the advertised
documentation unavailable. It has not been configured or verified.
