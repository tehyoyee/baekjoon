# 1074.py
# 23.1.12 21:17~21:54

def f(l, r, c, lst):
	temp = 0
	if r < l:
		if c < l:
			temp = 0
		else:
			temp = 1
			c -= l
	else:
		r -= l
		if c < l:
			temp = 2
		else:
			temp = 3
			c -= l
	lst.append(temp)
	if l == 1:
		return lst
	else:
		return f(l // 2, r, c, lst)

n, r, c = map(int, input().split())

lst = []
result = 0
lst = f(pow(2, n) // 2, r, c, lst)
for x in lst:
	result += x * pow(4, n - 1)
	n -= 1
print(result)

# 2^n  * 2^n
# 4^n
# 0 1*4^n-1 2*4^n-1  3*4^n-1
# 0 1*4^n-2 ~~

# 0 <= x,y,z ... < 4
# x*4^n-1 + y*4^n-2 + z*4^n-3 + ...

# 2 3 1
# 1: 
# 3행 1열
# 0~3행열
# 가로세로 4칸
# 행 0~1 2~3
# 열 0~1 2~3

# 행수 = 2^n
# 열수 = 2^n
# x*4^n-2



# 4^n-1