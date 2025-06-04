# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

import math

def count_distinct_prime_factors(x):
    count = 0
    max_value =math.ceil(math.sqrt(x)) + 1

    for i in range(2, max_value):
        if x % i == 0:
            count += 1
            while x % i == 0:
                x //= i

    if x > 1:
        count += 1  # x itself is a prime > sqrt(x)
    return count

# Main logic using list comprehension + sum
n = int(input())
print(sum(1 for x in range(1, n + 1) if count_distinct_prime_factors(x) == 2))
