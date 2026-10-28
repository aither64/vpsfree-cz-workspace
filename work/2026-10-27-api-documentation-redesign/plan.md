# 2026-10-27-api-documentation-redesign

## Goal

i'm looking at haveapi-generated html documentation in vpsadmin api. first, since we have introduced new client examples, the languages don't fit on a single line, see image-1.png. maybe we could collapse language variants (sync, async, etc.) into a dropdown menu. or make a better suggestion. further, it might be useful to switch all examples to the selected language... however, I bet this would mess with page scroll position if the user would change the language in the middle of the page. maybe put the global example selection in the sidebar.

secondly, the client examples are extremely convoluted. only the ruby/php/cli examples seems to have kept their simplicity. I dunno, I realize that you're showing how to be thorough and handle errors... but it is making it hard to see the important bits.

all in all, looking at the documentation, I'd be open to a redesign, both visual and functional. API description doesn't have to be a single large page that takes long to load. we could have per-resource pages, for example. and the design could be updated as well... introduce dark/light/auto themes. my requirements are that it must be clear for users. the current version for example has a list of resources and actions on the right and scrolling the content keeps the sidebar in sync. so we need clear navigation.

the authentication as it is leaves a lot to be desired as well -- it allows only http basic. to be done properly, it should use the API's oauth server. although I guess that is a large change.

anyway, if you're going to be changing the design and functionality, I'll need a way to review it, so connect to some development server of yours.

Attached local files (inputs; keep these files outside version control):
[
  {
    "name": "image-1.png",
    "size": 631455,
    "path": "/home/aither/.local/state/dev-workspaces/portal/vpsfree.cz-8a2a555cb2f65b33/uploads/files/7b72f3b3-b3fd-434c-aa4b-6ff7ba27ac84/file.png"
  }
]

## Affected repositories

- HaveAPI owns generated HTML documentation, example templates, and browser behavior.
- vpsAdmin is the integration consumer and source of the realistic review API;
  application changes are conditional on the designer's authentication findings.
- No production deployment, release, or default-branch integration is authorized.

## Approach

Deliver a functional development preview of a clearer API reference. Prefer
resource-sized pages, persistent resource/action navigation, a global example
language selector with compact variants, short idiomatic examples, and
light/dark/system themes. Preserve useful deep links and the reader's position
when changing examples. Investigate the API's existing OAuth support before
choosing the authentication boundary. Keep the uploaded screenshot outside Git.

The retained architect owns investigation and `design.md`. Implementers own
complete packages identified in that design, including checks and commits.
The lead owns coordination, acceptance, user-facing wording, and preview access.

## Decisions

## Compatibility and deployment

Keep protocol descriptions, generated SDK contracts, database state, and CLI
behavior compatible. Assess old documentation links and browser state explicitly.
OAuth changes must preserve supported clients and avoid credentials in browser
storage or records. Preview deployment must be isolated from production and
have a documented stop/recovery path. Integration needs separate user approval.

## Documentation

Readers are API users, HaveAPI maintainers, and operators serving the reference.
Keep lasting behavior and setup in the owning project's existing documentation;
keep design choices, exact preview revisions, and verification here.

## Testing plan

Use repository Nix environments and mandatory hooks. Run focused generator,
example, and browser checks before committing the final deliverable. Review the
complete committed branch independently, including history and migration
provenance, before longer integration checks. Verify the actual served preview,
navigation, selectors, themes, mobile layout, and authentication behavior.
