# 9935.py

# haystack = list(input())
# needle = list(input())
# h_len = len(haystack)
# n_len = len(needle)
# i = 0
# j = 0

# while True:
# 	if i > h_len - n_len:
# 		break
# 	while i + n_len < h_len - 1 and haystack[i] != needle[0]:
# 		i += 1
# 	if haystack[i + n_len - 1] != needle[-1]:
# 		i += 1
# 		continue
# 	while i + j < h_len and j < n_len and haystack[i + j] == needle[j]:
# 		j += 1
# 	if j == n_len:
# 		del haystack[i : i + j]
# 		if i > n_len:
# 			i -= n_len - 1
# 		else:
# 			i = 0
# 		h_len -= j
# 	else:
# 		i += 1
# 	j = 0

# if len(haystack) == 0:
# 	print("FRULA")
# else:
# 	for x in haystack:
# 		print(x, end='')



# haystack = input()
# needle = input()
# h_len = len(haystack)
# n_len = len(needle)
# i = 0
# j = 0

# while True:
# 	if i + n_len > h_len:
# 		break
# 	while i + n_len < h_len and haystack[i] != needle[0]:
# 		i += 1
# 	if haystack[i + n_len - 1] != needle[n_len - 1]:
# 		i += 1
# 		continue
# 	while j < n_len and haystack[i + j] == needle[j]:
# 		j += 1
# 	if j == n_len:
# 		haystack = haystack[0:i] + haystack[i + j:]
# 		if i >= n_len:
# 			i -= n_len
# 		else:
# 			i = 0
# 		h_len -= j
# 		if h_len == 0:
# 			break
# 	else:
# 		i += 1
# 	j = 0

# if len(haystack) == 0:
# 	print("FRULA")
# else:
# 	for x in haystack:
# 		print(x, end='')



# haystack = input()
# needle = input()
# h_len = len(haystack)
# n_len = len(needle)
# i = 0

# while True:
# 	if i + n_len > h_len:
# 		break
# 	while i + n_len < h_len and haystack[i] != needle[0]:
# 		i += 1
# 	if haystack[i + n_len - 1] != needle[n_len - 1]:
# 		i += 1
# 		continue
# 	if haystack[i:i + n_len] == needle:
# 		haystack = haystack[0:i] + haystack[i + n_len:]
# 		if i >= n_len:
# 			i -= n_len - 1
# 		else:
# 			i = 0
# 		h_len -= n_len
# 		if h_len == 0:
# 			break

# if h_len == 0:
# 	print("FRULA")
# else:
# 	for x in haystack:
# 		print(x, end='')


import sys
input = sys.stdin.readline

haystack = input().rstrip()
needle = input().rstrip()
i = len(needle)

while True:
	if i > len(haystack):
		break
	while i < len(haystack) and haystack[i - 1] != needle[len(needle) - 1]:
		i += 1
	if haystack[i - len(needle)] != needle[0]:
		i += 1
		continue
	if haystack[i - len(needle):i] == needle:
		haystack = haystack[:i - len(needle)] + haystack[i:]
		i -= len(needle)
		if len(haystack) == 0:
			break
	else:
		i += 1

if len(haystack) == 0:
	print("FRULA")
else:
	for x in haystack:
		print(x, end='')