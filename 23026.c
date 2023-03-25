#include <stdio.h>

int main(void)
{
	int t;
	scanf("%d", &t);
	for (; t > 0; t--)
	{
		int n, b, r;
		int v[4001];
		int dp[4001] = {0};
		int box_cnt = 1;
		int truck_cnt = 1;
		int i = 0;
		scanf("%d %d %d", &n, &b, &r);
		for (int j = 0; j < n; j++)
			scanf("%d ", &v[j]);
		while (true)
		{
	}
}