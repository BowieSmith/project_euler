# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# Given location (m, n) (top left) in grid, return number of possible paths to
# get to location (0, 0) (bottom right)
# Key insight. num_paths(m, n) = num_paths(m - 1, n) + num_paths(m, n - 1)
# Memoize solutions in dict
def num_paths(m, n):
    memo_dict = {}
    def helper(m, n):
        if m == 0 or n == 0:
            return 1
        if (m, n) in memo_dict:
            return memo_dict[(m, n)]
        memo_dict[(m, n)] = helper(m - 1, n) + helper(m, n - 1)
        return memo_dict[(m, n)]
    return helper(m, n)

if __name__ == "__main__":
    ans = num_paths(20, 20)
    print(ans)
