# 10164.py
# 23.02.22. 21:32 ~

n, m, k = map(int, input().split())
steps = [[1] * m]
for _ in range(n - 1):
	steps.append([1] + [0] * (m - 1))
if k == 0:
	ny = n - 1
	nx = m - 1
else:
	ny = (k - 1) // m
	nx = (k - 1) % m

for i in range(1, n):
	for j in range(1, m):
		steps[i][j] = steps[i - 1][j] + steps[i][j - 1]
print(steps[ny][nx] * steps[n - ny - 1][m - nx - 1])