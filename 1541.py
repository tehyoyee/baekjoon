# 1541 py

import sys
input = sys.stdin.readline

result = 0

str = input().split('-')
result += sum(map(int, str[0].split('+')))
for i in str[1:]:
	result -= sum(map(int, i.split('+')))
print(result)