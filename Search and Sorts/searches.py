# === Linear Search Problems ===

def linear_search(arr, target):
    """
    Return the index of target in arr, or -1 if not found.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i


def linear_search_all_indexes(arr, target):
    """
    Return a list of all indexes where target appears in arr.
    Return empty list if target not found.
    """
    lst = []
    for i in range(len(arr)):
        if arr[i] == target:
            lst.append(i)


def linear_search_minimum(arr):
    """
    Return the minimum value in arr using linear search.
    """
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min.append(arr[i])

# === Binary Search Problems ===

def binary_search_iterative(arr, target):
    """
    Iterative binary search.
    Return index of target in arr or -1 if not found.
    Assumes arr is sorted.
    """
    low = 0
    high = len(arr) - 1

    while low<=high:
        mid = (low+high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            low = mid + 1
        else:
            high = mid -1

    return -1


def binary_search_recursive(arr, target, low, high):
    """
    Recursive binary search.
    Return index of target or -1 if not found.
    Assumes arr is sorted.
    """
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)



def binary_search_first_occurrence(arr, target):
    """
    Return index of first occurrence of target in sorted arr with duplicates.
    Return -1 if target not found.
    """
    pass


def test_binary_search_on_unsorted():
    """
    Test what happens if binary search is run on an unsorted array.
    Return the index if found, else -1.
    """
    pass


# === TESTS ===
if __name__ == "__main__":
    arr_sorted = [1, 2, 2, 4, 5, 5, 7, 9]
    arr_unsorted = [4, 2, 9, 1, 7]

    # Add your tests here to verify your solutions
