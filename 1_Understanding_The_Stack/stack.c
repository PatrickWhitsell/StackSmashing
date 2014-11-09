//Compiling to x86-64 Assembly code 
// $ gcc -S stack.c -o stack.s

//For x86 32bit Assembly code
// $ gcc -fno-stack-protector stack.c -o stack.x -m32
// $ gdb stack.x
// (gdb) disassemble func1

#include <stdio.h>

void func1(int a, int b, int c)
{
	char buffer1[8];
	char buffer2[32];
	
	printf("a: %p\n", &a);
	printf("b: %p\n", &b);
	printf("c: %p\n", &c);

	printf("buffer2: %p\n", &buffer2);
	printf("buffer1: %p\n", &buffer1);

	printf("ret addr addr: %p\n", buffer2+52);
	printf("ret addr: %p\n", __builtin_return_address(0));
}
	
int main()
{
	func1(1,2,3);
}

