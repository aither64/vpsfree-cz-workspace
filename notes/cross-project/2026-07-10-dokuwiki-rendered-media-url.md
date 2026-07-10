# Verify rendered DokuWiki media URLs after HTML decoding

Related initiative: `work/2026-07-10-kb-czech-fixes/`

When checking screenshot URLs extracted from rendered DokuWiki HTML, direct
requests to resized images returned HTTP 412 even though the media existed and
API hash verification passed. The extracted query string still contained the
HTML entity `&amp;`, so DokuWiki received an invalid resize token.

Decode HTML entities in each extracted `src` before resolving and requesting
the URL. In Ruby, use `CGI.unescapeHTML(src)`. Also match all `<img>` tags whose
source is in the expected media namespace; image alignment changes the CSS
class, so matching only `class="media"` can miss valid embeds.

After applying both rules, all 30 draft pages rendered successfully, all 63
expected embeds were present, and all 60 unique screenshot URLs returned PNG
responses.
