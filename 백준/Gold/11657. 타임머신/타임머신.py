# X
import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            ci, ni, cost = edges[j]
            if dist[ci] != INF and dist[ni] > dist[ci] + cost:
                dist[ni] = dist[ci] + cost
                if i == N - 1:
                    return True
    return False

N, M = map(int, input().split())
edges = []
dist = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    
negative_cycle = bf(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, N + 1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])