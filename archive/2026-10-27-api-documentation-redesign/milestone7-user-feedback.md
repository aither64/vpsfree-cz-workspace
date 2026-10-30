# Milestone7 verbatim user feedback

Copied from the current lead conversation, in order.

> - I'm confused about examples of the generated typescript client. why does it call actions like `api["vps"]["create"]`? I thought we have some proper properties/classes/types.
> - go client example sometimes shows `This response field is unavailable in the configured Go SDK.`, no idea why
> - `// Configured SDK: vpsadmin-typescript-client; runtime: haveapi-client@0.30.2.` -- where does this come from? I mean the precise haveapi-client version
> - I think calling the generated clients SDK is a bit too much, they're simply API clients, so find a better wording.
> - when I'm viewing docs of a resource:
>   - actions should have an indented submenu in the sidebar with links to subsections like Input parameters, Output parameters, Examples, etc.. Show it only for the currently displayed action
>   - show subresources in the sidebar
> - headings in the reference documentation could have permalinks so that we can easily link to them

> authentication types in the sidebar could also have a submenu to individual sections

> the copy icon should be inside the code example blocks, not outside

> we don't have to say "generated". just API client.

> And I don't understand "haveapi-client@0.30.2 is hardcoded in the renderer.", what sort of design is this to hardcode it, it makes no sense to me

> and the top-level menu icon is weird, it seems to mean "filters". we want an icon for settings, or use three dots

> pressing slash `/` should focus the search input

> the example types are also weird. for example, initialization for rust/go/maybe others is the same for "Simple" and "With error handling". So either the error handling is missing, or it shouldn't offer its selection. Verify this so that this switch is always meaningful.

> but like before, keep the selector visible, just offer only meaningful choices

> on page "Resources', remove the duplicit search input&submit in  the content. search will be done only through the sidebar
