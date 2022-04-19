# 4344 py

n = int(input())

for _ in range(n):
    arr = list(map(int,input().split()))
    c = arr.pop(0)
    avg = sum(arr[:c]) / c
    result = 0
    for i in arr:
        if i > avg:
            result += 1
    result = result / c * 100
    print(f'{result:.3f}%')
