# 2026-11-17-ct-top-display-bug

## Goal

This is a test of the pi backend in the workspace. I found a bug in `osctl ct top` and I'd like you to find the root cause and suggest a fix. I noticed the problem during osctld restart, but also during normal operation. Essentially ct top content is not stable. In some refreshes, the container list disappears. Or they are listed, but have no CPU usage (just CPU socket assignment is shown). The attach screenshots were taken from the same ct top run and demonstrate how the content disappears/reappears. Find the root cause and suggest a solution.

## Affected repositories

## Approach

## Decisions

## Compatibility and deployment

## Documentation

## Testing plan
