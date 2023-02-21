# 1325.py
# 23.02.20. 16:57 ~ 19, 22~ 윽.시간초과 default

import sys
input = sys.stdin.readline
from collections import deque

result = []
max_cnt = 0
def bfs(x):
	cnt = 0
	visit = [False] * (n + 1)
	visit[x] = 1
	q = deque([x])
	while q:
		c = q.popleft()
		cnt += 1
		for nc in graph[c]:
			if not visit[nc]:
				visit[nc] = True
				q.append(nc)
	return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    b, a = map(int, input().split())
    graph[a].append(b)
for i in range(1, n + 1):
	cnt = bfs(i)
	if cnt > max_cnt:
		max_cnt = cnt
		result = [i]
	elif cnt == max_cnt:
		result.append(i)
for x in result:
	print(x, end=" ")