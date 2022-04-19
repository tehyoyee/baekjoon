# 8958 py

n = int(input())
arr = []
point = 0
bonus = 0

for _ in range(n):
    arr.append(input())
for i in arr:
    for j in i:
        if j == 'O':
            point += 1 + bonus
            bonus += 1
        else:
            bonus = 0
    print(point)
    point = 0
    bonus = 0