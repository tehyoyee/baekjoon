# 11724 py

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
	result = 0
	for x in range(1, n + 1):
		if visited[x]:
			continue
		result += 1
		queue = deque([x])
		visited[x] = True
		while queue:
			x = queue.popleft()
			for i in graph[x]:
				if not visited[i]:
					queue.append(i)
					visited[i] = True
	print(str(result))

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
visited = [False] * (n + 1)

bfs()
