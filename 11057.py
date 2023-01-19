# 11057.py
# 23.01.15 01:29~01:43
r = int(input())
n = 10 + r - 1
result = 1
for i in range(r):
	result *= n
	n -= 1
for i in range(1, r + 1):
	result //= i
print(result % 10007)
# a = combinations([1,2,3],2)
# print(a)
# 1	0~9
# 2	1+...+10
# 	0~9
# 	0	0~9
# 	1	1~9
# 	2	2~9

# 0123456789

# 중복조합

# n+r-1 C r
# 10 2 - 1 C 2