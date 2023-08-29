#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int main() {
	int n;
	char str[5004] = "";
	scanf("%d", &n);
	n /= 4;
	for (int i = 0; i < n; i++) {
		strcat(str, "long ");
	}
	strcat(str, "int");
	printf("%s", str);
	return 0;
}