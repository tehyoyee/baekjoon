# 1717.py

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def union_parent(b, c):
	b = find_parent(b)
	c = find_parent(c)
	parent[max(b, c)] = min(b, c)

def find_parent(x):
	if parent[x] == x:
		return x
	parent[x] = find_parent(parent[x])
	return parent[x]

n, m = map(int, input().split())
parent = [x for x in range(n + 1)]
for _ in range(m):
	a, b, c = map(int, input().split())
	if a == 0:
		union_parent(b, c)
	else:
		find_parent(b)
		find_parent(c)
		if parent[b] == parent[c]:
			print("YES")
		else:
			print("NO")
	print(parent)