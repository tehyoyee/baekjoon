# 1.py

N = int(input())
graph = []
dp = []

for i in range(N):
	graph.append(list(map(int, input().split())))
	if i == 0 or i == N - 1:
		if len(graph[i]) == 1:
			dp.append([1])
		else:
			dp.append([2] + [3] * (len(graph[i]) - 2) + [2])
	else:
		if len(graph[i]) ==  1:
			dp.append([2])
		else:
			dp.append([3] + [4] * (len(graph[i]) - 2) + [3])
	for j in range(1, len(graph[i])):
		graph[i][j] += graph[i][j - 1]

for k in range(N - 1):
	i = j = 0
	while i < len(graph[k]) and j < len(graph[k + 1]):
		if graph[k][i] < graph[k + 1][j]:
			i += 1
			dp[k + 1][j] += 1
		elif graph[k][i] > graph[k + 1][j]:
			j += 1
			dp[k][i] += 1
		else:
			i += 1
			j += 1

for x in dp:
	print(x)