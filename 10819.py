# 10819.py
# 24.3.11. 13:50 ~ 14:12

import sys
input = sys.stdin.readline
from copy import deepcopy

global result
result = 0

def dfs(idx, ci, acc, visit):
    global result
    if idx == N - 1:
        result = max(result, acc)
    for ni in range(N):
        if not visit[ni]:
            visit[ni] = True
            dfs(idx + 1, ni, acc + abs(lst[ci] - lst[ni]), visit)
            visit[ni] = False
    return result

N = int(input())

lst = list(map(int, input().split()))

for i in range(N):
    v = [False] * N
    v[i] = True
    result = max(result, dfs(0, i, 0, deepcopy(v)))

print(result)
