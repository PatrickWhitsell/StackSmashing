Understanding The Stack
==============

The stack is a way for computer programs to store and organize data. Stacks are created when a program calls a function. The function's arguments and local variables are stored on this stack, along with the function's return address which points to the next instruction to be executed once the function finishes running. 

The Stack: Generally the stack is layed out with local variables at the lowest memory addresses, the function arguments at the highest memory addressses, and the return address inbetween them. However, the top of the stack resides at higher addresses. The program writes data from the top to the bottom of the stack.

                                                     <----------- stack pushes
        lower memory addr                                   higher memory addr
        [------local variables------][--ret addr--][------function args------]
        top of stack                                           bottom of stack
        buffer writes --------->                  

The basic concept of a buffer overflow is that we write too much data to a local variable so that the write continues into the return address. We can then carfully modify the return address to execute arbitrary code on the system.

<b>Let's take a deeper look:</b>

The program stack.c contains the functions main() and func1(). func1() accepts three integer arguments and declares two character arrays. All of these get pushed onto func1's stack. If we compile and run stack.c we will see where and how space is allocated for these variables, and also where the functions return address is at and where it points to. 

    $ gcc -fno-stack-protector stack.c -o stack.x -m32 -std=c99
    $ ./stack.x

If you are familiar with C you may notice a few interesting things in the gcc command above. First, -fno-stack-protector disables the stacks 'canary' field. The canary is between the return address and the local variables on the stack, and is checked at run time before executing the return instruction. If the canary has been tampared with, execution is immidiately haulted by the operating system. 

Sample Stack Output From stack.c:

    buffer1: 0xffffd154
    buffer2: 0xffffd15c
    a: 0xffffd190
    b: 0xffffd194
    c: 0xffffd198
    ret addr: 0x8048528
