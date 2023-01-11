import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	n = int(input())
	graph = []
	graph.append(list(map(int, input().split())))
	graph.append(list(map(int, input().split())))
	dp = [[0] * n for _ in range(2)]
	dp[0][0] = graph[0][0]
	dp[1][0] = graph[1][0]
	if n == 1:
		print(max(dp[0][0], dp[1][0]))
		continue
	dp[0][1] = graph[0][1] + dp[1][0]
	dp[1][1] = graph[1][1] + dp[0][0]
	
	for j in range(2, n):
		for i in range(2):
			if i == 0:
				dp[i][j] = max(dp[1][j - 1], dp[1][j - 2]) + graph[i][j]
			else:
				dp[i][j] = max(dp[0][j - 1], dp[0][j - 2]) + graph[i][j]
	print(max(dp[0][n - 1], dp[0][n - 2], dp[1][n - 1], dp[1][n - 2]))