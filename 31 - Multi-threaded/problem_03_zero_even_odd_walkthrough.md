# 🚶‍♂️ Walkthrough: Print Zero Even Odd

## 👶 Explain Like I'm 5
Three workers: Zero, Even, and Odd. They need to print numbers like a zipper: "0 1 0 2 0 3 0 4".
Zero *always* goes first. After Zero goes, it looks at what number is next. If it's an odd number, it wakes up the Odd worker. If it's even, it wakes up the Even worker. When Even/Odd finishes, they hand the baton back to Zero!

## 🎯 Core Strategy
**Three Semaphores**.

1. `zero_sem = Semaphore(1)` (starts unlocked)
2. `odd_sem = Semaphore(0)` (starts locked)
3. `even_sem = Semaphore(0)` (starts locked)

- **Zero**: Loops `i` from 1 to `N`. Acquires `zero_sem`, prints 0. If `i` is odd, releases `odd_sem`. If `i` is even, releases `even_sem`.
- **Odd**: Loops `i` from 1 to `N` stepping by 2. Acquires `odd_sem`, prints `i`, releases `zero_sem`.
- **Even**: Loops `i` from 2 to `N` stepping by 2. Acquires `even_sem`, prints `i`, releases `zero_sem`.

## 🏃‍♂️ Step-by-Step Execution (Dry Run)
**N = 3**

| Turn | Zero Thread | Odd Thread | Even Thread | Output |
|---|---|---|---|---|
| 1 | `zero.acquire()` -> prints `0`. `i=1` (odd) -> `odd.release()` | `odd.acquire()` (unblocked!) | `even.acquire()` (blocked) | "0" |
| 2 | `zero.acquire()` (blocked) | prints `1`. `zero.release()` | (blocked) | "01" |
| 3 | (unblocked!) prints `0`. `i=2` (even) -> `even.release()` | `odd.acquire()` (blocked) | (unblocked!) | "010" |
| 4 | `zero.acquire()` (blocked) | (blocked) | prints `2`. `zero.release()`| "0102" |
| 5 | (unblocked!) prints `0`. `i=3` (odd) -> `odd.release()` | (unblocked!) | (blocked) | "01020" |
| 6 | (done loop) | prints `3`. `zero.release()` | (done loop) | "010203" |

Final Output: "010203" ✅

## 📊 Visual Diagram

```mermaid
flowchart TD
    Z["Zero Thread\nPrints '0'"]
    O["Odd Thread\nPrints '1, 3, 5...'"]
    E["Even Thread\nPrints '2, 4, 6...'"]
    
    Z -->|If next is Odd\nrelease(odd_sem)| O
    Z -->|If next is Even\nrelease(even_sem)| E
    
    O -->|release(zero_sem)| Z
    E -->|release(zero_sem)| Z
    
    style Z fill:#bbdefb,color:#000
    style O fill:#c8e6c9,color:#000
    style E fill:#fff9c4,color:#000
```

## 🛑 Complexity
- **Time:** $O(N)$
- **Space:** $O(1)$
