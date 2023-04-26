#include <stdio.h>
#include <string.h>

int vuln() {
    printf("Not so good\n");
    return 0;
}

int main(int argc, char **argv) {
    if (argc <= 1) {
        printf("Please hack me");
        return 1;
    }
    char buf[8];
    strcpy(buf, argv[1]);
    return 0;
}