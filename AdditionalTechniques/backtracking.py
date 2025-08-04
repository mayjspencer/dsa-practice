# ---- EASY BACKTRACKING PRACTICE ----

def run_easy_tests():
    print("Easy Problem 1 (Binary Strings):", problem_easy_1_binary_strings())
    print("Easy Problem 2 (Sum ≤ Target):", problem_easy_2_sum_to_max())


# --------------------------------------------------
# Easy Problem 1:
# Generate all binary strings of length n = 2.
# Example output: ['00', '01', '10', '11']
def problem_easy_1_binary_strings():
    result = []
    n = 2

    def backtrack(path):
        # ✅ Base case: length is 2 → record result
        if len(path) == n:
            result.append("".join(path))  # Join into a string like "01"
            return

        # ✅ Choices: binary digits '0' and '1'
        for digit in ['0', '1']:
            path.append(digit)      # Choose
            backtrack(path)         # Explore
            path.pop()              # Backtrack (undo)

    backtrack([])
    return result



# --------------------------------------------------
# Easy Problem 2:
# Use numbers [1, 2] to build combinations with sum ≤ 3.
# Allow reuse of numbers. Example output: [[], [1], [2], [1,1], [1,2], ...]
def problem_easy_2_sum_to_max():
    result = []
    candidates = [1, 2]
    max_total = 3

    def backtrack(path, total):
        if total > max_total:
            return
        
        result.append(path[:])

        for num in candidates:
            path.append(num)
            backtrack(path, total + num)
            path.pop()


    backtrack([], 0)
    return result


if __name__ == "__main__":
    run_easy_tests()

# ---- Easy Backtracking Practice: Two Problems ----

def run_easy_3_and_4_tests():
    print("Easy Problem 3 (Generate Parentheses):", problem_easy_3_generate_parentheses(2))
    print("Easy Problem 4 (Letter Case Permutation):", problem_easy_4_letter_case_permutation("a1b"))

# --------------------------------------------------
# Easy Problem 3:
# Generate all combinations of balanced parentheses with n pairs.
# Example for n=2: ["(())", "()()"]
def problem_easy_3_generate_parentheses(n):
    result = []

    def backtrack(path, open_count, close_count):
        if len(path) == 2 * n:
            result.append(path)
            return
        
        if open_count < n:
            backtrack(path + '(', open_count + 1, close_count)
        
        if close_count < open_count:
            backtrack(path + ')', open_count, close_count + 1)

    backtrack("", 0, 0)
    return result


# --------------------------------------------------
# Easy Problem 4:
# Given a string with letters and digits, return all possible letter case permutations.
# Example: "a1b" → ["a1b", "A1b", "a1B", "A1B"]
def problem_easy_4_letter_case_permutation(s):
    result = []

    def backtrack(index, path):
        # TODO: Implement backtracking for letter case permutations
        if index == len(s):
            result.append(path)
            return
    
        if s[index].isalpha():
            backtrack(index + 1, path + s[index].upper())
            backtrack(index + 1, path + s[index].lower())
        else:
            backtrack(index + 1, path + s[index])

    backtrack(0, "")
    return result

if __name__ == "__main__":
    run_easy_3_and_4_tests()
