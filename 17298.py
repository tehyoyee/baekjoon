# 17298.py
# 23.03.29. 09:27 ~ 09:41

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
NGE = [-1] * N
stack = []

for i in range(0, N):
	if len(stack):
		while stack[-1][0] < A[i]:
			NGE[stack.pop()[1]] = A[i]
			if not len(stack):
				break
	stack.append([A[i], i])
	
print(*NGE)