#define _CRT_SECURE_NO_WARNINGS 1
//#define LOCAL
#include <stdio.h>
int main()
{
#ifdef LOCAL
	freopen("2-4in.txt", "r", stdin);
	freopen("2-4out.txt", "w", stdout);
#endif // 
	int m, n, kase = 0;
	while (~scanf("%d%d", &m, &n)&& m)
	{
		double s = 0;
		for (long int i = n; i <= m; i++)
		{
			s += 1.0 / i / i;
		}
		printf("Case %d: %.5lf\n", ++kase, s);
	}
	return 0;
}