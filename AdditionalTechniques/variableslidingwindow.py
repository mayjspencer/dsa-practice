# ✅ Finds the **minimum length** of a contiguous subarray whose sum is at least `target`
def min_subarray_len(target, arr):
    start = 0
    end = 0
    current_sum = 0
    minlen = float('inf')  # initialize to infinity to find the minimum

    while end < len(arr):
        current_sum += arr[end]
        end += 1

        # Shrink the window from the left while the sum is large enough
        while current_sum >= target:
            minlen = min(minlen, end - start)
            current_sum -= arr[start]
            start += 1

    return minlen if minlen != float('inf') else 0


# ✅ Finds the **maximum length** of a subarray with sum at most `k`
def longest_subarray_with_sum_at_most_k(k, arr):
    start = 0
    current_sum = 0
    maxlen = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        # Shrink the window from the left while the sum exceeds k
        while current_sum > k and start <= end:
            current_sum -= arr[start]
            start += 1

        # Valid window: update max length
        maxlen = max(maxlen, end - start + 1)

    return maxlen


# ✅ Counts the number of **contiguous subarrays** whose sum is strictly less than `k`
def count_subarrays_with_sum_less_than_k(k, arr):
    count = 0

    for start in range(len(arr)):
        current_sum = 0

        # Expand the window until the sum is no longer less than k
        for end in range(start, len(arr)):
            current_sum += arr[end]
            if current_sum < k:
                count += 1  # valid subarray
            else:
                break  # stop early if sum goes over or equals k

    return count


# 🔍 Test cases
def test_variable_size_window():
    print("Testing min_subarray_len...")
    print(min_subarray_len(7, [2, 1, 5, 2, 3, 2]))  # Expected: 2 ([5,2] or [2,3,2])
    print(min_subarray_len(15, [1, 2, 3, 4, 5]))     # Expected: 5 ([1,2,3,4,5])
    print(min_subarray_len(100, [1, 2, 3]))          # Expected: 0

    print("Testing longest_subarray_with_sum_at_most_k...")
    print(longest_subarray_with_sum_at_most_k(5, [1, 2, 1, 1, 1]))  # Expected: 5
    print(longest_subarray_with_sum_at_most_k(3, [2, 2, 2]))        # Expected: 1

    print("Testing count_subarrays_with_sum_less_than_k...")
    print(count_subarrays_with_sum_less_than_k(8, [2, 1, 3]))  # Expected: 6
    print(count_subarrays_with_sum_less_than_k(5, [2, 3, 1]))  # Expected: 5

if __name__ == "__main__":
    test_variable_size_window()
