"""
============================================================
Problem: 'K' Closest Points to the Origin
Pattern: Top K Elements
Difficulty: Easy
Link: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1cb2a00cc465d6c8276f
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a map of a city, and you are standing at the very center (the origin).
There are many coffee shops scattered around the city (these are the "points").
You want to find the 3 coffee shops that are CLOSEST to you.
To find the closest ones, we want to kick out the ones that are FARTHEST away!
So, we use a Max-Heap again!
The Max-Heap will keep the FARTHEST of the K coffee shops right at the front door.
When we find a new coffee shop, we ask: "Is this new shop CLOSER than the 
farthest shop in our VIP club?"
If yes, we kick the far one out and let the close one in!
How do we calculate distance? Math says it's `sqrt(x^2 + y^2)`.
But since we are just comparing them, we don't even need the `sqrt`! 
`x^2 + y^2` works perfectly fine and is faster.

APPROACH:
---------
1. Create a `distance(point)` helper function that returns `x^2 + y^2`.
2. Initialize `max_heap = []`.
3. Loop through the points. For the first K points, push them into the heap.
   - We must push a tuple: `(-distance, i, point)`.
   - Python's `heapq` sorts tuples by their first element. If there's a tie, 
     it checks the second. If we don't put the index `i`, it will try to compare 
     the `point` lists, which crashes Python!
4. For the remaining points, calculate distance. 
   - The largest distance in the heap is at `max_heap[0][0]` (but negated!).
   - So the positive value is `-max_heap[0][0]`.
   - If `new_distance < -max_heap[0][0]`, pop and push!
5. Return the points from the heap.

COMPLEXITY:
-----------
Time:  O(N * log K)
Space: O(K)

EDGE CASES:
-----------
- Edge case 1: K is larger than the number of points. Just return all points.
============================================================
"""

import heapq
from typing import List

def find_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Returns the K closest points to the origin (0, 0).
    """
    def dist_squared(point):
        return point[0] * point[0] + point[1] * point[1]
        
    max_heap = []
    
    # 1. Put the first 'K' points in the max heap
    for i in range(min(k, len(points))):
        # We push (-distance, index, point)
        heapq.heappush(max_heap, (-dist_squared(points[i]), i, points[i]))
        
    # 2. Go through the remaining points
    for i in range(k, len(points)):
        curr_dist = dist_squared(points[i])
        
        # 3. If the current point is CLOSER than the FARTHEST point in our club
        # -max_heap[0][0] gets the positive distance of the farthest point in the heap
        if curr_dist < -max_heap[0][0]:
            heapq.heappushpop(max_heap, (-curr_dist, i, points[i]))
            
    # Extract just the points from the heap tuples to return
    result = []
    for item in max_heap:
        result.append(item[2])
        
    return result

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    points1 = [[1, 2], [1, 3]]
    # Distances are 5 and 10. Closest 1 is [1, 2]
    assert find_closest_points(points1, 1) == [[1, 2]], "Test 1"
    
    points2 = [[1, 3], [3, 4], [2, -1]]
    # Distances are 10, 25, 5. Closest 2 are [1, 3] and [2, -1]
    result2 = find_closest_points(points2, 2)
    # The order doesn't matter, so sort them for the assert
    assert sorted(result2) == [[1, 3], [2, -1]], f"Test 2 failed. Got {result2}"

    # 🔲 Edge cases
    assert sorted(find_closest_points([[1,1], [2,2]], 5)) == [[1,1], [2,2]], "Edge 1: K > N"

    print("All tests passed!")
