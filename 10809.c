// 10809 C

#include <stdio.h>

int	main(void)
{
	char	str[101] = { 0, };
	int		check[27] = { 0, };
	
	scanf("%s", str);
	for (int i = 0; i < 26; i++)
		check[i] = -1;
	for (int i = 0; i < strlen(str); i++)
	{
		if (check[str[i] - 'a'] == -1)
			check[str[i] - 'a'] = i;
	}
	for (int i = 0; i < 26; i++)
			printf("%d ", check[i]);
}
