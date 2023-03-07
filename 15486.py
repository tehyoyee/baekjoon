# 15486.py
# 23.03.06. 15:13 ~44

#31분
n = int(input())
graph = [0]
dp = [0] * (n + 1)
prevMax = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    
for i in range(1, n + 1):
	prevMax = max(prevMax, dp[i - 1])
	if i + graph[i][0] - 1 < n + 1:
		dp[i + graph[i][0] - 1] = max(dp[i + graph[i][0] - 1], prevMax + graph[i][1])
print(max(dp))




