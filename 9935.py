from collections import deque

s = input()
s_len = len(s)
kk = s_len
s = deque(s)
b = input()
b_len = len(b)
b = deque(b)

i = 0
ro_cnt = 0
op = s_len
while op > 1:
	if s_len < 1:
		break
	while s[0] != b[0]:
		s.rotate(1)
		ro_cnt += 1
		op -= 1
		if ro_cnt >= s_len:
			break
	while s[0] == b[0]:
		s.rotate(-1)
		b.rotate(-1)
		i += 1
		ro_cnt -= 1
	if i == b_len:
		for _ in range(b_len):
			s.pop()
	s.rotate(-ro_cnt)
	b.rotate(-ro_cnt)
	i = 0
	if ro_cnt >= s_len:
		break
	ro_cnt = 0
	s_len -= 1

if op == kk:
	print("FRULA")
else:
	for i in s:
		print(i, end='')
	print()
