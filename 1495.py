# 1495.py
# 23.02.15. 11:40 ~

# n, s, m = map(int, input().split())
# v = list(map(int, input().split()))
# result = -1

# q = [[0, s]]
# while q:
# 	idx, vol = q.pop(0)
# 	if idx == n:
# 		result = max(vol, result)
# 	else:
# 		if 0 <= vol - v[idx] <= m:
# 			q.append([idx + 1, vol - v[idx]])
# 		if 0 <= vol + v[idx] <= m:
# 			q.append([idx + 1, vol + v[idx]])
# print(result)

n, s, m = map(int, input().split())
v = list(map(int, input().split()))
result = -1
dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][s] = True
for i in range(n):
	for j in range(m + 1):
		if dp[i][j]:
			if 0 <= j + v[i] <= m:
				dp[i + 1][j + v[i]] = True
			if 0 <= j - v[i] <= m:
				dp[i + 1][j - v[i]] = True
for i in range(m, -1, -1):
	if dp[-1][i]:
		print(i)
		exit()
print(-1)