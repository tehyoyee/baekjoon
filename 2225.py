# 2225.py
# 23.02.13. 15:13 ~ 15:43

n, k = map(int, input().split())

result = 1
r = n
n = n + k - 1
if n // 2 < r:
	r = n - r
for i in range(n, n - r, -1):
	result *= i
for i in range(1, r + 1):
	result //= i
print(result % 1000000000)