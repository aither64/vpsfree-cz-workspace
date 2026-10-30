# Milestone8 user feedback

User review after the M7 preview:

> I like it overall, except the copy icon in client examples moves the code down, it shouldn't do that. the icon can also be smaller.
>
> I also wish that the client examples wouldn't use environment variables for the secrets. just provide the secrets as literals. it's not like using environment variables for secrets is a good pattern and it will simplify the examples.
>
> and about the language/client/example selection... it's weird when both language and client is the same, like for go and php. the selects could be disabled when there's only one choice... and I don't really know how to improve the duplicity. the selection makes sense when there are actually multiple variants, but otherwise it seems confusing.
>
> and why don't more clients have the "With error handling" variant? e.g. php isn't showing how to handle errors... ruby either. seems like an omission.

Additional user request:

> another nit: parameter inclusion/exclusion validators are listing acceptable values and they're quoted. that's unnecessary. it's already marked by <code> tag and so the quotes don't have to be there.

Audit scope clarified by the user:

> well see if other clients miss the error handling variant as well... and if it would be useful, add it.

Main's stated direction: smaller overlay copy control without code displacement;
literal example credentials; remove the duplicate Client choice for single-variant
languages, keep Examples visible and disable one-choice selectors; useful runtime-
correct error handling across all clients/kinds; string validator values retain
code markup/HTML escaping without presentation quotes. Architect owns the exact
interface and verification amendment before product edits. Current documented
legacy adapter and direct rendering contracts remain relevant.

M7 review/publication/CI/browser evidence remains at its actual source scope.
Stop old copy-UI browser reruns; retain 390 pass and partial 768 results. New
browser acceptance will include focused 768 touch/copy diagnosis on final M8
and failed/unexecuted cases, preserving unaffected supported evidence.

Further user instructions:

> as for the settings dropdown... the icon looks good. however, the content can now be more verbose... so add a label for the theme controls so that it is clearer.
>
> after this milestone is implemented, let the vpsadmin session deploy it in the dev cluster, so that I could test the integration and oauth2 in the dev cluster. I suppose this will need updating the dev cluster fixtures in order to add the API itself as an oauth2 client. we'll have to do that later in production as well, it must be a part of deployment notes.
>
> (production deployment is done using vpsfree-cz-configuration)

Main-approved visible label is Theme. Peer lead receives final exact reviewed M8
source/all-five/package/acceptance handoff, owns development client fixtures and
HTTPS integration/OAuth2 deployment under its authorization. Concrete later
production registration/protected-config/order/operator notes belong in
vpsfree-cz-configuration; HaveAPI keeps generic setup guidance. No production
activation, release or default integration is implied.
