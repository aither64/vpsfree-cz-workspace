# Mail content and scope evidence

Latest copy addition: exact `*` password field in /etc/shadow means no usable
password, not an empty field. Advisory also requires another account with a
real password and SSH password authentication enabled. Lead added these
conditions to both intros after user request. No blanket default-image or
package-origin claim: user expressed uncertainty; advisory names configurations
where `*` accounts already exist. musl/PAM runtime conditions remain in source
evidence above; copy does not imply every Alpine installation is exploitable.

Lead applied vpsfree-user-facing-writing and its complete English/Czech
humanizer guidance directly. Final copy candidates: mail-cs.erb and mail-en.erb.
Informal singular Czech, plain English, normal task salutation/signature.

Facts retained: conditional password-authentication issue, advisory URL,
confirmed changed-VPS setting/backup only, prompt system/OpenSSH update and
service restart, log inspection for possible earlier compromise, public-key
upload plus explicit deployment to an existing running VPS, console access,
localized KB links. No fixed-version claim or claim of detected compromise.
Latest user correction removes failed-VPS discussion from email; failed results
remain eligible internally. No mail has been sent.

Verified sources:

- https://sshhole.com/ (HTTPS curl; web reader unavailable): conditional musl,
  no-PAM password authentication bypass and temporary password-disable measure.
- https://www.openssh.com/txt/release-10.6p2 (HTTPS curl): official 2026-11-05
  security release confirms bypass on musl Linux with PAM disabled. Copy uses
  versionless upgrade wording, avoiding a fixed release for all Alpine branches.
- https://kb.vpsfree.cz/navody/server/ssh and
  https://kb.vpsfree.org/manuals/server/ssh: public-key upload and later
  deployment form in running VPS details. Profile storage alone is insufficient
  to deploy the key to an existing VPS.
- https://kb.vpsfree.cz/navody/vps/konzole and
  https://kb.vpsfree.org/manuals/vps/console: console access via vpsAdmin.

Uploaded raw log remains read-only at its original portal upload path, outside
Git. User received six failed VPS IDs in chat on request. No private raw log or
mail recipients are copied into source or tracking by the lead.

Latest operator confirmation supersedes earlier failed-only eligibility: only
30231 among six failures had password auth enabled, operator fixed it and
confirmed backup exists; treat as other changed VPS. Other five excluded. Final
mail uses simple changed_vpses list for 43 script changes + manual30231 after DB
filters; same backup statement applies. No failed-VPS prose or recipients remain.
