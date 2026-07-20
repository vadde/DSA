"""
============================================================
Problem: Design Add and Search Words Data Structure
Pattern: Trie
Difficulty: Medium
LeetCode: #211
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Like a dictionary, but search can use '.' as a wildcard matching any character.
"d.g" matches "dog", "dig", "dag" etc.

APPROACH: Trie + DFS for Wildcards
---------
- Insert: standard Trie insert.
- Search: walk Trie character by character.
  - Regular char: go to that child if it exists.
  - '.': try ALL children recursively.

COMPLEXITY:
-----------
Time:  Insert O(L), Search O(L) average, O(26^L) worst (all dots)
Space: O(N * L) for the Trie
============================================================
"""


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_end: bool = False


class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, idx: int) -> bool:
            if idx == len(word):
                return node.is_end
            ch = word[idx]
            if ch == '.':
                return any(dfs(child, idx + 1) for child in node.children.values())
            if ch not in node.children:
                return False
            return dfs(node.children[ch], idx + 1)

        return dfs(self.root, 0)


if __name__ == "__main__":
    wd = WordDictionary()
    wd.add_word("bad")
    wd.add_word("dad")
    wd.add_word("mad")
    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True
    assert wd.search("...") is True
    assert wd.search("....") is False
    print("All tests passed!")
