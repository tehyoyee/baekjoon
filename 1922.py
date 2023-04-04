# 1922.py
# 23.04.04. 10:45 ~ x

import sys
input = sys.stdin.readline

def findRoot(x):
	if root[x] != x:
		root[x] = findRoot(root[x])
	return root[x]

N = int(input())
M = int(input())
graph = []
root = [i for i in range(N+1)]
for _ in range(M):
	s, e, v = map(int, input().split())
	graph.append([v, s, e])


result = 0
graph.sort()
for v, s, e in graph:
	sRoot = findRoot(s)
	eRoot = findRoot(e)
	if sRoot != eRoot:
		result += v
		if sRoot < eRoot:
			root[eRoot] = sRoot
		else:
			root[sRoot] = eRoot
 
print(result)

# 1   2
#   3   4
#     5   6
#
