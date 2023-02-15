# 2447.py
# 23.02.15. 15:39 ~ 16:12

def clear(i, j, size):
	for y in range(i, i + size):
		for x in range(j, j + size):
			graph[y][x] = ' '

n = int(input())
tab = n
graph = [['*'] * n for _ in range(n)]
while tab != 1:
	tab_prev = tab
	tab //= 3
	for i in range(tab, n - tab, tab_prev):
		for j in range(tab, n - tab, tab_prev):
			clear(i, j, tab)

for i in range(n):
	for j in range(n):
		print(graph[i][j], end="")
	print()