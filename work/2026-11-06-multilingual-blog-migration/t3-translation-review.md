# T3: English archive drafts

Source checkpoint accepted by the lead. Main-context prose checks and requested
corrections are complete. Independent final review awaits completion and quick
checks of C/E/T2. Every T3 translation remains a draft pending human review of
meaning and voice. Implementer3 retains technical and review-fix ownership.

## Scope and exact revisions

- Repository: `git@github.com:vpsfreecz/blog.git`, feature branch
  `2026-11-06-multilingual-blog-migration`.
- Checkout: `worktrees/2026-11-06-multilingual-blog-migration/blog`.
- Parent: `e9c286b2f403603907265ac28f4bd38b3ae00227`.
- T3 commit: `e8aed2ef787217e8085d782e38a760cd51ddbd90`,
  **Translate 63 archived articles into English drafts**.
- Exactly 63 new `content/posts/<id>/index.en.html` files, 2,213 inserted lines.
  The authoritative ID inventory is implementer3's batch in
  [translation-batches.json](translation-batches.json): 21,528 Czech source words.
- Final inventory digest:
  `b522ed1cde36f23be33c456e9cb1d4f02bb3ab52d070651d86ec3b46eb79977b`.
  Compute SHA-256 over the concatenation, in assigned batch order, of relative
  English path, tab, file SHA-256, newline.

The complete T3 series is this one coherent commit; no superseded T3 approaches,
follow-up commits, database migrations or dependency/generated update streams.
Historical migration narratives inside articles are preserved content, not new
application migrations. Review the exact parent-to-commit diff; the lead owns the
complete multi-package branch packet and history conclusion.

## Sources and editorial decisions

The sanitized public Czech import manifest has SHA-256
`e3c56173acbc2dd018da1d7ce5cd8b73d52e5ef83847a0353b17b107e5a36ab4`.
Each English `translation_source_sha256` records the exact complete Czech-file
hash from that manifest. Original dates, lastmod, taxonomy slugs, article IDs,
translation keys and shared author/discussion metadata remain unchanged.

Read all assigned Czech bodies and the public author map before translation.
Applied repository authoring instructions, D6, the lead's voice brief,
vpsfree-user-facing-writing and English Humanizer guidance. The two reference
Discourse announcements were verified as aither/Jakub Skokan. Translations retain
each source author's byline, viewpoint, first person, jokes and historical claims;
they do not invent experiences or update old recommendations. Complete prose,
headings, lists, tables, captions and relevant alt text were translated. Literal
code, including Czech comments and arguments, stays in the original language.

Lead performed contextual prose checks across all 63, including full paired
source reading for the pilot and next ten. Requested wording corrections were
applied before committing. This is agent editorial checking, not human approval.

Recorded source/presentation exceptions:

- wp-592: interpreted the invitation's missing Czech negation as “don't miss it,”
  accepted by the lead; Czech source remains unchanged.
- wp-662: retained the original weekday/date mismatch. Lead approved the explicit
  clarification “4 June (4.6.)” for the symbolic date.
- wp-746: translated the source's “before 13” as “before 13:00,” as directed;
  the complete supplier statement and all other dates/times remain intact.
- Decimal commas and spaces before percent signs were localized to English
  presentation, preserving values. Original statistical inconsistencies were
  retained; the missing-value en dash in wp-702 is source table data.
- wp-821 retains its source HTML list nesting. Protected relative Czech links
  remain literal; render-time resolution belongs to the theme owner.

## Verification and limits

All 63 passed complete-source hash freshness, draft/status/no-human-review-fields,
date/lastmod/taxonomy/identity, HTML tag/end/comment/nonlocalized attribute order,
URL/media order, original more-anchor and normalized numeric-value checks.
Numeric comparison includes the two explicit equivalent date/time presentations
above. Routes had no collisions in the concurrent snapshot of 113 English
articles; that was not a claim of final 125-article completion.

Final **raw-byte** pre/code parity passed for all 63. Earlier text-mode checking
missed newline normalization during prose edits in wp-662 and wp-824. Commit was
stopped, owned index entries were unstaged, and the lead renewed the repair window.
Restored exact protected spans from authoritative Czech bytes: 11 CRLF in wp-662
and 21 CRLF in wp-824. Removed only unprotected EOF blank lines across all 63;
accepted prose stayed unchanged. The final verifier compared raw bytes.

