# 1038.py
# 23.02.28. 15:27 ~ 16:00

# n = int(input())
# dp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# cnt = 9
# for i in range(0, 1000000):
# 	if cnt > n:
# 		break
# 	for j in range(len(str(i)) - 1):
# 		if cnt > n:
# 			break
# 		if not str(i)[j] > str(i)[j + 1]:
# 			break
# 		dp.append(i)
# 		cnt += 1
# print(cnt)
# if cnt > n:
# 	print(dp[-1])
# else:
# 	print(-1)

n = int(input())
result = 0
cnt = 10
flag = 0
i = 10
while i <= 9876543210:
	if cnt > n:
		break
	for j in range(len(str(i)) - 1):
		flag = 0
		if not str(i)[j] > str(i)[j + 1]:
			break
		flag = 1
	if flag == 1:
		cnt += 1
		result = i
	i += 1
if n < 10:
	print(n)
elif cnt > n:
	print(result)
else:
	print(-1)