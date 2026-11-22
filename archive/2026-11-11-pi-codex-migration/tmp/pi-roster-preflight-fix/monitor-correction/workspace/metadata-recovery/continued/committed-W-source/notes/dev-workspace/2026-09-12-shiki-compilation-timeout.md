# Shiki compilation can consume its soft tokenization timeout

In portal/review-ui, tokenizeTimeLimit:100 sometimes colored an entire
JavaScript line as its first token. First-use JavaScript regex compilation
counts against Shiki's soft time limit, which returns partial tokenization
without an error. Set the soft limit to0 and enforce an8-second hard timeout
by terminating the bounded worker. Keep the source and long-line limits.
Packaged tests and actual Chromium computed-color checks passed afterward.
Related initiative: work/2026-09-12-portal-review-experience/.