Remaining `git diff --cached --check` diagnostics were all byte-identical protected
source code: 43 locations, wp-15=2, wp-174=4, wp-397=5, wp-662=11, wp-824=21.
Every diagnostic was mapped to a source-identical pre/code span; no unprotected
whitespace remained. No hook framework or active custom hook is declared. No hook
was bypassed. Commit used an ordinary temporary message file with `git commit -F`.
Working and staged inventories matched the final digest; post-commit checks
confirmed exactly 63 committed paths and an empty index, then index ownership
was yielded. No whole-checkout cleanliness claim: T2/C/E work was preserved.

No push, default-branch integration, production change, forum write or deployment
was performed by T3. No runtime build was launched for this source batch; the
lead coordinates combined source checks and independent review. All translations
have `draft=true`, `translation_status="draft"`, no human reviewer/date, and
explicit English root paths. Human review and publication approval remain later
requirements. Source changes invalidate affected translation hashes.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/>.

## T9-3: contextual repetition audit
Status: main-context writing accepted all13, with wp-547 refinement applied; source committed as `d6c673c9e6addc8cf4f32f10cd653d8a632f0ddb`. Independent final review remains lead-owned.
Read all 63 complete assigned English articles with Czech source context. Inspected IDs: wp-8, wp-15, wp-69, wp-94, wp-107, wp-123, wp-133, wp-156, wp-174, wp-191, wp-205, wp-229, wp-264, wp-284, wp-299, wp-316, wp-333, wp-347, wp-358, wp-362, wp-367, wp-381, wp-390, wp-397, wp-403, wp-408, wp-448, wp-481, wp-493, wp-506, wp-516, wp-539, wp-547, wp-557, wp-560, wp-564, wp-573, wp-576, wp-592, wp-597, wp-606, wp-621, wp-639, wp-646, wp-662, wp-667, wp-678, wp-692, wp-702, wp-713, wp-722, wp-730, wp-738, wp-746, wp-759, wp-762, wp-773, wp-821, wp-824, wp-828, wp-835, wp-841, wp-847.
Proposed changes: wp-69, wp-299, wp-316, wp-358, wp-448, wp-516, wp-539, wp-547, wp-597, wp-646, wp-738, wp-841, wp-847. Other50 unchanged. Intentional anaphora (347), milestone celebration/interview (381), failed-experiment narrative (678), migration reassurance (713/730) retained. No Czech, metadata, code, URLs, HTML structure or review-state change proposed.
Reading base: `3dff9d7dbf61d7bf7c76e10fd72929711cd2bbf7`.

### wp-69
The body repeats the teaser question before adding the geographic finding.
Current teaser (context; unchanged except listed wp-597 edit):
```html
<p>Where do vpsFree.cz members come from? We've put together detailed statistics, including maps.</p>
```
Old:
```html
<p>We wanted to know where vpsFree.cz members actually come from, and whether the internet really breaks down geographical boundaries. It turns out it does: our members come from all corners of our two countries.</p>
```
Proposed:
```html
<p>We wanted to see whether the internet really breaks down geographical boundaries. It turns out it does: our members come from all corners of our two countries.</p>
```

### wp-299
Keep date, location and event in the teaser; body develops the eight-year history and current membership.
Current teaser (context; unchanged except listed wp-597 edit):
```html
<p>OSS Víkend took place in Bratislava on the weekend of 9 and 10 April, where Tomáš Srnka spoke about the past of vpsFree.cz and more.<br>
<!--more--><span id="more-299"></span></p>
```
Old:
```html
<p>Last weekend's <a href="http://ossvikend.sk/">OSS Víkend</a> in Bratislava included a talk by Tomáš Srnka on how vpsFree.cz began eight years ago. Today, the project has almost a thousand members.</p>
```
Proposed:
```html
<p>In his <a href="http://ossvikend.sk/">OSS Víkend</a> talk, Tomáš Srnka looked back at how vpsFree.cz began eight years ago. Today, the project has almost a thousand members.</p>
```

