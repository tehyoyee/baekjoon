# 1202.py
# 23.07.12. X

import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewelries = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewelries.sort(reverse=True)
bags.sort()

result = 0
tmp = []
for bag in bags:
	while jewelries and jewelries[-1][0] <= bag:
		heapq.heappush(tmp, -jewelries.pop()[1])
	if tmp:
		result += -heapq.heappop(tmp)
print(result)