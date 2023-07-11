# 1700_멀티탭스케줄링.py
# 23.07.11. 13:08 ~ 14:04

from collections import deque

N, K = map(int, input().split())
result = 0
dp = [[0] * N for _ in range(K + 1)]
plan = list(map(int, input().split()))
v = [deque([]) for _ in range(K + 1)]
v[0].append(0)
for i in range(K):
	v[plan[i]].append(i)
pos = []
for i in range(len(plan)):
	if plan[i] in pos:
		v[plan[i]].popleft()
		continue
	if len(pos) < N:
		pos.append(plan[i])
		v[plan[i]].popleft()
		continue

	tmp = 0
	for candi in pos:
		if not v[candi]:
			tmp = candi
			break
		if v[candi][0] > v[tmp][0]:
			tmp = candi
	pos.remove(tmp)
	result += 1
	pos.append(plan[i])
	v[plan[i]].popleft()

print(result)