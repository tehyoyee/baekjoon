# 1766_1.py
# 23.10.29.

import sys
input = sys.stdin.readline
from collections import deque
import heapq

N, M = map(int, input().split())
result = []
tp = [[] for _ in range(N + 1)]
cnt = [0] * (N + 1)
q = []

for _ in range(M):
	a, b = map(int, input().split())
	cnt[b] += 1
	tp[a].append(b)

for i in range(1, N + 1):
	if cnt[i] == 0:
		q.append(i)

while q:
	ci = heapq.heappop(q)
	if cnt[ci] == 0:
		result.append(ci)	
	for ni in tp[ci]:
		cnt[ni] -= 1
		if cnt[ni] == 0:
			heapq.heappush(q, ni)

print(*result)