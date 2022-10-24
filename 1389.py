# 1389.py

def bfs(kevin, relations, start, n):
	kevin = [0] * (n + 1)
	queue = [start]
	while queue:
		v = queue.pop(0)
		for x in relations[v]:
			if not kevin[x] and x != start:
				queue.append(x)
				kevin[x] = kevin[v] + 1
	return sum(kevin)

n, m = map(int, input().split())
kevin = [0] * (n + 1)
relations = [[] * (n + 1) for _ in range(n + 1)]
result = 10000
result_index = 0

for _ in range(m):
	a, b = map(int, input().split())
	relations[a].append(b)
	relations[b].append(a)
for i in range(1, n + 1):
	tmp = bfs(kevin, relations, i, n)
	if result > tmp:
		result = tmp
		result_index = i
print(result_index)