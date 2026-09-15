# Review v7: omit exemption paragraph in forced-release emails

Scope: the user clarified that when opt-outs are disabled, the emails should
say nothing about keeping an unassigned address via an administrator exemption.
A proposed support-reply instruction was immediately withdrawn and was never
committed/pushed. Remove the whole exemption paragraph. Keep the common VPS
assignment instruction, and the reason-form instruction when opt-outs are on.

Tracking: /home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-ip-release-mechanism
Worktrees under /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism:

- vpsadmin: previous reviewed head 37e08d8be10c2f38138f5511403c94523126d033;
  current committed head 7483c4d2535b994a10ea3a82856052bd78c4913c.
- vpsfree-notification-templates: previous reviewed head
  ff5cc7c474cab76dbdebabcd706b5d43c8d5319a; current committed head
  00519f79fa9a5073eb83f41bae3857bc66229e17.

Use git diff between each previous reviewed head and current head for this
review. These are amendments of the latest unmerged prose-only commits, keeping
one final copy commit per repository. The prior reviewed heads remain immutable
Git objects; they are not parents of the amended heads. Their parents remain
feccc0073 (vpsadmin) and 0c80160f (overlay). All worktrees are clean.

Changes: delete the else branch under campaign.allow_keep in 12 templates:
built-in EN plus overlay EN/CS, initial/reminder, text/HTML. The existing model
spec now checks the reason form is not offered when opt-outs are off. The local
overlay harness uses the retained assignment instruction as its expected text
for forced mode. No new code flow, API, schema, policy, support routing or
exemption behavior. Generic automated-mail footers remain unchanged per repo
rules. Review only this bounded delta; v1-v6 feature and CI reviews are complete.
The prior CI investigation and runtime failure are not new work in this review.

Verification of this final wording:
- nix develop .#api -c bundle exec rspec -I spec
  spec/models/ip_release_campaign_spec.rb:424 <tracking>/overlay-check.rb
  with IP_RELEASE_OVERLAY pointing to the overlay worktree: 25 examples, 0
  failures (1 existing campaign-notification example plus 24 EN/CS x event x
  policy x address-family rendering/routing combinations). Captured at
  /tmp/ip-release-forced-copy-check.log; existing safe previews regenerated.
- Overlay nix flake check passed: /tmp/ip-release-forced-copy-flake.log.
- All commit hooks, including RuboCop, i18n and text width passed.
- git diff --check passed; source searches show no exemption/policy-history
  prose or proposed reply instructions in any of the 12 templates.

Low risk: prose/ERB branch removal only with matching existing assertion; no
new abstraction or runtime/public/persisted contract. General lane only,
gpt-5.6-sol/xhigh. No need to repeat a long integration test for this surface.
The API/WebUI implementation and KB contract inputs are unchanged; no new KB
pin, schema rollout, merge, deployment, real email or session lifecycle action.

Read applicable AGENTS.md and mandatory-change-review general guidance. Inspect
the two committed diffs directly. Do not edit code or launch nested agents.
Report concrete findings or no findings and residual gaps. Keep the review
focused on this deletion and its verification, rather than re-auditing v1-v6.
