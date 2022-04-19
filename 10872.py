# 10872 py

def recursive(n):
	if n == 0:
		return 1
	else:
		return (n * recursive(n - 1))

t = int(input())
print(recursive(t))
