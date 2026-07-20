"""
============================================================
Problem: Number of Provinces (Connected Components)
Pattern: Graphs
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-provinces/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you have a map of cities. 
Some cities have roads connecting them. If City A is connected to City B, and 
City B is connected to City C, they all belong to the same "Province".
But what if City D and City E are connected to each other, but have NO roads 
leading to A, B, or C? Then D and E form a SECOND Province.
Your job is to count how many completely separate Provinces there are.
How do we do this? We just pick a city, say City A, and start exploring (DFS).
We put a red "X" (visited) on City A, then we walk down the road to City B and 
put an "X" on it, then to City C and put an "X" on it.
Once we hit a dead end, we know we have fully explored Province 1!
Then we look at our list of all cities. 
"Is City B visited?" Yes. "City C?" Yes. 
"What about City D?" No! City D doesn't have an "X". 
That means City D is in a brand new Province!
So we increment our Province count, start exploring from City D, and repeat 
until every single city has an "X".

APPROACH:
---------
1. `n` is the number of cities.
2. Initialize `visited = set()` and `provinces = 0`.
3. Define a recursive helper `dfs(city)`:
   - Loop through all possible `neighbors` (from 0 to `n-1`).
   - If `isConnected[city][neighbor] == 1` AND the neighbor is NOT visited:
     - Mark it as visited: `visited.add(neighbor)`.
     - Recursively call `dfs(neighbor)`.
4. Loop through every `city` from 0 to `n-1`. This outer loop ensures we don't 
   miss any disconnected components!
   - If `city` is NOT in `visited`:
     - We found a new, unexplored province! `provinces += 1`.
     - Mark the city as visited: `visited.add(city)`.
     - Call `dfs(city)` to explore and mark all cities connected to it.
5. Return `provinces`.

COMPLEXITY:
-----------
Time:  O(N^2) — The matrix is N x N. We essentially check every cell in the matrix once to find connections.
Space: O(N) — The `visited` set stores up to N cities, and the DFS recursion stack can go N deep.

EDGE CASES:
-----------
- Edge case 1: No connections at all (identity matrix). Returns `N` provinces.
- Edge case 2: All cities connected to each other. Returns `1` province.
============================================================
"""

from typing import List

def find_circle_num(is_connected: List[List[int]]) -> int:
    """
    Finds the total number of provinces (connected components) in a graph.
    """
    if not is_connected:
        return 0

    n = len(is_connected)
    visited = set()
    provinces = 0

    def dfs(city: int):
        # Check all possible neighbors for this city
        for neighbor in range(n):
            # If there is a road AND we haven't visited it yet
            if is_connected[city][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    # 4. Outer loop to catch all disconnected components
    for city in range(n):
        if city not in visited:
            # We found a city that hasn't been explored. It's a new province!
            provinces += 1
            visited.add(city)
            
            # Send our DFS explorer out to mark all connected cities
            dfs(city)

    return provinces

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    # 1 - 2   3 (Disconnected)
    matrix1 = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    assert find_circle_num(matrix1) == 2, f"Test 1 failed: {find_circle_num(matrix1)}"

    # 1   2   3 (All disconnected)
    matrix2 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    assert find_circle_num(matrix2) == 3, f"Test 2 failed"
    
    # 1 - 2 - 3 (All connected)
    matrix3 = [
        [1, 1, 0],
        [1, 1, 1],
        [0, 1, 1]
    ]
    assert find_circle_num(matrix3) == 1, f"Test 3 failed"

    # 🔲 Edge cases
    assert find_circle_num([]) == 0, "Edge 1: Empty graph"
    assert find_circle_num([[1]]) == 1, "Edge 2: Single city"

    print("All tests passed!")
