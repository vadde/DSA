# Pattern 01: Warmup

## 👶 Explain Like I'm 5

Before a sprinter runs a race, they do stretches and light jogs. This "warmup" section is exactly that.
These are NOT hard problems — they are the **mental stretches** before the real interview marathon begins.
Each problem here teaches you ONE small building block: checking if something is balanced, reversing a string, finding duplicates.
Think of them like LEGO bricks. On their own, they seem too simple. But without knowing how to snap bricks together, you can't build the castle later.

---

## 🧩 Core Idea & Pattern Detection

The Warmup section covers foundational techniques that appear as **sub-problems** inside almost every harder coding pattern:
- **Frequency counting** with dictionaries/Counter
- **Two-pointer tricks** on strings and arrays
- **Set-based deduplication**
- **Integer math** (integer square root, digit manipulation)

### Techniques covered:
- **Set membership check** — `O(1)` duplicate detection
- **Character frequency maps** — `Counter` for anagram/palindrome checks
- **Two pointers on a string** — Left meets Right for palindrome validation
- **Math: integer square root** — Newton's method / binary search on answer

---

## 🔧 Algorithmic Anatomy

### 1. Frequency Map (Counter)
```python
from collections import Counter
freq = Counter(s)          # O(N) time, O(K) space where K = distinct chars
```

### 2. Two Pointers on a String
```python
left, right = 0, len(s) - 1
while left < right:
    # compare s[left] and s[right]
    left += 1
    right -= 1
```

### 3. Set Deduplication
```python
seen = set()
for x in arr:
    if x in seen:
        return True   # duplicate found
    seen.add(x)
```

### 4. Integer Square Root (Binary Search)
```python
lo, hi = 0, n
while lo <= hi:
    mid = (lo + hi) // 2
    if mid * mid == n: return mid
    elif mid * mid < n: lo = mid + 1
    else: hi = mid - 1
return hi    # floor of sqrt
```

---

## ⏱️ Complexity Analysis

| Problem | Time | Space | Key Technique |
|---------|------|-------|---------------|
| Contains Duplicate | O(N) | O(N) | Hash Set |
| Pangram | O(N) | O(1) | Set of seen chars |
| Reverse Vowels | O(N) | O(1) | Two Pointers |
| Valid Palindrome | O(N) | O(1) | Two Pointers |
| Valid Anagram | O(N) | O(K) | Counter |
| Shortest Word Distance | O(N) | O(1) | Linear scan + index tracking |
| Number of Good Pairs | O(N) | O(N) | Counter math |
| Sqrt (integer) | O(log N) | O(1) | Binary Search |

---

## ⚠️ Common Pitfalls

1. **Valid Palindrome**: Don't forget to `.lower()` and skip non-alphanumeric characters before comparing.
2. **Valid Anagram**: Two strings with different lengths can NEVER be anagrams — short-circuit early.
3. **Good Pairs**: If element `x` appears `k` times, it contributes `k*(k-1)//2` good pairs — don't iterate O(N²).
4. **Sqrt**: Use `hi = mid - 1` (not `hi = mid`) to avoid infinite loop when `mid*mid < n`.

---

## ✅ Problems in This Pattern

| # | Problem | Difficulty |
|---|---------|------------|
| 1 | Contains Duplicate | Easy |
| 2 | Pangram | Easy |
| 3 | Reverse Vowels | Easy |
| 4 | Valid Palindrome | Easy |
| 5 | Valid Anagram | Easy |
| 6 | Shortest Word Distance | Easy |
| 7 | Number of Good Pairs | Easy |
| 8 | Sqrt (integer floor) | Medium |
