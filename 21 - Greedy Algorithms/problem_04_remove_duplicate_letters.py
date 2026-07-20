"""
============================================================
Problem: Remove Duplicate Letters
Pattern: Greedy Algorithms
Difficulty: Medium
LeetCode: #316
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given a string, remove duplicate letters so each letter appears exactly once.
Among all possible results, return the LEXICOGRAPHICALLY SMALLEST one.
"cbacdcbc" → "acdb"

Think of building the result letter by letter, always choosing the smallest
available letter — but ONLY if we can still include all other required letters.

APPROACH: Greedy Monotonic Stack
---------
1. Count the frequency of each character (so we know if a char appears later).
2. Maintain a result stack (which will be our answer).
3. Use a `in_stack` set to avoid adding a char already in the stack.
4. For each char:
   - Decrement its frequency (we're consuming this occurrence).
   - If it's already in_stack → skip (we already have it).
   - While the stack is not empty AND the top of stack > current char
     AND the top of stack still has future occurrences (freq[top] > 0):
       → Pop the top (we can get a better, lexicographically smaller result).
       → Remove from in_stack.
   - Push current char, add to in_stack.
5. Return "".join(stack).

COMPLEXITY:
-----------
Time:  O(N) — each char is pushed and popped at most once
Space: O(K) — stack holds at most K distinct chars (26 for lowercase English)

EDGE CASES:
-----------
- Single char → return it
- All same chars → return single char
- Already sorted/lexicographic → no pops needed
============================================================
"""

from collections import Counter


def remove_duplicate_letters(s: str) -> str:
    freq = Counter(s)     # remaining occurrences
    in_stack: set[str] = set()
    stack: list[str] = []

    for ch in s:
        freq[ch] -= 1     # we're using this occurrence now

        if ch in in_stack:
            continue      # already represented in our result

        # Greedy: pop chars that are larger AND appear later
        while stack and stack[-1] > ch and freq[stack[-1]] > 0:
            in_stack.discard(stack.pop())

        stack.append(ch)
        in_stack.add(ch)

    return "".join(stack)


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert remove_duplicate_letters("bcabc") == "abc",    "Test 1"
    assert remove_duplicate_letters("cbacdcbc") == "acdb", "Test 2"
    assert remove_duplicate_letters("a") == "a",          "Edge: single"
    assert remove_duplicate_letters("aaa") == "a",        "Edge: all same"
    assert remove_duplicate_letters("abcd") == "abcd",    "Test 3: already sorted"
    print("All tests passed!")
