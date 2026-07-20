"""
============================================================
Problem: Encode and Decode Strings
Pattern: Serialize and Deserialize (Length Prefixing)
Difficulty: Medium
LeetCode: #271 (Premium)
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a list of strings: ["Hello", "World"]. You need to combine them into a single string.
If you just use a comma: "Hello,World", what if a string has a comma in it? ["Hello, World", ""] -> "Hello, World,". How do you split it?
You can't just pick a separator character because the strings might contain that character!

APPROACH: Length Prefixing
---------
Write the LENGTH of the string, then a special delimiter like `#`, then the string itself.
["Hello", "World"] -> "5#Hello5#World"
When decoding, read the number until you see `#`. The number tells you exactly how many
characters to grab next. So even if the string contains `#` or numbers, it's safe!

COMPLEXITY:
-----------
Time:  O(N) where N is total number of characters.
Space: O(N)
============================================================
"""

from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Find the # delimiter
            while s[j] != '#':
                j += 1
            
            # The number before # is the length
            length = int(s[i:j])
            
            # The string starts after # and goes for `length` characters
            string_start = j + 1
            string_end = string_start + length
            
            res.append(s[string_start:string_end])
            
            # Move `i` to the start of the next encoded string
            i = string_end
            
        return res


if __name__ == "__main__":
    codec = Codec()
    
    # Test 1: Normal strings
    strs1 = ["Hello", "World"]
    assert codec.decode(codec.encode(strs1)) == strs1, "Test 1"
    
    # Test 2: Strings with special characters and numbers
    strs2 = ["5#Hello", "3#", "#", ""]
    assert codec.decode(codec.encode(strs2)) == strs2, "Test 2"
    
    # Test 3: Empty list
    assert codec.decode(codec.encode([])) == [], "Test 3"
    
    print("All tests passed!")
