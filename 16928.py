# 16928.py
# 23.01.31.

def find_(x):
	for l in ladder:
		if l[0] == x:
			return l[1]
	for s in snake:
		if s[0] == x:
			return s[1]
	return x

n, m = map(int, input().split())
ladder = []
snake = []
visit = [False] * 101
steps = [0] * 101
for _ in range(n):
	ladder.append(list(map(int, input().split())))
for _ in range(m):
	snake.append(list(map(int, input().split())))

q = [[1, 0]]

while q:
	cur, step = q.pop(0)
	if cur == 100:
		print(step)
	for k in range(1, 7):
		if 1 <= cur + k <= 100:
			tmp = find_(cur+k)
			if not visit[tmp]:
				visit[tmp] = True
				q.append([tmp, step+1])