# 1976.py
# 23.07.11. 12:42 ~

import sys
input = sys.stdin.readline

def findRoot(x):
	if x != root[x]:
		root[x] = findRoot(root[x])
	return root[x]

N = int(input())
graph = [[] for _ in range(N + 1)]
root = [i for i in range(N + 1)]
M = int(input())
for i in range(1, N + 1):
	tmp = list(map(int, input().split()))
	for j in range(N):
		if tmp[j]:
			graph[i].append(j + 1)
plan = list(map(int, input().split()))

for i in range(1, N+1):
	for j in graph[i]:
		x = findRoot(i)
		y = findRoot(j)
		if x > y:
			root[x] = y
		else:
			root[y] = x

tmp = root[min(plan)]

for x in plan:
	if tmp != root[x]:
		print("NO")
		break
else:
	print("YES")