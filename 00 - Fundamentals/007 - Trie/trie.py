"""
============================================================
Problem: Trie (Prefix Tree) Implementation
Pattern: Data Structures (Fundamentals)
Difficulty: Medium
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine a dictionary book. When you look for the word "APPLE", you first flip 
to the 'A' section. Then you look for 'P', then another 'P', then 'L', then 'E'.
A Trie (pronounced "try") works exactly like this! 
Instead of storing the whole word "APPLE" in one box, we have a tree of letters. 
The Root connects to 'A', 'A' connects to 'P', and so on. 
If we also add "APP", they both share the exact same 'A'->'P'->'P' path! We just 
put a little sticker on the second 'P' saying "A valid word ends here."

APPROACH: High-Performance Modern Python 3.14
---------
- We use a `TrieNode` class with two `__slots__`:
  1. `children`: A Python dictionary mapping a character (string) to another `TrieNode`.
     (Using a dict is much more memory efficient and flexible than a size-26 list).
  2. `is_end_of_word`: A boolean flag.
- **Insert**: Walk down the tree, character by character. If a char isn't in `children`, 
  create a new node. Mark the final node's flag as True.
- **Search**: Walk down the tree. If you ever can't find a char, return False. 
  If you finish the word, return the `is_end_of_word` flag.
- **StartsWith**: Same as Search, but return True immediately if you finish the prefix, 
  even if `is_end_of_word` is False.

COMPLEXITY:
-----------
Time:  O(L) for Insert, Search, and StartsWith, where L is the length of the word.
Space: O(N * L) in the worst case (no shared prefixes), but heavily compressed 
       if there are many shared prefixes!
============================================================
"""

class TrieNode:
    """
    A single node in the Trie.
    __slots__ ensures we don't waste memory on dynamic dictionaries, except 
    for the explicit 'children' dict we need!
    """
    __slots__ = ("children", "is_end_of_word")

    def __init__(self):
        self.children: dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False

    def __repr__(self) -> str:
        return f"TrieNode(children={list(self.children.keys())}, is_end={self.is_end_of_word})"


class Trie:
    """
    A highly optimized Prefix Tree.
    """
    __slots__ = ("root",)

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie in O(L) time."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Returns True if the exact word is in the trie. O(L) time."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Returns True if there is any word in the trie that starts with the given prefix. O(L) time."""
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


if __name__ == "__main__":
    print("Testing Trie (Prefix Tree)...")
    trie = Trie()
    
    # 1. Insert
    trie.insert("apple")
    print("✅ Inserted 'apple'")

    # 2. Search
    assert trie.search("apple") is True
    assert trie.search("app") is False
    print("✅ Search passed!")

    # 3. StartsWith
    assert trie.starts_with("app") is True
    assert trie.starts_with("apl") is False
    print("✅ StartsWith passed!")

    # 4. Insert Sub-word
    trie.insert("app")
    assert trie.search("app") is True
    print("✅ Insert Sub-word passed!")
    
    print("🎉 All Trie tests passed successfully!")

# ==============================================================================
# ⚠️ PYTHON < 3.12 COMPATIBILITY FALLBACK
# ==============================================================================
# The modern `class Name[T]:` syntax (PEP 695) requires Python 3.12+.
# If you are running this code in an older environment (like an online IDE), 
# you will get a "SyntaxError: invalid syntax".
# 
# To fix this, replace the modern syntax with the traditional Generic typing:
# 
# 1. Import Generic and TypeVar:
#    from typing import Generic, TypeVar
# 
# 2. Define the TypeVar:
#    T = TypeVar('T')
# 
# 3. Inherit from Generic[T]:
#    class Node(Generic[T]):
#        ...
#    
#    class DataStructure(Generic[T]):
#        ...
# ==============================================================================
