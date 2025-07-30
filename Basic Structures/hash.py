class BadHash:
    def __init__(self, val):
        self.val = val
    def __hash__(self):
        return 42  # Force all keys to collide
    def __eq__(self, other):
        return self.val == other.val

d = {}
d[BadHash("a")] = 1
d[BadHash("b")] = 2
d[BadHash("c")] = 3
print(d)


# === Problem 1: Character Frequency ===
def char_frequency(s):
    """
    Return a dictionary mapping each character in the string `s`
    to the number of times it appears.
    
    Example: "hello" → {'h':1, 'e':1, 'l':2, 'o':1}
    """
    # Your code here
    d = {}
    for char in s:
        d[char] = d.get(char,0) + 1
    
    return d


# === Problem 2: First Non-Repeating Character ===
def first_unique_char(s):
    """
    Return the first non-repeating character in the string `s`.
    If none exists, return None.

    Example: "swiss" → 'w'
    """
    # Your code here
    d = {}
    for char in s:
        d[char] = d.get(char,0) + 1

    for key in d.keys():
        if d[key] == 1:
            return key
    
    return None


# === Problem 3: Group by Remainder ===
def group_by_remainder(nums, divisor):
    """
    Group numbers in the list by their remainder when divided by `divisor`.
    
    Example: [1, 2, 3, 4, 5], divisor=3 → {1: [1, 4], 2: [2, 5], 0: [3]}
    """
    # Your code here
    d = {}
    for num in nums:
        numdiv = num % divisor
        templst = d.get(numdiv,[])
        templst.append(num)
        d[numdiv] = templst
    return d


# === Problem 4: Invert Dictionary ===
def invert_dict(d):
    """
    Given a dictionary `d`, return a new dictionary where keys become values
    and values become keys. Assume all values are unique.

    Example: {'a': 1, 'b': 2} → {1: 'a', 2: 'b'}
    """
    # Your code here
    d2 = {}
    for key, value in d.items():
        d2[value] = key
    return d2


# === Problem 5: Merge Dictionaries with Sums ===
def merge_dicts_sum(dict1, dict2):
    """
    Merge two dictionaries by summing values of common keys.
    
    Example:
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    → {'a': 1, 'b': 5, 'c': 4}
    """
    d = {}
    for key in dict1.keys():
        d[key] = dict1[key]

    for key in dict2.keys():
        d[key] = d.get(key, 0) + dict2[key]
    
    return d



# === Main Test Runner ===
if __name__ == "__main__":
    print("Problem 1:", char_frequency("hello"))
    print("Problem 2:", first_unique_char("swiss"))
    print("Problem 3:", group_by_remainder([1, 2, 3, 4, 5], 3))
    print("Problem 4:", invert_dict({'a': 1, 'b': 2}))
    print("Problem 5:", merge_dicts_sum({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
