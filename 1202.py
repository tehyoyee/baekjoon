# # 1202.py

# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# jw = []				# m, v
# bag = []
# for _ in range(n):
# 	jw.append(list(map(int, input().split())))
# for _ in range(k):
# 	bag.append(int(input()))
# result = 0

# # jw.sort()
# # jw.sort(key=lambda x : x[1])
# jw.sort(reverse=True)
# jw.sort(reverse=True, key=lambda x:x[1])
# # bag.sort()
# bag.sort(reverse=True)

# print(jw)
# print(bag)
# bag_cur = bag.pop()
# start = 0
# for bag_cur in bag:
# 	for j in range(start, len(jw)):
# 		print(bag_cur, j)
# 		if jw[j][0] <= bag_cur:
# 			print(bag_cur, j)
# 			result += jw[j][1]
# 			start = j
# 			break
# print(result)
			

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
jw = []				# m, v
bag = []
for _ in range(n):
	jw.append(list(map(int, input().split())))
for _ in range(k):
	bag.append(int(input()))
result = 0

jw.sort()
jw.sort(reverse=True, key=lambda x : x[1])
bag.sort()

for x in jw:
	for j in range(len(bag)):
		if x[0] <= bag[j]:
			result += x[1]
			del bag[:j]
			break
print(result)	