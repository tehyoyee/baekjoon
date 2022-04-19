// 4673 C

#include <stdio.h>

void	self_num(void);

int	main(void)
{
	self_num();
}

void	self_num(void)
{
	int	arr[10001] = { 0, };
	int	num;
	int	temp;

	for (int i = 1; i < 10001; i++)
	{
		num = i;
		temp = 0;
		temp += num;
		while (num > 0)
		{
			temp += num % 10;
			num /= 10;
		}
		if (temp > 10000)
			continue;
		arr[temp] = 1;
	}
	for (int i = 1; i < 10001; i++)
	{
		if (arr[i] != 1)
			printf("%d\n", i);
	}
}
