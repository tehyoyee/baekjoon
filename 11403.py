# 11403.py
# 23.02.07. 10:21 ~ 10:56

n = int(input())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))
result = []
def bfs(i, visit, n):
	q = [i]
	while q:
		cur = q.pop(0)
		for k in range(n):
			if not visit[k] and graph[cur][k] == 1:
				q.append(k)
				visit[k] = 1
	result.append(visit)

for i in range(n):
	bfs(i, [0] * n, n)
for x in result:
	for y in x:
		print(y, end=" ")
	print()