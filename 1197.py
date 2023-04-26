# 1197.py
# 23.04.26.

import sys
input = sys.stdin.readline

def findRoot(x):
	if x != root[x]:
		root[x] = findRoot(root[x])
	return root[x]

V, E = map(int, input().split())
graph = []
root = [i for i in range(V + 1)]
for _ in range(E):
	a, b, c = map(int, input().split())
	graph.append([a, b, c])
graph.sort(key=lambda x:x[2])
result = 0

for s, e, w in graph:
	sRoot = findRoot(s)
	eRoot = findRoot(e)
	if sRoot != eRoot:
		if sRoot > eRoot:
			root[sRoot] = eRoot
		else:
			root[eRoot] = sRoot
		result += w

print(result)