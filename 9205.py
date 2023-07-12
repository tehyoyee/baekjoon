# 9205.py
# 23.04.27. 09:15 ~ 09:35

import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
	N = int(input())
	visit = [False] * N
	house = list(map(int, input().split()))
	stores = []
	for _ in range(N):
		stores.append(list(map(int, input().split())))
	target = list(map(int, input().split()))
	q = deque([house])
	result = "sad"
	while q:
		ci, cj = q.popleft()
		if abs(target[0] - ci) + abs(target[1] - cj) <= 1000:
			result = "happy"
			break
		for k in range(N):
			si, sj = stores[k][0], stores[k][1]
			if not visit[k] and abs(si - ci) + abs(sj - cj) <= 1000:
				visit[k] = True
				q.append([si, sj])
	print(result)