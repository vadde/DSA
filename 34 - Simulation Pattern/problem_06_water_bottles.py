"""
============================================================
Problem: Water Bottles
Pattern: Simulation
Difficulty: Easy
Link: https://leetcode.com/problems/water-bottles/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You start with N full water bottles. After drinking them, you have N empty
bottles. You can exchange every `numExchange` empty bottles for 1 full bottle.
How many bottles can you drink in total?

APPROACH:
---------
1. Start: total_drunk = numBottles, empty = numBottles.
2. While empty >= numExchange:
   - new_full = empty // numExchange
   - remaining_empty = empty % numExchange
   - Drink the new_full bottles: total_drunk += new_full
   - empty = remaining_empty + new_full (the new empties)
3. Return total_drunk.

COMPLEXITY:
-----------
Time:  O(log N) — each round reduces bottles significantly.
Space: O(1)

EDGE CASES:
-----------
- numExchange = 1 → infinite loop (but problem guarantees >= 2).
- numBottles < numExchange → just drink what you have.
============================================================
"""


def num_water_bottles(numBottles: int, numExchange: int) -> int:
    total = numBottles
    empty = numBottles

    while empty >= numExchange:
        new_full = empty // numExchange
        empty = empty % numExchange + new_full
        total += new_full

    return total


if __name__ == "__main__":
    assert num_water_bottles(9, 3) == 13, "Test 1"
    assert num_water_bottles(15, 4) == 19, "Test 2"
    assert num_water_bottles(1, 2) == 1, "Test 3: can't exchange"
    assert num_water_bottles(2, 2) == 3, "Test 4: exact exchange"
    print("All tests passed!")
