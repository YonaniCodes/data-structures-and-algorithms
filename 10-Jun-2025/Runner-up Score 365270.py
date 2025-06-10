# Problem: Runner-up Score - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    first= float("-inf")
    second= float("-inf")+1
    
for score in arr:
    if score > first:
        # New highest found, update second to old first
        second = first
        first = score
    elif first > score > second:
        # Score is between first and second, update second
        second = score

print(second)