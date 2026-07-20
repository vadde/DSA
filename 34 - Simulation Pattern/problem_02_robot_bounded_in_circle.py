"""
============================================================
Problem: Robot Bounded In Circle
Pattern: Simulation + State Tracking
Difficulty: Medium
LeetCode: #1041
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a robot at (0,0) facing North. It receives instructions:
- 'G': Go straight 1 unit
- 'L': Turn left 90 degrees
- 'R': Turn right 90 degrees
After it finishes the instructions ONE TIME, will it eventually get trapped
in a circle if it repeats the instructions forever?

APPROACH: Simulating One Cycle
---------
We simulate exactly ONE execution of the instructions.
After one cycle, the robot will be trapped in a circle IF AND ONLY IF:
1. It returns to the starting point (0, 0)
OR
2. It is NO LONGER facing North.
(If it faces East/West/South, repeating the instructions will eventually
bring it back to (0,0) after 4, 4, or 2 cycles respectively).

COMPLEXITY:
-----------
Time:  O(N) — One pass through instructions.
Space: O(1)
============================================================
"""


def is_robot_bounded(instructions: str) -> bool:
    # Directions: North, East, South, West
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    x, y = 0, 0
    facing = 0  # 0: North, 1: East, 2: South, 3: West
    
    for instruction in instructions:
        if instruction == 'G':
            x += dirs[facing][0]
            y += dirs[facing][1]
        elif instruction == 'L':
            facing = (facing - 1) % 4
        elif instruction == 'R':
            facing = (facing + 1) % 4
            
    # Trapped if at origin OR not facing North
    return (x == 0 and y == 0) or facing != 0


if __name__ == "__main__":
    assert is_robot_bounded("GGLLGG") is True,  "Test 1: Returns to start"
    assert is_robot_bounded("GG") is False,     "Test 2: Keeps going North forever"
    assert is_robot_bounded("GL") is True,      "Test 3: Faces West, will form a square"
    print("All tests passed!")
