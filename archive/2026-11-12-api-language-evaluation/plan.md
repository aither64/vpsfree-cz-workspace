# 2026-11-12-api-language-evaluation

## Goal

I wonder what language would be suitable for vpsAdmin API. Ruby was good for humans, pleasure to read and write. However, with LLMs, I'd like a language with types so that more issues are caught during development. Naturally the best for this is arguably rust... however, that is a rather low-level language and the API contains a lot of business logic. If we were to rewrite the API into something more suitable for LLMs to ensure correctness, maintainability and reduce the number of bugs... what language would be appropriate? We would also have to rewrite haveapi into the same language, since that's what the server is based on.

vpsAdmin has multiple components that are run in different places, so this can be a part of the consideration. I suppose using a single language would make sense. It could still be rust of course... but I wonder if there isn't a better choice.

## Affected repositories

Read-only evaluation of vpsadmin, haveapi and relevant vpsadminos component boundaries. No rewrite, code changes, deployment or integration requested.

## Approach

Compare compile-time domain modeling, human readability, persistence and asynchronous transaction semantics, deployment footprint, distributed compatibility and framework replacement cost. Distinguish language guarantees from architectural and testing obligations; avoid unsupported claims about LLM performance.

Architect0 owns a bounded source investigation and records findings in design.md. Lead owns scope, primary-source verification, acceptance, tracking and the conversational recommendation. No implementation packages are needed for this advisory request.

## Decisions

Accepted advisory recommendation: Kotlin first for API/HaveAPI business logic; compare Rust if broader control-plane unification matters. C# is a close alternative. Go and TypeScript offer useful tradeoffs but are less aligned with maximizing direct compile-time domain checks. F# is a conditional domain-modeling alternative. No language or rewrite has been selected for implementation.

## Compatibility and deployment

Any future rewrite must preserve or deliberately version HaveAPI schemas, authentication/authorization, generated clients, database data, queued transaction and node communication formats. Mixed versions, rollback and single-writer ownership matter independently of language. No operational changes in this evaluation.

## Documentation

Readers: vpsAdmin maintainer considering a future investment. Destination: this session's design.md findings and final conversational advice; no project documentation changes are warranted by an unadopted proposal.

## Testing plan

Read representative source and current official language documentation. No executable changes or builds; any future pilot must compare a realistic business operation including authorization, database transaction, durable node command and recovery, rather than CRUD alone.
