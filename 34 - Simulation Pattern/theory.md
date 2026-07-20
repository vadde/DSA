# Pattern 34: Simulation Pattern

## 👶 Explain Like I'm 5

Imagine playing a board game where the card says:
"Move forward 3 spaces, turn right, and if you land on a red square, go back 1 space."
You don't need a fancy math formula to figure out where you end up. You just
**do exactly what the card says**, step by step, and see where you finish!

In programming, a **Simulation** problem is one where the easiest (or only) way
to solve it is to simply "play the game" according to the rules given in the problem.

---

## 🧩 Core Idea & Pattern Detection

There is no "secret data structure" for Simulation. The challenge is usually about
translating complex, wordy rules into clean, bug-free code.

### Strategies for Simulation:
1. **Direction Vectors**: If moving on a grid, use arrays like `dr = [0, 1, 0, -1]` and `dc = [1, 0, -1, 0]` to represent Right, Down, Left, Up.
2. **State Machines**: Keep track of the current "state" (e.g., heading North, heading East).
3. **Boundary Checks**: Always know your limits (`0 <= r < ROWS`).
4. **Copying States**: If elements update simultaneously (like Game of Life), you must read from the *old* state while writing to a *new* state (or use bit manipulation trickery).

### When to use it:
- Traversing a matrix in a spiral.
- Simulating a robot's movements.
- Grid games (Tic-Tac-Toe, Minesweeper, Game of Life).
- Keywords: "simulate", "robot moves", "turn right", "spiral".

---

## 🔧 Visual Anatomy

Using Direction Vectors for Grid Movement (Right -> Down -> Left -> Up):

```mermaid
flowchart TD
    A["dir = 0 (Right)"] --> B["dr = 0, dc = 1"]
    B --> C["Hit wall! Turn right: dir = (dir + 1) % 4"]
    C --> D["dir = 1 (Down)"]
    D --> E["dr = 1, dc = 0"]
```

---

## ⏱️ Complexity Analysis

| Scenario | Time | Space |
|----------|------|-------|
| Matrix Traversal | O(R * C) | O(1) (excluding output) |
| Robot Instructions | O(N) | O(1) |

---

## ✅ Problems in This Pattern

| # | Problem | Difficulty | LeetCode |
|---|---------|------------|----------|
| 1 | Spiral Matrix | Medium | #54 |
| 2 | Robot Bounded In Circle | Medium | #1041 |
| 3 | Game of Life | Medium | #289 |
| 4 | Design Tic-Tac-Toe | Medium | #348 |
