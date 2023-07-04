# 15685.py
# 23.07.03. 16:29 ~ 17:45 시간초과

# import sys
# input = sys.stdin.readline
# from itertools import combinations

# N, M, H = map(int, input().split())

# trans = [[False] * (N + 1) for _ in range(H + 1)]
# candi = []

# for i in range(1, H + 1):
# 	for j in range(1, N):
# 		candi.append([i, j])

# for i in range(M):
# 	a, b = map(int, input().split())
# 	trans[a][b] = True
# 	if [a, b] in candi:
# 		candi.remove([a, b])
# 	if [a, b + 1] in candi:
# 		candi.remove([a, b + 1])
# 	if [a, b - 1] in candi:
# 		candi.remove([a, b - 1])

# def f(pos, candiCheck, H):
# 	ci, cj = pos[0], pos[1]
# 	if ci == H + 1:
# 		return cj
# 	if trans[ci][cj] or pos in candiCheck:
# 		return f([ci + 1, cj + 1], candiCheck, H)
# 	elif trans[ci][cj - 1] or [ci, cj - 1] in candiCheck:
# 		return f([ci + 1, cj - 1], candiCheck, H)
# 	else:
# 		return f([ci + 1, cj], candiCheck, H)

# def isValid(x):
# 	x.sort()
# 	for i in range(len(x) - 1):
# 		if x[i][1] + 1 == x[i + 1][1]:
# 			if x[i][0] == x[i + 1][0]:
# 				return False
# 	return True

# for i in range(M + 1):
# 	for x in list(combinations(candi, i)):
# 		flag = True
# 		for j in range(1, N + 1):
# 			if j != f([1, j], x, H):
# 				flag = False
# 			if not flag:
# 				break
# 		if flag and isValid([x]):
# 			print(len(x))
# 			exit()
# print(-1)



# import sys
# input = sys.stdin.readline


# global N, H, start, check

# N, M, H = map(int, input().split())
# graph = [[False] * N for _ in range(H + 1)]
# for i in range(M):
# 	a, b = map(int, input().split())
# 	graph[a][b] = True

# def dfs(depth, idx, chance):
# 	global N, H, start, check

# 	if depth == H + 1:
# 		# print(start, idx)
# 		if start == idx:
# 			check = True
# 		return
# 	if idx == 1:
# 		if graph[depth][idx]:
# 			dfs(depth + 1, idx + 1, chance)
# 		else:
# 			dfs(depth + 1, idx, chance)
# 			if chance:
# 				dfs(depth + 1, idx + 1, chance - 1)
# 	elif idx == N:
# 		if graph[depth][idx - 1]:
# 			dfs(depth + 1, idx - 1, chance)
# 		else:
# 			dfs(depth + 1, idx, chance)
# 			if chance:
# 				dfs(depth + 1, idx - 1, chance - 1)
# 	else:
# 		if graph[depth][idx]:
# 			dfs(depth + 1, idx + 1, chance)
# 		elif graph[depth][idx - 1]:
# 			dfs(depth + 1, idx - 1, chance)
# 		else:
# 			dfs(depth + 1, idx, chance)
# 			if chance:
# 				dfs(depth + 1, idx + 1, chance - 1)
# 				dfs(depth + 1, idx - 1, chance - 1)

# for c in range((N - 1) * H - M + 1):
# 	for i in range(1, N + 1):
# 		start = i
# 		check = False
# 		dfs(1, i, c)
# 		print(c, i, check)
# 		if check == False:
# 			break
# 	if check == True:
# 		print(c)
# 		exit()
# print(-1)


n, m, h = map(int, input().split())
visited = [[False] * (n+1) for _ in range(h+1)]
combi = []
for _ in range(m):
    a, b = map(int, input().split())
    visited[a][b] = True

def check():
    for i in range(1, n+1):
        now = i
        for j in range(1, h+1):
            if visited[j][now-1]:
                now -= 1
            elif visited[j][now]:
                now += 1
        if now != i:
            return False
    return True

def dfs(depth, idx):
    global answer
    if depth >= answer:
        return
    if check():
        answer = depth
        return

    for c in range(idx, len(combi)):
        x, y = combi[c]
        if not visited[x][y-1] and not visited[x][y+1]:
            visited[x][y] = True
            dfs(depth+1, c+1)
            visited[x][y] = False

for i in range(1,h+1):
    for j in range(1, n):
        if not visited[i][j-1] and not visited[i][j] and not visited[i][j+1]:
            combi.append([i, j])

answer = 4
dfs(0, 0)

print(answer if answer < 4 else -1)