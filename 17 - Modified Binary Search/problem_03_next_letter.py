"""
============================================================
Problem: Next Letter
Pattern: Modified Binary Search
Difficulty: Medium
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1c8a14b308e2f89f24db
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are playing a game with the alphabet.
You have a list of letters: `['a', 'c', 'f', 'h']`.
I give you a key, let's say `'f'`, and you have to find the NEXT letter in the 
list that is STRICTLY greater than `'f'`.
If you look at the list, the letter after `'f'` is `'h'`.
What if I give you `'h'`? There are no letters greater than `'h'`!
In this game, the alphabet is a circle. If you go past the end, you just wrap 
around back to the very first letter!
So the next letter after `'h'` is `'a'`.
This is exactly like the Ceiling problem, with two small differences:
1. We want the STRICTLY greater letter. So if we see the exact letter, we still 
   want to search to its right.
2. If we fall off the edge of the array, we wrap around using the modulo operator `%`!

APPROACH:
---------
1. Initialize `left = 0` and `right = len(letters) - 1`.
2. Loop while `left <= right`:
   - Calculate `mid`.
   - If `key < letters[mid]`, the answer might be `mid`, so we throw away the 
     right half (`right = mid - 1`).
   - If `key >= letters[mid]`, the `mid` letter is too small or exactly equal 
     (and we want STRICTLY greater), so we throw away the left half (`left = mid + 1`).
3. When the loop ends, `left` will point to the smallest letter greater than `key`.
4. To handle wrapping around, just return `letters[left % len(letters)]`.

COMPLEXITY:
-----------
Time:  O(log N) — Standard binary search.
Space: O(1)

EDGE CASES:
-----------
- Edge case 1: Key is greater than or equal to the last letter. `left` will 
  become `len(letters)`. `left % len(letters)` safely wraps it back to `0`.
============================================================
"""

from typing import List

def search_next_letter(letters: List[str], key: str) -> str:
    """
    Returns the smallest letter in the given array strictly greater than the key.
    Wraps around circularly if no such letter exists.
    """
    n = len(letters)
    left = 0
    right = n - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # We only go left if the key is strictly smaller than the middle letter.
        if key < letters[mid]:
            right = mid - 1
        else:
            # If key >= letters[mid], we must keep searching right to find a GREATER letter.
            left = mid + 1
            
    # 'left' will point to the index of the next letter.
    # The modulo handles the circular wrapping beautifully!
    return letters[left % n]

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert search_next_letter(['a', 'c', 'f', 'h'], 'f') == 'h', "Test 1"
    assert search_next_letter(['a', 'c', 'f', 'h'], 'b') == 'c', "Test 2"

    # 🔲 Edge cases (Circular wrap around)
    assert search_next_letter(['a', 'c', 'f', 'h'], 'm') == 'a', "Edge 1: Wrap around"
    assert search_next_letter(['a', 'c', 'f', 'h'], 'h') == 'a', "Edge 2: Exact match on last letter wraps around"

    print("All tests passed!")
