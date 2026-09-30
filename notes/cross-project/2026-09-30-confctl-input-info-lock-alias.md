# Confctl input metadata can select a colliding nested lock node

In a flake with two `flake.lock` nodes derived from the same input name,
confctl's generation `inputs_info` can report the wrong revision even though
the built input path is correct.

This occurred in `vpsfree-cz-configuration` at `ee99382c`. The root
`llm-agents` input maps to lock node `llm-agents_2` at `af40d966`, while the
nested dev-workspace dependency occupies node `llm-agents` at `ddc89534`.
Confctl's role metadata lookup used the role input name as the lock-node key,
so the generation summary displayed `ddc89534`. The generation's actual
`llm-agents.input` symlink matched the root flake input source at `af40d966`,
and the built and activated system executable reported Codex 0.159.2.

When these disagree, do not accept the displayed revision as package selection
evidence. Compare the generation input symlink with the root flake input's
evaluated `outPath`, inspect the built toplevel, and verify the executable from
that exact toplevel before activation. A future confctl fix should derive
metadata through the root input mapping instead of assuming the input attribute
name is also the final lock-node key.

Related initiative:
`work/2026-09-30-portal-review-improvements/`
