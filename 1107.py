# 1107.py
# 23.02.13. 19:00 ~

target = int(input())
target_lst = list(map(int, str(target)))
target_len = len(str(target))
m = int(input())
if m == 0:
    button = sorted(list(x for x in range(0, 10)))
else:
    button = sorted(list(set(x for x in range(0, 10)) - set(map(int, input().split()))))
result = abs(target - 100)
for x in range(11):
    flag = 1
    for j in str(x):
        if not int(j) in button:
            flag = 0
            break
    if flag == 1:
        result = min(abs(int(x) - target) + len(str(x)), result)
print(result)