# Transaction chain STI and one-off scripts

- Date: 2026-05-31
- Initiative: `work/2026-05-30-dev-vpsadmin-clusters`
- Symptom: the web UI returned HTTP 500 after admin login when loading
  `/?page=`.
- Cause: the dashboard lists recent transaction chains. One-off maintenance
  scripts had created custom `TransactionChain` subclasses named
  `DcDnsRefresh` and `DevclusterDnsRefresh`. Those class names were persisted
  in `transaction_chains.type`, but normal API workers do not load the scripts
  that defined them. ActiveRecord STI then raised `SubclassNotFound` while
  instantiating the transaction-chain list.
- Related observation: plugin transaction-chain classes are safe only when the
  API process loads the same plugin set as rake tasks. The payments scheduled
  task creates
  `VpsAdmin::API::Plugins::Payments::TransactionChains::MailOverview`; the API
  can list it when the payments plugin is enabled.
- Fix/workaround: do not persist ad-hoc `TransactionChain` subclass names from
  one-off scripts. Use an existing loadable chain class, define reusable chains
  in the application code, or clean/delete the temporary chains afterwards. In
  the running devcluster, the two temporary DNS-refresh chain rows were
  normalized to an existing loadable chain type.
- Verification: `vpsadminctl --raw transaction_chain list -- limit=3` succeeds
  through the running API. Restoring the payments chain row to
  `VpsAdmin::API::Plugins::Payments::TransactionChains::MailOverview` also
  succeeds, confirming the API process has the payments plugin loaded.
