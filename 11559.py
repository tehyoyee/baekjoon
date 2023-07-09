# 11559.py
# 23.07.09. 23:40 ~ 

from collections import deque
import sys
input = sys.stdin.readline

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

lines = [deque([]) for _ in range(6)]
result = 0
for _ in range(12):
	a = input().rstrip()
	for i in range(6):
		lines[i].appendleft(a[i])
flag = 1

while flag:
	flag = 0
	visit = [[False] * 12 for _ in range(6)]
	for i in range(6):
		for j in range(12):
			if not visit[i][j] and lines[i][j] != '.':
				cnt = 0
				candi = []
				visit[i][j] = True
				q = deque([(i, j, lines[i][j])])
				while q:
					ci, cj, color = q.popleft()
					cnt += 1
					candi.append((ci, cj))
					for k in range(4):
						ni, nj = ci + di[k], cj + dj[k]
						if 0 <= ni < 6 and 0 <= nj < 12 and not visit[ni][nj] and lines[ni][nj] != '.' and color == lines[ni][nj]:
							visit[ni][nj] = True
							q.append((ni, nj, lines[ni][nj]))
				if cnt >= 4:
					flag = 1
					for i, j in candi:
						lines[i][j] = '.'

	if flag == 1:
		result += 1
		for i in range(6):
			newQ = deque([])
			while lines[i]:
				tmp = lines[i].popleft()
				if tmp == '.':
					continue
				else:
					newQ.append(tmp)
			while len(newQ) < 12:
				newQ.append('.')
			lines[i] = newQ
print(result)