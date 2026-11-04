# Live Go/HTTP detail-control probe

The reported visible Examples/detail selector was not reproduced in 24 fresh
Chromium states against the current live exact
`ef4c0cdcb349815538bb93cedab9d3964c565998` service. This result does not explain
the user's browser state and is not a claim that the report is resolved.

Matrix: English/Czech × overview/public Test/authentication × Go/HTTP ×
JavaScript interactive language selection/no-JavaScript explicit selection URL.
The native URLs deliberately requested `example_detail=thorough` to exercise the
singleton fallback. All selected clients were correct (`go` or HTTP `6`). Every
state had one `simple` option and page metadata `details: ["simple"]`; the detail
wrapper had `hidden=true`, computed `display:none`, and wrapper/select layout
boxes were both 0×0. No legitimate two-choice Go union or CSS hidden override
was observed in these fixture states.

Full URLs, options, metadata, geometry and open panels are retained in
[raw probe evidence](preview-go-http-live-probe.json). Representative native URL:
<http://aitherdev.int.vpsfree.cz:4567/v1.0/?resource=test&doc_lang=cs&example_language=http&example_client=6&example_detail=thorough>.

The architect received direct same-session evidence and owns further diagnosis;
the lead is collecting the exact reported URL/browser-refresh state. Asset cache
reuse is a hypothesis, not a verified cause. No source/index, live runtime,
service, dependency, host or configuration changes were made. Prior generalized
refinement checks covered Go but did not establish the newly reported HTTP
states; any successor acceptance must directly cover real Go and HTTP cases.
