# 6549.py
# 23.05.04. 11:26 ~ x

import sys
input = sys.stdin.readline

result = []
while True:
	N, *lst = map(int, input().split())
	if N == 0:
		break
		
	maxSize = 0
	stack = []

	for i in range(N):
		min_i = i
		while stack and stack[-1][0] >= lst[i]:
			h, min_i = stack.pop()
			maxSize = max(maxSize, h * (i-min_i))
		stack.append((lst[i], min_i))

	for h, i in stack:
		maxSize = max(maxSize, (N-i)*h)

	print(maxSize)