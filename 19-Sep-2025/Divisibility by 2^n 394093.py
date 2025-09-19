# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    needed = n
    twos = 0

    
    for num in arr:
        while num % 2 == 0:
            num //= 2
            twos += 1

    if twos >= needed:
        print(0)
        continue

    
    contrib = []
    for i in range(1, n+1):
        val = 0
        temp = i
        while temp % 2 == 0:
            temp //= 2
            val += 1
        if val > 0:
            contrib.append(val)

   
    contrib.sort(reverse=True)

    op = 0
    for c in contrib:
        twos += c
        op += 1
        if twos >= needed:
            print(op)
            break
    else:
        print(-1)