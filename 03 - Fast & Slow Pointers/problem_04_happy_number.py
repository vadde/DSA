"""
============================================================
Problem: Happy Number
Pattern: Fast & Slow Pointers (Virtual Sequence)
Difficulty: Medium
Link: https://leetcode.com/problems/happy-number/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
A "Happy Number" is a number that eventually turns into 1 if you keep squaring 
its digits and adding them together. 
For example, 23 -> 2^2 + 3^2 = 4 + 9 = 13. Then 1^2 + 3^2 = 10. Then 1^2 + 0^2 = 1. 
Yay, 23 is a Happy Number!

But what if a number is NOT happy? It won't just keep growing forever. Math proves 
that it will eventually get stuck in a LOOP (a cycle)!
Since we are dealing with a sequence of numbers where we want to know if it ends 
in a '1' or gets stuck in a loop, this is EXACTLY like our Tortoise and Hare problem! 
The only difference is we don't have a real LinkedList; we just GENERATE the "next node" 
by doing the math!

APPROACH:
---------
1. Create a helper function `find_square_sum(num)` to do the math and get the "next" number.
2. Initialize `slow = num` and `fast = num`.
3. Loop infinitely (`while True`):
   - `slow = find_square_sum(slow)` (Takes 1 step)
   - `fast = find_square_sum(find_square_sum(fast))` (Takes 2 steps)
   - If `slow == fast`, they caught each other in a loop! Break out of the loop.
4. After breaking out, check if `slow == 1`. If it is, the loop was just 1 -> 1 -> 1, 
   so the number is Happy! Return True. Otherwise, return False.

COMPLEXITY:
-----------
Time:  O(log N) — The sum of squares of digits of a number N is bounded, and the cycle length is small.
Space: O(1) — We don't store the history of numbers like a HashSet would. Just pointers!

EDGE CASES:
-----------
- Edge case 1: Number is already 1. Handled correctly.
- Edge case 2: Single digit unhappy numbers (e.g., 2). Quickly falls into a cycle.
============================================================
"""

def find_square_sum(num: int) -> int:
    """
    Helper function to calculate the sum of the squares of the digits of a number.
    This acts as our "node.next".
    """
    _sum: int = 0
    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum

def find_happy_number(num: int) -> bool:
    """
    Determines if a number is a "Happy Number" using Floyd's Cycle Detection.
    """
    slow: int = num
    fast: int = num

    while True:
        slow = find_square_sum(slow)
        fast = find_square_sum(find_square_sum(fast))
        
        # If they meet, there is a cycle
        if slow == fast:
            break

    # If the cycle is at the number 1, it's a happy number!
    return slow == 1

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert find_happy_number(23) == True, "Test 1 failed: 23 should be happy"
    assert find_happy_number(12) == False, "Test 2 failed: 12 should be unhappy"
    
    # 🔲 Edge cases
    assert find_happy_number(1) == True, "Edge 1: 1 is happy"
    assert find_happy_number(2) == False, "Edge 2: 2 is unhappy (falls into 4->16->... cycle)"

    print("All tests passed!")
