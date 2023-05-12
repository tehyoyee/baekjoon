#2


# width = 51
# height = 37
# diagonals = [[17, 19]]
# # diagonals = [[1, 1], [2, 2]]
# # diagonals = [[2, 3]]

# from math import factorial

# def solution(width, height, diagonals):
# 	result = 0
# 	for cx, cy in diagonals:
# 		tmp = 1
# 		tmp *= (factorial(cx-1 + cy) // (factorial(cx-1) * factorial(cy)))
# 		tmp *= (factorial(width - cx + height - (cy - 1)) // (factorial(width - cx) * factorial(height - (cy - 1))))
# 		result += tmp
# 		result %= 10000019
# 		tmp = 1
# 		tmp *= (factorial(cx + cy-1) // (factorial(cx) * factorial(cy-1)))
# 		tmp *= (factorial(width - (cx - 1) + height - (cy)) // (factorial(width - (cx - 1)) * factorial(height - cy)))
# 		result += tmp
# 		result %= 10000019
# 	return result

# print(solution(width, height, diagonals))




width = 51
height = 37
diagonals = [[17, 19]]

from math import factorial

def fact(x):
	if x == 2:
		return 2
	elif x == 1:
		return 1
	return x * fact(x-1)

def solution(width, height, diagonals):
	result = 0
	for cx, cy in diagonals:
		tmp = 1
		tmp *= (factorial(cx-1 + cy) // (factorial(cx-1) * factorial(cy)))
		tmp *= (factorial(width - cx + height - (cy - 1)) // (factorial(width - cx) * factorial(height - (cy - 1))))
		result += tmp
		result %= 10000019
		tmp = 1
		tmp *= (factorial(cx + cy-1) // (factorial(cx) * factorial(cy-1)))
		tmp *= (factorial(width - (cx - 1) + height - (cy)) // (factorial(width - (cx - 1)) * factorial(height - cy)))
		result += tmp
		result %= 10000019
	return result

print(solution(width, height, diagonals))
