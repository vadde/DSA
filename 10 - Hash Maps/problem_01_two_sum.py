"""
============================================================
Problem: Two Sum
Pattern: Hash Maps
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a bunch of numbers: [2, 7, 11, 15] and a target number: 9.
You need to find exactly two numbers that add up to 9, and give their indices.
You COULD look at 2, and then ask every single other number: "Hey, are you 7?"
But if the list is a million numbers long, that takes forever!
Instead, as you walk down the line, you use a magical notebook (Hash Map).
When you look at 2, you write down: "I saw a 2 at index 0."
When you get to 7, you think: "I need a 2 to make 9. Let me check my notebook!"
You look in the notebook, see that you found a 2 earlier at index 0, and boom! 
You instantly know the answer is index 0 and index 1.

APPROACH:
---------
1. Initialize an empty dictionary `seen_map = {}` to store numbers and their indices.
2. Loop through the array using `enumerate` to get both `i` (index) and `num`.
3. Calculate the number you NEED to reach the target: `needed = target - num`.
4. Check if `needed` is already a key in your `seen_map`.
   - If it is, you found your pair! Return `[seen_map[needed], i]`.
5. If it's not, just write down the current number and its index in the map: 
   `seen_map[num] = i`.
6. Return an empty list if no pair is found (though the problem usually guarantees one).

COMPLEXITY:
-----------
Time:  O(N) — We loop through the array exactly once. Looking up things in a Hash Map takes O(1) time.
Space: O(N) — The Hash Map can store up to N numbers in the worst case.

EDGE CASES:
-----------
- Edge case 1: The two numbers are the same (e.g., `[3, 3]`, target `6`). The logic handles this perfectly because we only put the first `3` in the map, and when we see the second `3`, we find the first one!
============================================================
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Finds two numbers such that they add up to a specific target number.
    Returns their indices.
    """
    seen_map: dict[int, int] = {}

    for i, num in enumerate(nums):
        needed = target - num
        
        # O(1) instant lookup in our magical notebook!
        if needed in seen_map:
            return [seen_map[needed], i]
            
        # Store the current number and its index for future reference
        seen_map[num] = i

    return []

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert two_sum([2, 7, 11, 15], 9) == [0, 1], "Test 1 failed"
    assert two_sum([3, 2, 4], 6) == [1, 2], "Test 2 failed"
    
    # 🔲 Edge cases
    assert two_sum([3, 3], 6) == [0, 1], "Edge 1: Same numbers"
    
    # Negative numbers
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4], "Edge 2: Negative numbers"

    print("All tests passed!")
