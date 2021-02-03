#include<stdio.h>
#include<string.h>
int main()
{
	char sin, c;
	while(sin = getchar() != EOF)
		c = sin;
	printf("%c", c);
	return 0;
}
