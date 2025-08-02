def count_pairs_with_sum_less_than_target(arr, target):
    # Two pointers: one at the start, one at the end of the sorted array
    left = 0
    right = len(arr) - 1
    count = 0

    while left < right:
        currsum = arr[left] + arr[right]

        if currsum < target:
            # All elements between left and right form valid pairs with arr[left]
            # So we add (right - left) to the count
            count += (right - left)

            # Move left pointer forward to try next value
            left += 1
        else:
            # If sum is too large, move right pointer left to try smaller values
            right -= 1

    return count
