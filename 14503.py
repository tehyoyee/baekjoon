# 14503.py
# 23.02.07. 13:20 ~

#	v 0 1 2 3 북 동 남 서
#		0
#	3		1
#		2

global steps

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, v = map(int, input().split())
graph = []
steps = 0
for _ in range(n):
	graph.append(list(map(int, input().split())))
visit = [[0] * (m) for _ in range(n)]

def is_no_way(r, c, v):
	for k in range(4):
		if not graph[r + di[k]][c + dj[k]] and not visit[r + di[k]][c + dj[k]]:
			return False
	return True

def is_back(r, c, v):
	new_i = r + di[(v + 2) % 4]
	new_j = c + dj[(v + 2) % 4]
	if not graph[new_i][new_j]:
		return True
	return False

def is_left(r, c, v):
	new_i = r + di[(v + 3) % 4]
	new_j = c + dj[(v + 3) % 4]
	if not visit[new_i][new_j] and not graph[new_i][new_j]:
		return True
	return False

def step_1(r, c, v):
	global steps
	visit[r][c] = 1
	steps += 1
	step_2(r, c, v)

def step_2(r, c, v):
	while True:
		if is_no_way(r, c, v):
			if is_back(r, c, v):
				r += di[(v + 2) % 4]
				c += dj[(v + 2) % 4]
			else:
				break
		elif is_left(r, c, v):
			step_1(r + di[(v + 3) % 4], c + dj[(v + 3) % 4], (v + 3) % 4)
			return
		else:
			v = (v + 3) % 4

step_1(r, c, v)
print(steps)