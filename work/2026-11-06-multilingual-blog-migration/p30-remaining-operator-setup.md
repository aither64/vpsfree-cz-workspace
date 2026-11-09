# P30 remaining Discourse setup

P31 update: the user deployed Discourse, corrected the pilot host rules to accept
canonical and normalized slashless paths, and moved existing topic374 into public
Blog10. Both-parent anonymous embed delivery is verified; the user confirms both
Czech and English browser pilots work. CSP frame-ancestors takes precedence over
X-Frame-Options; its console notice needs no header change. The broader
rules below include the source-guide correction; global embedding/counts stay off.

The original P30 source was committed, reviewed, built and published on the feature branches.
BLOG CI42613369754/#17 passed. This checklist describes remaining operator work;
the P31 update above supersedes its earlier pending deployment/pilot status.

The intended shared forum source is the English article URL on blog.vpsfree.org.
Both blog languages use that same source so there is one topic, with an English
opening post and source link. Original Czech article/navigation provenance remains.

The CONFIG feature declares twelve ordinary site-setting defaults: article-body
extraction, configured admin fallback, restricted framing, excerpt imports,
initial unlisted visibility, full-app mode and SameSite=None for cross-site
`.org` sessions. Existing HTTPS configuration supplies Secure cookies; normal
CSRF and origin protection remain. The cookie default applies to the whole
forum. Browser cookie blocking can still require top-level forum navigation.

Stored UI overrides take precedence over Nix defaults. The user reports not
changing these settings. The final native build passed, but actual deployment,
effective-setting/account checks and browser testing remain separate steps.
No Discourse activation or UI mutation has happened in P30.

Operator-owned UI records remain:

1. Select a publicly readable category and verify ordinary member replies.
2. Under /admin/customize/embedding add exact host blog.vpsfree.org as import source,
   selecting that category and leaving Post author blank. Final supported path rule:

   ```text
   \A/(?!(?:cs|en|search|feed|author|authors|category|categories|tag|tags|archive|archives|page|posts|assets|images|pagefind|admin|login|logout|robots|sitemap)(?:/|\z)|[0-9]{4}/[0-9]{2}(?:/|\z))[a-z0-9]+(?:[-_][a-z0-9]+)*(?:/[a-z0-9]+(?:[-_][a-z0-9]+)*)*/?\z
   ```

3. Add blog.vpsfree.cz with its supported Czech article-path allowlist, the same
   category and blank Post author. Full-app mode checks the parent article path,
   so a reject-all Czech rule blocks framing. Its supported rule is:

   ```text
   \A/(?!(?:feed|search|author|authors|category|categories|tag|tags|archive|archives|page|posts|assets|images|pagefind|admin|login|logout|robots|sitemap)(?:/|\z)|wp-|[0-9]+(?:/|\z))[a-z0-9]+(?:-[a-z0-9]+)*/?\z
   ```

   The blog still sends only the shared English source; Discourse host records also allow native imports from their
   permitted paths, so this does not enforce server-side English-only identity.
4. Check existing blog RSS importers and topic/source mappings before enabling.
   Changing identity does not merge or migrate any preexisting Czech topic.
5. Check mapped accounts: aither, snajpa, krcmar and martyet; remaining existing
   authors use admin fallback. Michal Janoušek=KerryCZE is a future confirmed
   mapping; no current author/article record was invented.
6. After source/settings delivery, test one published pair from both production
   origins, checking one shared topic, attribution, extraction, ordinary reply,
   framing, inline login/reply from both domains and notification effects.
   Do not mass-open the archive or seed topics.

The blog's enabled=false stays unchanged during preparation. The count
client uses one background batch for rendered listing articles and displays forum
reply phrases only. Historical comments remain on article pages. Missing/failed
counts stay plain links; no guessed zero or combined total. Count requests share
the embed opt-in, so they are currently off too. Response phrasing follows forum
locale behavior; local labels identify it as Discourse discussion.

A later reviewed enablement release must update the affected production checks
and the opt-in flag before enabling embed/count traffic.
No default integration, web.int deployment, forum topic migration or cleanup is
implied. See state.md, design.md:4976 and the final BLOG docs/discussions.md.
