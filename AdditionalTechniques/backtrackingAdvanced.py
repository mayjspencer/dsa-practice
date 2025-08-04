# ---- BACKTRACKING + PRUNING PRACTICE ----

def run_tests():
    print("Problem 1 (Combinations to Target) Output:", problem1_combinations_to_target())
    print("Problem 2 (Unique Subsets) Output:", problem2_unique_subsets())
    print("Problem 3 (Permutations No Repeats) Output:", problem3_permutations_no_repeats())

# -------------------------------------
# 1. Find all combinations of numbers that sum to target (target = 7)
#    You can use numbers from [2, 3, 6, 7], each unlimited times.
#    Prune when total > target.
def problem1_combinations_to_target():
    result = []
    candidates = [2, 3, 6, 7]
    target = 7

    def backtrack(path, start, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(path, i, total + candidates[i])
            path.pop()

    backtrack([], 0, 0)
    return result

# -------------------------------------
# 2. Find all unique subsets from [1, 2, 2]
#    Avoid duplicate subsets using pruning.
#    Prune repeated values at the same tree level.
def problem2_unique_subsets():
    result = []
    nums = [1, 2, 2]
    nums.sort()  # important for duplicate skipping

    def backtrack(start, path):
        # TODO: Backtrack, and skip duplicates when nums[i] == nums[i-1]
        result.append(path[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()


    backtrack(0, [])
    return result

# -------------------------------------
# 3. Find all permutations of [1, 2, 3]
#    No element can be reused in a single permutation.
#    Use a visited array to prune repeats.
def problem3_permutations_no_repeats():
    result = []
    nums = [1, 2, 3]
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            backtrack(path)
            path.pop()
            used[i] = False


    backtrack([])
    return result


if __name__ == "__main__":
    run_tests()
