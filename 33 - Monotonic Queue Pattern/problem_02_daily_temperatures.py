"""
============================================================
Problem: Daily Temperatures
Pattern: Monotonic Stack
Difficulty: Medium
LeetCode: #739
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Given an array of daily temperatures, how many days do you have to wait until
a warmer temperature? If there is no future warmer day, put 0.
[73, 74, 75, 71, 69, 72, 76, 73] -> [1, 1, 4, 2, 1, 1, 0, 0]

APPROACH: Monotonic Decreasing Stack (store INDICES)
---------
Exactly like "Next Greater Element", but we need the DISTANCE in days, not the
temperature itself. So, we store the INDICES in the stack instead of the values.
When a warmer day comes along, we pop the index from the stack, and the answer
for that popped day is `current_index - popped_index`.

COMPLEXITY:
-----------
Time:  O(N)
Space: O(N)
============================================================
"""

from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    answer = [0] * n
    stack: List[int] = []  # Stores indices
    
    for i, temp in enumerate(temperatures):
        # Found a warmer day for the indices in the stack!
        while stack and temp > temperatures[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
            
        stack.append(i)
        
    return answer


if __name__ == "__main__":
    assert daily_temperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0], "Test 1"
    assert daily_temperatures([30,40,50,60]) == [1,1,1,0],                     "Test 2"
    assert daily_temperatures([30,20,10]) == [0,0,0],                          "Test 3"
    print("All tests passed!")
