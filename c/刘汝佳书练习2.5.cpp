#include<stdio.h> 
int main()
{
	int a, b ,c, n;
	scanf("%d", &n);
	a = n / 100;
	b = n % 100 / 10;
	c = n % 100 % 10;
	if (a*a*a + b*b*b + c*c*c == n)
		printf("%d��ˮ�ɻ���", n);
	else
		printf("%d����ˮ�ɻ���", n);
	return 0;
 } 
