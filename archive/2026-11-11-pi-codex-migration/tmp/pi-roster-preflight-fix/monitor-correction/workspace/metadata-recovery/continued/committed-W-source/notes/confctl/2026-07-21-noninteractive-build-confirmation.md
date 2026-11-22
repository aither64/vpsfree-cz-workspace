# Non-interactive confctl builds need `-y`

Related initiative: `work/2026-07-20-security-advisory-review/`

`confctl build '<machine-pattern>'` prompts for confirmation after listing the
selected machines. When invoked through a non-interactive command runner, it
receives EOF and exits before starting the build.

Use `confctl build -y '<machine-pattern>'` for an already reviewed machine set.
The failed invocation is safe: it only evaluates and lists the selection before
the confirmation prompt and does not build or deploy anything.
