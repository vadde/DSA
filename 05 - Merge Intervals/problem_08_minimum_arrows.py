"""
============================================================
Problem: Minimum Number of Arrows to Burst Balloons
Pattern: Merge Intervals (Greedy End-Time Sort)
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine there are several long balloons taped to a wall. You have a bow and arrow. 
When you shoot an arrow straight up, it pops EVERY balloon it touches on its way up.
You want to pop all the balloons using the FEWEST arrows possible.
To pop the most balloons with a single arrow, you want to wait as long as possible 
before shooting. Specifically, you should shoot at the exact moment the FIRST 
balloon in your line of sight is about to end.
If you shoot there, you pop that balloon, AND you pop any other balloons that have 
already started!
To do this easily, we DON'T sort by the start time. We sort the balloons by their 
END time. Then we shoot an arrow at the end of the first balloon, and skip over 
all other balloons that get popped by that arrow.

APPROACH:
---------
1. Sort the balloons based on their END time, not start time.
2. Initialize `arrows = 1`. We will always need at least one arrow.
3. Set `current_arrow_pos = balloons[0].end`. This is where we shoot our first arrow.
4. Loop through the remaining balloons:
   - If the next balloon starts AFTER our `current_arrow_pos` (`balloon.start > current_arrow_pos`):
     - Oh no! Our arrow missed this one. We need to shoot a NEW arrow!
     - `arrows += 1`
     - Update our new shooting spot to the end of this new balloon: 
       `current_arrow_pos = balloon.end`.
   - If it starts BEFORE or EXACTLY ON the arrow position, it gets popped by the 
     current arrow. We do nothing and keep going!
5. Return the total number of `arrows`.

COMPLEXITY:
-----------
Time:  O(N log N) — Sorting by end time takes O(N log N). The greedy pass takes O(N).
Space: O(N) or O(log N) — Depending on Python's sort overhead.

EDGE CASES:
-----------
- Edge case 1: Empty list. Returns 0 arrows.
- Edge case 2: Balloons exactly touch boundaries (e.g. `[1, 2], [2, 3]`). One arrow at `x=2` pops both!
============================================================
"""

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def find_min_arrows(balloons: list[Interval]) -> int:
    """
    Finds the minimum number of arrows required to burst all balloons.
    """
    if not balloons:
        return 0

    # 1. Sort the balloons by END time (Greedy strategy)
    balloons.sort(key=lambda x: x.end)

    arrows: int = 1
    # 2. Shoot the first arrow at the end of the first balloon
    current_arrow_pos: int = balloons[0].end

    for i in range(1, len(balloons)):
        current_balloon = balloons[i]

        # 3. If the next balloon starts AFTER our arrow, it is completely missed.
        if current_balloon.start > current_arrow_pos:
            # We need a new arrow
            arrows += 1
            # Shoot this new arrow at the end of the current balloon
            current_arrow_pos = current_balloon.end

    return arrows

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    b1 = [Interval(10, 16), Interval(2, 8), Interval(1, 6), Interval(7, 12)]
    # Sorted by end: [1,6], [2,8], [7,12], [10,16]
    # Arrow 1 at 6 pops [1,6], [2,8]
    # Arrow 2 at 12 pops [7,12], [10,16]
    assert find_min_arrows(b1) == 2, "Test 1 failed"

    b2 = [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8)]
    assert find_min_arrows(b2) == 4, "Test 2 failed: 4 distinct balloons"
    
    # 🔲 Edge cases
    b3 = [Interval(1, 2), Interval(2, 3)]
    assert find_min_arrows(b3) == 1, "Edge 1: Touching boundaries pop with 1 arrow"
    
    assert find_min_arrows([]) == 0, "Edge 2: Empty list"

    print("All tests passed!")
