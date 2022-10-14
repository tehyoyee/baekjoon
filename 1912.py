# 1912py

import sys
input = sys.stdin.readline

sum = []
cnt = int(input())
arr = list(map(int, input().split()))
result = 0

sum.append(arr[0])
for i in range(cnt - 1):
	sum.append(max(arr[i + 1], sum[i] + arr[i + 1]))
print(max(sum))

# 배열을 참조하며 합한걸 배열에 추가해준다. 참조값이 더한수보다 크면 끊고 참조값부터 다시 더하기 시작한다.