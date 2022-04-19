# 2577 py

arr = []
for i in range(10):
    arr.append(int(input()) % 42)
arr = set(arr)
print(len(arr))