### wp-316
Avoid repeating that we deal with DDoS attacks; retain network perimeter and the isolation aim.
Current teaser (context; unchanged except listed wp-597 edit):
```html
<p>Among other things, we have to deal with DDoS attacks on our infrastructure. Fortunately, there aren't too many, and we can handle them.<br>
<!--more--><span id="more-316"></span></p>
```
Old:
```html
<p>DDoS attacks are becoming more frequent; you can watch them live on <a href="http://www.digitalattackmap.com/">Digital Attack Map</a>. We have to deal with them too and defend our network perimeter. Our main aim is to stop an attack on one IP address affecting other members and their services.</p>
```
Proposed:
```html
<p>DDoS attacks are becoming more frequent; you can watch them live on <a href="http://www.digitalattackmap.com/">Digital Attack Map</a>. Our main aim in defending the network perimeter is to stop an attack on one IP address affecting other members and their services.</p>
```

### wp-358
The body repeats the entire teaser; go straight to names, versions and selection.
Current teaser (context; unchanged except listed wp-597 edit):
```html
<p>We've added two more distribution templates.<br>
<!--more--><span id="more-358"></span></p>
```
Old:
```html
<p>Two more distribution templates are available: <a href="https://alpinelinux.org/">Alpine Linux</a> 3.3 and <a href="http://slackware.com">Slackware</a> 14.1. Both are available directly on the membership application form.</p>
```
Proposed:
```html
<p>You can select <a href="https://alpinelinux.org/">Alpine Linux</a> 3.3 or <a href="http://slackware.com">Slackware</a> 14.1 directly on the membership application form.</p>
```

### wp-448
Develop the web-interface announcement directly into its name and scope.
Current teaser (context; unchanged except listed wp-597 edit):
```html
<p>HaveAPI version 0.6 is out, bringing a web interface.<br>
<!--more--><span id="more-448"></span></p>
```
Old:
```html
<p>HaveAPI <a href="https://github.com/vpsfreecz/haveapi">version 0.6</a> mainly introduces the new <a href="https://github.com/vpsfreecz/haveapi-webui">haveapi-webui</a> web interface. It lets you administer any API based on HaveAPI. I'd compare it to phpMyAdmin, which can administer any MySQL database.</p>
```
Proposed:
```html
<p>The main addition in HaveAPI <a href="https://github.com/vpsfreecz/haveapi">version 0.6</a> is <a href="https://github.com/vpsfreecz/haveapi-webui">haveapi-webui</a>, a client for administering any API based on HaveAPI. I'd compare it to phpMyAdmin, which can administer any MySQL database.</p>
```

### wp-516
Keep the no-surprises warning in the teaser; proceed to figures in the body.
Current teaser (context; unchanged except listed wp-597 edit):
```html
<p>A year on, here are the statistics on the Linux distributions running on our infrastructure. Don't expect surprises, but there are some trends.<br>
<!--more--><span id="more-516"></span></p>
```
Old:
```html
<p>Don't expect any dramatic surprises. We've added 525 new VPSes over the year, so naturally all distributions have grown in absolute numbers. The only exception is Scientific Linux, which continues to decline and is probably being gradually replaced on VPSes by the more widespread CentOS. Here's the resulting table:</p>
```
Proposed:
```html
<p>We've added 525 new VPSes over the year, so naturally all distributions have grown in absolute numbers. The only exception is Scientific Linux, which continues to decline and is probably being gradually replaced on VPSes by the more widespread CentOS. Here's the resulting table:</p>
```

### wp-539
Avoid restating the weekend timing; keep the tenth edition and enthusiasm.
Current teaser (context; unchanged except listed wp-597 edit):
```html
<p>We were at InstallFest over the weekend, showing our work-in-progress project vpsAdminOS.<br>
<!--more--><span id="more-539"></span></p>
```
Old:
```html
<p>The <a href="https://installfest.cz/if18/">tenth InstallFest</a> took place over the weekend, and we couldn't miss it. We had a stand, made excellent coffee and talked with visitors about our <a href="https://github.com/vpsfreecz/vpsadminos">vpsAdminOS project</a>. It's a small Linux operating system based on <a href="https://nixos.org/">NixOS</a>, providing a virtualization platform for virtual servers in containers.</p>
```
Proposed:
```html
<p>We couldn't miss the <a href="https://installfest.cz/if18/">tenth InstallFest</a>. We had a stand, made excellent coffee and talked with visitors about our <a href="https://github.com/vpsfreecz/vpsadminos">vpsAdminOS project</a>. It's a small Linux operating system based on <a href="https://nixos.org/">NixOS</a>, providing a virtualization platform for virtual servers in containers.</p>
```

