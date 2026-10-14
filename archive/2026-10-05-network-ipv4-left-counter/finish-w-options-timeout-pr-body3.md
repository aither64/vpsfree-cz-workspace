IP suggestions could stay loading while shared OPTIONS discovery stalled. Each suggestion now has one 12-second budget across capability discovery and its IP request. A timeout settles as an error so later locations can load; it leaves shared discovery available to other callers. Explicit retry gets a fresh caller budget, and manual filtering keeps its separate results.

Closes #30.

Validation at `cce681424b866f6a51cbc0a1e4daa226ed33fc07`: hosted quick checks, all 1,794 unit tests (including 28 hook cases), production build and Chromium script regression pass. Desktop smoke passes 464 cases; mobile Chrome passes 405. Separate WebKit smoke passes 64 with one retained skip. Independent review found no source issues. The 12 CS/EN desktop/mobile images show partial-load feedback, manual-filter isolation and recovered suggestions under controlled API fixtures.

The budget applies to each suggestion caller. It does not restart a still-pending shared OPTIONS request or change assignment discovery. Existing act() and build-size warnings remain. Real API and PHP KB capture acceptance are separate.
