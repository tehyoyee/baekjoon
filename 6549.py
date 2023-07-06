# 6549.py
# 23.05.04. 11:26 ~

import sys
input = sys.stdin.readline

while True:
	lst = list(map(int, input().split()))
	if len(lst) == 1 and lst[0] == 0:
		break
	stack = []
	graph = []
	