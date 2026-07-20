"""
============================================================
Problem: Print in Order
Pattern: Multi-threaded
Difficulty: Easy
LeetCode: #1114
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have three methods: `first()`, `second()`, and `third()`.
They will be called by THREE DIFFERENT threads at the exact same time.
You must guarantee that `first()` runs before `second()`, and `second()`
runs before `third()`, no matter which thread starts first!

APPROACH: Threading Events
---------
Use `threading.Event`. It's like a traffic light.
- `first_done` event starts RED. `second()` waits for it to turn GREEN.
- `second_done` event starts RED. `third()` waits for it to turn GREEN.
- `first()` finishes -> turns `first_done` GREEN.
- `second()` finishes -> turns `second_done` GREEN.

COMPLEXITY:
-----------
Time:  O(1)
Space: O(1)
============================================================
"""

from typing import Callable
from threading import Event, Thread


class Foo:
    def __init__(self) -> None:
        self.first_done = Event()
        self.second_done = Event()

    def first(self, printFirst: Callable[[], None]) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_done.set()  # Green light for second

    def second(self, printSecond: Callable[[], None]) -> None:
        self.first_done.wait() # Wait for first to finish
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_done.set() # Green light for third

    def third(self, printThird: Callable[[], None]) -> None:
        self.second_done.wait() # Wait for second to finish
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


if __name__ == "__main__":
    import time
    
    output = []
    
    def printFirst(): output.append("first")
    def printSecond(): output.append("second")
    def printThird(): output.append("third")

    foo = Foo()
    
    # Start them in reverse order to prove synchronization works!
    t3 = Thread(target=foo.third, args=(printThird,))
    t2 = Thread(target=foo.second, args=(printSecond,))
    t1 = Thread(target=foo.first, args=(printFirst,))
    
    t3.start()
    t2.start()
    time.sleep(0.1) # Give t2 and t3 time to wait
    t1.start()
    
    t1.join()
    t2.join()
    t3.join()
    
    assert output == ["first", "second", "third"], f"Failed: {output}"
    print("All tests passed!")
