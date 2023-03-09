# 12904.py
# 23.03.09. 15:48 ~ 16:04

target = list(input())
clue = list(input())

while len(target) != len(clue):
	if clue[-1] == 'A':
		clue.pop()
	else:
		clue.pop()
		clue.reverse()
if clue == target:
	print(1)
else:
	print(0)