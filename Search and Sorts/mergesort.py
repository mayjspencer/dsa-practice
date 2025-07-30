def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: a single-element array is already sorted

    # Step 1: Divide
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])   # Recursively sort left half
    right_half = merge_sort(arr[mid:])  # Recursively sort right half

    # Step 2: Conquer (Merge the two halves)
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Compare elements from left and right halves and build sorted array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Append any remaining elements from left or right
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

# Example test
arr = [5, 2, 9, 1, 5, 6]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
