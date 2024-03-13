# 5639.py
# 24.03.13. 10:51 ~ 11:30

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def runPostOrder(rootIdx, endIdx):
	if rootIdx > endIdx:
		return
	rightRootIdx = endIdx + 1
	for i in range(rootIdx + 1, endIdx + 1):
		if lst[rootIdx] < lst[i]:
			rightRootIdx = i
			break

	runPostOrder(rootIdx + 1, rightRootIdx - 1)
	runPostOrder(rightRootIdx, endIdx)
	print(lst[rootIdx])

lst = []
while True:
	try:
		lst.append(int(input().rstrip()))
	except:
		break

runPostOrder(0, len(lst) - 1)