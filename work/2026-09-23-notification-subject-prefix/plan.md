# 2026-09-23-notification-subject-prefix

## Goal

Require `[vpsFree.cz] ` before the actual subject of every user-facing email
template. Administrator-only templates are exempt. Bring existing templates
into line with the rule.

## Affected repositories

- `vpsfree-notification-templates`: subject metadata and authoring guidance.
- The coordination workspace holds this plan and the session state.

## Approach

- State the rule in the repository `AGENTS.md`, allowing `Re: ` before the
  `[vpsFree.cz] ` prefix in reply subjects.
- Audit every `meta.rb` subject, classify recipients, and add the prefix
  in noncompliant user-facing subjects without changing the remaining text or
  ERB expressions.

## Decisions

- The requested text is a prefix: it precedes the actual subject despite the
  word "suffix" in the request.
- The user confirmed that `Re: [vpsFree.cz] …` is the correct reply format.
- Generic outage mail is not demonstrably administrator-only: it is sent with
  `user: nil` and configured template recipients. Apply the user-facing rule.

## Compatibility and deployment

- Subject metadata changes only. No persisted state, schema, API, CLI, protocol,
  NixOS configuration, or body format changes are expected.
- Existing messages and their headers remain unchanged. Future messages use the
  new subject strings after templates are installed. Replies retain their
  existing `Re:` text before the site prefix. The outage sender also sets
  Message-ID and In-Reply-To headers. Rolling installation may briefly yield
  mixed subject formats. Reinstalling prior metadata restores old formats.
- Template upload is a separate operational step; no production install is
  planned without a reviewed target and authorization.

## Documentation

- Update the repository `AGENTS.md` at its subject-authoring guidance.
- Check `README.md` for any related rule or installation guidance to adjust.

## Testing plan

- Check Ruby syntax of all changed `meta.rb` files and audit every subject
  against its recipient category, including both languages and reply subjects.
- Run repository checks that do not require an API endpoint. API authentication
  and staging upload require a configured target and credentials.
