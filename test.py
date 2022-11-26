import sys
input = sys.stdin.readline



def union_parent(a, b):
	a = find_parent(a)
	b = find_parent(b)
	if graph[max(a, b)] = graph[min(a, b)]

def find_parent(x):
	if parent[x] == x:
		return x
	graph[x] = find_parent(graph[x])
	return parent[x]

while True:
	n, m = map(int, input().split())
	if n == 0 and m == 0:
		break
	graph = [x for x in range(m + 1)]
	for _ in range(m):
		a, b = map(int, input().split())
		union_parent(a, b)
	for i in range(m):
		graph[i] = find_parent(i)
	graphs = set(graph)
	print(len(graph))