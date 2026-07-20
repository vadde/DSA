import math


def smallest_sub_array(arr, k):
    window_start, window_sum, min_length = 0, 0, math.inf

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= k:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
        print(f"iteration: {window_end}; minimum length: {min_length}")
    return min_length if min_length != math.inf else 0
    
print(smallest_sub_array([4,0,2,1,5,6,4,7,5], 12))
