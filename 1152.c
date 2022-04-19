// 1152 C

#include <stdio.h>

int	check_space(char c)
{
	if (c == 32)
		return (1);
	if (c == '\0')
		return (1);
	return (0);
}

int	main(void)
{
	char	str[1000001];
	int		result = 0;
	int		len;

	scanf_s("%[^\n]", str);
	len = strlen(str);
	if (len == 1)
	{
		if (check_space(str[0]))
		{
			printf("0");
			return (0);
		}
	}
	for (int i = 1; len - 1; i++)
	{
		if (check_space(str[i]))
			result++;
	}
	result++;
	printf("%d", result);
	return (0);
}