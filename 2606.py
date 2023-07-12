# 2606.py
# 23.07.08. 00:45 ~

import sys
input = sys.stdin.readline
from collections import deque

# N = int(input())
# M = int(input())

# result = 0
# graph = [[] for _ in range(N + 1)]
# visit = [False] * (N + 1)

# for _ in range(M):
# 	a, b = map(int, input().split())
# 	graph[a].append(b)
# 	graph[b].append(a)

# q = deque([1])
# visit[1] = True
# while q:
# 	ci = q.popleft()
# 	for ni in graph[ci]:
# 		if not visit[ni]:
# 			result += 1
# 			visit[ni] = True
# 			q.append(ni)

# print(result)



def find(x):
	if parent[x] == x:
		return x
	parent[x] = find(parent[x])
	return parent[x]

def union(a, b):
	a = find(a)
	b = find(b)
	if a > b:
		parent[a] = b
	else:
		parent[b] = a

result = 0
N = int(input())
M = int(input())
parent = [i for i in range(N+1)]
for _ in range(M):
	a, b = map(int, input().split())
	union(a, b)
for i in range(2, N + 1):
	find(i)
for i in range(2, N + 1):
	if parent[i] == 1:
		result += 1
print(result)









# import sys
# #7
# read_ints = lambda:list(map(int, sys.stdin.readline().rstrip().split()))
# read_int = lambda:read_ints()[0]

# N = read_int()
# M = read_int()
# parent = [i for i in range(N+1)]
# lst = [read_ints() for _ in range(M)]

# def find(x):
#     if parent[x] == x:
#         return x
#     parent[x] = find(parent[x])
#     return parent[x]

# def union(a, b):
#     a = find(a)
#     b = find(b)
#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a
#     return

# def solution():
#     for a, b in lst:
#         union(a, b)
#     for i in range(1, N+1):
#         find(i)
#     cnt = 0
#     for i in range(2, N+1):
#         if parent[i] == 1:
#             cnt += 1
#     print(cnt)
#     return

# solution()