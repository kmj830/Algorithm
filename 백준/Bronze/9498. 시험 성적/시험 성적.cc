#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int num1;
	scanf("%d",&num1);
	if (num1 >= 90) {
		printf("A");
	}
	else if (num1>=80) {
		printf("B");
	}
	else if (num1 >= 70) {
		printf("C");
	}
	else if (num1 >= 60) {
		printf("D");
	}
	else {
		printf("F");
	}
	
	return 0;
}