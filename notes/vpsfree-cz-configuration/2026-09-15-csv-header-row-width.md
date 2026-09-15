# Validate CSV rows against the original header

Related initiative: `work/2026-09-15-abuse-uceprotect`.

A UCEPROTECT regression test with an extra column in the first data row failed:
the parser accepted that malformed row and rejected the next correctly sized
row. `CSV.parse(text, headers: true)` exposed table headers extended with a nil
header for the extra field. Comparing row width with `table.headers.length`
therefore did not validate against the original header line.

Parse the CSV into arrays, shift the explicit header array, validate its names,
and compare every row's length against that array before using its fields.
Reject malformed rows without changing the expected shape for later rows.

Verified with the MasterDC parser regression covering an extra first-row field,
a correct subsequent row, and a prose mention that must not bypass CSV failure.
