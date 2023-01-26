# 2504.py
# 23.01.22.15:19 ~ 

# () = 2
# [] = 3

lst = list(input())
print(lst)
dp = [[0, 0] for _ in range(len(lst) + 1)]
lst1 = []
lst2 = []
print(dp)

for i in range(1, len(lst)):
	dp[i][0] += dp[i - 1][0]
	dp[i][1] += dp[i - 1][1]
	if lst[i] == "(":
		dp[i][0] += 1
	elif lst[i] == ")":
		dp[i][0] -= 1
	elif lst[i] == "[":
		dp[i][1] += 1
	else:
		dp[i][1] -= 1
	print(dp)

# (     () [[]] ) ( [ ] )
# 2 * ( 2 + 3^2 )  2*3

# )[  =  +
# ([  =  *
# 