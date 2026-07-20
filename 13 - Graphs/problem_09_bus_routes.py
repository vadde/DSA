"""
============================================================
Problem: Bus Routes
Pattern: Graphs (BFS on Routes, not Stops)
Difficulty: Hard
Link: https://leetcode.com/problems/bus-routes/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You're in a city with bus routes. Each route visits certain stops. You start at
stop `source` and want to reach stop `target`. Each time you get on a bus, you
can ride it to any of its stops for free, but switching buses counts as 1 more bus.
What is the MINIMUM number of buses you need to take?

KEY INSIGHT: Don't BFS on individual stops — that's too slow!
Instead, BFS on BUS ROUTES. Two routes are "neighbors" if they share a stop.
We want the shortest path from any route containing `source` to any route
containing `target`.

APPROACH:
---------
1. Build a mapping: stop -> list of route indices that visit this stop.
2. BFS on routes. Start by enqueueing all routes that contain `source`.
3. For each route in the queue, check all its stops. If any stop is `target`, done!
4. For each stop, enqueue all other routes that share that stop (neighbors).
5. Mark routes as visited to avoid re-processing.

COMPLEXITY:
-----------
Time:  O(N * M) where N = number of routes, M = avg stops per route.
Space: O(N * M) for the stop-to-routes mapping.

EDGE CASES:
-----------
- source == target → 0 buses needed.
- source and target on the same route → 1 bus.
- No route connects them → return -1.
============================================================
"""

from typing import List
from collections import defaultdict, deque


def num_buses_to_destination(routes: List[List[int]], source: int, target: int) -> int:
    if source == target:
        return 0

    # Map each stop to the routes that visit it
    stop_to_routes = defaultdict(set)
    for route_idx, stops in enumerate(routes):
        for stop in stops:
            stop_to_routes[stop].add(route_idx)

    # BFS on routes
    visited_routes = set()
    visited_stops = {source}
    queue = deque()

    # Seed: enqueue all routes that contain the source stop
    for route_idx in stop_to_routes[source]:
        queue.append((route_idx, 1))
        visited_routes.add(route_idx)

    while queue:
        route_idx, buses = queue.popleft()

        for stop in routes[route_idx]:
            if stop == target:
                return buses

            if stop not in visited_stops:
                visited_stops.add(stop)
                for next_route in stop_to_routes[stop]:
                    if next_route not in visited_routes:
                        visited_routes.add(next_route)
                        queue.append((next_route, buses + 1))

    return -1


if __name__ == "__main__":
    assert num_buses_to_destination([[1,2,7],[3,6,7]], 1, 6) == 2, "Test 1"
    assert num_buses_to_destination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12) == -1, "Test 2"
    assert num_buses_to_destination([[1,2,3]], 1, 3) == 1, "Test 3: same route"
    assert num_buses_to_destination([[1,2]], 1, 1) == 0, "Test 4: same stop"
    print("All tests passed!")
