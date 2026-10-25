# Diagnosed native fixture failure at f722adab

Original evidence preserved as `verification-native-f722-failed.log` and
`verification-native-f722-failed-result.json`; bounded phase extraction is
`package-a-native-f722-phases.json`. Native ownership passed. Protocol fixture
failed only native-retry/native-terminal (~0.10s each), full watcher exit1 in22s.

Both failures show 13 phases ending at thread/start response error -32600,
with no thread identity, turn/start, provider POST or WebSocket upgrade. Thus
no overload SSE, native retry event or utility settlement path was exercised.
The captured diagnostic was intentionally sanitized; its exact message is not
retained and is not claimed as observed.

Pinned source `/nix/store/9is267xl3palxb615kk86qlli9nggkf9-source/codex-rs`
proves the cause: `config/src/config_toml.rs:67–73,929–957` rejects configured
reserved provider ID openai before checking other provider fields. A's two
labelled modes alone inserted per-thread dotted model_providers.openai retry
fields. App Server `request_processors/thread_processor.rs:1355` loads that
configuration; `config_errors.rs:32` maps its error to invalid request, matching
the observed pre-inference -32600. Architect independently confirmed the chain.
This is a fixture configuration defect; it does not demonstrate a production
client/parser defect.

Lead released the smallest correction: delete the whole reserved-provider retry
override block. Preserve built-in OpenAI capabilities and retry defaults. Native
`model-provider-info/src/lib.rs:67,499–510` supplies stream ceiling5, sufficient
for two advised overloads then success; `core/src/responses_retry.rs:88–90`
returns an advice-free overload before ceiling handling. HTTP200 SSE does not
enter HTTP request retry handling. B uses valid custom-provider IDs, so its
labelled2/0 controls remain unchanged. No new provider, workaround, model,
production policy, parser or public contract is needed.

Lead owns focused delta inspection and a fresh diagnosed native rerun after
quick checks/publication. Implementer0 runs no native or long test. A failed
f722 patch/narrative/diff are preserved; all candidates remain undeployed.
