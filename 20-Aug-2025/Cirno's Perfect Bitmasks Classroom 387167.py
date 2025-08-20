# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input().strip())
for _ in range(t):
    x = int(input().strip())
    if x==1: 
        print(3)
    else:
        lsb = x & (-x)  
        if x & (x - 1)== 0: 
            print(x + 1)
        else:
            print(lsb)