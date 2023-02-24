# 17070.py
# 23.02.22 16:26 ~  


from collections import deque

result = 0
n = int(input())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))
dp = [[[0] * n for _ in range(n)] for _ in range(n)]
print(dp)
dp[0][1][1] = 1
for i in range(n):
	for j in range(n):
		dp[i][j + 1][0] += dp[i][j][0]
		dp[i][j
		dp[i + 1][j + 1][2] += dp[i][j][0]

		dp[i + 1][j][1] += dp[i][j][1]
		dp[i + 1][j + 1][2] += dp[i][j][1]
		
		dp[i + 1][j + 1] += dp[i - 1][j - 1][2]

# while q:
# 	ci, cj, cd = q.popleft()
# 	if ci == n - 1 and cj == n - 1:
# 		result += 1
# 	else:
# 		if 0 <= ci < n - 1 and 0 <= cj < n - 1 and graph[ci][cj + 1] == 0 and graph[ci + 1][cj] == 0 and graph[ci + 1][cj + 1] == 0:
# 			q.append([ci + 1, cj + 1, 2])
# 			if cd != 1:
# 				q.append([ci, cj + 1, 0])
# 			if cd != 0:
# 				q.append([ci + 1, cj, 1])
# 		else:
# 			if cd != 1 and 0 <= cj < n - 1 and graph[ci][cj + 1] == 0:
# 				q.append([ci, cj + 1, 0])
# 			if cd != 0 and 0 <= ci < n - 1 and graph[ci + 1][cj] == 0:
# 				q.append([ci + 1, cj, 1])
print(result)

