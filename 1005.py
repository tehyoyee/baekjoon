# 1005.py
# 23.04.02. 18:55 ~

import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
	N, K = map(int, input().split())
	buildings = [0] + list(map(int, input().split()))
	graph = [[] for _ in range(N + 1)]
	flag = [0] * (N + 1)
	dp = [0] * (N + 1)
	for _ in range(K):
		a, b = map(int, input().split())
		graph[a].append(b)
		flag[b] += 1
	target = int(input())
	q = deque([])
	for i in range(1, N + 1):
		if flag[i] == 0:
			q.append((i, buildings[i]))
	tmp = []
	for i, j in q:
		if i == target:
			tmp.append(j)
	if len(tmp) > 0:
		print(min(tmp))
	else:
		while q:
			cur, cost = q.popleft()
			if cur == target:
				dp[cur] = min(cost, dp[cur])
			for new in graph[cur]:
				flag[new] -= 1
				dp[new] = max(dp[new], cost + buildings[new])
				if flag[new] > 0:
					continue
				else:
					q.append([new, cost + dp[new]])
		print(dp[target])