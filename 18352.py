# 18352.py
# 23.01.19. 19:43 ~ 21:00

import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
steps = [0] * (n + 1)
def bfs(i, k, x):
	q = [[i, 0]]
	while q:
		cur, s = q.pop(0)
		if steps[cur] == 0:
			steps[cur] = s
		for cur_ in graph[cur]:
			if cur_ != x and steps[cur_] == 0 and s < k:
				q.append([cur_, s + 1])
bfs(x, k, x)
flag = 0
for i in range(len(steps)):
	if steps[i] == k:
		flag+=1
		print(i)
if flag == 0:
	print(-1)


# import sys
# input = sys.stdin.readline

# n, m, k, x = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
# 	a, b = map(int, input().split())
# 	graph[a].append(b)
# step_graph = [float('inf')] * (n + 1)

# def dfs(x, k, steps):
# 	if steps > k:
# 		return
# 	if step_graph[x] > steps:
# 		step_graph[x] = steps
# 	for i in graph[x]:
# 		dfs(i, k, steps + 1)
# dfs(x, k, 0)
# flag = 0
# for i in range(len(step_graph)):
# 	if step_graph[i] == k:
# 		print(i)
# 		flag+=1
# if flag == 0:
# 	print(-1)