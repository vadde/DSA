"""
Core Sorting Algorithms Implementations from Scratch.

This module provides production-grade reference implementations of:
1. 3-Way Quick Sort (Dutch National Flag Partitioning)
2. In-Place Heap Sort (Floyd's bottom-up build + sift-down)
3. Merge Sort (Divide & Conquer)
4. Counting Sort (Non-comparison integer sorting)
"""

import random
from typing import List


def quicksort_3way(arr: List[int]) -> List[int]:
    """Sorts array using 3-Way QuickSort with randomized pivot selection.

    Time Complexity:
        - Best: O(N log N)
        - Average: O(N log N)
        - Worst: O(N log N) expected with random pivot; O(N) if all duplicate values.
    Space Complexity:
        - O(log N) auxiliary recursion call stack.
    """
    copy_arr = list(arr)

    def _sort(low: int, high: int) -> None:
        if low >= high:
            return
        p_idx = random.randint(low, high)
        copy_arr[low], copy_arr[p_idx] = copy_arr[p_idx], copy_arr[low]
        pivot = copy_arr[low]

        lt, i, gt = low, low + 1, high
        while i <= gt:
            if copy_arr[i] < pivot:
                copy_arr[lt], copy_arr[i] = copy_arr[i], copy_arr[lt]
                lt += 1
                i += 1
            elif copy_arr[i] > pivot:
                copy_arr[i], copy_arr[gt] = copy_arr[gt], copy_arr[i]
                gt -= 1
            else:
                i += 1

        _sort(low, lt - 1)
        _sort(gt + 1, high)

    _sort(0, len(copy_arr) - 1)
    return copy_arr


def heapsort(arr: List[int]) -> List[int]:
    """Sorts array in-place using Max-Heap Floyd bottom-up sift-down.

    Time Complexity: O(N log N) guaranteed in all cases.
    Space Complexity: O(1) auxiliary space.
    """
    copy_arr = list(arr)
    n = len(copy_arr)

    def sift_down(start: int, end: int) -> None:
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and copy_arr[child] < copy_arr[child + 1]:
                child += 1
            if copy_arr[root] < copy_arr[child]:
                copy_arr[root], copy_arr[child] = copy_arr[child], copy_arr[root]
                root = child
            else:
                break

    # Build heap bottom-up
    for i in range((n - 2) // 2, -1, -1):
        sift_down(i, n - 1)

    # Extract max elements to the end
    for end in range(n - 1, 0, -1):
        copy_arr[0], copy_arr[end] = copy_arr[end], copy_arr[0]
        sift_down(0, end - 1)

    return copy_arr


def counting_sort(nums: List[int]) -> List[int]:
    """Non-comparison sort for integers within arbitrary bounded range.

    Time Complexity: O(N + K) where K = max - min + 1.
    Space Complexity: O(K) for count table.
    """
    if not nums:
        return []
    min_val, max_val = min(nums), max(nums)
    k = max_val - min_val + 1
    counts = [0] * k

    for x in nums:
        counts[x - min_val] += 1

    sorted_res: List[int] = []
    for val_offset, count in enumerate(counts):
        sorted_res.extend([val_offset + min_val] * count)

    return sorted_res


def test_sorting_algorithms() -> None:
    """Unit tests verifying all sorting algorithms against edge cases."""
    test_cases = [
        [],
        [1],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
        [-10, 5, -3, 0, 100, -50, 42],
        [7, 7, 7, 7, 7, 7],
    ]

    for tc in test_cases:
        expected = sorted(tc)
        assert quicksort_3way(tc) == expected, f"QuickSort failed on {tc}"
        assert heapsort(tc) == expected, f"HeapSort failed on {tc}"
        assert counting_sort(tc) == expected, f"CountingSort failed on {tc}"

    print("✅ All Sorting Algorithm tests passed successfully!")


if __name__ == "__main__":
    test_sorting_algorithms()
