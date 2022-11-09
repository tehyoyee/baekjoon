# 15686.py

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
graph = []
result = 0
houses = []
chickens = []	
candi = []

for i in range(n):
	graph.append(list(map(int, input().split())))
	for j in range(n):
		if graph[i][j] == 1:
			houses.append([i, j, 10000, 100000])
		elif graph[i][j] == 2:
			chickens.append([i, j])

for house in houses:
	for i in range(len(chickens)):
		if house[3] > abs(house[0] - chickens[i][0]) + abs(house[1] - chickens[i][1]):
			house[3] = abs(house[0] - chickens[i][0]) + abs(house[1] - chickens[i][1])
			house[2] = i

def find(chicken_list, idx, m):
	if m == 0:
		return(chicken_list)
	for i in range(idx + 1, len(chickens)):
		find(chicken_list + [i], i, m - 1)

candi.append(find([], -1, m))
result = [[0] * n]
for house in houses:
	dist = 11110
	for i in candi:
		tmp = 0
		for j in len(candi[i]):
			tmp += abs(candi[i][j] - )

print(graph)
print(chickens)
print(houses)