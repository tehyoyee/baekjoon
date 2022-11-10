# 1987.py

# set으로 해야 중복이 줄어 시간초과를 피한다.

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
graph = []
for _ in range(r):
	graph.append(list(input().rstrip()))

# len = 0
result = 0
q = set([(1, graph[0][0], 0, 0)])
while q:
	# len += 1
	print(q)
	steps, visit, i, j = q.pop()
	result = max(result, steps)
	for k in range(4):
		if 0 <= i + di[k] < r and 0 <= j + dj[k] < c:
			if graph[i + di[k]][j + dj[k]] not in visit:
				q.add((steps + 1, visit + graph[i + di[k]][j + dj[k]], i + di[k], j + dj[k]))
print(result)
# print(len)

# import sys
# input = sys.stdin.readline

# r, c = map(int, input().split())
# di = [1, -1, 0, 0]
# dj = [0, 0, 1, -1]
# graph = []
# for _ in range(r):
# 	graph.append(list(input().rstrip()))

# len = 0
# result = 0
# q = [[1, [graph[0][0]], 0, 0]]
# while q:
# 	len += 1
# 	print(q)
# 	steps, visit, i, j = q.pop(0)
# 	result = max(result, steps)
# 	for k in range(4):
# 		if 0 <= i + di[k] < r and 0 <= j + dj[k] < c:
# 			if graph[i + di[k]][j + dj[k]] not in visit:
# 				q.append([steps + 1, visit + [graph[i + di[k]][j + dj[k]]], i + di[k], j + dj[k]])
# print(result)
# print(len)