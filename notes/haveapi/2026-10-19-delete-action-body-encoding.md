# HaveAPI DELETE actions read JSON input

The initial Rust runtime classified GET and DELETE as query methods. Real
HaveAPI fixture tests showed GET receiving its expected fields but DELETE
receiving an empty input hash in both transports. HaveAPI's Ruby server
classifies only GET, HEAD and OPTIONS as query methods; DELETE reads the JSON
body. The Go generator likewise uses its query path only for GET.

The supported Rust action enum contains GET, DELETE, POST, PUT and PATCH. Its
shared classifier now selects query encoding only for GET; all other supported
methods use the existing JSON envelope and Content-Type. Keep metadata in its
normal body namespaces and preserve omission, null, falsy values, nested Custom
values and supported named-list input. Do not fall back to replaying a DELETE
with another encoding, since the first request may already have changed state.

Regression assertions should compare actual server input and metadata, with a
paired GET control. Merely accepting a success envelope missed this defect.
The correction changes no public Rust signatures or API-version snapshot, but
embedded runtime consumers need regeneration to receive it.

Session: [Rust client generator](../../work/2026-10-18-rust-client-generator/state.md).
Detailed contract: [Clarification5](../../work/2026-10-18-rust-client-generator/design.md).
