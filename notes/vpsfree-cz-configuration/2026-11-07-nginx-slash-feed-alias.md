# Serve a feed file from a slash URL with try_files

An exact nginx `/feed/` location with a file-valued `alias` passed generated
configuration checks but returned HTTP 500 in the real nginx rehearsal. The
index phase appended `index.html` to `feed/index.xml`, producing an ENOTDIR
error. A syntactically valid nginx configuration did not prove this response.

For a fixed language document root, use `try_files /feed/index.xml =404` in
the exact location and retain `types { }` plus
`default_type application/rss+xml`. The selected regular-file URI avoids the
slash-URI index phase and serves RSS without an external redirect.

Verification in session `2026-11-06-multilingual-blog-migration` included both
language mappings in the generated module fixture and real nginx HTTP 200/RSS
responses. Original failing evidence and passed alias cases were retained; only
changed feeds and previously unexecuted routing cases were probed again. See the
session's release-preparation record and H18 runtime evidence.
