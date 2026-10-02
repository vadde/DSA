# ⚡ Bit Manipulation: The Silicon-Level Speed Engine

> *"High-level languages offer abstractions; hardware offers bits. When you manipulate bits directly, your code runs at the raw speed of physical CPU silicon transistors — zero overhead, zero allocation, 1 clock cycle."*

---

## 📍 Level 100 — The Napkin Sketch (30 Seconds)

### The Real-World Analogy: 8 Light Switches on a Wall Panel
Imagine a wall panel in a smart home with 8 toggle switches:

```
Switch:  [ 7 ] [ 6 ] [ 5 ] [ 4 ] [ 3 ] [ 2 ] [ 1 ] [ 0 ]
State:     0     0     1     0     1     0     0     1
Meaning:        (Heater)       (Garage)            (Front Door)
```

To record whether 8 household appliances are ON or OFF:
- You do **not** allocate 8 strings or a heavy dictionary with 8 keys.
- You store a single tiny number: `0b00101001` = **41**.
- To check if the Garage (Switch 3) is open, you slide a stencil over Switch 3 (`x & (1 << 3)`).
- To flip the Garage switch, you toggle it (`x ^ (1 << 3)`).

### The Two's Complement Invariant
> **The Two's Complement Law:** In modern computer hardware, negative numbers are represented by inverting all bits and adding 1:
> $$-x = (\sim x) + 1$$
> Because of this mathematical symmetry, bitwise ANDing a number with its negative instantly isolates its **lowest set bit (rightmost 1-bit)**:
> $$\text{Lowest Set Bit} = x \ \& \ (-x)$$
> This single formula powers Fenwick Trees, bitmap scans, and high-speed graph traversals.

---

## 🎯 Level 200 — Street Fundamentals (5 Minutes)

> 🧠 **Mental Model Card**
> - **The Core Superpower:** 32 or 64 independent boolean flags stored in a single integer register, manipulated in 0.25 nanoseconds.
> - **The Kryptonite:** Operator precedence bugs (bitwise operators bind looser than addition/subtraction) and language integer overflows.
> - **When to Reach for It:**
>   - "Find the unique element when all others appear twice" $\to$ XOR cancellation.
>   - "Check if integer is a power of 2" $\to$ `x > 0 and (x & (x - 1)) == 0`.
>   - Generating all $2^N$ subsets $\to$ Count from $0$ to $2^N - 1$.
>   - State-space DP with $N \le 20$ elements (TSP, Hamiltonian path).
> - **When to Run Away:** When flags exceed 64 bits and change dynamically $\to$ Use `bitarray` or Python's `set()`.
> - **Complexity Budget:** Every standard bit operation runs in strict **$O(1)$ Time** and **$O(1)$ Space**.

### The 6 Primitive Bitwise Operators

