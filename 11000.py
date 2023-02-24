# 11000.py
# 23.02.24. 16:22 ~ 16:57

from collections import deque

n = int(input())
start = []
end = []

for _ in range(n):
	a, b = map(int, input().split())
	start.append(a)
	end.append(b)

start.sort(); end.sort()
start, end = deque(start), deque(end)
result, cnt = 0, 0

while start and end:
	s = start.popleft()
	cnt += 1
	while s >= end[0]:
		end.popleft()
		cnt -= 1
	result = max(result, cnt)
print(result)