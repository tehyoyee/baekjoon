#47분
import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
candi = [[] for _ in range(N + 1)]
cnt = [0] * (N + 1)
result = []
for _ in range(M):
	a, b = map(int, input().split())
	candi[a].append(b)
	cnt[b] += 1

q = []
for i in range(1, N + 1):
	if cnt[i] == 0:
		heapq.heappush(q, i)
while q:
	cur = heapq.heappop(q)
	if cnt[cur] == 0:
		result.append(cur)
		for x in candi[cur]:
			cnt[x] -= 1
			if cnt[x] == 0:
				heapq.heappush(q, x)

print(*result)