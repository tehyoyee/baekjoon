# 13460.py
# 23.04.25. 2:30분 정도 푼듯;

import sys
input = sys.stdin.readline
from collections import deque

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

N, M = map(int, input().split())

graph = []
for i in range(N):
	graph.append(list(input().rstrip()))
	for j in range(M):
		if graph[i][j] == 'B':
			posB = [i, j]
			graph[i][j] = '.'
		elif graph[i][j] == 'R':
			posR = [i, j]
			graph[i][j] = '.'
		elif graph[i][j] == 'O':
			END = [i, j]
			graph[i][j] = '.'

def getNewPos(b, r, k):
	bci, bcj = b
	rci, rcj = r
	flag = 0
	for _ in range(2):
		bni, bnj = bci + di[k], bcj + dj[k]
		rni, rnj = rci + di[k], rcj + dj[k]
		while True:
			if bci == END[0] and bcj == END[1]:
				flag = 1
				break
			if graph[bni][bnj] == '#':
				break
			if flag == 0 and bni == rci and bnj == rcj:
				break
			bci, bcj = bni, bnj
			bni, bnj = bci + di[k], bcj + dj[k]
		while True:
			if rci == END[0] and rcj == END[1]:
				flag = 1
				break
			if graph[rni][rnj] == '#':
				break
			if flag == 0 and bci == rni and bcj == rnj:
				break
			rci, rcj = rni, rnj
			rni, rnj = rci + di[k], rcj + dj[k]
	return [[bci, bcj], [rci, rcj]]

result = -1
q = deque([[posB, posR, 0]])
cnt = 0
while q and cnt <= 10:
	cPosB, cPosR, cnt = q.popleft()
	if cPosR == END and cPosB != END:
		result = cnt
		break
	for k in range(4):
		nPosB, nPosR = getNewPos(cPosB, cPosR, k)
		if nPosB != END and (cPosB != nPosB or cPosR != nPosR):
			q.append([nPosB, nPosR, cnt + 1])

print(result)
