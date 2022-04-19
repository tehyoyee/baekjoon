// 2675 C

#include <string.h>

int	main(void)
{
	int		n;
	int		r;
	char	s[20];

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &r);
		scanf("%s", s);
		for (int i = 0, k = 0; i < strlen(s); i++)
		{
			for (int j = 0; j < r; j++, k++)
				printf("%c", s[i]);
		}
		printf("\n");
	}
}
