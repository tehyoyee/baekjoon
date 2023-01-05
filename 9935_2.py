# 9935py

haystack = input()
needle = input()
new_str = []
start = 0
n_len = len(needle)

for i in range(start, len(haystack)):
	new_str.append(haystack[i])
	if len(new_str) < n_len:
		continue
	if new_str[-1] == needle[-1] and new_str[-n_len] == needle[0]:
		j = 0
		while j < n_len and new_str[-n_len + j] == needle[j]:
			j += 1
		if j == n_len:
			del new_str[-n_len:]

if len(new_str) == 0:
	print("FRULA")
else:
	for x in new_str:
		print(x, end = '')
