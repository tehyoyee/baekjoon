# 9663 py

global result
result = 0

def check_position(y, cnt, arr):
	for x in range(cnt):
		if (y in arr) or (arr[x] - y == cnt - x) or (arr[x] - y == x - cnt):
			return False
	return True

def n_queen(n, cnt, arr):
	global result
	if cnt == n:
		result += 1
		return
	else:
		for y in range(n):
			if check_position(y, cnt, arr):
				arr.append(y)
				n_queen(n, cnt + 1, arr)
				arr.pop()

n = int(input())
arr = []
n_queen(n, 0, arr)
print(result)