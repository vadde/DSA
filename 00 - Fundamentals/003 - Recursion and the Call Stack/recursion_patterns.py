"""
Recursion Patterns and Call Stack Simulation.

This module provides implementations of the 4 core recursive paradigms:
1. Divide and Conquer (Merge Sort)
2. Tree Traversal (Recursive vs Iterative Explicit Stack)
3. Backtracking with State Management (Subsets)
4. Tail Recursion with Accumulators
"""

from typing import Any, List, Optional


class TreeNode:
    """Standard binary tree node."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def merge_sort(nums: List[int]) -> List[int]:
    """Classic Divide-and-Conquer Sort.

    Recurrence: T(N) = 2T(N/2) + O(N) -> O(N log N) time, O(N) space.
    """
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    # Combine step
    merged: List[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def inorder_recursive(root: Optional[TreeNode]) -> List[int]:
    """Standard recursive DFS traversal."""
    result: List[int] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result


def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Iterative in-order traversal using an explicit list as call stack."""
    result: List[int] = []
    stack: List[TreeNode] = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result


def generate_subsets(nums: List[int]) -> List[List[int]]:
    """Backtracking pattern exploring a binary state-space decision tree.

    Time: O(2^N), Space: O(N) auxiliary recursion stack.
    """
    results: List[List[int]] = []
    subset: List[int] = []

    def backtrack(idx: int) -> None:
        if idx == len(nums):
            results.append(list(subset))
            return

        # Decision 1: Pick nums[idx]
        subset.append(nums[idx])
        backtrack(idx + 1)

        # Undo decision
        subset.pop()

        # Decision 2: Do NOT pick nums[idx]
        backtrack(idx + 1)

    backtrack(0)
    return results


def tail_factorial(n: int, accumulator: int = 1) -> int:
    """Tail-recursive factorial with accumulator."""
    if n <= 1:
        return accumulator
    return tail_factorial(n - 1, n * accumulator)


def test_recursion_patterns() -> None:
    """Unit tests verifying recursive implementations."""
    # 1. Merge Sort test
    nums = [38, 27, 43, 3, 9, 82, 10]
    sorted_nums = merge_sort(nums)
    assert sorted_nums == [3, 9, 10, 27, 38, 43, 82]

    # 2. Tree Traversal (Recursive vs Iterative)
    # Tree:   1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)

    rec_result = inorder_recursive(root)
    iter_result = inorder_iterative(root)
    assert rec_result == [4, 2, 5, 1, 3]
    assert iter_result == [4, 2, 5, 1, 3]

    # 3. Subsets Backtracking
    subsets = generate_subsets([1, 2])
    assert len(subsets) == 4
    assert [1, 2] in subsets
    assert [1] in subsets
    assert [2] in subsets
    assert [] in subsets

    # 4. Tail Factorial
    assert tail_factorial(5) == 120
    assert tail_factorial(0) == 1

    print("✅ All Recursion pattern tests passed successfully!")


if __name__ == "__main__":
    test_recursion_patterns()
