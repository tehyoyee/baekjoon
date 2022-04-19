// 2908 C

#include <stdio.h>

int	reverse(int a)
{
	int	new_a = 0;

	for (int i = 0; i < 3; i++)
	{
		new_a = new_a * 10 + a % 10;
		a /= 10;
	}
	return (new_a);
}

int	main(void)
{
	int	a;
	int	b;

	scanf_s("%d %d", &a, &b);
	a = reverse(a);
	b = reverse(b);
	if (a > b)
		printf("%d", a);
	else
		printf("%d", b);
}
