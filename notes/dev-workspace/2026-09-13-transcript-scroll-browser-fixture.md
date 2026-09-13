# Simulate user scrolling when testing transcript retention

Setting transcript.scrollTop and emitting scroll alone does not pause automatic
following. The portal intentionally distinguishes programmatic layout changes
from wheel, pointer, keyboard and touch input. A new connection notice can
resize the transcript and return a still-following view to the bottom.

In a browser fixture, dispatch an upward wheel (or use WebDriver wheel actions)
before setting the intended position. This exercises a paused user view. The
recovery acceptance then preserved the exact top through failures and refreshes.
Related: work/2026-09-13-portal-recovery/.
