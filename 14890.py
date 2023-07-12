# 14890.py
# 23.04.04. 3시간 정도 품... 빡구현 문제

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
graph = []
for _ in range(N):
	graph.append(list(map(int, input().split())))
result = 0

def ascendingX(i, j, v):
	for k in range(1, L + 1):
		if visit[i][j - k + 1] or graph[i][j - k + 1] != v:
			return False
		visit[i][j - k + 1] = True
	return True

def ascendingY(i, j, v):
	for k in range(1, L + 1):
		if visit[i - k + 1][j] or graph[i - k + 1][j] != v:
			return False
		visit[i - k + 1][j] = True
	return True

def descendingX(i, j, v):
	for k in range(1, L + 1):
		if visit[i][j + k] or graph[i][j + k] != v:
			return False
		visit[i][j + k] = True
	return True

def descendingY(i, j, v):
	for k in range(1, L + 1):
		if visit[i + k][j] or graph[i + k][j] != v:
			return False
		visit[i + k][j] = True
	return True

# visit = [[False] * N for _ in range(N)]

for i in range(N):
	for j in range(N):
		if j == N - 1:
			result += 1
		elif graph[i][j + 1] == graph[i][j]:
			continue
		elif graph[i][j + 1] + 1 == graph[i][j]:
			if j + L >= N:
				break
			if not descendingX(i, j, graph[i][j + 1]):
				break
		elif graph[i][j + 1] - 1 == graph[i][j]:
			if j - L + 1 < 0:
				break
			if not ascendingX(i, j, graph[i][j]):
				break
		else:
			break

visit = [[False] * N for _ in range(N)]
print()
for j in range(4,5):
	for i in range(N):
		for x in range(6):
			print(visit[i][j], end=' ')
		print()
		if i == N - 1:
			print("j", j)
			result += 1
		elif graph[i + 1][j] == graph[i][j]:
			continue
		elif graph[i + 1][j] + 1 == graph[i][j]:
			if i + L >= N:
				break
			if not descendingY(i, j, graph[i + 1][j]):
				break
		elif graph[i + 1][j] - 1 == graph[i][j]:
			if i - L + 1 < 0:
				break
			if not ascendingY(i, j, graph[i][j]):
				break
		else:
			break

print(result)


# import sys
# input = sys.stdin.readline

# N, L = map(int, input().split())
# graph = []
# for _ in range(N):
# 	graph.append(list(map(int, input().split())))
# visit = [[False] * N for _ in range(N)]
# result = 0

# for i in range(N):
# 	cur = graph[i][0]
# 	steps = 1
# 	for j in range(1, N):
# 		cur = graph[i][j]
		
# 			if steps < L:
# 				break
