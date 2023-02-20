# 1325.py
# 23.02.20. 16:57 ~ 19, 22~

import sys
input = sys.stdin.readline
from collections import deque

result = [0, []]

def bfs(x):
	visit = [False] * (n + 1)
	visit[x] = 1
	q = deque([[x, 1]])
	while q:
		c, l = q.popleft()
		for y in graph[c]:
			if not visit[y]:
				visit[y] = True
				q.append([y, l + 1])
	if l > result[0]:
		result[0] = l
		result[1] = [x]
	elif l == result[0]:
		result[1].append(x)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    b, a = map(int, input().split())
    graph[a].append(b)
for i in range(1, n + 1):
	bfs(i)
for x in result[1]:
	print(x, end=" ")