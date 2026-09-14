# Planning question controls investigation

## Finding

The reported behavior is implemented by the dev-workspace portal. The earlier
full-composer hiding change applies only to the completed-plan decision panel;
it does not apply to the question wizard displayed while a planning turn is active.
No codex-web change is needed to address the identified host-layout omission.

## Evidence

Inspected dev-workspace master `e9ed544bf66ba8be07b4fca27aede6e6fd1bfe0a` and
codex-web master `6335da93acdcc82cc26200d2fbc7f479655aa7c3`.

- `portal/internal/web/static/app.js:79`: `setPlanDecisionVisible` sets
  `form.hidden = visible` for the completed-plan panel only.
- `app.js:1909`: `renderPlanActions` passes false for an active turn, making the
  ordinary form visible even while Codex waits on a planning question.
- `app.js:2537`: `renderPendingEntries` mounts question/approval cards without
  changing the ordinary form's visibility.
- `portal/internal/web/static/style.css:363`: a max-height 600px media query
  shortens the textarea and hides model/reasoning/mode selectors. It deliberately
  leaves the prompt, Send, attachment controls and Interrupt in the layout.
  Above 600px height, these question-specific rules do not apply.
- Commit `1906812b702fbd341e9484d1e3d0e5a6201e4bf1`, September 13:
  `portal: replace the composer with current plan decisions`. Its description and
  implementation explicitly cover the completed-plan decision panel. Earlier
  `703b1a9` changed question scrolling and retained the compact composer rules.

Read-only GETs of the deployed portal's `/static/app.js` and `/static/style.css`
through its private Unix socket returned HTTP 200 and byte-for-byte identical
assets to the inspected master. Results and hashes are in `deployed-assets.json`.
The missing behavior exists in the deployed source; browser cache clearing cannot
supply it. This does not establish which files the reporting browser cached.

## Browser reproduction

Ran Nix-packaged Chromium/Playwright against the real portal chat template,
stylesheet and exported visibility helper, with a synthetic pending question DOM.
No live conversation was opened, interrupted, answered or otherwise changed.

| Viewport | Question | Prompt and Send | Model, reasoning, mode | Composer height |
| --- | --- | --- | --- | --- |
| 1440 × 1000 | Visible | Visible | Visible | 163px |
| 1280 × 720 | Visible | Visible | Visible | 163px |
| 1280 × 540 | Visible | Visible | Hidden | 100px |
| 390 × 844 | Visible | Visible | Visible | 231px |

Interrupt remained visible in every case. The completed-plan helper successfully
hid the full composer, and dismissal restored it with the draft intact. See
`reproduce-layout.cjs` and `layout-results.json`.

The fixture validates the layout and existing visibility helper; it does not
exercise real App Server request delivery or question answer submission.

## Fix scope

Extend the portal's composer visibility policy to include a displayed question
wizard, as well as the completed-plan decision panel. Account for both in one
place: setting `form.hidden` only in pending-question rendering would be undone
by subsequent `renderPlanActions` calls during snapshot refreshes.

Preserve typed drafts and uploads, move keyboard focus out of hidden controls,
close attachment popovers, and restore the ordinary form when the question ends.
Preserve a way to interrupt an active turn when moving its current button out of
the hidden composer. Question input availability and blocking/asynchronous
semantics should remain unchanged. A regression check should cover refreshes,
question disappearance, completed-plan decisions and responsive layouts.

No repository source was changed, no implementation commits were made, and no
package was deployed. The requested investigation is complete. The session and
clean worktrees remain open for follow-up implementation.
