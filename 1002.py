# 1002 py
# 23.07.09. 17:02 ~

import sys
input = sys.stdin.readline

def getDots(x1, y1, r1, x2, y2, r2):
	dist = (x1 - x2)**2 + (y1 - y2)**2
	if dist == 0 and r1==r2:
			return -1
	elif dist == (r1+r2)**2 or dist == (r1-r2)**2:
		return 1
	elif (r1-r2)**2 < dist < (r1+r2)**2:
		return 2
	else:
		return 0

N = int(input())
for _ in range(N):
	x1, y1, r1, x2, y2, r2 = map(int, input().split())
	print(getDots(x1, y1, r1, x2, y2, r2))