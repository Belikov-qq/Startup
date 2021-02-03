#define _CRT_SECURE_NO_WARNINGS 1
#define LOCAL
#include <stdio.h>
int main()
{
	int a, b, c, kase = 0;
	double n;
	while (scanf("%d%d%d", &a, &b, &c))
	{
		if ((a == b) && (b == c) && (c == 0))
			break;
		else
		{
			n = 1.0 / b;
			n *= a;
			printf("Case %d: %.*f", ++kase, c, n);
		}

	}
	return 0;
}