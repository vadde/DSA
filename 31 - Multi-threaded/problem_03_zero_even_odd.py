"""
============================================================
Problem: Print Zero Even Odd
Pattern: Multi-threaded
Difficulty: Medium
LeetCode: #1116
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Three threads: Zero, Even, Odd.
Output should be: "01020304..."
Pattern: Zero -> Odd -> Zero -> Even -> Zero -> Odd -> ...

APPROACH: Semaphores
---------
Use three semaphores.
- `zero_sem`: starts at 1
- `odd_sem`: starts at 0
- `even_sem`: starts at 0

Zero prints '0', then decides whether to unlock `odd` or `even`.
Odd prints its number, unlocks `zero`.
Even prints its number, unlocks `zero`.

COMPLEXITY: O(N)
============================================================
"""

from typing import Callable
from threading import Semaphore, Thread


class ZeroEvenOdd:
    def __init__(self, n: int):
        self.n = n
        self.zero_sem = Semaphore(1)
        self.odd_sem = Semaphore(0)
        self.even_sem = Semaphore(0)

    def zero(self, printNumber: Callable[[int], None]) -> None:
        for i in range(1, self.n + 1):
            self.zero_sem.acquire()
            printNumber(0)
            if i % 2 == 1:
                self.odd_sem.release()
            else:
                self.even_sem.release()

    def even(self, printNumber: Callable[[int], None]) -> None:
        for i in range(2, self.n + 1, 2):
            self.even_sem.acquire()
            printNumber(i)
            self.zero_sem.release()

    def odd(self, printNumber: Callable[[int], None]) -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_sem.acquire()
            printNumber(i)
            self.zero_sem.release()


if __name__ == "__main__":
    output = []
    def printNumber(x: int): output.append(str(x))

    zeo = ZeroEvenOdd(5)
    t1 = Thread(target=zeo.zero, args=(printNumber,))
    t2 = Thread(target=zeo.even, args=(printNumber,))
    t3 = Thread(target=zeo.odd, args=(printNumber,))

    t3.start(); t2.start(); t1.start()
    t1.join(); t2.join(); t3.join()

    assert "".join(output) == "0102030405", f"Failed: {output}"
    print("All tests passed!")
