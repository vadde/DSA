"""
============================================================
Problem: Split a String Into the Max Number of Unique Substrings
Pattern: Backtracking
Difficulty: Medium
LeetCode: #1593
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Split a string into as many UNIQUE (non-repeating) substrings as possible.
E.g. "ababccc" → ["a","b","ab","c","cc"] → 5 parts.

APPROACH: Backtracking
---------
Try all prefix splits from current position.
If the prefix hasn't been seen before, add it to the set and recurse on the rest.
Track the maximum count seen across all valid splits.
Backtrack by removing from the set.

COMPLEXITY: O(2^N) — exponential but N <= 16 in constraints.
============================================================
"""


def max_unique_split(s: str) -> int:
    best = [0]

    def backtrack(start: int, seen: set) -> None:
        if start == len(s):
            best[0] = max(best[0], len(seen))
            return
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if sub not in seen:
                seen.add(sub)
                backtrack(end, seen)
                seen.discard(sub)

    backtrack(0, set())
    return best[0]


if __name__ == "__main__":
    assert max_unique_split("ababccc") == 5, "Test 1"
    assert max_unique_split("aba") == 2,     "Test 2: a|ba or ab|a → 2"
    assert max_unique_split("aa") == 1,      "Test 3: aa → a (only 1 unique)"
    assert max_unique_split("a") == 1,       "Edge: single"
    print("All tests passed!")