| Operator | Syntax | Description | Example (A = 5 `0101`, B = 3 `0011`) |
|---|:---:|---|---|
| **AND** | `A & B` | 1 only if *both* bits are 1 | `5 & 3 = 1` (`0001`) |
| **OR** | `A \| B` | 1 if *either* bit is 1 | `5 \| 3 = 7` (`0111`) |
| **XOR** | `A ^ B` | 1 if bits *differ* ($x \oplus x = 0$, $x \oplus 0 = x$) | `5 ^ 3 = 6` (`0110`) |
| **NOT** | `~A` | Inverts all bits (in two's complement: $\sim x = -(x+1)$) | `~5 = -6` |
| **Left Shift** | `A << k` | Shifts bits left by $k$ positions (multiplies by $2^k$) | `5 << 1 = 10` (`1010`) |
| **Right Shift** | `A >> k` | Shifts bits right by $k$ positions (integer divides by $2^k$) | `5 >> 1 = 2` (`0010`) |

### The 7 Golden Street Tricks Cheat Sheet

```python
# 1. Test if k-th bit is set (0-indexed from right)
is_set = (x >> k) & 1 == 1

# 2. Set k-th bit to 1
x |= (1 << k)

# 3. Clear k-th bit to 0
x &= ~(1 << k)

# 4. Toggle k-th bit (0 -> 1, 1 -> 0)
x ^= (1 << k)

# 5. Clear lowest set bit (Brian Kernighan's trick)
x &= (x - 1)  # e.g., 01100 -> 01000

# 6. Isolate lowest set bit
lowest = x & (-x)  # e.g., 01100 -> 00100

# 7. Check if x is a power of 2
is_pow2 = x > 0 and (x & (x - 1)) == 0
```

### Street Code Snippets: 2 Core Interview Workhorses

```python
# 1. Brian Kernighan's Algorithm: Count Set Bits (Hamming Weight)
# Runs in O(Set Bits) time, NOT O(32) — skips all 0-bits instantly!
def count_set_bits(n: int) -> int:
    count = 0
    while n:
        n &= (n - 1)  # Clears rightmost 1-bit
        count += 1
    return count


# 2. Single Number (XOR Cancellation) — O(N) Time, O(1) Space
# Given an array where every element appears twice except one:
def single_number(nums: list[int]) -> int:
    unique = 0
    for x in nums:
        unique ^= x  # x ^ x = 0; 0 ^ unique = unique
    return unique
```

---

## ⚙️ Level 300 — Working Professional (15 Minutes)

### Real-System Architecture: Production Applications
1. **Linux POSIX File Permissions**:
   A 9-bit bitmask determines file access rights:
   `rwxr-xr--` $= (111 \ 101 \ 100)_2 = 0754$ in octal.
   Checking read permission takes a single `mode & S_IRUSR` CPU instruction.
2. **Bloom Filters & Bitmaps**:
   High-throughput databases (Cassandra, Redis, RocksDB) check if a key exists among 100 million rows by testing $k$ bit positions in a compact shared 128 MB bit array.
3. **Bitmask Dynamic Programming ($N \le 20$)**:
   In the Traveling Salesperson Problem (TSP) or job scheduling, representing the visited subset of $N$ cities as a Python `frozenset` creates huge hash overhead. An integer `mask` in range $[0, 2^N - 1]$ fits in a CPU register and indexes DP arrays directly: `dp[mask][curr_city]`.

### Complete Implementation: BitHacks Production Suite

```python
"""
Production Bit Manipulation Library.
Includes Brian Kernighan popcount, two non-repeating numbers, and submask iterator.
"""

from typing import Iterator, List, Tuple

class BitHacks:
    """Production suite of silicon-level bit manipulation algorithms."""

    @staticmethod
    def count_set_bits(n: int) -> int:
        """Counts set bits using Brian Kernighan's algorithm in O(K) where K = set bits."""
        count = 0
        while n > 0:
            n &= (n - 1)
            count += 1
        return count

    @staticmethod
    def two_single_numbers(nums: List[int]) -> Tuple[int, int]:
        """Finds the two unique numbers in an array where all other elements appear twice.

        Time: O(N)
        Space: O(1)
        """
        # Step 1: XOR all elements -> gives xor_all = a ^ b
        xor_all = 0
        for x in nums:
            xor_all ^= x

        # Step 2: Find any bit where a and b differ (isolate lowest set bit)
        diff_bit = xor_all & (-xor_all)

        # Step 3: Partition all numbers into two groups based on diff_bit
        a = b = 0
        for x in nums:
            if x & diff_bit:
                a ^= x
            else:
                b ^= x

        return (min(a, b), max(a, b))

    @staticmethod
    def enumerate_submasks(mask: int) -> Iterator[int]:
        """Iterates through all submasks of a given mask in descending order.

        Complexity:
            Iterating over submasks of all masks takes O(3^N) total time, not O(4^N)!
        """
        sub = mask
        while sub > 0:
            yield sub
            sub = (sub - 1) & mask
        yield 0  # Empty submask
```

### Critical Edge Cases & Operator Precedence Traps
1. **The Python Precedence Trap (HIGH SEVERITY)**:
   In Python, addition and subtraction have **higher precedence** than bit shifts!
   ```python
   # ❌ BUG: Evaluates as 1 << (2 + 1) = 1 << 3 = 8!
   val = 1 << 2 + 1

   # ✅ FIX: Explicit parentheses
   val = (1 << 2) + 1  # Equals 5
   ```
2. **The `==` vs `&` Precedence Trap**:
   `==` binds tighter than `&`:
   ```python
   # ❌ BUG: Evaluates as x & (1 == 0) -> x & False -> 0!
   if x & 1 == 0: ...

   # ✅ FIX: Always wrap bitwise expressions in parentheses!
   if (x & 1) == 0: ...
   ```
3. **Python Arbitrary-Precision Sign Extension**:
   In C/Java, an integer is fixed at 32 or 64 bits. In Python, integers have arbitrary precision. Therefore, `~0` is not `0xFFFFFFFF` (all 1-bits), but `-1`. To simulate 32-bit two's complement in Python:
   ```python
   MASK_32 = 0xFFFFFFFF
   val_32 = x & MASK_32
   ```

---

## 🔬 Level 400 — Staff & Senior Engineer (30 Minutes)

### SWAR Parallel Bit Counting (Hamming Weight in $O(1)$)
How does hardware `POPCNT` count 1-bits in a 32-bit integer in constant time without any loops?
Using **SIMD Within A Register (SWAR)**:

```python
def popcount_32(x: int) -> int:
    """Computes number of set bits in a 32-bit int in 5 clock cycles using SWAR."""
    x = x - ((x >> 1) & 0x55555555)  # Sum 2-bit pairs
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)  # Sum 4-bit nibbles
    x = (x + (x >> 4)) & 0x0F0F0F0F  # Sum 8-bit bytes
    x = x + (x >> 8)  # Sum 16-bit words
    x = x + (x >> 16)  # Sum 32-bit full register
    return x & 0x0000003F
```

### The $O(3^N)$ Submask Enumeration Proof
When solving Bitmask DP (e.g. partition an array into $K$ subsets), we iterate over every mask, and for each mask, iterate over all its submasks:
```python
sub = mask
while sub:
    sub = (sub - 1) & mask
```
How many total operations occur?
A mask with $k$ set bits has exactly $2^k$ submasks.
By the **Binomial Theorem**:
$$\sum_{k=0}^N \binom{N}{k} 2^k = (1 + 2)^N = 3^N$$
Instead of naive nested loops taking $O(2^N \times 2^N) = O(4^N)$, submask enumeration takes strictly **$O(3^N)$**! For $N = 15$, $4^{15} \approx 10^9$ (TLE), but $3^{15} \approx 14 \times 10^6$ (passes within 0.05 seconds).

---

## 🎓 Level 500 — Researcher's Corner (Collapsible)

<details>
<summary><b>📜 De Bruijn Sequences & Branchless Log2 (Click to expand)</b></summary>

### Branchless $\lfloor \log_2 x \rfloor$ via De Bruijn Sequences
How do you find the most significant bit (MSB) of an integer in 3 assembly instructions without hardware `BSR` (Bit Scan Reverse)?
Using a **De Bruijn Sequence** $B(2, 5)$ of length $2^5 = 32$:
A cyclic sequence where every possible 5-bit pattern appears exactly once as a contiguous substring.

The magic 32-bit constant is `0x077CB531`:
```python
DE_BRUIJN_LOOKUP = [
    0, 1, 28, 2, 29, 14, 24, 3, 30, 22, 20, 15, 25, 17, 4, 8,
    31, 27, 13, 23, 21, 19, 16, 7, 26, 12, 18, 6, 11, 5, 10, 9
]

def floor_log2(v: int) -> int:
    """Returns floor(log2(v)) in 3 operations without branches or loops."""
    # Round down to power of 2
    v |= v >> 1
    v |= v >> 2
    v |= v >> 4
    v |= v >> 8
    v |= v >> 16
    v = (v >> 1) + 1
    # Multiply by De Bruijn constant and shift
    return DE_BRUIJN_LOOKUP[(v * 0x077CB531 & 0xFFFFFFFF) >> 27]
```
</details>

---

## 🧭 Navigation & Cross-Pillar Bridges

| ← Previous Module | ↑ Fundamentals Hub | Next Module → |
|:---|:---:|---:|
| [🌲 013 - Union-Find](../013%20-%20Union-Find%20%28Disjoint%20Set%29/) | [📚 Fundamentals Index](../README.md) | [🌲 015 - Trees (Complete Guide) →](../015%20-%20Trees%20%28The%20Complete%20Guide%29/) |

> ### ⚔️ Algorithmic Patterns Powered by Bits:
> - **[Pattern 18: Bitwise XOR](../../18%20-%20Bitwise%20XOR/)** — Single Number I, II, III, Missing Number.
> - **[Pattern 42: Binary Indexed Tree (Fenwick)](../../42%20-%20Binary%20Indexed%20Tree/)** — Prefix sum updates using `x & (-x)`.
> - **[000 - Chapter 12: Kill Mode vs Pull the Plug](../000%20-%20Theoretical%20Foundations%20%28The%20Complete%20Guide%29/12_kill_mode_vs_pull_plug.md)** — Bitmask DP execution when $N \le 20$.
