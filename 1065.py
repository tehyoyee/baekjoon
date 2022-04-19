# 1065 py

def check(i):
    if int(i) >= 100:
        if int(i[1]) - int(i[0]) != int(i[2]) - int(i[1]):
            return (False)
    return (True)
    
n = int(input())
result = 0
for i in range(1, n + 1):
    if check(str(i)):
        result += 1
print(result)
