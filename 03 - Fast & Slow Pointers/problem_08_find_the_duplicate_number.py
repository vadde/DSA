"""
============================================================
Problem: Find the Duplicate Number
Pattern: Fast & Slow Pointers (Advanced: Array as a LinkedList)
Difficulty: Medium
Link: https://leetcode.com/problems/find-the-duplicate-number/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a box of toys numbered 1 to N, and there are exactly N+1 toys in the box. 
Because there are more toys than numbers, at least ONE number must be duplicated!
We can't sort the toys, and we can't bring in a second box to keep track of what 
we've seen. 
But there's a magical trick! We can pretend this box is a LinkedList!
If we are at index 0, the number inside (let's say 3) tells us to go to index 3 next. 
Then the number at index 3 tells us where to go next.
Because multiple spots in the array contain the SAME duplicate number, multiple 
paths will POINT to the same exact index. This creates a CYCLE! 
And the exact spot where the cycle BEGINS is the duplicate number itself! 
So, we just use our Tortoise and Hare trick to find the start of the cycle, exactly 
like we did in the 'Start of LinkedList Cycle' problem.

APPROACH:
---------
1. Initialize `slow = 0` and `fast = 0`.
2. Phase 1 (Detect Cycle):
   - Move `slow` 1 step: `slow = nums[slow]`
   - Move `fast` 2 steps: `fast = nums[nums[fast]]`
   - Loop this until `slow == fast`.
3. Phase 2 (Find Start of Cycle):
   - Leave `fast` where it is.
   - Send a new pointer `slow2` back to the start (`slow2 = 0`).
   - Move BOTH pointers 1 step at a time: `fast = nums[fast]` and `slow2 = nums[slow2]`.
   - The exact number they land on when they meet (`fast == slow2`) is the duplicate number!
4. Return that number.

COMPLEXITY:
-----------
Time:  O(N) — Phase 1 and Phase 2 each take at most O(N) steps. Total is O(N).
Space: O(1) — We just use integer pointers. The array is not modified.

EDGE CASES:
-----------
- Edge case 1: Multiple copies of the same duplicate (e.g., `[2, 2, 2, 2]`). Handled perfectly.
- Edge case 2: The duplicate is at the very beginning or end.
============================================================
"""

def find_duplicate(nums: list[int]) -> int:
    """
    Finds the duplicate number in an array using Floyd's Cycle Detection.
    """
    slow = 0
    fast = 0

    # Phase 1: Detect the cycle
    while True:
        slow = nums[slow]           # 1 step
        fast = nums[nums[fast]]     # 2 steps
        
        if slow == fast:
            break

    # Phase 2: Find the start of the cycle
    slow2 = 0
    while slow != slow2:
        slow = nums[slow]           # 1 step
        slow2 = nums[slow2]         # 1 step

    return slow

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert find_duplicate([1, 3, 4, 2, 2]) == 2, "Test 1 failed"
    assert find_duplicate([3, 1, 3, 4, 2]) == 3, "Test 2 failed"
    
    # 🔲 Edge cases
    assert find_duplicate([2, 2, 2, 2, 2]) == 2, "Edge 1: All identical elements"
    assert find_duplicate([1, 1]) == 1, "Edge 2: Minimum possible array"

    print("All tests passed!")
