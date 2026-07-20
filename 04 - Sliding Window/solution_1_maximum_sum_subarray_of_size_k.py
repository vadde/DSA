def max_sub_array(arr, k):
    """
    Find the maximum sum of any contiguous subarray of size K.
    """
    if len(arr) < k:
        return -1
    window_start = 0
    window_sum = 0
    max_sum = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
        # print(f"iteration: {window_end}; maximum sum: {max_sum}")
    return max_sum
    
print(max_sub_array([2,1,5,0,3,2,7], 3))
