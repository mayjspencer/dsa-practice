def max_sum_fixed_window(arr, k):
    low = 0
    high = k
    sum = 0
    for i in range(low, high):
            sum += arr[i]
    maxsum = sum
    while high <= len(arr):
        sum = 0
        for i in range(low, high):
            sum += arr[i]
        if sum > maxsum:
            maxsum = sum
        low += 1
        high += 1
    return maxsum

def min_sum_fixed_window(arr, k):
    low = 0
    high = k
    sum = 0
    for i in range(low, high):
            sum += arr[i]
    minsum = sum
    while high <= len(arr):
        sum = 0
        for i in range(low, high):
            sum += arr[i]
        if sum < minsum:
            minsum = sum
        low += 1
        high += 1
    return minsum

def average_fixed_window(arr, k):
    low = 0
    high = k
    avgs = []
    while high <= len(arr):
        sum = 0
        for i in range(low, high):
            sum += arr[i]
        avg = sum / k
        avgs.append(avg)
        low += 1
        high += 1
    return avgs

# Test cases
def test_fixed_window():
    arr1 = [2, 1, 5, 1, 3, 2]
    k1 = 3
    print("Max sum:", max_sum_fixed_window(arr1, k1))  # Expected: 9
    print("Min sum:", min_sum_fixed_window(arr1, k1))  # Expected: 5 (from window [1,1,3])
    print("Averages:", average_fixed_window(arr1, k1))  # Expected: [2.67, 2.33, 3.0, 2.0]

    arr2 = [3000, 4500, 5000, 5500, 4000, 7000, 6500, 6000]
    k2 = 4
    print("Max sum:", max_sum_fixed_window(arr2, k2))  # Expected: 19000
    print("Min sum:", min_sum_fixed_window(arr2, k2))  # Expected: 18000
    print("Averages:", average_fixed_window(arr2, k2))  # Expected: list of averages for each window

if __name__ == "__main__":
    test_fixed_window()
