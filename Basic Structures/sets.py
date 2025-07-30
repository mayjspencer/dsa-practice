# === Problem 1: Remove Duplicates from List ===
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# === Problem 2: Check Subset ===
def is_subset(small, big):
    """
    Return True if set `small` is a subset of set `big`, else False.
    
    Example: {1,2} is subset of {1,2,3} -> True
    """
    # Your code here
    intersection = small & big
    if intersection == small:
        return True
    else:
        return False


# === Problem 3: Set Operations ===
def set_operations(a, b):
    """
    Return a tuple of four sets:
    (union, intersection, difference, symmetric_difference)
    
    Example:
    a = {1, 2, 3}, b = {2, 3, 4}
    returns ({1,2,3,4}, {2,3}, {1}, {1,4})
    """
    # Your code here
    union = a | b
    intersection = a & b
    difference = a - b
    symdif = a ^ b
    return (union, intersection, difference, symdif)


# === Problem 4: Find Common Elements in Multiple Lists ===
def common_elements(lists):
    """
    Given a list of lists, return the set of elements common to all.
    
    Example:
    [[1,2,3], [2,3,4], [2,5]] -> {2}
    """
    # Your code here
    s = set(lists[0])
    for i in range(1, len(lists)):
        temps = set(lists[i])
        s = s & temps

    return s
        


# === Main Test Runner ===
if __name__ == "__main__":
    print("Problem 1:", remove_duplicates([1, 2, 2, 3, 1]))
    print("Problem 2:", is_subset({1, 2}, {1, 2, 3}))
    print("Problem 3:", set_operations({1, 2, 3}, {2, 3, 4}))
    print("Problem 4:", common_elements([[1, 2, 3], [2, 3, 4], [2, 5]]))
