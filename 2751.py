# 2751.py
# 23.07.06. 20:05 ~

# #12
# N = int(input())
# table = [False] * 2000001
# for _ in range(N):
# 	table[int(input()) + 1000000] = True
# i = 0
# while N > 0:
# 	if table[i]:
# 		N -= 1
# 		print(i-1000000)
# 	i += 1

#15   stdout해봄
N = int(input())
table = [False] * 2000001
for _ in range(N):
	table[int(input()) + 1000000] = True
i = 0
while N > 0:
	if table[i]:
		N -= 1
		sys.stdout.write(str(i-1000000) + '\n')
	i += 1