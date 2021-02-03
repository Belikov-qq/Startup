#define _CRT_SECURE_NO_WARNINGS 1
#define LOCAL
#include<stdio.h>
int main()
{
#ifdef LOCAL
	freopen("2-2 in.txt", "r", stdin);
	freopen("2-2 out.txt", "w", stdout);
#endif //
	int x, y, z, kase = 0;
	while (scanf("%d%d%d", &x, &y, &z) == 3)
	{
		for (int i = 10; i < 101; i++)
		{
			if (i % 3 == x && i % 5 == y && i % 7 == z)
				printf("Case %d: %d\n", ++kase, i);
		}
		printf("Case %d: No answer\n", ++kase);
	}
	return 0;
}