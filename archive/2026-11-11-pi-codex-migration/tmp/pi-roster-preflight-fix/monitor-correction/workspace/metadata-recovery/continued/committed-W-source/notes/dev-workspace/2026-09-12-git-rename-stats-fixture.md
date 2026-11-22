# Added/deleted fixtures can become a rename

The native Git numstat/status test expected one addition and one deletion but
used identical contents for both files. Git correctly returned an R100 rename.
Use distinct contents when testing separate added/deleted statuses; retain a
separate rename fixture. The repository suite and focused race checks passed.
Related initiative: work/2026-09-12-portal-review-experience/.
