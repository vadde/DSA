"""
============================================================
Problem: Ransom Note
Pattern: Hash Maps
Difficulty: Easy
Link: https://leetcode.com/problems/ransom-note/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you want to write a secret message (a ransom note) by cutting out letters 
from a magazine.
If your note needs the letter 'A' two times, but the magazine only has one 'A', 
you can't write your note! 
You can only use each letter from the magazine exactly as many times as it appears.
So, what's the plan?
First, you read the whole magazine and write down exactly how many of each letter 
you have. (e.g., A: 5, B: 2, C: 0...)
Then, you look at your ransom note letter by letter.
For every letter, you check your list. Do I have this letter? 
If yes, cross one out (subtract 1 from the count). 
If no (or if the count is 0), then it's impossible to write the note!

APPROACH:
---------
1. Initialize an empty dictionary `magazine_freq = {}`.
2. Loop through every character in the `magazine`.
   - Add 1 to its count in `magazine_freq`.
3. Loop through every character in the `ransomNote`.
   - If the character exists in `magazine_freq` AND its count is > 0:
     - Subtract 1 from its count.
   - Else (the character doesn't exist or we ran out of them):
     - Return `False`.
4. If we made it through the whole ransom note, it means we had enough letters! 
   Return `True`.

COMPLEXITY:
-----------
Time:  O(N + M) — Where N is length of the note, M is length of the magazine.
Space: O(1) — The Hash Map stores at most 26 lowercase English letters.

EDGE CASES:
-----------
- Edge case 1: Note is longer than the magazine. Impossible! We can return `False` immediately.
- Edge case 2: Empty note `""`. Returns `True` (needs 0 letters).
============================================================
"""

def can_construct(ransom_note: str, magazine: str) -> bool:
    """
    Returns True if ransom_note can be constructed from magazine, False otherwise.
    """
    # Quick optimization: If the note is longer, it's impossible
    if len(ransom_note) > len(magazine):
        return False

    magazine_freq: dict[str, int] = {}

    # 1. Count all letters available in the magazine
    for char in magazine:
        magazine_freq[char] = magazine_freq.get(char, 0) + 1

    # 2. Try to construct the ransom note
    for char in ransom_note:
        if magazine_freq.get(char, 0) > 0:
            # Use one letter
            magazine_freq[char] -= 1
        else:
            # We don't have this letter (or we ran out of it)
            return False

    return True

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert can_construct("a", "b") == False, "Test 1 failed"
    assert can_construct("aa", "ab") == False, "Test 2 failed"
    assert can_construct("aa", "aab") == True, "Test 3 failed"
    
    # 🔲 Edge cases
    assert can_construct("", "abc") == True, "Edge 1: Empty note"
    assert can_construct("abc", "") == False, "Edge 2: Empty magazine"
    assert can_construct("longer", "short") == False, "Edge 3: Note longer than magazine"

    print("All tests passed!")
