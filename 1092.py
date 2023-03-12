# 1092.py
# 23.03.12. 15:17 ~ 15:49

import sys
input = sys.stdin.readline

result = 0
N = int(input())
crains = list(map(int, input().split()))
M = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)
crains.sort(reverse=True)
if boxes[0] > crains[0]:
	print(-1)
	exit()
while boxes:
	for crain in crains:
		for box in boxes:
			if crain >= box:
				boxes.remove(box)
				break
	result += 1
print(result)