# 2887.py
# 23.07.09. 22:19 ~

import sys
input = sys.stdin.readline

def findRoot(x):
	if x != root[x]:
		root[x] = findRoot(root[x])
	return root[x]

N = int(input())
pos = []
costs = []
xlst = []
ylst = []
zlst = []
for i in range(N):
	a, b, c = map(int, input().split())
	xlst.append((a, i))
	ylst.append((b, i))
	zlst.append((c, i))

xlst.sort()
ylst.sort()
zlst.sort()
for i in range(N - 1):
	costs.append((abs(xlst[i][0] - xlst[i + 1][0]), xlst[i][1], xlst[i + 1][1]))
	costs.append((abs(ylst[i][0] - ylst[i + 1][0]), ylst[i][1], ylst[i + 1][1]))
	costs.append((abs(zlst[i][0] - zlst[i + 1][0]), zlst[i][1], zlst[i + 1][1]))

root = [i for i in range(N)]
visit = [False] * N
result = 0
costs.sort()
for cost, a, b in costs:
	s = findRoot(a)
	e = findRoot(b)
	if s != e:
		if s > e:
			root[s] = e
		else:
			root[e] = s
		result += cost

print(result)
