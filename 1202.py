# # 1202.py

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
jw = []				# m, v
bag = []
for _ in range(n):
	jw.append(list(map(int, input().split())))
for _ in range(k):
	bag.append([int(input()), [0, 0]])
result = 0

jw.sort(reverse=True, key=lambda x : (x[1], x[0]))
bag.sort()
i = 0
for w, v in jw:
	if w <= bag[i][0] and bag[i][1][0] == 0:
		bag[i][1] = [w, v]
		result += v
		break
	else:
		i+=1

print(result)
		
