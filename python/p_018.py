# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# parse triangle text into two-dimensional list
def parse_triangle(t):
    rows = t.strip().split('\n')
    rows = [list(map(int, row.split())) for row in rows]
    return rows

# use dynamic programming to find max path
# key insight:
#   max_path(row, col) = tri[row][col] + max(max_path(row + 1, col), max_path(row + 1, col + 1))
def max_path(t):
    max_path_dict = {}
    last_row = len(t) - 1
    # initialize math_path for last row
    for col in range(len(t)):
        max_path_dict[(last_row, col)] = t[last_row][col]
    for row in range(len(t) - 2, -1, -1):
        for col in range(row + 1):
            max_path_dict[(row, col)] = t[row][col] + max(
                    [max_path_dict[(row + 1, col)], max_path_dict[(row + 1, col + 1)]])
    return max_path_dict[(0, 0)]

if __name__ == "__main__":
    tri = parse_triangle('''
        75
        95 64
        17 47 82
        18 35 87 10
        20 04 82 47 65
        19 01 23 75 03 34
        88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
        41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
        63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    ''')
    ans = max_path(tri)
    print(ans)
