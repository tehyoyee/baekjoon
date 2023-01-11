# 1541_1.py

s = input()
k = s.find('-')
n_list = []
result = 0

new_s = list(s.split("-"))
for i in range(len(new_s)):
	new_s[i] = new_s[i].split("+")
for x in new_s[0]:
	result += int(x)
if k != -1:
	for i in range(1, len(new_s)):
		for x in new_s[i]:
			result -= int(x)
print(result)