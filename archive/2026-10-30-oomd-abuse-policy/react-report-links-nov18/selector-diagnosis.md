# Retired link test selector failure

Final typecheck passed0/72.242s. Focused9files stopped1 with86tests passed/2failed,
only EN/CS retiredhref CSS assertion. Original final-quick logs/results unchanged.
No runtime/source link correction was necessary.

A minimal installedJSDOM control (native60239,exit0) created five literalanchors:
alpha current/history, beta current/history, retiredhistory. Querying existing
alpha/beta anchors worked; querying absentretiredcurrent returnednull and then
querying the exact existing retiredhistory CSSselector also returnednull. Enumerating
allanchors/getAttribute showed the exactexpected retiredhref present. Thus this is
the JSDOM selector boundary, not browsernavigation/linkbehavior. Control code used
new JSDOM(...), document.querySelector with exactattribute strings and final
querySelectorAll('a').map(getAttribute). No product/dependencychange.

The test now asserts the complete ordered fivehref array, strengthening exact
destination coverage and avoiding the faulty selector. Existing negative retired
current assertion, allcount/privacy and othercases remain. Soleaffectedfile9/9
passed (retired-link-diagnostic.*), no fullbatch/reretry. Narrowaffected TypeScript
and11unruncommands follow; oldfulltype evidence remains tied to originaltesthash.
