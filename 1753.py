# 1753.py

import sys
import math
input = sys.stdin.readline

v, e = map(int, input().split())
s = int(input())
graph = [[] for _ in range(v + 1)]
w = [math.inf for _ in range(v + 1)]
for _ in range(e):
	a, b, c = map(int, input().split())
	graph[a].append([b, c])

w[s] = 0
q = [[s, 0]]
while q:
	cur, cur_w = q.pop(0)
	if w[cur] < cur_w:
		continue
	for x in graph[cur]:
		if w[x[0]] > cur_w + x[1]:
			q.append([x[0], cur_w + x[1]])

for x in range(1, v + 1):
	print("INF") if w[x] == math.inf else print(w[x])




# import sys
# import math
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def dfs(cur):
# 	print(cur)
# 	for x in graph[cur]:
# 		if w[x[0]] < w[cur] + x[1]:
# 			continue
# 		w[x[0]] = w[cur] + x[1]
# 		dfs(x[0])

# v, e = map(int, input().split())
# s = int(input())
# graph = [[] for _ in range(v + 1)]
# w = [math.inf for _ in range(v + 1)]
# for _ in range(e):
# 	a, b, c = map(int, input().split())
# 	graph[a].append([b, c])

# w[s] = 0
# dfs(s)
# for x in range(1, v + 1):
# 	print("INF") if w[x] == math.inf else print(w[x])