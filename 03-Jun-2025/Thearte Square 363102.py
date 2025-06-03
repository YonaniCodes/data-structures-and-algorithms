# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

import math

# Read input values
n, m, a = map(int, input().split())

# Use math.ceil to compute the number of flagstones needed in each direction
tiles_along_length = math.ceil(n / a)
tiles_along_width = math.ceil(m / a)

# Calculate total number of flagstones
total_tiles = tiles_along_length * tiles_along_width

# Output the result
print(total_tiles)
