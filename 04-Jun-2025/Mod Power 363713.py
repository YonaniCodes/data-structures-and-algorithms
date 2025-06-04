# Problem: Mod Power - https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read input values
a = int(input())
b = int(input())
m = int(input())

# First line: a to the power of b
print(pow(a, b))

# Second line: (a to the power of b) modulo m
print(pow(a, b, m))
