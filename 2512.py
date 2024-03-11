# 2512.py
# 24.3.11. 11:18 ~ 11:38

import sys
input = sys.stdin.readline

N = int(input())
budget = list(map(int, input().split()))
limit = int(input())
start = 0
end = max(budget)
result = 0

while start <= end:
    mid = (start + end) // 2
    acc = 0
    upDown = 0
    for x in budget:
        if mid <= x:
            acc += mid
        else:
            acc += x
    if limit == acc:
        result = mid
        break
    elif limit < acc:
        end = mid - 1
        result = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
