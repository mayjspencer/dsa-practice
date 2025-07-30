# Sorting Algorithms Practice

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        minindex = i

        for j in range(i + 1, n):
            if arr[j] < arr[minindex]:
                minindex = j
        
        arr[i], arr[minindex] = arr[minindex], arr[i]

def test_basic_sorts():
    arrays = [
        [5, 2, 4, 6, 1, 3],
        [],
        [1],
        [2, 1],
        [3, 3, 3],
    ]

    for arr in arrays:
        arr1, arr2, arr3 = arr[:], arr[:], arr[:]

        bubble_sort(arr1)
        insertion_sort(arr2)
        selection_sort(arr3)

        assert arr1 == sorted(arr)
        assert arr2 == sorted(arr)
        assert arr3 == sorted(arr)

    print("Basic sorts tests passed.")

# Uncomment to test after implementation
test_basic_sorts()
