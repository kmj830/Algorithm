#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int main() {
	int n;
	scanf("%d", &n);
	char star[100]="";
	for (int i = 0; i < n; i++) {
		strcat(star, "*");
		printf("%s\n", star);
	}
	return 0;
}