#include<stdio.h>
int main()
{
	float x, y, z;
	scanf("%f", x);
	if (x*95 >= 300)
		y = 0.85;
	else
		y = 1;
	z = 95 * y *x;
	printf("%f", z);
	return 0;
}
