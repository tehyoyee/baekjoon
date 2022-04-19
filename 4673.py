# 4673 py

non_self_num = set()
natural_num = set(range(1, 10001))

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    non_self_num.add(i)

self_num = sorted(natural_num - non_self_num)

for i in self_num:
    print(i)
