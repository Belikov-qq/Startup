#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int main()
{
	int a, b, n;
	scanf("%d", &n);
	for (int i = n; i >= 1; i--)
	{
		a = 2 * i - 1; //#数量;
		b = n - i;//空格数量
		for (int c = 1; c <= b; c++)
			printf(" ");
		for (int c = 1; c <= a; c++)
			printf("#");
		printf("\n");
	}
	return 0;
}