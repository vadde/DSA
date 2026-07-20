"""
============================================================
Problem: Print FooBar Alternately
Pattern: Multi-threaded
Difficulty: Medium
LeetCode: #1115
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Two threads: one prints "foo", one prints "bar".
They run N times. We want them to perfectly alternate: "foobarfoobar...".

APPROACH: Semaphores
---------
Use two Semaphores (like lock tokens).
- `foo_lock` starts with 1 token (unlocked).
- `bar_lock` starts with 0 tokens (locked).
- Thread A takes `foo_lock`, prints "foo", releases `bar_lock` (+1 token).
- Thread B takes `bar_lock`, prints "bar", releases `foo_lock` (+1 token).
They endlessly pass the token back and forth!

COMPLEXITY:
-----------
Time:  O(N)
Space: O(1)
============================================================
"""

from typing import Callable
from threading import Semaphore, Thread


class FooBar:
    def __init__(self, n: int):
        self.n = n
        self.foo_lock = Semaphore(1) # Start unlocked
        self.bar_lock = Semaphore(0) # Start locked

    def foo(self, printFoo: Callable[[], None]) -> None:
        for _ in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar: Callable[[], None]) -> None:
        for _ in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()


if __name__ == "__main__":
    output = []
    
    def printFoo(): output.append("foo")
    def printBar(): output.append("bar")

    foobar = FooBar(3)
    
    t2 = Thread(target=foobar.bar, args=(printBar,))
    t1 = Thread(target=foobar.foo, args=(printFoo,))
    
    t2.start()
    t1.start()
    
    t1.join()
    t2.join()
    
    expected = ["foo", "bar", "foo", "bar", "foo", "bar"]
    assert output == expected, f"Failed: {output}"
    print("All tests passed!")
