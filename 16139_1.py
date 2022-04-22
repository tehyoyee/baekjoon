# 16139 py

import sys
input = sys.stdin.readline

arr = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
ret = []
n = int(input())

for x in alphabet:
	temp = [0]
	cnt = 0
	for y in arr:
		if x == y:
			cnt += 1
		temp.append(cnt)
	ret.append(temp)
for _ in range(n):
	a, l, r= input().split()
	a = ord(a) - 97
	l = int(l)
	r = int(r)
	result = ret[a][r + 1] - ret[a][l]
	print(result)
