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
	dp = [0] * (N + 1)
	for i in range(K):
		a, b = map(int, input().split())
		graph[a].append(b)
		dp[b] += 1
	W = int(input())
	q = deque([])
	for i in range(1, N + 1):
		if dp[i] == 0:
			q.append([i, 0])
	while q:
		ci, t = q.popleft()
		if ci == W:
			W = t
			break
		for ni in graph[ni]:
			d
	print(q)