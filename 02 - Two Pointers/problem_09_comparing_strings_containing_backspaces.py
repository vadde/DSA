"""
============================================================
Problem: Comparing Strings containing Backspaces
Pattern: Two Pointers (Opposite Ends - Backwards)
Difficulty: Medium
Link: https://leetcode.com/problems/backspace-string-compare/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you are typing on a keyboard, and sometimes you make a mistake and hit 
the 'Backspace' key (represented by '#').
If you type "a b c # d", it really means "a b d", because the '#' deleted the 'c'.
You are given two strings representing what someone typed. You need to tell if 
the final typed words are exactly the same.
Instead of actually "typing" out both words and saving them (which takes extra 
memory), we can just read the strings BACKWARDS! If we see a '#', we remember that 
we have to skip the next letter we see. We compare the valid letters from right 
to left.

APPROACH:
---------
1. We use two pointers, `p1` and `p2`, starting at the end of `str1` and `str2`.
2. Create a helper function `get_next_valid_char_index(string, index)`:
   a. This function loops backwards.
   b. If it sees a '#', it adds 1 to a `backspace_count`.
   c. If it sees a normal character, but `backspace_count > 0`, it skips the 
      character and subtracts 1 from `backspace_count`.
   d. If it sees a normal character and `backspace_count == 0`, it returns that index!
3. Inside the main loop (`while p1 >= 0 or p2 >= 0`):
   a. Find the next valid character index for both strings using the helper function.
   b. If both indices are less than 0, we've successfully verified everything. Return True.
   c. If only ONE index is less than 0, the strings are different lengths. Return False.
   d. If the characters at `str1[p1]` and `str2[p2]` are different, return False.
   e. Move both pointers one step backwards (`p1 -= 1`, `p2 -= 1`) and repeat.
4. If the loop finishes, return True.

COMPLEXITY:
-----------
Time:  O(N + M) — Where N and M are the lengths of the two strings. We scan them once.
Space: O(1) — No extra strings are built, we just use integer pointers.

EDGE CASES:
-----------
- Edge case 1: Multiple backspaces in a row ("ab##").
- Edge case 2: Backspacing an empty string ("a#b#c#"). It deletes nothing extra.
============================================================
"""

def get_next_valid_char_index(s: str, index: int) -> int:
    """
    Finds the index of the next valid character moving backwards, 
    accounting for backspaces ('#'). Returns -1 if no valid character exists.
    """
    backspace_count: int = 0
    while index >= 0:
        if s[index] == '#':
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break
        index -= 1
    return index

def compare_strings(str1: str, str2: str) -> bool:
    """
    Compares two strings with backspaces to see if they are identical.
    """
    p1: int = len(str1) - 1
    p2: int = len(str2) - 1

    while p1 >= 0 or p2 >= 0:
        i1 = get_next_valid_char_index(str1, p1)
        i2 = get_next_valid_char_index(str2, p2)

        # If both strings ran out of characters simultaneously
        if i1 < 0 and i2 < 0:
            return True
        
        # If one string ran out but the other didn't
        if i1 < 0 or i2 < 0:
            return False
            
        # If the valid characters don't match
        if str1[i1] != str2[i2]:
            return False

        # Move backwards for the next iteration
        p1 = i1 - 1
        p2 = i2 - 1

    return True

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert compare_strings("xy#z", "xzz#") == True, "Test 1 failed"
    assert compare_strings("xy#z", "xyz#") == False, "Test 2 failed"
    assert compare_strings("xp#", "xyz##") == True, "Test 3 failed"
    
    # 🔲 Edge cases
    assert compare_strings("xywrrmp", "xywrrmu#p") == True, "Edge 1"
    assert compare_strings("a#c", "b") == False, "Edge 2: Complete deletion"
    assert compare_strings("###", "") == True, "Edge 3: Backspacing empty string"

    print("All tests passed!")
