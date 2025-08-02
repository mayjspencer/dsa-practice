# Finds the **maximum sum** of any subarray of size `k` using the fixed sliding window approach
def max_sum_fixed_window(arr, k):
    low = 0
    high = k
    sum = 0
    # Calculate the sum of the first window
    for i in range(low, high):
        sum += arr[i]
    maxsum = sum

    # Slide the window one element at a time and track max sum
    while high <= len(arr):
        sum = 0
        for i in range(low, high):
            sum += arr[i]
        if sum > maxsum:
            maxsum = sum
        low += 1
        high += 1

    return maxsum

# Finds the **minimum sum** of any subarray of size `k`
def min_sum_fixed_window(arr, k):
    low = 0
    high = k
    sum = 0
    # Calculate the sum of the first window
    for i in range(low, high):
        sum += arr[i]
    minsum = sum

    # Slide the window one element at a time and track min sum
    while high <= len(arr):
        sum = 0
        for i in range(low, high):
            sum += arr[i]
        if sum < minsum:
            minsum = sum
        low += 1
        high += 1

    return minsum

# Calculates the **average** of each subarray of size `k`
def average_fixed_window(arr, k):
    low = 0
    high = k
    avgs = []

    # Slide the window and calculate average for each position
    while high <= len(arr):
        sum = 0
        for i in range(low, high):
            sum += arr[i]
        avg = sum / k
        avgs.append(avg)
        low += 1
        high += 1

    return avgs

# Test the above functions with example arrays
def test_fixed_window():
    arr1 = [2, 1, 5, 1, 3, 2]
    k1 = 3
    print("Max sum:", max_sum_fixed_window(arr1, k1))  # Expected: 9 (from window [5,1,3])
    print("Min sum:", min_sum_fixed_window(arr1, k1))  # Expected: 5 (from window [1,1,3])
    print("Averages:", average_fixed_window(arr1, k1))  # Expected: [2.67, 2.33, 3.0, 2.0]

    arr2 = [3000, 4500, 5000, 5500, 4000, 7000, 6500, 6000]
    k2 = 4
    print("Max sum:", max_sum_fixed_window(arr2, k2))  # Expected: 23500 (from window [7000, 6500, 6000])
    print("Min sum:", min_sum_fixed_window(arr2, k2))  # Expected: 18000 (from window [3000, 4500, 5000, 5500])
    print("Averages:", average_fixed_window(arr2, k2))  # Expected: list of averages for each 4-day window

if __name__ == "__main__":
    test_fixed_window()