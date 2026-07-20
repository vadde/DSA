"""
============================================================
Problem: Building H2O
Pattern: Multi-threaded / Concurrency
Difficulty: Medium
LeetCode: #1117
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have an infinite stream of Hydrogen (H) and Oxygen (O) threads.
Water is H2O. You must group them into 2 H's and 1 O before they can proceed.
If an O arrives, it waits for two H's. If an H arrives, it waits for another H and an O.

APPROACH: Semaphores & Barriers
---------
Use a Semaphore for H (capacity 2) and a Semaphore for O (capacity 1).
Use a threading.Barrier(3) to wait for exactly 3 threads (2H + 1O) to group up.
Once grouped, they cross the barrier together!
Then release the semaphores to let the next batch in.

COMPLEXITY: O(1) space, time depends on thread scheduling.
============================================================
"""

from typing import Callable
from threading import Semaphore, Barrier, Thread
import time
import random


class H2O:
    def __init__(self):
        # Allow at most 2 Hydrogen threads and 1 Oxygen thread at a time
        self.sem_h = Semaphore(2)
        self.sem_o = Semaphore(1)
        # Wait until 3 threads (2H, 1O) are ready to bond
        self.barrier = Barrier(3)

    def hydrogen(self, releaseHydrogen: Callable[[], None]) -> None:
        self.sem_h.acquire()
        self.barrier.wait()  # Wait for the other H and the O
        releaseHydrogen()
        self.sem_h.release()

    def oxygen(self, releaseOxygen: Callable[[], None]) -> None:
        self.sem_o.acquire()
        self.barrier.wait()  # Wait for the two H's
        releaseOxygen()
        self.sem_o.release()


if __name__ == "__main__":
    output = []
    
    def releaseHydrogen(): output.append("H")
    def releaseOxygen(): output.append("O")

    h2o = H2O()
    
    # Input: "OOHHHH" (2 O's, 4 H's) -> should form 2 water molecules
    threads = []
    for char in "OOHHHH":
        if char == 'H':
            threads.append(Thread(target=h2o.hydrogen, args=(releaseHydrogen,)))
        else:
            threads.append(Thread(target=h2o.oxygen, args=(releaseOxygen,)))
            
    # Start randomly to simulate real conditions
    random.shuffle(threads)
    for t in threads:
        t.start()
        
    for t in threads:
        t.join()

    # The exact output string might vary (HHO, HOH, OHH), but every 3 chars MUST have 2 H and 1 O
    res = "".join(output)
    assert len(res) == 6
    assert res[:3].count('H') == 2 and res[:3].count('O') == 1
    assert res[3:6].count('H') == 2 and res[3:6].count('O') == 1
    
    print(f"Produced: {res}")
    print("All tests passed!")
