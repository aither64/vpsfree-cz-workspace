# GC interference with exact preparation

The first final469/bce/401 machine preparation exited75 after3m43s, with no
snapshot returned. The profile phase never started; no activation job was
submitted. Keep original machine request, empty output, log and status.

Adapter preparation built and copied exact system mvn0jq6s successfully, then
coordinator retention failed because its immutable helper environment
/nix/store/zwnp17zzpqbgnqgac2h69j02j06khzh7-workspace-confctl-environment
was absent. The helper's derivation aaa7vcc8 was also missing.

Read-only journal evidence from nix-store-gc-on-pressure.service shows both
exact paths deleted at17:45:27+02:00, during preparation17:42:41–17:46:24.
The pressure collector ran17:44:03–17:45:57 and freed2.3GiB. This establishes
this preparation failure's GC interference; it says nothing about the earlier
notification/provider/browser failure causes. No service/GC policy is changed.

Recovery uses the same adapter-owned expression at the exact retained config
source to rebuild that exact helper with a session-owned nix build --out-link
GC root before repeating preparation. Assert the output is exactly zwnp17zz;
never edit or manufacture a prepared artifact/snapshot. Use new machine request
UUID and separate-v2 evidence; the original unexecuted profile request remains.
Keep the root after preparation; coordinator retains its own artifact roots.
Same source/check/review identities remain valid. No source edit, new application
review, reset, replayed activation or lifecycle action is implied.

Parent owns v2 wrapper handle87499; fresh utility observes original status files.

The first pre-retention helper reconstruction used historical adapter irchsv
from the earlier4ed preparation rather than the currently selected catalog
adapter7fmkxa. It produced xbfy (retained) and the exact zwnp assertion refused
before any preparation call. Preserve that log/root/expression. Corrected
reconstruction now uses the selected immutable catalog adapter; the exact
assertion remains. No snapshot or product operation was bypassed.

Corrected helper root exactly matched zwnp17zz and its registered GC root was
verified. Machine preparation v2 succeeded in100s with genuine snapshot and
original artifact5f80960c; exact environment retained. Systemmvn0jq6 built/copied,
current identity stillgfan1lz7. No new source tests required for this operational
recovery. Profile preparation proceeds through the original unused request.
