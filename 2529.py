# 2529.py
# 24.03.12. 19:00 ~ 19:20

import sys
input = sys.stdin.readline

def toNumber(x):
    result = 0
    for i in range(len(x)):
        result += x[i] * 10**(len(x) - i - 1)
    return result

def dfs(ci, path):
    global minResult, maxResult

    if len(path) == K + 1:
        x = toNumber(path)
        minResult = min(minResult, x)
        maxResult = max(maxResult, x)
        return
    for ni in range(10):
        if lst[len(path)-1] == '<' and ci >= ni:
            continue
        if lst[len(path)-1] == '>' and ci <= ni:
            continue
        if ni not in path: 
            path.append(ni)
            dfs(ni, path)
            path.pop()

global minResult, maxResult
minResult = 10000000000
maxResult = 0

K = int(input())
lst = list(input().split())

for i in range(10):
    dfs(i, [i])

print(maxResult)
for i in range(K + 1 - len(str(minResult))):
    print(0, end='')
print(minResult)
