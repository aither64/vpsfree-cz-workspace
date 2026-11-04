# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/dataset_downloads_keyset_pagination.spec.ts >> @pr-smoke @pr-smoke-mobile Dataset downloads keyset pagination >> next/prev updates URL and rows
- Location: e2e/specs/app/dataset_downloads_keyset_pagination.spec.ts:67:3

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: getByTestId('dataset.downloads.list')
Expected: visible
Timeout: 15000ms
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 15000ms
  - waiting for getByTestId('dataset.downloads.list')

```

```yaml
- link "Skip to main content":
  - /url: "#main-content"
- banner:
  - button "Open navigation"
  - button "Search"
  - button "Open tasks"
  - button "Open account menu"
- main:
  - text: Failed to load dataset Please try again.
  - button "Retry"
  - link "Back":
    - /url: /app/datasets
  - link "Status":
    - /url: /
  - button "Copy details"
  - group: Details
```

# Test source

```ts
  1   | import { expect, test } from "@playwright/test";
  2   | 
  3   | import { bootstrapVpsAdminWindow, installHaveApiMock } from "../../fixtures";
  4   | 
  5   | test.describe("@pr-smoke @pr-smoke-mobile Dataset downloads keyset pagination", () => {
  6   |   let requestedDownloadParams: URLSearchParams[];
  7   | 
  8   |   test.beforeEach(async ({ page }) => {
  9   |     requestedDownloadParams = [];
  10  |     await bootstrapVpsAdminWindow(page, {
  11  |       sessionToken: "TEST",
  12  |     });
  13  | 
  14  |     const dataset = {
  15  |       id: 10,
  16  |       full_name: "tank/vps/ds10",
  17  |       name: "ds10",
  18  |       used: 2048,
  19  |       refquota: 10240,
  20  |       snapshots_count: 123,
  21  |       mount_count: 0,
  22  |       export_count: 0,
  23  |       object_state: "active",
  24  |       vps: { id: 300, hostname: "alpha.example" },
  25  |     };
  26  | 
  27  |     const makeDl = (id: number) => ({
  28  |       id,
  29  |       dataset: 10,
  30  |       snapshot: {
  31  |         id: id + 1000,
  32  |         name: `snap-${id + 1000}`,
  33  |         label: `Snapshot ${id + 1000}`,
  34  |       },
  35  |       format: id % 2 === 0 ? "archive" : "incremental_stream",
  36  |       size: 1024 * 1024,
  37  |       sha256: "00".repeat(32),
  38  |       url: `/download/${id}`,
  39  |       ready: true,
  40  |       expiration_date: "2099-12-27T00:00:00.000Z",
  41  |     });
  42  | 
  43  |     const allDownloads = Array.from({ length: 100 }, (_, i) => i + 1).map(makeDl);
  44  | 
  45  |     await installHaveApiMock(page, {
  46  |       user: { id: 1, login: "test", level: 1 },
  47  |       handlers: {
  48  |         "GET datasets/10": () => dataset,
  49  |         "GET snapshot_downloads": ({ searchParams }) => {
  50  |           requestedDownloadParams.push(new URLSearchParams(searchParams));
  51  |           const ds = searchParams.get("snapshot_download[dataset]");
  52  |           if (ds !== "10")
  53  |             return { snapshot_downloads: [], _meta: { total_count: 0 } };
  54  |           const fromId = Number(searchParams.get("snapshot_download[from_id]") ?? 0);
  55  |           const limit = Number(searchParams.get("snapshot_download[limit]") ?? 50);
  56  |           return {
  57  |             snapshot_downloads: allDownloads
  58  |               .filter((download) => download.id > fromId)
  59  |               .slice(0, limit),
  60  |             _meta: { total_count: allDownloads.length },
  61  |           };
  62  |         },
  63  |       },
  64  |     });
  65  |   });
  66  | 
  67  |   test("next/prev updates URL and rows", async ({ page }) => {
  68  |     const mobile = (page.viewportSize()?.width ?? 1024) < 768;
  69  |     const item = (id: number) =>
  70  |       page.getByTestId(`dataset.downloads.${mobile ? "card" : "row"}.${id}`);
  71  |     const paginationKind = mobile ? "mobile" : "desktop";
  72  |     const pagination = page.getByTestId(`dataset.downloads.pagination.${paginationKind}`);
  73  | 
  74  |     await page.goto("/app/datasets/10/downloads");
  75  | 
> 76  |     await expect(page.getByTestId("dataset.downloads.list")).toBeVisible();
      |                                                              ^ Error: expect(locator).toBeVisible() failed
  77  |     await expect(item(1)).toBeVisible();
  78  |     expect(requestedDownloadParams.at(-1)?.get("snapshot_download[limit]")).toBe("51");
  79  | 
  80  |     await pagination
  81  |       .getByTestId(`dataset.downloads.pagination.${paginationKind}.next`)
  82  |       .click();
  83  |     await expect(page).toHaveURL(/from_id=50/);
  84  |     await expect(page).toHaveURL(/page=2/);
  85  |     await expect(item(51)).toBeVisible();
  86  |     expect(requestedDownloadParams.at(-1)?.get("snapshot_download[limit]")).toBe("51");
  87  |     await expect(item(1)).toHaveCount(0);
  88  |     await expect(
  89  |       pagination.getByTestId(`dataset.downloads.pagination.${paginationKind}.next`),
  90  |     ).toBeDisabled();
  91  | 
  92  |     await pagination
  93  |       .getByTestId(`dataset.downloads.pagination.${paginationKind}.prev`)
  94  |       .click();
  95  |     await expect(page).toHaveURL(/page=1/);
  96  |     await expect(page).not.toHaveURL(/from_id=/);
  97  |     await expect(item(1)).toBeVisible();
  98  |   });
  99  | 
  100 |   test("does not offer or send the unsupported q filter", async ({ page }) => {
  101 |     const mobile = (page.viewportSize()?.width ?? 1024) < 768;
  102 |     await page.goto("/app/datasets/10/downloads?q=legacy-search");
  103 | 
  104 |     await expect(
  105 |       page.getByTestId(`dataset.downloads.${mobile ? "card" : "row"}.1`),
  106 |     ).toBeVisible();
  107 |     await expect(page.getByTestId("dataset.downloads.search.input")).toHaveCount(0);
  108 |     expect(requestedDownloadParams.length).toBeGreaterThan(0);
  109 |     expect(requestedDownloadParams.every((params) => !params.has("snapshot_download[q]"))).toBe(true);
  110 |     expect(
  111 |       requestedDownloadParams.every((params) => params.get("_meta[count]") === "true"),
  112 |     ).toBe(true);
  113 |   });
  114 | });
  115 | 
```