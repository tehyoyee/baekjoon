# 1778.py

import sys
input = sys.stdin.readline

def union_parent(a, b):
	a = find_parent(a)
	b = find_parent(b)
	parent[max(a,b)] = min(a,b)
def find_parent(x):
	if parent[x] == x:
		return x
	parent[x] = find_parent(parent[x])
	return parent[x]

k = 0
while True:
	k += 1
	result = 0
	n, m = map(int, input().split())
	if n == 0 and m == 0:
		break
	parent = [x for x in range(n + 1)]
	check = [0] * (n + 1)
	for _ in range(m):
		a, b = map(int, input().split())
		union_parent(a, b)
	for i in range(1, n + 1):
		parent[i] = find_parent(i)
	parents = set(parent)
	print("Case %d: %d" %(k, len(parents) - 1))



## dfs

# import sys
# input = sys.stdin.readline

# def dfs(i):
# 	check[i] = 1
# 	for x in parent[i]:
# 		if not check[x]:
# 			dfs(x)
# k = 0
# while True:
# 	result = 0
# 	k += 1
# 	n, m = map(int, input().split())
# 	if n == 0 and m == 0:
# 		break
# 	parent = [[] for _ in range(n + 1)]
# 	check = [0] * (n + 1)
# 	for _ in range(m):
# 		a, b = map(int, input().split())
# 		parent[a].append(b)
# 		parent[b].append(a)
# 	for i in range(1, n + 1):
# 		if not check[i]:
# 			dfs(i)
# 			result += 1
# 	print("Case %d: %d" %(k, result))