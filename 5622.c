// 5622 C

#include <stdio.h>

int	find(char c)
{
	int	a = c - 65;
	if (a < 3)
		return (3);
	if (a < 6)
		return (4);
	if (a < 9)
		return (5);
	if (a < 12)
		return (6);
	if (a < 15)
		return (7);
	if (a < 19)
		return (8);
	if (a < 22)
		return (9);
	if (a < 26)
		return (10);
}

int	main(void)
{
	char	str[16];
	int		len;
	int		result = 0;

	scanf("%s", str);
	len = strlen(str);
	for (int i = 0; i < len; i++)
		result += find(str[i]);
	printf("%d", result);
}
