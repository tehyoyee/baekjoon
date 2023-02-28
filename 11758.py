# 11758.py
# 23.02.28. 11:26 ~ 11:40, 13:16 ~

# pos = []
# for _ in range(3):
# 	pos.append(list(map(float, input().split())))
# if pos[1][0] - pos[0][0] >= 0:
# 	flag = 1
# else:
# 	flag = -1
# if pos[1][0] - pos[0][0] == 0:
# 	m1 = float('inf') * (pos[1][1] - pos[0][1])
# else:
# 	m1 = float((pos[1][1] - pos[0][1]) / (pos[1][0] - pos[0][0]))
# if pos[2][0] - pos[1][0] == 0:
# 	m2 = float('inf') * (pos[2][1] - pos[1][1])
# else:
# 	m2 = float((pos[2][1] - pos[1][1]) / (pos[2][0] - pos[1][0]))
# if (pos[1][1] - pos[0][1]) * (pos[2][0] - pos[0][0]) == (pos[1][0] - pos[0][0]) * (pos[2][1] - pos[0][1]):
# 	print(0)
# elif m1 * (pos[2][0] - pos[0][0]) + pos[0][1]  < pos[2][1]:
# 	print(flag * 1)
# else:
# 	print(flag * -1)

# 외적사용

pos = []
for _ in range(3):
	pos.append(list(map(float, input().split())))
ab = [pos[1][0] - pos[0][0], pos[1][1] - pos[0][1]]
bc = [pos[2][0] - pos[1][0], pos[2][1] - pos[1][1]]
k = ab[0] * bc[1] - ab[1] * bc[0]
if k == 0:
	print(0)
elif k > 0:
	print(1)
else:
	print(-1)
