vuln: vuln.c
	gcc -g -fno-stack-protector -no-pie -o vuln vuln.c

static: vuln.c
	gcc -g -fno-stack-protector -no-pie -static -o vuln vuln.c
