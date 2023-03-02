# 2251.py
# 23.03.02. 16:13 ~ 16:53

import sys
input = sys.stdin.readline

result = []
def pour(i, j, m):
	if i >= m - j:
		return i - (m - j), m
	elif i < m - j:
		return 0, j + i
	return -1, -1

def dfs(i, j, k):
	result = []
	if i == 0:
		result.append(k)
	if i and not j == cups[1]:				# i - j
		tmp_i, tmp_j = pour(i, j, cups[1])
		if tmp_i != -1 and not visit[tmp_i][tmp_j]:
			visit[tmp_i][tmp_j] = 1
			result += dfs(tmp_i, tmp_j, k)
	if i and not k == cups[2]:				# i - k
		tmp_i, tmp_k = pour(i, k, cups[2])
		if tmp_i != -1 and not visit[tmp_i][j]:
			visit[tmp_i][j] = 1
			result += dfs(tmp_i, j, tmp_k)
	if j and not i == cups[0]:				# j - i
		tmp_j, tmp_i = pour(j, i, cups[0])
		if tmp_j != -1 and not visit[tmp_i][tmp_j]:
			visit[tmp_i][tmp_j] = 1
			result += dfs(tmp_i, tmp_j, k)
	if j and not k == cups[2]:				# j - k
		tmp_j, tmp_k = pour(j, k, cups[2])
		if tmp_j != -1 and not visit[i][tmp_j]:
			visit[i][tmp_j] = 1
			result += dfs(i, tmp_j, tmp_k)
	if k and not i == cups[0]:				# k - i
		tmp_k, tmp_i = pour(k, i, cups[0])
		if tmp_k != -1 and not visit[tmp_i][j]:
			visit[tmp_i][j] = 1
			result += dfs(tmp_i, j, tmp_k)
	if k and not j == cups[1]:				# k - j
		tmp_k, tmp_j = pour(k, j, cups[1])
		if tmp_k != -1 and not visit[i][tmp_j]:
			visit[i][tmp_j] = 1
			result += dfs(i, tmp_j, tmp_k)
	return result

cups = list(map(int, input().split()))
visit = [[0] * (cups[1] + 1) for _ in range(cups[0] + 1)]
visit[0][0] = 1
print(*sorted(dfs(0, 0, cups[2])))