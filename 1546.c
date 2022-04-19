// 1546 C

#include <stdio.h>

int    main(void)
{
	float	n;
	float	point[1000];
	float	max = 0;
	float	total = 0;

	scanf_s("%f", &n);
	for (int i = 0; i < n; i++)
		scanf_s("%f", &point[i]);
	for (int i = 0; i < n; i++)
	{
		if (max < point[i])
			max = point[i];
	}
	for (int i = 0; i < n; i++)
		total += point[i] / max * 100;
	printf("%f", total / n);
}