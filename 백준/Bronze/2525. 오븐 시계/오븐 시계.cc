#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int num1, num2, num3;
	scanf("%d %d\n%d",&num1, &num2, &num3);
	num2 += num3;
	num1+=num2/60;
	num1 %= 24;
	num2%=60;
	printf("%d %d", num1, num2);
	return 0;
}