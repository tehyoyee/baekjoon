# 1920.py

import sys
input = sys.stdin.readline

n = int(input())
list_n = list(map(int, input().split()))
m = int(input())
list_m = list(map(int, input().split()))
list_n.sort()

for x in list_m:
	is_exist = 0
	start = 0
	end = n - 1
	pivot = (end - start) // 2
	while start <= end:
		pivot = (end + start) // 2
		if list_n[pivot] == x:
			is_exist = 1
			break
		elif list_n[pivot] < x:
			start = pivot + 1
		else:
			end = pivot - 1
	print(is_exist)