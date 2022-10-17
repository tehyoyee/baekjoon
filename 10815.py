# 10815.py

from __future__ import print_function				# 버젼 낮은 리눅스에서 필요.   end = ' '  인식 안됨.
import sys
input = sys.stdin.readline

n = int(input())
num_n = list(map(int, input().split()))
m = int(input())
num_m = list(map(int, input().split()))
result = [0] * m
num_n.sort()

for i in range(m):						# 이진탐색
	start = 0
	end = n - 1
	while start <= end:
		mid = (start + end) // 2
		if num_n[mid] > num_m[i]:
			end = mid - 1
		elif num_n[mid] < num_m[i]:
			start = mid + 1
		else:
			result[i] += 1
			break

for x in result:
	print(x, end=' ')
