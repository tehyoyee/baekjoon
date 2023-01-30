# 2096.py
# 23.01.30. 9:45 ~

n = int(input())
graph = []
dp_min = [0] * (3 * n)
dp_max = [0] * (3 * n)

for _ in range(n):
	a, b, c = map(int, input().split())
	graph.append(a)
	graph.append(b)
	graph.append(c)

for i in range(3):
	dp_min[i] = graph[i]
	dp_max[i] = graph[i]
for i in range(3, 3 * n):
	if i % 3 == 0:
		dp_max[i] = max(dp_max[i - 2], dp_max[i - 3]) + graph[i]
		dp_min[i] = min(dp_min[i - 2], dp_min[i - 3]) + graph[i]
	elif i % 3 == 1:
		dp_max[i] = max(dp_max[i - 2], dp_max[i - 3], dp_max[i - 4]) + graph[i]
		dp_min[i] = min(dp_min[i - 2], dp_min[i - 3], dp_min[i - 4]) + graph[i]
	else:
		dp_max[i] = max(dp_max[i - 3], dp_max[i - 4]) + graph[i]
		dp_min[i] = min(dp_min[i - 3], dp_min[i - 4]) + graph[i]
		
print(max(dp_max[-3:]), min(dp_min[-3:]))
