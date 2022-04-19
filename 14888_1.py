# 14888 py my

n = int(input())
min = 1000000000
max = -1000000000
op_sequence = []

def calculator(op_sequence, num):
	s = num[0]
	for i in range(len(op_sequence)):
		if op_sequence[i] == 0:
			s += num[i + 1]
		elif op_sequence[i] == 1:
			s -= num[i + 1]
		elif op_sequence[i] == 2:
			s *= num[i + 1]
		elif op_sequence[i] == 3:
			s /= num[i + 1]
			s = int(s)
	return s

def dfs(idx, op, num, s):
	global min
	global max
	global op_sequence

	if idx == len(num) - 1:
		s = calculator(op_sequence, num)
		if max < s:
			max = s
		if min > s:
			min = s
	for i in range(4):
		if op[i] != 0:
			if i == 0:
				op[i] -= 1
				op_sequence.append(i)
				dfs(idx + 1, op, num, s)
				op_sequence.pop()
				op[i] += 1
			elif i == 1:
				op[i] -= 1
				op_sequence.append(i)
				dfs(idx + 1, op, num, s)
				op_sequence.pop()
				op[i] += 1
			elif i == 2:
				op[i] -= 1
				op_sequence.append(i)
				dfs(idx + 1, op, num, s)
				op_sequence.pop()
				op[i] += 1
			elif i == 3:
				op[i] -= 1
				op_sequence.append(i)
				dfs(idx + 1, op, num, s)
				op_sequence.pop()
				op[i] += 1

num = list(map(int, input().split()))
op = list(map(int, input().split()))

dfs(0, op, num, num[0])
print(max)
print(min)