# 2580py

arr = []
blank = []

for _ in range(9):
	arr.append(list(map(int, input().split())))

blank = [(i, j) for i in range(0, 9) for j in range(0, 9) if arr[i][j] == 0]

def check_row(x, test_input):
	if test_input in arr[x]:
		return False
	return True

def check_col(y, test_input):
	for i in range(0, 9):
		if test_input == arr[i][y]:
			return False
	return True

def check_square(x, y, test_input):
	for i in range((x // 3) * 3, (x // 3) * 3 + 3):
		for j in range((y // 3) * 3, (y // 3) * 3 + 3):
			if test_input == arr[i][j]:
				return False
	return True

def dfs(index):
	if index == len(blank):
		for i in arr:
			print(" ".join(map(str, i)))
		exit(0)

	x = blank[index][0]
	y = blank[index][1]

	for test_input in range(1, 10):
		if check_row(x, test_input) and check_col(y, test_input) and check_square(x, y, test_input):
			arr[x][y] = test_input
			dfs(index + 1)
			arr[x][y] = 0

dfs(0)