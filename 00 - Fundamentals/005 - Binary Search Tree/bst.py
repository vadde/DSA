"""
============================================================
Problem: Binary Search Tree (BST) Implementation
Pattern: Data Structures (Fundamentals)
Difficulty: Medium
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine a family tree, but with a strict rule: 
- Anyone smaller than you goes to your Left.
- Anyone bigger than you goes to your Right.

If you are looking for the number 5, and you are standing at 10, you know you 
must go Left! This cuts the search space in half every time, making it super fast 
to find things, just like flipping through a dictionary.

APPROACH: High-Performance Modern Python 3.14
---------
- We use a generic `Node[T]` with `val`, `left`, and `right`.
- **Insert**: Recursively (or iteratively) go left or right until a spot is found.
- **Search**: O(H) time where H is the height of the tree.
- **Delete**: The hardest part!
  - Case 1: No children (leaf) -> Just delete it.
  - Case 2: One child -> Replace the node with its only child.
  - Case 3: Two children -> Find the Minimum element in the Right Subtree 
    (the in-order successor), replace the node's value with it, and delete that successor.
- **Traversals**: We use python Generators (`yield`) to perform In-Order, 
  Pre-Order, and Post-Order traversals elegantly.

COMPLEXITY:
-----------
Time:  O(H) for Insert, Search, and Delete. (H is log(N) if balanced, N if skewed).
       O(N) for Traversals.
Space: O(H) for recursive call stacks.
============================================================
"""

from typing import Optional, Generator
import collections.abc

class Node[T]:
    __slots__ = ("val", "left", "right")

    def __init__(self, val: T):
        self.val = val
        self.left: Optional['Node[T]'] = None
        self.right: Optional['Node[T]'] = None

    def __repr__(self) -> str:
        return f"Node({self.val})"


class BinarySearchTree[T]:
    __slots__ = ("root", "_size")

    def __init__(self):
        self.root: Optional[Node[T]] = None
        self._size: int = 0

    @property
    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

    def insert(self, val: T) -> None:
        """Inserts a value into the BST. O(H) time."""
        if not self.root:
            self.root = Node(val)
            self._size += 1
            return
            
        curr = self.root
        while True:
            if val < curr.val:
                if not curr.left:
                    curr.left = Node(val)
                    self._size += 1
                    return
                curr = curr.left
            elif val > curr.val:
                if not curr.right:
                    curr.right = Node(val)
                    self._size += 1
                    return
                curr = curr.right
            else:
                # Value already exists, ignore (or handle duplicates if desired)
                return

    def search(self, val: T) -> bool:
        """Searches for a value in the BST. O(H) time."""
        curr = self.root
        while curr:
            if val == curr.val:
                return True
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def delete(self, val: T) -> bool:
        """Deletes a value from the BST. Returns True if deleted. O(H) time."""
        def _delete_recursive(node: Optional[Node[T]], target: T) -> tuple[Optional[Node[T]], bool]:
            if not node:
                return None, False
                
            if target < node.val:
                node.left, deleted = _delete_recursive(node.left, target)
                return node, deleted
            elif target > node.val:
                node.right, deleted = _delete_recursive(node.right, target)
                return node, deleted
            else:
                # We found the node to delete!
                
                # Case 1 & 2: 0 or 1 child
                if not node.left:
                    return node.right, True
                elif not node.right:
                    return node.left, True
                    
                # Case 3: 2 children. Find in-order successor (min of right subtree)
                successor = node.right
                while successor.left:
                    successor = successor.left
                    
                # Copy successor value to this node
                node.val = successor.val
                # Delete the successor from the right subtree
                node.right, _ = _delete_recursive(node.right, successor.val)
                return node, True

        self.root, deleted = _delete_recursive(self.root, val)
        if deleted:
            self._size -= 1
        return deleted

    # --- Traversals Using Generators ---
    
    def in_order(self) -> Generator[T, None, None]:
        """Left -> Root -> Right. Yields elements in sorted order."""
        def _traverse(node: Optional[Node[T]]):
            if node:
                yield from _traverse(node.left)
                yield node.val
                yield from _traverse(node.right)
        yield from _traverse(self.root)

    def pre_order(self) -> Generator[T, None, None]:
        """Root -> Left -> Right. Good for making a copy of the tree."""
        def _traverse(node: Optional[Node[T]]):
            if node:
                yield node.val
                yield from _traverse(node.left)
                yield from _traverse(node.right)
        yield from _traverse(self.root)

    def post_order(self) -> Generator[T, None, None]:
        """Left -> Right -> Root. Good for deleting the tree."""
        def _traverse(node: Optional[Node[T]]):
            if node:
                yield from _traverse(node.left)
                yield from _traverse(node.right)
                yield node.val
        yield from _traverse(self.root)


if __name__ == "__main__":
    print("Testing Binary Search Tree...")
    bst: BinarySearchTree[int] = BinarySearchTree()
    
    # 1. Insert
    for num in [50, 30, 20, 40, 70, 60, 80]:
        bst.insert(num)
        
    assert len(bst) == 7
    print("✅ Insert passed!")

    # 2. Traversals
    in_order_list = list(bst.in_order())
    assert in_order_list == [20, 30, 40, 50, 60, 70, 80]
    
    pre_order_list = list(bst.pre_order())
    assert pre_order_list == [50, 30, 20, 40, 70, 60, 80]
    
    post_order_list = list(bst.post_order())
    assert post_order_list == [20, 40, 30, 60, 80, 70, 50]
    print("✅ Traversals passed!")

    # 3. Search
    assert bst.search(60) is True
    assert bst.search(99) is False
    print("✅ Search passed!")

    # 4. Delete
    # Leaf node (20)
    bst.delete(20)
    assert list(bst.in_order()) == [30, 40, 50, 60, 70, 80]
    
    # Node with 1 child (30 now only has 40)
    bst.delete(30)
    assert list(bst.in_order()) == [40, 50, 60, 70, 80]
    
    # Node with 2 children (70 has 60 and 80)
    bst.delete(70)
    assert list(bst.in_order()) == [40, 50, 60, 80]
    
    # Delete Root (50)
    bst.delete(50)
    assert list(bst.in_order()) == [40, 60, 80]
    assert bst.root.val == 60  # 60 is the in-order successor of 50
    assert len(bst) == 3
    print("✅ Delete passed!")

    print("🎉 All BST tests passed successfully!")

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
