"""
============================================================
Problem: Daily Temperatures
Pattern: Monotonic Stack
Difficulty: Medium
Link: https://leetcode.com/problems/daily-temperatures/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a list of temperatures for the next few days.
For every single day, you want to know: "How many days do I have to wait until 
it is WARMER than today?"
If it never gets warmer, you just say "0 days".
This is exactly the "Next Greater Element" problem, but instead of writing down 
the *temperature* of the warmer day, you want to write down the *distance* 
between today and the warmer day.
Because we store the INDEX of the day in our Monotonic Stack, calculating the 
distance is super easy! It's just `warmer_day_index - today_index`.

APPROACH:
---------
1. Initialize an array `result` of the same length as `temperatures`, filled with `0`.
2. Initialize an empty `stack` (to store the indices of the days waiting for warmer weather).
3. Loop `for i, temp in enumerate(temperatures)`:
   - While the stack is not empty AND `temp` is GREATER than the temperature 
     of the day at the top of the stack (`temperatures[stack[-1]]`):
     - A warmer day arrived! 
     - Pop the index from the stack: `popped_day = stack.pop()`
     - Calculate how long that day waited: `wait_time = i - popped_day`
     - Update the result for that day: `result[popped_day] = wait_time`
   - Push the current day's index into the waiting room: `stack.append(i)`
4. Return `result`.

COMPLEXITY:
-----------
Time:  O(N) — Every day is pushed to the stack once and popped at most once.
Space: O(N) — The stack can store all days if the temperature is constantly dropping.

EDGE CASES:
-----------
- Edge case 1: Temperatures strictly decrease `[50, 40, 30]`. Result is `[0, 0, 0]`.
- Edge case 2: Temperatures strictly increase `[30, 40, 50]`. Result is `[1, 1, 0]`.
============================================================
"""

def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    Given an array of daily temperatures, returns an array of wait days for a warmer temperature.
    """
    if not temperatures:
        return []

    result: list[int] = [0] * len(temperatures)
    stack: list[int] = []  # Stores indices of the days

    for i, temp in enumerate(temperatures):
        # The 'rule' of our Monotonic Stack is perfectly decreasing temperatures.
        # If today is warmer, the rule is broken! Pop the colder days.
        while stack and temp > temperatures[stack[-1]]:
            popped_day = stack.pop()
            # Calculate how many days they had to wait
            result[popped_day] = i - popped_day
            
        # Push today into the waiting room
        stack.append(i)

    return result

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    temps1 = [73, 74, 75, 71, 69, 72, 76, 73]
    # Expected: [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures(temps1) == [1, 1, 4, 2, 1, 1, 0, 0], f"Test 1 failed: {daily_temperatures(temps1)}"

    temps2 = [30, 40, 50, 60]
    assert daily_temperatures(temps2) == [1, 1, 1, 0], "Test 2 failed"
    
    # 🔲 Edge cases
    temps3 = [90, 80, 70, 60]
    assert daily_temperatures(temps3) == [0, 0, 0, 0], "Edge 1: Decreasing temperatures"
    
    temps4 = [30]
    assert daily_temperatures(temps4) == [0], "Edge 2: Single temperature"

    print("All tests passed!")
