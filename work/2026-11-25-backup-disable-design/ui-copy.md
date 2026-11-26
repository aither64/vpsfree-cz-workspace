# Disable backups: D3 shared UI copy

Lead-owned final English/Czech wording for the accepted ONE-chain D3 contract.
This replaces D2 phase/continuation copy. Owners retain all source edits, map
semantic names to repository keys and reuse existing task labels/messages where
available. No extra status endpoint, session receipt subsystem or workflow UI.
Lead directly applied vpsfree-user-facing-writing with EN/CS guidance.

| Meaning | English | Czech |
| --- | --- | --- |
| Plan-removal explanation | Removing this plan stops the snapshots and transfers scheduled by it. Existing snapshots remain on primary and backup pools. | Odebráním plánu se zastaví vytváření snapshotů a přenosy podle tohoto plánu. Existující snapshoty zůstanou na primárních i zálohovacích poolech. |
| Cleanup action | Disable backups and remove local snapshots | Vypnout zálohování a odstranit místní snapshoty |
| Backup-first checkbox | Back up existing snapshots first | Nejprve zálohovat existující snapshoty |
| Backup-first help | Back up existing snapshots to all configured open backup destinations before removing primary snapshots. If a snapshot cannot be preserved by the normal transfer, cleanup does not start. This may take time. | Před odstraněním snapshotů z primárního úložiště zazálohovat existující snapshoty do všech nastavených otevřených zálohovacích úložišť. Pokud některý snapshot nepůjde zazálohovat běžným přenosem, odstraňování nezačne. Přenos může trvat delší dobu. |
| Opt-out warning | If you turn this option off, cleanup permanently deletes snapshots that exist only on primary storage. | Pokud tuto možnost vypneš, při odstraňování se nenávratně smažou snapshoty, které existují jen na primárním úložišti. |
| Cleanup scope | This removes all primary snapshots, including manual snapshots. Existing backup-pool snapshots remain under their normal retention rules. Reenabling backups starts a new tree with a full transfer. | Odstraní se všechny snapshoty z primárního úložiště včetně ručně vytvořených. Snapshoty na zálohovacích poolech zůstanou zachované podle běžných pravidel uchovávání. Po opětovném zapnutí zálohování vznikne nový strom s plným přenosem dat. |
| Single-dataset scope | This action applies to dataset {dataset}. | Akce se vztahuje na dataset {dataset}. |
| Recursive scope | This action applies to dataset {dataset} and its existing subdatasets. Separately mounted datasets outside this subtree are excluded. | Akce se vztahuje na dataset {dataset} a jeho existující vnořené datasety. Nevztahuje se na samostatně připojené datasety mimo tento podstrom. |
| Existing snapshots only | This backs up existing snapshots. It does not create a new snapshot of the current filesystem. | Zálohují se existující snapshoty. Nový snapshot aktuálního stavu souborového systému se nevytváří. |
| Pending task | The task is running. It will continue if you close this page. | Úloha běží. Bude pokračovat i po zavření stránky. |
| Task failed | The task failed. Some changes may have completed. Check the task details before trying again. | Úloha selhala. Některé změny už mohly proběhnout. Než akci zopakuješ, zkontroluj podrobnosti úlohy. |
| Cleanup complete | Backups are disabled and primary snapshots have been removed. | Zálohování je vypnuté a snapshoty z primárního úložiště byly odstraněny. |
| Unknown submission | The request outcome is unknown. Check the task status before trying again. | Výsledek požadavku není známý. Než akci zopakuješ, zkontroluj stav úlohy. |
| Task link (reuse existing label preferred) | View task | Zobrazit úlohu |
| Rejected request title | Cannot disable backups | Zálohování nelze vypnout |
| Unsupported backend title | Disabling backups is unavailable | Vypnutí zálohování není dostupné |

Use normal task handling rather than adding new labels/controllers just to consume
this table. Never show completion before successful ordinary receipt + fresh reads.
A failed receipt does not establish that every plan/head change or deletion happened;
use existing task details. No preservation/cleanup phase protocol, Continue button,
client cancellation promise or second mutation. API old-gap errors are ordinary
rejections, without a new retry-needed protocol or automatic transfer fallback.
