# 2675 py

n = int(input())
for _ in range(n):
    cnt, str = input().split()
    result = ''
    for str in str:
        result += str * int(cnt)
    print(result)
