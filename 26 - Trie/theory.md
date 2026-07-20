# Pattern 26: Trie (Prefix Tree)

## 👶 Explain Like I'm 5

A Trie is like a dictionary organized as a tree.
Imagine each word is a path through the tree, letter by letter.
"app" and "apple" share the path A→P→P, then apple has an extra L→E.
This means if you look up "app", you've automatically checked the first
3 letters of "apple" too — no repeated work!
Tries are perfect for PREFIX searches: "Find all words starting with 'pre'".

---

## 🧩 Core Idea & Pattern Detection

**Trie = Each node represents ONE character, children represent next characters.**

```
root
 ├── a
 │   └── p
 │       └── p (end)
 │           └── l
 │               └── e (end)
 └── b
     └── a
         └── t (end)
```

### When to use it:
- Prefix matching / autocomplete.
- Word existence check in a dictionary of words.
- "Does any word in my set start with X?"
- Keywords: "prefix", "suggest", "search words", "autocomplete".

---

## 🔧 TrieNode Structure

```python
class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False
```

---

## ⏱️ Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| Insert | O(L) | O(L) per word |
| Search | O(L) | O(1) |
| StartsWith | O(L) | O(1) |

Where L = word length.

---

## ✅ Problems in This Pattern

| # | Problem | Difficulty | LeetCode |
|---|---------|------------|----------|
| 1 | Implement Trie (Prefix Tree) | Medium | #208 |
| 2 | Index Pairs of a String | Easy | #1065 |
| 3 | Design Add and Search Words Data Structure | Medium | #211 |
| 4 | Extra Characters in a String | Medium | #2707 |
| 5 | Search Suggestions System | Medium | #1268 |
