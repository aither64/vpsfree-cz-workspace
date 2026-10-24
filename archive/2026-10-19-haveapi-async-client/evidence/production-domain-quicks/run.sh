#!/usr/bin/env bash
set -u
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-haveapi-async-client/vpsadmin-webui-async
start=$(date -u +%FT%TZ)
nix develop --command node node_modules/vitest/vitest.mjs run src/lib/api/audit.test.ts src/lib/api/clusterResourcePackages.test.ts src/lib/api/datasets.test.ts src/lib/api/dns.test.ts src/lib/api/dnsResolvers.test.ts src/lib/api/exports.test.ts src/lib/api/finance.test.ts src/lib/api/incidents.test.ts src/lib/api/infra.test.ts src/lib/api/ipAddresses.test.ts src/lib/api/mailer.test.ts src/lib/api/migrations.test.ts src/lib/api/networkInterfaces.test.ts src/lib/api/networks.test.ts src/lib/api/nodeHistory.test.ts src/lib/api/nodes.test.ts src/lib/api/oom.test.ts src/lib/api/outageScopePaging.test.ts src/lib/api/outages.test.ts src/lib/api/payments.test.ts src/lib/api/profile.test.ts src/lib/api/requests.test.ts src/lib/api/securityAdvisoryUpdates.test.ts src/lib/api/systemConfig.test.ts src/lib/api/transactions.test.ts src/lib/api/userDossier.test.ts src/lib/api/userLookups.test.ts src/lib/api/userNamespaces.test.ts src/lib/api/users.test.ts src/lib/api/vps.blocking.test.ts src/lib/api/vps.test.ts src/lib/api/vpsAccess.test.ts src/lib/api/vpsFeatures.test.ts src/lib/api/vpsMounts.test.ts src/lib/api/vpsUserData.test.ts > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-haveapi-async-client/evidence/production-domain-quicks/verification.log 2>&1
result=$?
printf '%s\n' "$result" > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-haveapi-async-client/evidence/production-domain-quicks/exit-status
printf 'start=%s\nend=%s\n' "$start" "$(date -u +%FT%TZ)" > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-haveapi-async-client/evidence/production-domain-quicks/timing.txt
exit "$result"
