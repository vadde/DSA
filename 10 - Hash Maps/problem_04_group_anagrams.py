"""
============================================================
Problem: Group Anagrams
Pattern: Hash Maps
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a bucket of words: ["eat", "tea", "tan", "ate", "nat", "bat"].
An anagram is a word made by mixing up the letters of another word. "eat", "tea", 
and "ate" all have exactly one 'e', one 'a', and one 't'.
You want to group all the mixed-up words together!
How do you know if two words are anagrams of each other?
If you put their letters in alphabetical order, they will look EXACTLY the same!
"eat" sorted is "aet".
"tea" sorted is "aet".
"ate" sorted is "aet".
We can use a Hash Map where the "Key" is the sorted word ("aet"), and the "Value" 
is a list of all the original words that sort to that key: `["eat", "tea", "ate"]`.

APPROACH:
---------
1. Initialize an empty dictionary `groups = {}` (Key: string, Value: list of strings).
2. Loop through every `word` in the input list.
3. Sort the characters in the word and join them back into a single string.
   - `sorted_word = "".join(sorted(word))`
4. If `sorted_word` is not already a key in `groups`, add it with an empty list.
   - `if sorted_word not in groups: groups[sorted_word] = []`
5. Append the original `word` to that list.
   - `groups[sorted_word].append(word)`
6. Finally, return all the values from the dictionary as a list of lists.
   - `return list(groups.values())`

COMPLEXITY:
-----------
Time:  O(N * K log K) — Where N is the number of words, and K is the maximum length of a word. Sorting each word takes K log K time.
Space: O(N * K) — The Hash Map stores all the words.

EDGE CASES:
-----------
- Edge case 1: Empty list of strings. Returns `[]`.
- Edge case 2: List with empty strings `[""]`. Returns `[[""]]`.
============================================================
"""

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Groups an array of strings into anagrams.
    """
    groups: dict[str, list[str]] = {}

    for word in strs:
        # Sort the word to use as the dictionary key
        sorted_word = "".join(sorted(word))
        
        # If we haven't seen this sorted word before, create a new list
        if sorted_word not in groups:
            groups[sorted_word] = []
            
        # Add the original word to the correct group
        groups[sorted_word].append(word)

    # Return just the grouped lists
    return list(groups.values())

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    def compare_groups(g1, g2):
        # Helper to compare lists of lists irrespective of order
        return sorted([sorted(g) for g in g1]) == sorted([sorted(g) for g in g2])

    # ✅ Normal cases
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected1 = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    res1 = group_anagrams(strs1)
    assert compare_groups(res1, expected1), f"Test 1 failed: {res1}"
    
    # 🔲 Edge cases
    assert group_anagrams([""]) == [[""]], "Edge 1: Empty string"
    assert group_anagrams(["a"]) == [["a"]], "Edge 2: Single character"
    
    # Words with identical characters but different frequencies
    strs2 = ["aab", "aba", "baa", "abb", "bab", "bba"]
    expected2 = [["aab", "aba", "baa"], ["abb", "bab", "bba"]]
    res2 = group_anagrams(strs2)
    assert compare_groups(res2, expected2), "Edge 3: Similar but different counts"

    print("All tests passed!")
