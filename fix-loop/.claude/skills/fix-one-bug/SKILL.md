---
name: fix-one-bug
description: Fixes one failing test in this repo, on its own branch, then sends the diff to the reviewer. Use for the fix loop.
---

# Fix one bug

1. Run `pytest` and identify the single failing test.
2. Create a branch named `claude/fix-<short-slug>`.
3. Write the smallest fix in the source file that solves that one problem.
   Do not bundle unrelated changes.
4. Do NOT edit any test file.
5. Run `pytest` again and show the real output.
6. Send the diff to the reviewer agent. Wait for its verdict.
7. On PASS, report the branch name and stop. On FAIL, report the reasons and stop.
   Do not fix and retry on your own.