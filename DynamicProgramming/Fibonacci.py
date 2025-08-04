# ----------------- FIBONACCI PRACTICE -----------------

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


def fib_tab(n):
    if n == 0:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def test_fibonacci():
    print("Testing Fibonacci")
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(5) == 5
    assert fib(10) == 55

    assert fib_tab(0) == 0
    assert fib_tab(1) == 1
    assert fib_tab(6) == 8
    assert fib_tab(20) == 6765
    print("All Fibonacci tests passed!")

if __name__ == "__main__":
    test_fibonacci()
# ------------------------------------------------------
