# Quick Sort is a Divide-and-Conquer sorting algorithm.
# It works by selecting a 'pivot' element, partitioning the array such that
# elements less than pivot go to the left and greater go to the right, 
# and then recursively sorting the subarrays.

def quick_sort(arr, low, high):
    # Base case: If the subarray has one or zero elements, it's already sorted
    if low < high:
        # Partition the array and get the index of the pivot after partitioning
        pivot_index = partition(arr, low, high)

        # Recursively sort the subarray to the left of the pivot
        quick_sort(arr, low, pivot_index - 1)

        # Recursively sort the subarray to the right of the pivot
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # Choose the last element as the pivot
    pivot = arr[high]

    # `i` will mark the end of the "smaller than pivot" section
    i = low - 1

    # Iterate through the subarray from `low` to `high - 1`
    for j in range(low, high):
        # If current element is less than or equal to the pivot
        if arr[j] <= pivot:
            # Move the boundary of the smaller elements section
            i += 1
            # Swap current element with the element at index `i`
            arr[i], arr[j] = arr[j], arr[i]

    # After the loop, place the pivot in its correct position (after all smaller elements)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the index of the pivot
    return i + 1

# ------------------ TESTING ------------------

if __name__ == "__main__":
    test1 = [9, 3, 7, 4, 69, 420, 42]   # Random numbers
    test2 = [5, 4, 3, 2, 1]             # Reversed
    test3 = [1, 2, 3, 4, 5]             # Already sorted
    test4 = [10]                        # Single element

    # Run quick sort on each test case and print the sorted array
    for test in [test1, test2, test3, test4]:
        quick_sort(test, 0, len(test) - 1)
        print(test)
