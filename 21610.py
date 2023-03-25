# 21610.py
# 23.03.14. 15:56 ~

from collections import deque
import sys
input = sys.stdin.readline

def shiftCloud(d, s, N):
	for _ in range(len(clouds)):
		i, j = clouds.popleft()
		ni = (i + di[d] * s) % N
		nj = (j + dj[d] * s) % N
		clouds.append((ni, nj))

def rain():
	for i, j in clouds:
		graph[i][j] += 1

def copyWater(N):
	for i, j in clouds:
		flag = 0
		for d in range(2, 10, 2):
			ni = i + di[d]
			nj = j + dj[d]
			if 0 <= ni < N and 0 <= nj < N:
				if graph[ni][nj]:
					flag += 1
		graph[i][j] += flag
	
def shapeClouds(N):
	newClouds = deque([])
	for i in range(N):
		for j in range(N):
			if graph[i][j] >= 2 and (i, j) not in clouds:
				graph[i][j] -= 2
				newClouds.append((i, j))
	return newClouds

di = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dj = [0, -1, -1, 0, 1, 1, 1, 0, -1]

result = 0
N, M = map(int, input().split())
graph = []
orders = deque([])
clouds = deque([(N - 2, 0), (N - 2, 1), (N - 1, 0), (N - 1, 1)])

for _ in range(N):
	graph.append(list(map(int, input().split())))
for _ in range(M):
	orders.append(list(map(int, input().split())))

while orders:
	d, s = orders.popleft()
	shiftCloud(d, s, N)
	rain()
	copyWater(N)
	clouds = shapeClouds(N)

for x in graph:
	result += sum(x)
print(result)