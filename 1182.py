# 1182.py
# 23.07.09. 17:33 ~

import sys
input = sys.stdin.readline

result = 0
N, S = map(int, input().split())
lst = list(map(int, input().split()))
acc = [0] * (N + 1)
for i in range(N):
	acc[i + 1] = acc[i] + lst[i]

for i in range(N):
	for j in range(i + 1, N + 1):
		if acc[j] - acc[i] == S:
			result += 1
print(result)