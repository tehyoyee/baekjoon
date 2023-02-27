# 11758.py
# 23.02.27. 18:42 ~

pos = []
dist = []
for _ in range(3):
	pos.append(list(map(float, input().split())))
for i in range(-1, 2):
	dist.append(pow(pos[i][0] - pos[i + 1][0], 2) + pow(pos[i][1] - pos[i + 1][1], 2))
dist.sort()
if dist[0] + dist[1] < dist[2]:
	flag = -1
else:
	flag = 1
if pos[1][0] - pos[0][0] == 0:
	m1 = float('inf') * (pos[1][1] - pos[0][1])
else:
	m1 = (pos[1][1] - pos[0][1]) / (pos[1][0] - pos[0][0])
if pos[2][0] - pos[0][0] == 0:
	m2 = float('inf') * (pos[2][1] - pos[0][1])
else:
	m2 = (pos[2][1] - pos[0][1]) / (pos[2][0] - pos[0][0])
if m1 == m2:
	print(0)
elif m1 > m2:
	print(-1 * flag)
else:
	print(1 * flag)