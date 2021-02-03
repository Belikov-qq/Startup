#include<stdio.h>
int main()
{
	char s[];
	int c = 0;
	while(scanf("%s", &s) != EOF)
	{
		for (int i = 0; i <= 1; i++)
		{
			if (s[i] > s[i+1])
				{
					int t = s[i];
					s[i] = s[i+1];
					s[i+1] = t;
				}
		}
		if (s[0] > s[1])
		{
			int t = s[0];
			s[0] = s[1];
			s[1] = t;
		}
	}
	for(int i = 0; i <= ; i++)
		printf("%c ", s[i]);
		printf("\n");
	return 0;
 } 
