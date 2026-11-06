# Verification batch 5

Source795134a48cdee269bdccabb68168de2d190c6830, cleanHEAD/lock verified.
Parentmonitoring fallback, handle46138. Command1 exited1 after190.39 seconds;
commands2-6 notrun. Full verification-5-vm.log/status.json.

All earlier isolation/security/greylist/DNSBL/delivery/content/IPv4IPv6/TLS/
missingmilter/policydown gates passed. The acceptedoutagequeue survived both
Postfix restart and the actual same-disk guestreboot, including Postgrey state;
restored primary received the intact original message and queue drained.
That complete persistence/recovery subtest passed in63.10s.

Primary4xx then deferred the accepted message with the intended controlled reply:
queue7F7FCF8, recipienttemporary@vpsfree.cz, reason
`450 4.2.0 <temporary@vpsfree.cz>: Recipient address rejected: fixture temporary rejection`.
The R2 assertion demanded contiguous code+fixturetext, so failed on Postfix's
standard recipient decoration. Recovery-after4xx/latercases not completed.
Owner0 corrects only assertionformat matching, keeping queueID/recipient/code/
controlledreason bindings; no production/fixture change or blindretry.

Nativecleanup stopped all3QemuMachines0.78s; Nix/parentexited1, running=null,
no owned process/VM or productioneffects. Failed assertion does not erase the
successful earlier gates; full final run still required at corrected source.
