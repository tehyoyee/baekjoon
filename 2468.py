# 2468 py

import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs_flood(graph, height, n):
	result = 0
	print(graph)
	for i in range(n):
		for j in range(n):
			if graph[i][j] <= height:
				continue
			result += 1
			queue = [[i, j]]
			graph[0][0] = 0
			while queue:
				x = queue[0][0]
				y = queue[0][1]
				queue.pop(0)
				for k in range(4):
					if 0 <= x + dx[k] < n and 0 <= y + dy[k] < n and graph[x + dx[k]][y + dy[k]] > height:
						queue.append([x + dx[k], y + dy[k]])
						graph[x + dx[k]][y + dy[k]] = 0
	return result
			

n = int(input())
graph = []
result = []
for _ in range(n):
	graph.append(list(map(int, input().split())))
for height in range(1, n + 1):
	result.append(bfs_flood(graph.deepcopy(), height, n))
print(result)