# 🚶‍♂️ Walkthrough: Building H2O

## 👶 Explain Like I'm 5
You have an infinite stream of Hydrogen (H) threads and Oxygen (O) threads. They want to pass through a gate to become water (H2O). 
To make water, you need EXACTLY two H's and one O to hold hands and walk through the gate together at the exact same time.

## 🎯 Core Strategy
**Semaphores + Barrier**.

1. **Gatekeepers (Semaphores)**: Limit the waiting area to exactly 2 H's and 1 O.
   - `sem_h = Semaphore(2)` (Only 2 H's can enter the waiting room).
   - `sem_o = Semaphore(1)` (Only 1 O can enter the waiting room).
2. **Holding Hands (Barrier)**: A barrier makes threads wait until a specific number of them have arrived.
   - `barrier = Barrier(3)` (Wait until exactly 3 threads are here).
3. **Execution**:
   - An H arrives: takes an H-token. Waits at the barrier. Once the barrier breaks (3 threads arrive), it prints "H", then puts the H-token back!
   - An O arrives: takes the O-token. Waits at the barrier. Once the barrier breaks, prints "O", puts O-token back!

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**Input**: Stream of `O, O, H, H, H, H` (in random order)
Let's say they arrive in order: `O, H, O, H, H, H`

| Event | `sem_h` (cap 2) | `sem_o` (cap 1) | Barrier (needs 3) | Action |
|---|---|---|---|---|
| `O` arrives | 2 | 0 | 1 waiting | Waits at barrier |
| `H` arrives | 1 | 0 | 2 waiting | Waits at barrier |
| `O` arrives | 1 | **0 (blocked)** | - | Too many O's! This one waits outside. |
| `H` arrives | 0 | 0 | **3 reached!** | **BARRIER BREAKS** |
| (Barrier breaks) | 0 -> 2 | 0 -> 1 | 0 waiting | 1 O and 2 H's print, then release sems. |
| (Tokens returned)| 2 | 1 | 0 waiting | The blocked `O` from earlier now gets in! |

The first 3 that pass print `HHO` (or `HOH`, etc.). Then the remaining `OHH` form the next molecule. ✅

## 📊 Visual Diagram

```mermaid
flowchart TD
    A["H-Thread"] -->|acquire(sem_h)| C["Waiting Room"]
    B["O-Thread"] -->|acquire(sem_o)| C
    
    C --> D{"Barrier(3)\nAre there 2 H's and 1 O?"}
    D -->|NO| C
    D -->|YES| E["All 3 cross at once!"]
    
    E --> F["Print H, H, O"]
    F --> G["release(sem_h) x2\nrelease(sem_o) x1"]
    
    style D fill:#ffcdd2,color:#000
    style E fill:#c8e6c9,color:#000
```

## 🛑 Complexity
- **Time:** $O(1)$ per thread.
- **Space:** $O(1)$.
