# 1546 py

total = 0
max = 0
arr = []
n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    if max < i:
        max = i
for i in arr:
    total += i / max * 100
print(total / n)
