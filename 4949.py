## 4949 py

def check(str):
	stack = [0]
	for x in str:
		if x == ')' or x == ']':
			if x == ')':
				if '(' != stack.pop():
					return False
			elif x == ']':
				if '[' != stack.pop():
					return False
		if x == '(' or x == '[':
			stack.append(x)
	if len(stack) != 1:
		return False
	return True

while True:
	str = input()
	if str == '.':
		break
	if check(str):
		print("yes")
	else:
		print("no")
