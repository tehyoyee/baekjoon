def vps(str_0):
	a = 0
	b = 0
	if str_0[-1] == ')' and str_0[0] == '(':
		if str_0.count(')') == str_0.count('('):
			for x in str_0:
				if b > a:
					return 0
				if x == '(':
					a += 1
				elif x == ')':
					b += 1
			return 1
	return 0

n = int(input())
for _ in range(n):
	str_0 = input()
	if vps(str_0):
		print("YES")
	else:
		print("NO")