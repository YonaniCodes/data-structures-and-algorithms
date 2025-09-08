# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

def find_number(size, count, sequence):
    sequence.sort()
    if count == 0:
        return sequence[0] - 1 if sequence[0] > 1 else -1
    if count == size:
        return sequence[-1]
    if sequence[count - 1] < sequence[count]:
        return sequence[count - 1]
    return -1


n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(find_number(n, k, arr))

