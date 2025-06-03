# Problem: Domino Piling - https://codeforces.com/problemset/problem/50/A

import math

# Read input values
n, m = map(int, input().split())

 

rectangle_area= m*n

 
total_tiles =  rectangle_area//2

# Output the result
print(total_tiles)
