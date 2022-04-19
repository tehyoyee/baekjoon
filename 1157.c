// 1157 C

#include <stdio.h>

int	main(void)
{
	char	str[1000000];
	char	count[26] = { 0, };
	int		max = 0;
	int		len;
	int		check = 0;

	scanf_s("%s", str, sizeof(str));
	len = strlen(str);
	for (int i = 0; i < len; i++)
		if ('a' <= str[i] && str[i] <= 'z')
			count[str[i] - 'a']++;
		else
			count[str[i] - 'A']++;
	for (int i = 0; i < 26; i++)
		if (count[max] < count[i])
			max = i;
	for (int i = 0; i < 26; i++)
		if (count[max] == count[i])
			check++;
	if (check > 1)
		printf("?");
	else
		printf("%c", max + 'A');
}
