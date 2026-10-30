# Milestone6 verbatim user feedback

The following messages are copied from the current lead conversation in order.
Main-selected labels and technical design in the packet are implementation
decisions; they are not additional user quotations.

> - uff, I meant placeholder for the search input like "Resource...", not just "..."
> - it shouldn't *hide* client type/example type select boxes... it should just offer only the available values.
> - http://172.16.106.40:4567/v7.0/ works, while http://172.16.106.40:4567/v7.0 (without trailing slash) returns different (useless) content
> - not sure how it is now, but the built-in http-basic based auth should be removed from the API docs. offer only oauth when it is available
> - as for the haveapi internal docs, page http://172.16.106.40:4567/doc is useless. let's just show the readme there.
> - there's a mismatch between how resource names are matched in search and what is shown in the sidebar. search uses '.' as a separator, the sidebar uses '/'. let's use '.'. breadcrumb navigation can use the slash

> as for the Overview page, "The sidebar follows the action in view; breadcrumbs link to parent resources." sentence is useless, remove it.

> as for the API title/label at the top... the preview has it as `172.16.106.40:4567` and it already uses two lines, since there's not enough space... `api.vpsfree.cz` in production is unlikely to fit as well. so, not that I'd want the icons moved below it... but we must find some space so that it fits.

> maybe we could have just one icon for a dropdown menu that would include theme control and login control

> in that way, the theme control could be expanded as it was before (it doesn't need a second dropdown menu)

> I don't want to make the sidebar wider
