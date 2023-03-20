# 1167.py
# 23.03.20. 10:45 ~ 11:50

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i):
	for ni, cost in graph[i]:
		if visit[ni] == -1:
			visit[ni] = visit[i] + cost
			dfs(ni)

result = 0
V = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(1, V + 1):
	j = 1
	tmp = list(map(int, input().split()))
	while tmp[j] != -1:
		graph[tmp[0]].append([tmp[j], tmp[j + 1]])
		j += 2

visit = [-1] * (V + 1)
visit[1] = 0
dfs(1)
start = 0
for i in range(2, V + 1):
	if visit[start] < visit[i]:
		start = i
visit = [-1] * (V + 1)
visit[start] = 0
dfs(start)
print(max(visit))

