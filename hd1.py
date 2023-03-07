import sys
input = sys.stdin.readline
from collections import deque

result = 0
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
s, t = map(int, input().split())
v1 = [0] * (n + 1)
v2 = [0] * (n + 1)

def dfs(x, v, target):
	if x == target:
		return 2
	for nx in graph[x]:
		if not v[nx] or nx == target:
			v[nx] = 1	
			v[x] = dfs(nx, v, target)
	return v[x]

v1[s], v2[t] = 1, 1
dfs(s, v1, t)
dfs(t, v2, s)
for i in range(1, n + 1):
	if v1[i] == 2 and v2[i] == 2:
		result += 1
		print(i, end=" ")
print()
print(result)


# q = deque([s])
# v1[s] = True
# while q:
# 	ci = q.popleft()
# 	for ni in graph[ci]:
# 		if not v1[ni] and ni != t:
# 			v1[ni] = True
# 			q.append(ni)
# q = deque([t])
# v2[t] = True
# while q:
# 	ci = q.popleft()
# 	for ni in graph[ci]:
# 		if not v2[ni] and ni != s:
# 			v2[ni] = True
# 			q.append(ni)

# for i in range(1, n + 1):
# 	if v1[i] and v2[i]:
# 		result += 1
# 		print(i)
# print(result)
















# n, m = map(int, input().split())
# table = [[False] * 4 for _ in range(m)]
# candi = []
# s = []
# for _ in range(n):
# 	s.append(list(input().rstrip()))
# print(s)
# for j in range(m):
# 	for i in range(n):
# 		if s[i][j] == 'a':
# 			table[j][0] = True
# 		elif s[i][j] == 'c':
# 			table[j][1] = True
# 		elif s[i][j] == 'g':
# 			table[j][2] = True
# 		elif s[i][j] == 't':
# 			table[j][3] = True
# print(table)