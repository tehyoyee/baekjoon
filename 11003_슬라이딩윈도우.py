# 11003.py
# 23.07.12. 21:44 ~

import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
lst = list(map(int, input().split()))

q = deque()
for i in range(N):
	while q and q[-1][0] > lst[i]:
		q.pop()
	while q and q[0][1] < i - L + 1:
		q.popleft()
	q.append((lst[i], i))
	print(q[0][0], end=' ')