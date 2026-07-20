# Pattern 24: Palindromic Subsequence (Dynamic Programming)

## 👶 Explain Like I'm 5

Think of palindromes like a mirror: "racecar" reads the same from both sides.
Now the tricky question: what's the LONGEST subsequence (letters you can pick,
not necessarily adjacent) from a word that forms a palindrome?
"bbbab" → "bbbb" is the longest palindromic subsequence (length 4).

The key insight: expand from the outside in. Compare the first and last character.
If they match → both can be part of our palindrome → add 2 to whatever is in the middle.
If they don't match → take the best of (ignore first) or (ignore last).
**This builds a 2D DP table where dp[i][j] = LPS length for substring s[i..j].**

---

## 🧩 Core Idea & Pattern Detection

The **interval DP** template: solve small substrings first, build up to the full string.
```
dp[i][j] = LPS of s[i..j]
if s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
else:            dp[i][j] = max(dp[i+1][j], dp[i][j-1])
```

### When to use it:
- Questions about palindromic subsequences, substrings, counts in a string.
- Any problem requiring you to compare the string against its reverse.

---

## ⏱️ Complexity Analysis

| Aspect | Complexity |
|--------|-----------|
| **Time** | O(N²) |
| **Space** | O(N²) or O(N) with rolling rows |

---

## ✅ Problems in This Pattern

| # | Problem | Difficulty | LeetCode |
|---|---------|------------|----------|
| 1 | Longest Palindromic Subsequence | Medium | #516 |
| 2 | Longest Palindromic Substring | Medium | #5 |
| 3 | Count of Palindromic Substrings | Medium | #647 |
| 4 | Minimum Deletions to Make a Palindrome | Medium | #1312 variant |
| 5 | Palindromic Partitioning (Min Cuts) | Hard | #132 |
