"""
============================================================
Problem: Online Stock Spanner
Pattern: Monotonic Stack
Difficulty: Medium
Link: https://leetcode.com/problems/online-stock-span/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You are tracking the stock price of your favorite toy company every day.
When you check the price today, you want to know: "How many days in a row (looking 
backward from today) was the price lower than or equal to today's price?"
If the prices were: [10, 20, 30]
On day 1 (price 10), it's the first day, so the streak is 1.
On day 2 (price 20), 20 is bigger than 10. So the streak is today (1) + yesterday's streak (1) = 2.
On day 3 (price 30), 30 is bigger than 20. So the streak is today (1) + yesterday's streak (2) = 3.
We can use a Stack to remember previous days! But instead of just remembering the price, 
we remember a combo meal: `(price, streak)`.
When a big price comes in, it "eats" all the smaller prices in the stack and 
absorbs their streaks!

APPROACH:
---------
1. We are designing a class `StockSpanner`.
2. In `__init__`, we initialize `self.stack = []`. The stack will store tuples of `(price, span)`.
3. In `next(price)`:
   - Initialize the `span` for today as 1 (today itself counts).
   - While the stack is not empty AND the price at the top of the stack is `<= price`:
     - This older price is smaller, so it gets absorbed!
     - `popped_price, popped_span = self.stack.pop()`
     - Add its span to our current span: `span += popped_span`
   - Push our `(price, span)` onto the stack.
   - Return the `span`.

COMPLEXITY:
-----------
Time:  Amortized O(1) per call to `next`. Each element is pushed once and popped at most once.
Space: O(N) — The stack can grow to size N if prices are strictly decreasing.

EDGE CASES:
-----------
- Edge case 1: Prices strictly decrease. Span is always 1. Stack grows to size N.
- Edge case 2: Prices are all identical. The span keeps growing and accumulating.
============================================================
"""

class StockSpanner:
    def __init__(self):
        # Stack stores tuples of (price, span)
        self.stack: list[tuple[int, int]] = []

    def next(self, price: int) -> int:
        span = 1
        
        # While the stack has elements and the top price is less than or equal to today's price
        while self.stack and self.stack[-1][0] <= price:
            # Pop it and absorb its span!
            popped_price, popped_span = self.stack.pop()
            span += popped_span
            
        # Push the new price and its total accumulated span
        self.stack.append((price, span))
        
        return span

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    spanner = StockSpanner()
    
    # ✅ Normal cases (Prices: 100, 80, 60, 70, 60, 75, 85)
    assert spanner.next(100) == 1, "Test 1 failed"  # [ (100, 1) ]
    assert spanner.next(80) == 1, "Test 2 failed"   # [ (100, 1), (80, 1) ]
    assert spanner.next(60) == 1, "Test 3 failed"   # [ (100, 1), (80, 1), (60, 1) ]
    
    # 70 is greater than 60, so it absorbs 60.
    assert spanner.next(70) == 2, "Test 4 failed"   # [ (100, 1), (80, 1), (70, 2) ]
    
    assert spanner.next(60) == 1, "Test 5 failed"   # [ (100, 1), (80, 1), (70, 2), (60, 1) ]
    
    # 75 is greater than 60 (span 1) and 70 (span 2), so it absorbs both! (1 + 1 + 2 = 4)
    assert spanner.next(75) == 4, "Test 6 failed"   # [ (100, 1), (80, 1), (75, 4) ]
    
    # 85 is greater than 75 (span 4) and 80 (span 1), so it absorbs both! (1 + 4 + 1 = 6)
    assert spanner.next(85) == 6, "Test 7 failed"   # [ (100, 1), (85, 6) ]

    print("All tests passed!")
