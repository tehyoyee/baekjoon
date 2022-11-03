# 2110.py

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
pos = []
for _ in range(n):
	pos.append(int(input()))
pos.sort()
start = 1
end = pos[n - 1] - pos[0]
result = 0
while start <= end:
	comp = pos[0]
	pivot = (start + end) // 2
	cnt = 0
	i = 0
	for i in range(0, n):
		if pos[i] - comp >= pivot:
			cnt += 1
			comp = pos[i]
	if cnt >= c - 1:
		start = pivot + 1
		result = pivot
	else:
		end = pivot - 1
print(result)

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
pos = []
for _ in range(n):
	pos.append(int(input()))
pos.sort()
start = pos[0]
end = pos[n - 1]
result = 0
while start <= end:
	comp = pos[0]
	pivot = (start + end) // 2
	cnt = 0
	i = 0
	for i in range(0, n):
		if pos[i] - comp >= pivot:
			cnt += 1
			comp = pos[i]
	if cnt >= c - 1:
		start = pivot + 1
		result = pivot
	else:
		end = pivot - 1
print(result)