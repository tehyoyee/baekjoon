# 1655.py
# 23.03.05. 18:40 ~

import sys
import heapq
input = sys.stdin.readline

n = int(input())
l_heap = []
r_heap = []
result = []
for i in range(n):
	tmp = int(input())
	print(l_heap)
	print(r_heap)
	print()
	if len(l_heap) == len(r_heap):
		heapq.heappush(l_heap, (-tmp, tmp))
	else:
		heapq.heappush(r_heap, (tmp, tmp))
	if r_heap and l_heap[0][1] > r_heap[0][0]:
		min = heapq.heappop(r_heap)[0]
		max = heapq.heappop(l_heap)[1]
		heapq.heappush(l_heap, (-min, min))
		heapq.heappush(r_heap, (max, max))
	result.append(l_heap[0][1])
for x in result:
	print(x)
