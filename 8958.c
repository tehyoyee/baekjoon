// 8958 C

#include <stdio.h>

int    main(void)
{
	int		n;
	char	arr[80];
	int		bonus = 0;
	int		point = 0;

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%s", arr);
		for (int j = 0; arr[j]; j++)
		{
			if (arr[j] == 'O')
				point += 1 + bonus++;
			else
				bonus = 0;
		}
	printf("%d\n", point);
	point = 0;
	bonus = 0;
	}
}

