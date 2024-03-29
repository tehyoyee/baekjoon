# 1865.py
# 23.07.09. 21:00 ~ X

import sys
input = sys.stdin.readline

def bf():
	for i in range(N):
		print("=======i=======\n", i);
		for j in range(len(edges)):
			print("========j=======")
			cur, next, cost = edges[j]
			print(cur, next, cost)
			if dist[next] > dist[cur] + cost:
				dist[next] = dist[cur] + cost
				print(dist)
				if i == N - 1:
					return True
	return False
                        
TC = int(input())

for _ in range(TC):
	N, M, W = map(int, input().split())
	edges = []
	dist = [0] * (N + 1)
	
	for _ in range(M):
		s, e, t = map(int, input().split())
		edges.append((e, s, t))
		edges.append((s, e, t))
	for _ in range(W):
		s, e, t = map(int, input().split())
		edges.append((e, s, -t))
	if bf():
		print("YES")
	else:
		print("NO")
	
