# 1629.py

# import sys
# input = sys.stdin.readline

# result = 1
# x, y, z = map(int, input().split())
# l = len(str(z))
# limit = z * 2
# limit = len(str(limit))
# print(limit)

# for i in range(y):
# 	print(result, x)
# 	result = int(str(result)[-limit + 1:])
# 	if result == 0:
# 		result = 10 ** (l - 1)
# 	result *= x
# print(result % z)

import sys
input = sys.stdin.readline

result = 1
x, y, z = map(int, input().split())
limit = 2 * z
l_l = len(str(limit))
print(l_l)
if len(str(x)) - l_l > 0:
	new_x = int(str(x)[-(len(str(x)) - l_l + 1):])
print(new_x)
for i in range(y):
	if result == 0:
		result = z
	print(result, new_x)
	result *= new_x
	result = int(str(result)[-l_l:])
	if result == 0:
		result = new_x
print(result % z)

# import sys
# input = sys.stdin.readline

# result = 1
# x, y, z = map(int, input().split())
# limit = 2 * z

# xx = []
# for i in str(x):
# 	xx.append(int(i))
# print(xx)