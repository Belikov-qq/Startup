#include<stdio.h> 
int main()
{
	int a, b ,c, n;
	scanf("%d", &n);
	a = n / 100;
	b = n % 100 / 10;
	c = n % 100 % 10;
	if (a*a*a + b*b*b + c*c*c == n)
		printf("%d是水仙花数", n);
	else
		printf("%d不是水仙花数", n);
	return 0;
 } 
