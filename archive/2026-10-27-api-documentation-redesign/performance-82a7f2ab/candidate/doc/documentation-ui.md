# Browsing API documentation

Open a version endpoint such as `/v7.0/` for the overview and client
initialization examples. The overview lists the available client libraries and
configured SDKs. Choose **Authentication** for sign-in examples or **Resources**
for the full resource directory. Nested resources have their own pages, with breadcrumbs linking
to their parents and action links in the sidebar.

Resource URLs use `?resource=vps` or `?resource=vps.snapshot`; the directory uses
`?page=resources` and authentication uses `?page=authentication`. These selectors
apply only to HTML documentation, leaving API actions and OPTIONS descriptions
unchanged. Mounted APIs retain
their prefix, for example `/api/v7.0/?resource=vps`. The unselected API root
continues to list versions; a selector there uses the default version.
Malformed or ambiguous selectors return 400. Resources absent from the current
user's description return 404. Navigation, examples and legacy anchor mappings
use the same filtered description, and HTML responses use `private, no-store`.

Each resource page shows that resource's own actions and links to its children.
Action links retain their existing `root-...` fragments. Old overview links
with resource, action or example fragments open the corresponding resource page
when JavaScript is enabled. Ordinary resource links work without JavaScript;
the resource directory remains usable without JavaScript.

## Search and visibility

Search is available on every documentation page. It finds resource names, action
names, aliases and paths, and input or output parameter names, labels and types.
Versioned pages search their selected API version. The versions index and
HaveAPI internals search the default version, identified in the search label.
Search does not include protocol text, examples, defaults or validator values.

Results open the resource, action or parameter row. Queries use the normal
resource-directory page, such as `?page=resources&q=hostname`, and work without
JavaScript. Typing can show suggestions; submitting the form opens the results
page. The list shows at most 20 matches and asks the reader to refine queries
with more results. Queries and results are not stored in browser preferences or
a shared index.

Anonymous documentation shows all declared resources, actions and parameters.
Signed-in documentation and search results show only those accessible to the
current account. The sidebar displays the actual account login and states which
view is shown. Each API request still checks authorization for its particular
operation; a documentation entry does not grant permission to execute it.

Parameter validators explain the advertised rules. Allowed values appear as
typed API literals beside their display labels. Validation messages and extra
options remain available; unknown rules retain their supplied details. The
Required column, defaults and API validation behavior are unchanged.

Version-specific navigation puts Authentication before Resources and indents
authentication methods beneath it. Technical references are linked under
HaveAPI internals in the versions-index sidebar, and retain their direct URLs.

## Themes and examples

The sidebar controls theme, language, client variant and example detail for
all examples on the page. The theme buttons select **Automatic**, **Light** or
**Dark**; Automatic follows the operating system. The versions index and shared
internal pages use the same layout and theme choices.

**Simple** examples focus on the operation and assume an initialized `api`
client, authenticated when required. **With error handling** includes additional
setup or error handling where it helps. Initialization and authentication
examples remain on their respective pages.

The browser stores these choices in `haveapi.docs.preferences.v1`. It stores no
credentials or API responses. Choices are checked against the clients available
in the current API; an unavailable saved client uses an available fallback.
Storage failures leave the controls usable for the current page. Without
JavaScript, native disclosure panels keep the examples readable.

## Extending documentation

Client renderers declare `language`, `language_label` and optional `variant`
metadata alongside their stable client `id`. Unspecified presentation metadata
falls back to the renderer's ID and label. Only available renderers appear;
generated SDKs require their configured profiles. See
[client examples](client-examples.md) for renderer and profile configuration.

HTML selection traverses description keys rather than Ruby constants or file
paths. Keep UI navigation separate from any complete private schema used by a
client generator for name resolution. New content should retain stable action
and example IDs, escaped source and the shared current-user description.

## Browser sign-in

APIs can optionally configure an OAuth documentation client for browser sign-in.
The server keeps its client secret and uses a secure encrypted cookie for the
documentation session. This session applies only to HTML documentation; API
actions still use their ordinary credentials. See the
[OAuth setup guide](documentation-oauth.md) for configuration and HTTPS
requirements. APIs without that configuration retain their existing sign-in
controls.
