# 15953.py

import sys
input = sys.stdin.readline

reward_17 = [0, 500, 300, 300, 200, 200, 200, 50, 50, 50, 50, 30, 30, 30, 30, 30, 10, 10, 10, 10, 10, 10]
reward_18 = [0, 512, 256, 256, 128, 128, 128, 128]
for _ in range(8):reward_18.append(64)
for _ in range(16):reward_18.append(32)

t = int(input())
for _ in range(t):
	a, b = map(int, input().split())
	if a >= 22:
		a = 0
	if b >= 32:
		b = 0
	print((reward_17[a] + reward_18[b]) * 10000)