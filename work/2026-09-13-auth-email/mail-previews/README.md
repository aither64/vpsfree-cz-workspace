# Verification email previews

Synthetic previews for the email refinement review. No production account data
or usable authentication code is included. The rendered plain-text and HTML
content is checked for equivalence by `../render-mail-previews.rb`.

- [vpsFree.cz Czech HTML](vpsfree-cs.html) · [plain text](vpsfree-cs.txt)
- [vpsFree.cz English HTML](vpsfree-en.html) · [plain text](vpsfree-en.txt)
- [Built-in Czech HTML](builtin-cs.html) · [plain text](builtin-cs.txt)
- [Built-in English HTML](builtin-en.html) · [plain text](builtin-en.txt)

The layout follows the existing password-recovery HTML email; login details
follow the production new-device notification. The expiration and request times
use the API's time-zone formatter with Europe/Prague for this synthetic example.
