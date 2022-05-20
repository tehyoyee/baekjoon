## 1874.py

n = int(input())

def search(n):
	cnt = 1
	stack = []
	op = []

	for i in range(n):
		num = int(input())
		while cnt <= num:
			stack.append(cnt)
			op.append('+')
			cnt += 1
		if stack[-1] == num:
			stack.pop()
			op.append('-')
		else:
			return False
	return op

op = search(n)
if op:
	for x in op:
		print(x)
else:
	print("NO")