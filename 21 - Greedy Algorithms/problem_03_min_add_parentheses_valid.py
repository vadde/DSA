"""
============================================================
Problem: Minimum Add to Make Parentheses Valid
Pattern: Greedy Algorithms
Difficulty: Medium
LeetCode: #921
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a string of '(' and ')'. Some are unmatched.
Find the MINIMUM number of parentheses to ADD to make it valid.
Think of it like a bank account:
  - '(' deposits $1 (opens a bracket, needs a future close).
  - ')' withdraws $1 (closes an open bracket).
  - If your balance goes negative, you need to ADD a '(' immediately → count it!
  - At the end, any remaining positive balance = unmatched '(' needing ')'.

APPROACH:
---------
1. Track `open` = number of unmatched '(' so far.
2. Track `additions` = number of extra ')' we needed to add.
3. For each char:
   - '(': open += 1
   - ')': if open > 0, close one open: open -= 1
           else: we need to add a '(' to match this ')': additions += 1
4. Return additions + open  (open unmatched '(' each need a ')')

COMPLEXITY:
-----------
Time:  O(N)
Space: O(1)

EDGE CASES:
-----------
- Already valid → 0
- All '(' → N (need N closing brackets)
- All ')' → N (need N opening brackets)
============================================================
"""


def min_add_to_make_valid(s: str) -> int:
    open_count = 0   # unmatched '(' count
    additions = 0    # unmatched ')' that forced us to add '('

    for ch in s:
        if ch == '(':
            open_count += 1
        else:  # ch == ')'
            if open_count > 0:
                open_count -= 1
            else:
                additions += 1   # need to insert '(' before this ')'

    return additions + open_count   # remaining '(' each need a ')'


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert min_add_to_make_valid("())") == 1,        "Test 1"
    assert min_add_to_make_valid("(((") == 3,        "Test 2"
    assert min_add_to_make_valid("()") == 0,         "Test 3: already valid"
    assert min_add_to_make_valid("()))((") == 4,     "Test 4"
    assert min_add_to_make_valid("") == 0,           "Edge: empty"
    assert min_add_to_make_valid("((()))") == 0,     "Edge: nested valid"
    print("All tests passed!")