### wp-547
Keep end-of-life/development-stop/move in the teaser; body retains all-node scope, distribution support issue and architecture.
Current teaser (context; unchanged except listed wp-597 edit):
```html
<p>The OpenVZ technology we use is reaching the end of its life, and development has stopped. We're therefore moving to a newer solution, vpsAdminOS.<br>
<!--more--><span id="more-547"></span></p>
```
Old:
```html
<p>We currently use OpenVZ Legacy container virtualization to run VPSes on all nodes. As it's ageing, development has ended and new distributions are dropping support, we're working on a move to <a href="https://vpsadminos.org">vpsAdminOS</a> (<a href="https://github.com/vpsfreecz/vpsadminos">GitHub</a>). This distribution is based on <a href="https://nixos.org">NixOS</a> and <a href="https://github.com/cleverca22/not-os">not-os</a>, and will serve as the hypervisor for VPSes on our nodes.</p>
```
Proposed:
```html
<p>We currently use OpenVZ Legacy container virtualization to run VPSes on all nodes. New distributions are also dropping support for it. Its replacement, <a href="https://vpsadminos.org">vpsAdminOS</a> (<a href="https://github.com/vpsfreecz/vpsadminos">GitHub</a>), is based on <a href="https://nixos.org">NixOS</a> and <a href="https://github.com/cleverca22/not-os">not-os</a> and will serve as the hypervisor for VPSes on our nodes.</p>
```

### wp-597
The same three capabilities are listed twice; retain current scope in the teaser, then provide instructions.
Current teaser (context; unchanged except listed wp-597 edit):
```html
<p>We have our own Terraform module for creating and modifying VPSes on our infrastructure, uploading public SSH keys and running commands over SSH.</p>
```
Old:
```html
<p>We have our own Terraform module for creating and modifying VPSes on our infrastructure, uploading public SSH keys and running commands over SSH.</p>
```
Proposed:
```html
<p>We have our own Terraform module that currently creates and modifies VPSes on our infrastructure, uploads public SSH keys and runs commands over SSH.</p>
```
Old:
```html
<p>Our Terraform plugin currently creates and modifies VPSes, uploads public SSH keys and runs commands over SSH. The plugin, installation instructions and an example are <a href="https://github.com/vpsfreecz/terraform-provider-vpsadmin">on GitHub</a>.</p>
```
Proposed:
```html
<p>The plugin, installation instructions and an example are <a href="https://github.com/vpsfreecz/terraform-provider-vpsadmin">on GitHub</a>.</p>
```

### wp-646
Keep Word spread quickly in the teaser; narrative develops what users did.
Current teaser (context; unchanged except listed wp-597 edit):
```html
<p>A look back at our first day hosting the video-calling platform. Word spread quickly, and we had hundreds of calls at once.<br>
<!--more--><span id="more-646"></span></p>
```
Old:
```html
<p>On Monday evening, the idea of a public videoconferencing platform came up. Overnight into Tuesday, we launched a <a href="https://blog.vpsfree.cz/spoustime-video-hovory-na-meet-vpsfree-cz-zdarma-a-bez-registrace/">public instance</a> of Jitsi Meet. Word spread quickly, and people began arranging meetings, calling for a chat and planning other uses. To join them, visit <a href="https://meet.vpsfree.cz">meet.vpsfree.cz</a>.</p>
```
Proposed:
```html
<p>On Monday evening, the idea of a public videoconferencing platform came up. Overnight into Tuesday, we launched a <a href="https://blog.vpsfree.cz/spoustime-video-hovory-na-meet-vpsfree-cz-zdarma-a-bez-registrace/">public instance</a> of Jitsi Meet. People began arranging meetings, calling for a chat and planning other uses. To join them, visit <a href="https://meet.vpsfree.cz">meet.vpsfree.cz</a>.</p>
```

### wp-738
Keep container/no-GRUB/replacement facts in teaser; body explains console and actions.
Current teaser (context; unchanged except listed wp-597 edit):
```html
<p>Our VPSes run in containers, so they don't have a bootloader such as GRUB. We're preparing an alternative: the VPS start menu.</p>
```
Old:
```html
<p>We're preparing a new menu that <a href="https://kb.vpsfree.cz/navody/vps/konzole">appears in the console</a> when a VPS starts. As well as starting normally, it lets you launch a shell or change the init process's parameters. It's an alternative to something like the GRUB menu in our environment. Our VPSes are containers, so they don't have a conventional bootloader.</p>
```
Proposed:
```html
<p>The menu <a href="https://kb.vpsfree.cz/navody/vps/konzole">appears in the console</a> when a VPS starts. As well as starting normally, it lets you launch a shell or change the init process's parameters.</p>
```

