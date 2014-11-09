Understanding The Stack
==============

The stack is a way for computer programs to store and organize data. Stacks are created when a program calls a function. The function's arguments and local variables are stored on this stack, along with the function's return address which points to the next instruction to be executed once the function finishes running. 

The Stack: Generally the stack is layed out with local variables 

Let's take a deeper look:

The program stack.c contains the functions main() and func1(). func1() accepts three integer arguments and declares two character arrays. All of these get pushed onto func1's stack. If we compile and run stack.c we will see where and how space is allocated for these variables, and also where the functions return address is at and where it points to. 

    $ gcc -fno-stack-protector stack.c -o stack.x -m32 -std=c99
    $ ./stack.x

If you are familiar with C you may notice a few interesting things in the gcc command above. First, -fno-stack-protector disables the stacks 'canary' field. 
