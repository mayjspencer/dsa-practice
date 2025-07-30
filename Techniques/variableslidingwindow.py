def min_subarray_len(target, arr):
    start = 0
    end = 0
    current_sum = 0
    minlen = float('inf')

    while end < len(arr):
        current_sum += arr[end]
        end += 1

        while current_sum >= target:
            minlen = min(minlen, end - start)
            current_sum -= arr[start]
            start += 1

    return minlen if minlen != float('inf') else 0

def longest_subarray_with_sum_at_most_k(k, arr):
    start = 0
    current_sum = 0
    maxlen = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        # shrink from the left if the sum exceeds k
        while current_sum > k and start <= end:
            current_sum -= arr[start]
            start += 1

        # check max length if valid
        maxlen = max(maxlen, end - start + 1)

    return maxlen

def count_subarrays_with_sum_less_than_k(k, arr):
    count = 0

    for start in range (len(arr)):
        current_sum = 0

        for end in range(start, len(arr)):
            current_sum += arr[end]
            if current_sum < k:
                count += 1
            else:
                break

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
