# 2660.py
# 23.03.13. 11:01 ~ 11:18

# 5
# 1 2
# 2 3
# 3 4
# 4 5
# 2 4
# 5 3
# -1 -1
#     5
# 1 2 3 4 5
#   4     3


def bfs(i):
	q = deque([[i, 0]])
	visit[i] = True
	while q:
		ci, steps = q.popleft()
		for ni in graph[ci]:
			if not visit[ni]:
				visit[ni] = True
				q.append([ni, steps + 1])
	return steps

import sys
from collections import deque
input = sys.stdin.readline

resultCnt = 50
result = []
N = int(input())
graph = [[] for _ in range(N + 1)]
while True:
	a, b = map(int, input().split())
	if a == -1 and b == -1:
		break
	else:
		graph[a].append(b)
		graph[b].append(a)

for i in range(1, N + 1):
	visit = [False] * (N + 1)
	tmp = bfs(i)
	if resultCnt > tmp:
		resultCnt = tmp
		result = [i]
	elif resultCnt == tmp:
		result.append(i)
print(resultCnt, len(result))
print(*result)