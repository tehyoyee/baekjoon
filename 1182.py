# 1182.py
# 23.07.09. 17:33 ~ 18:10

import sys
input = sys.stdin.readline

global result

def dfs(v, idx, N, S):
	global result

	if v == S:
		result += 1
	for i in range(idx + 1, N):
		dfs(v + lst[i], i, N, S)

result = 0
N, S = map(int, input().split())
lst = list(map(int, input().split())) + [0]
visit = [False] * (N + 1)

for i in range(N):
	dfs(lst[i], i, N, S)
print(result)