def count_pairs_with_sum_less_than_target(arr, target):
    left = 0
    right = len(arr) - 1
    count = 0

    while left < right:
        currsum = arr[left] + arr[right]
        if currsum < target:
            count += 1
            left += 1
        else:
            right -= 1
    return count

# Example test
arr = [1, 2, 3, 5, 7]  # Must be sorted
target = 8
print(count_pairs_with_sum_less_than_target(arr, target))  # Expected: 5
