#include <stdio.h>

int main()
{
	int A;
	//printf("A에 넣을 숫자를 입력하세요\n");
	scanf("%d", &A);
	int B;
	//printf(" B에 넣을 숫자를 입력하세요\n");
	scanf("%d", &B);
	
	if (A>0 && B<10)
	{
		printf("%d", A + B);
	}
}