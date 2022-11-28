# 1939.py

import sys
input = sys.stdin.readline

def find_parent(x):
	if parent[x] == x:
		return x
	else:
		parent[x] = find_parent(parent[x])
	return parent[x]

def union_parent(a, b):
	a = find_parent(a)
	b = find_parent(b)
	parent[max(a, b)] = min(a, b)

n, m = map(int, input().split())
parent = [x for x in range(n + 1)]
graph = []
for i in range(m):
	a, b, c = map(int, input().split())
	graph.append([c, a, b])
m, n = map(int, input().split())
graph.sort(reverse=True)
for x in graph:
	union_parent(x[1], x[2])
	if find_parent(n) == find_parent(m):
		print(x[0])
		break