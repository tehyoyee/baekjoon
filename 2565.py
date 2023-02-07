# 2565.py
# 23.02.07. 16:25 ~ 16:36

n = int(input())
graph = [[0, 0]]
for _ in range(n):
	graph.append(list(map(int, input().split())))
graph.sort(key = lambda x:(x[1], x[0]))
tmp = graph[0][0]
result = [[0, 0] for _ in range(n + 1)]
for i in range(1, n + 1):
	for j in range(i - 1, -1, -1):
		if graph[i][0] > result[i - j][0]:
			result[i][0] = graph[i][0]
			result[i][1] = result[i - j][1] + 1
result.sort(key = lambda x:(x[1], x[0]))
print(n - result[-1][1] - 1)

# n = int(input())
# graph = [[0, 0]]
# for _ in range(n):
# 	graph.append(list(map(int, input().split())))
# graph.sort()
# tmp = graph[0][0]
# result = [[0, 0] for _ in range(n + 1)]
# for i in range(1, n + 1):
# 	if graph[i][1] > graph[i - 1][1]:
# 		result[i][1] = graph[i][1]
# 		result[i][0] = result[i - 1][0] + 1
# 	else:
# 		for j in range(i):
# 			if graph[i][1] > graph[i - j][1]:
# 				result[i][1] = graph[i][1]
# 				result[i][0] = result[i - j][0] + 1
# 				break
# result.sort()
# print(result[-1][0])