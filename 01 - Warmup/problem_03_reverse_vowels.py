"""
============================================================
Problem: Reverse Vowels
Pattern: Warmup
Difficulty: Easy
LeetCode: #345
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a word written on a strip of paper: "hello".
You can ONLY swap the vowel letters around (a, e, i, o, u).
"hello" → "holle"  (e and o swap positions)
Use two hands at each end of the strip, move inward, and whenever BOTH hands
are on vowels, swap those letters and move both hands inward.

APPROACH: Two Pointers
---------
1. Convert string to list (strings are immutable in Python).
2. left starts at 0, right starts at len-1.
3. Move left right until it hits a vowel.
4. Move right left until it hits a vowel.
5. Swap s[left] and s[right], then move both inward.
6. Repeat until left >= right.

COMPLEXITY:
-----------
Time:  O(N) — each pointer moves at most N/2 steps
Space: O(N) — list copy of the string

EDGE CASES:
-----------
- Empty string or single character → return as-is
- No vowels → return unchanged
- All vowels → reversed order
============================================================
"""


def reverse_vowels(s: str) -> str:
    vowels = set("aeiouAEIOU")
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        while left < right and chars[left] not in vowels:
            left += 1
        while left < right and chars[right] not in vowels:
            right -= 1
        if left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    return "".join(chars)


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    assert reverse_vowels("hello") == "holle",   "Test 1"
    assert reverse_vowels("leetcode") == "leotcede", "Test 2"
    assert reverse_vowels("aA") == "Aa",         "Test 3: case preserved"
    assert reverse_vowels("") == "",             "Edge: empty"
    assert reverse_vowels("b") == "b",           "Edge: no vowel"
    assert reverse_vowels("aeiou") == "uoiea",   "Edge: all vowels"
    print("All tests passed!")
