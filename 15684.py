# 15685.py
# 23.07.03. 16:29 ~ 17:45 시간초과

import sys
input = sys.stdin.readline
from itertools import combinations

N, M, H = map(int, input().split())

trans = [[False] * (N + 1) for _ in range(H + 1)]
candi = []

for i in range(1, H + 1):
	for j in range(1, N):
		candi.append([i, j])

for i in range(M):
	a, b = map(int, input().split())
	trans[a][b] = True
	if [a, b] in candi:
		candi.remove([a, b])
	if [a, b + 1] in candi:
		candi.remove([a, b + 1])
	if [a, b - 1] in candi:
		candi.remove([a, b - 1])

def f(pos, candiCheck, H):
	ci, cj = pos[0], pos[1]
	if ci == H + 1:
		return cj
	if trans[ci][cj] or pos in candiCheck:
		return f([ci + 1, cj + 1], candiCheck, H)
	elif trans[ci][cj - 1] or [ci, cj - 1] in candiCheck:
		return f([ci + 1, cj - 1], candiCheck, H)
	else:
		return f([ci + 1, cj], candiCheck, H)

def isValid(x):
	x.sort()
	for i in range(len(x) - 1):
		if x[i][1] + 1 == x[i + 1][1]:
			if x[i][0] == x[i + 1][0]:
				return False
	return True

for i in range(M + 1):
	for x in list(combinations(candi, i)):
		flag = True
		for j in range(1, N + 1):
			if j != f([1, j], x, H):
				flag = False
			if not flag:
				break
		if flag and isValid([x]):
			print(len(x))
			exit()
print(-1)

