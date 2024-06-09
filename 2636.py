# 2636.py
# 24.06.08

di = (0, 0, 1, -1)
dj = (1, -1, 0, 0)

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = []
cheeseCnt = 0
candi = deque([])
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 1:
            # candi.append((i, j))
            cheeseCnt += 1
result = cheeseCnt

visit = [[False] * M for _ in range(N)]
q = deque([(0, 0)])
visit[0][0] = True
while q:
    ci, cj = q.popleft()
    for k in range(4):
        ni, nj = ci + di[k], cj + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if visit[ni][nj]:
                continue
            if graph[ni][nj] == 1:
                visit[ni][nj] = True
                candi.append((ni, nj))
            else:
                visit[ni][nj] = True
                q.append((ni, nj))

cnt = 0
while candi:
    if cheeseCnt == 0:
        break
    nextQ = []
    newAir = deque([])
    while candi:
        ci, cj = candi.popleft()
        cheeseCnt -= 1
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if visit[ni][nj]:
                    continue
                if graph[ni][nj] == 1:
                    visit[ni][nj] = True
                    graph[ni][nj] = 0
                    nextQ.append((ni, nj))
                else:
                    visit[ni][nj] = True
                    newAir.append((ni, nj))
    
    while newAir:
        ci, cj = newAir.popleft()
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if visit[ni][nj]:
                    continue
                if graph[ni][nj] == 0:
                    visit[ni][nj] = True
                    newAir.append((ni, nj))
                if graph[ni][nj] == 1:
                    visit[ni][nj] = True
                    nextQ.append((ni, nj))
    if cheeseCnt == 0:
        print(cnt+1)
        print(result)
        exit()
    result = cheeseCnt
    for x in nextQ:
        candi.append(x)
    cnt += 1
print(0)
print(0)