### wp-841
Replace adjacent You can now use announcements with the second-factor/device explanation.
Current teaser (context; unchanged except listed wp-597 edit):
```html
<p>We've prepared a new secure way to log in to vpsAdmin. You can now use passkeys.<br>
<!--more--><span id="more-841"></span></p>
```
Old:
```html
<p>You can now use a <a href="https://en.wikipedia.org/wiki/WebAuthn">passkey</a> as a second factor when logging in to vpsAdmin. Both hardware tokens (YubiKey, GoTrust IdemKey and similar) and software keychains (KeePassXC, KeePassium, iCloud Keychain, Google Password Manager, Microsoft Windows Hello, 1Password and others) work.</p>
```
Proposed:
```html
<p>As a second factor, vpsAdmin accepts a <a href="https://en.wikipedia.org/wiki/WebAuthn">passkey</a> from either a hardware token (YubiKey, GoTrust IdemKey and similar) or a software keychain (KeePassXC, KeePassium, iCloud Keychain, Google Password Manager, Microsoft Windows Hello, 1Password and others).</p>
```

### wp-847
Keep two-year interval in teaser; introduce the comparison directly.
Current teaser (context; unchanged except listed wp-597 edit):
```html
<p>After two years, we're back with our regular statistics on the Linux distributions running on our virtual servers.<br>
<!--more--><span id="more-847"></span></p>
```
Old:
```html
<p>It's been another two years since we last published <a href="https://blog.vpsfree.cz/linuxove-distribuce-rocky-linux-rychle-roste-slackware-uplne-zmizel/">statistics on the distributions our members use</a>. It's time to look at the current data and compare it with the previous figures.</p>
```
Proposed:
```html
<p>We'll compare the current data with the <a href="https://blog.vpsfree.cz/linuxove-distribuce-rocky-linux-rychle-roste-slackware-uplne-zmizel/">distribution statistics from our previous count</a>.</p>
```

No article source edits, index/commit, builds, services, remote requests or publication action performed. Draft and human-review requirements remain.

### T9-3 completion receipt

Lead accepted all13 proposals after reading the full English articles and Czech
openings, refining wp-547 to “New distributions are also dropping support for it.”
Applied byte-level replacements only; no newline normalization.

- Commit: `d6c673c9e6addc8cf4f32f10cd653d8a632f0ddb`.
- Parent: `3dff9d7dbf61d7bf7c76e10fd72929711cd2bbf7` (U9).
- Tree: `dac14783e018ebeb0b724349563bd1b8edd71eeb`.
- Exactly13 assigned English paths listed above,14 insertions/14 deletions.
  Other50 assigned English files stayed unchanged; T9-2/UI edits were preserved.
- Ordered changed-path/tab/file-SHA256/newline inventory digest:
  `2085560edf31e04379aca356ba36b8f00eae3459ca187ce67365ff51aa8e56d1`.
- All125 current translations passed complete-Czech-source hash freshness,
  draft/status/no-human-review-fields, dates/lastmod/taxonomy/article identity.
- All125 CS/EN raw pre/code byte pairs passed, including all63 assigned articles.
- All125 Czech files remained byte-identical and unchanged against the parent.
- All13 edits preserved exact frontmatter bytes, raw HTML tag/comment/attribute
  sequence, URLs/media and pre/code bytes. Whitespace checks passed.
- Repeated two-template wording in wp-358 and two-year wording in wp-847 were
  reduced by approved deduplication. This is not an identical numeric-sequence
  claim: every distinct numeric fact and both distribution versions remain.
- No hook framework or active custom hooks declared; ordinary `git commit -F`,
  no bypass. Exact owned working/staged inventories matched before commit;
  post-commit exact13-path and empty-index checks passed. Index yielded immediately.

One coherent T9-3 commit; no migrations, dependency updates or superseded T9-3
commits. No rebase, build, service, push, default integration or production action.
Human meaning/voice approval remains pending; all translations remain drafts.
