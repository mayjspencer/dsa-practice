# ---- PREFIX SUM IMPLEMENTATION PRACTICE ----

def build_prefix_sum(arr):
    """
    Builds and returns the prefix sum array for the given input array.
    """
    prefix = [0] * (len(arr) + 1)
    prefix[0] = 0
    for i in range(len(arr)):
        prefix[i+1] = prefix[i] + arr[i]
    return prefix

def range_sum_query(prefix, l, r):
    """
    Given the prefix sum array and a range [l, r], returns the sum of that subarray.
    """
    return prefix[r+1] - prefix[l]
    pass


# --------------2D Prefix Sum--------------------- #

def build_prefix_sum_2d(matrix):
    """
    Builds and returns the 2D prefix sum matrix for the given 2D input array.
    """
    m = len(matrix)
    n = len(matrix[0]) if m > 0 else 0
    prefix = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n +1):
            if i == 0 or j == 0:
                continue
            else:
                prefix[i][j] = matrix[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

    return prefix


def range_sum_query_2d(prefix, r1, c1, r2, c2):
    """
    Returns the sum of the submatrix defined by (r1, c1) to (r2, c2)
    """
    return prefix[r2 +1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
    

# --------------Tests--------------------- #

def test_prefix_sum_2d():
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]
    prefix = build_prefix_sum_2d(matrix)

    # Query 1
    assert range_sum_query_2d(prefix, 2, 1, 4, 3) == 8

    # Query 2
    assert range_sum_query_2d(prefix, 1, 1, 2, 2) == 11

    # Query 3
    assert range_sum_query_2d(prefix, 0, 1, 1, 2) == 10

    print("All 2D prefix sum tests passed!")


# Uncomment to run tests
test_prefix_sum_2d()


def test_prefix_sum():
    # Test Case 1
    arr1 = [3, 2, 4, 5, 1]
    prefix1 = build_prefix_sum(arr1)
    assert range_sum_query(prefix1, 1, 3) == 11  # 2 + 4 + 5
    
    # Test Case 2
    arr2 = [10, 20, 30, 40, 50]
    prefix2 = build_prefix_sum(arr2)
    assert range_sum_query(prefix2, 0, 2) == 60  # 10 + 20 + 30
    assert range_sum_query(prefix2, 2, 4) == 120  # 30 + 40 + 50
    
    # Test Case 3
    arr3 = [1, -1, 3, -3, 5]
    prefix3 = build_prefix_sum(arr3)
    assert range_sum_query(prefix3, 0, 4) == 5  # 1 - 1 + 3 - 3 + 5
    assert range_sum_query(prefix3, 1, 3) == -1  # -1 + 3 - 3

    print("All tests passed!")


# Uncomment this line to run your tests
test_prefix_sum()
