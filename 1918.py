# 1918.py
# 23.04.09. 09:20 ~ x

result = []
# string = list((input().split('+')))
# for i in range(len(string)):
# 	string[i] = list(string[i].split('-'))
string = input()
number = []
op = []
flag = 0
start = 0
for i in range(len(string)):
	if string[i] == '(':
		flag += 1
	elif string[i] == ')':
		flag -= 1
	elif flag == 0 and (string[i] == '+' or string[i] == '-'):
		number.append(string[start : i])
		op.append(string[i])
		start = i + 1
	elif i == len(string) - 1:
		number.append(string[start :])
	
def cal_braket(ss):
	tmp = []
	if 
	# op = []
	start = 0
	flag = 0
	i = 0
	while i != len(ss):
		# if len(lst) == 0 and 0 <= int(ss[i]) and int(ss[i]) <= 9:
			# lst.append(ss[i])
		if ss[i] == '(':
			if flag == 0:
				flag += 1
				start = i + 1
			i += 1
		elif ss[i] == ')':
			flag -= 1
			if flag == 0:
				end = i
				result.append(cal(ss[start:end]))
	i = 0
	tmp = ss.split("+")
	for i in range(len(tmp)):
		tmp[i] = tmp[i].split('-')
	for i in range(len(tmp)):
		for j in range(len(tmp[i])):
			for k in range(len(tmp[j])):
				if tmp[i][j][k] == '*':
					tmp[i][j][k], tmp[i][j][k - 1] = tmp[i][j][k - 1], tmp[i][j][k]

	while len(ss):
		0 <= int(ss[i]) and int(ss[i]) <= 9:
			tmp.append(ss[i])

		i += 1
	
# 	while True:
# 		if ss[i] == ')':
# 			end = i
# 			break


# number[1] = f1(number[1])
# print(number[1])

for i in range(number):
	for j in range(number[i]):
		if number[i].count('('):



# for i in range(len(string)):


# string = input()
# result = []
