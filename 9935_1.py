haystack = list(input())
needle = list(input())
n_len = len(needle)
i = n_len

while True:
	if i > len(haystack):
		break
	while i < len(haystack) and haystack[i - 1] != needle[n_len - 1]:
		i += 1
	if haystack[i - n_len] != needle[0]:
		i += 1
		continue
	if haystack[i - n_len:i] == needle:
		# haystack = haystack[:i - n_len] + haystack[i:]
		del haystack[i - n_len:i]
		i -= n_len
		if len(haystack) == 0:
			break
	else:
		i += 1
if len(haystack) == 0:
	print("FRULA")
else:
	for x in haystack:
		print(x, end='')