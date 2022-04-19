// 1316 c

#include <stdio.h>
#include <stdlib.h>

int result = 0;

void	check(int len, char* str)
{
	int	flag;

	for (int i = 0; i < len; i++)
	{
		for (flag = i + 1; str[flag] == str[i]; flag++) {}
		for (; flag < len; flag++)
		{
			if (str[i] == str[flag])
				return;
		}
	}
	result++;
}

int	main(void)
{
	int		n;
	char	arr[100];

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%s", arr);
		check(strlen(arr), arr);
	}
	printf("%d", result);
}