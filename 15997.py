# 15997.py

# 3 1 0

import sys
input = sys.stdin.readline

nation = list(input().split())
# a b w d l
# win = [[0] * 4 for _ in range(4)]
# win = [0] * 4
# for k in range(6):
# 	a, b, w, d, l = input().split()
# 	w = float(w)
# 	d = float(d)
# 	l = float(l)
# 	for i in range(4):
# 		if nation[i] == a:
# 			break
# 	for j in range(4):
# 		if nation[j] == b:
# 			break
# 	win[i] += w * 3 + d
# 	win[j] += (1 - w - d) * 3 + d
# for x in win:
# 	print(x / 9)

win = [[] for _ in range(4)]
draw = [[] for _ in range(4)]
lose = [[] for _ in range(4)]
result = [0] * 4

for k in range(6):
	a, b, w, d, l = input().split()
	w = float(w)
	d = float(d)
	l = float(l)
	for i in range(4):
		if nation[i] == a:
			break
	for j in range(4):
		if nation[j] == b:
			break
	win[i].append(w)
	win[j].append(1 - w)
	draw[i].append(d)
	draw[j].append(d)
	lose[i].append(l)
	lose[j].append(1 - l)
# for x in win:
# 	print(x)
# for x in draw:
# 	print(x)
# for x in lose:
# 	print(x)
for i in range(4):
	temp = 0
	# print(win[i][0] * win[i][1] * draw[i][2])
	temp += win[i][0] * win[i][1] * win[i][2]
	temp += win[i][0] * win[i][1] * draw[i][2]
	temp += draw[i][0] * win[i][1] * win[i][2]
	temp += win[i][0] * draw[i][1] * win[i][2]
	temp += win[i][0] * draw[i][1] * draw[i][2]
	temp += draw[i][0] * draw[i][1] * win[i][2]
	temp += draw[i][0] * win[i][1] * draw[i][2]

	temp += draw[i][0] * win[i][1]
	result[i] += temp

	# temp += draw[i][0] * draw[i][1] * draw[i][2]

print(result)

# 	a b c d
# a	0 1 8 6
# b	0
# c	2
# d	4

# no d

# www wll wwl lll

# 9 www
# 7 wwd
# 5 wdd			wdd wdd wdd lll			wdd	wwd wdl lll 		wdd wdd ldd ddl
# 4 wdl

# 3 ddd
# 2 ddl
# 1 dll
# 0 lll
# wdd 이상이면 무조건 진출

# www wd wdd - 1.0


# www
# wwl
# wll
# lll

# KOREA CCC BBB AAA
# KOREA CCC 1.0 0.0 0.0
# AAA BBB 0.6 0 0.4
# AAA KOREA 0.0 0.0 1.0
# CCC BBB 0.0 0.0 1.0
# KOREA BBB 1.0 0.0 0.0
# CCC AAA 0.0 0.0 1.0
