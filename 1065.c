// 1065 C

#include <stdio.h>

int	main(void)
{
	int	n;
	int	result = 0;
	int arr[3];
	int	temp;

	scanf_s("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		temp = i;
		if (i == 1000)
			continue;
		if (i < 100)
			result++;
		else
		{
			for (int j = 0; j < 3; j++)
			{
				arr[j] = temp % 10;
				temp /= 10;
			}
			if (arr[1] - arr[0] == arr[2] - arr[1])
				result++;
		}
	}
	printf("%d", result);
}