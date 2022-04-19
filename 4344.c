// 4344 C

#include <stdio.h>

int    main(void)
{
	int		n;
	int		c;
	int		arr[1000];
	float	avg = 0;
	float	result = 0;

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &c);
		for (int j = 0; j < c; j++)
		{
			scanf("%d", &arr[j]);
			avg += arr[j];
		}
		avg /= c;
		for (int k = 0; k < c; k++)
		{
			if (arr[k] > avg)
				result++;
		}
		result = result / c * 100;
		printf("%.3f%%\n", result);
		result = 0;
		avg = 0;
	}
}