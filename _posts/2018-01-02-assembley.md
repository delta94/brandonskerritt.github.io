---
title: "Assembley"
categories:
  - University
---

Binary is completely unusable but Assembley Language is usable and very close to binary.

Each line of assembley code is one operation.

Operation codes are called mneomics.

Registers have names that indiviudally identify them.

Addresses are specified using labels.

Example:
```
Adjust: mov eax num1 ; get first number
```
adjust is the label
mov is the opcode
eax is the register
num1 is a label
anything after ";" is a comment.

This can be translated to binary usign an assembler. _asm.

Hi Antony!

At the start of the video you talk about starting a company and appearing to be big but when the company goes big you pretend to be small, 

## Registers

EAX - Accumulator Register
Register for general purpose data storage. On an x86 CPU it looks like this:

```
    EAX
        AX
      AH AL
31  15  8 7 9
```

*Examples*
```assembley
mov eax, 42 ; put 42 into eax
mov ax, count ; gets 16 bit variable
mov al, 'x' ; put ascii value of x in low bite
inc eax ; increment eax
```
A simple assignment statement like 

```
num = count1 + count2 - 10
```


```assembley
mov eax, count1
add eax, count2
sub eax, 10
mov num, eax
```

EBX - Base register

ECX - Counter register

Often used for loops (seen later)
It can be used with sepcial jump instructions
```assembley
JECXZ ; jump if ecx is zero
JCXZ ; jump if cx is zero
```


EDX - Data register

Flags Register

Allows us to query the effect of the previous instruction. The status of an operation is stored in the Flags register. The flags register ocntains these flags:

```assembley
S: sign (indicates whether result is +ve (positive) or -ve (negative))
Z: zero (indicates if result is zero or not)
C: carry (indicates an arhimetic carry)
O: overflow (arhimetic overflow error)
```
The flags register can be used in conjunction with jump instructions to control program flow. So if flag O then jmp here etc

ESP Register

## Jump Instructions

The simplest jump instruction is the *unconditional* jump.
It jumps no matter what, as soon as it is reached in the instruction pointer.

It has the syntax
```assembley
JMP <address of the target instruction>
```
The address of the target instruction is normally a label

### Conditional Jump

Just like an if statement. 

Jumps that test flags:

Instruction | Jumps if | 0 or 1 | reason
--- | --- | --- | ---
JC | Carry flag is set | =1 | If arthimetic carry happens
JNC | Carry flag is clear | =0 | if no carry happens
JZ | Zero flag is set | =1 | if last result was a 0
JNZ | zero flag is clear | =0 | if last result *was not* 0
JS | Sign flag is set | =1 | Result is positive
JNS | Sign flag is not set | =0 | result is negative
JO | overflow flag is set | =1 | arhimetic overflow error has occured
JNO | Overflow flag is clear | =0 | arhimetic overflow error has not occured

Something cool to note is that every instruction has an inverse and the inverse has "N" in the middle of it, probably meaning "Not".

Example of using a jmp

```assembley
mov eax, num ; moves contents of num into eax
sub eax, 10
jnz store ; if number is not a zero then jump to store, otherwise run this
mov eax, 100

store:
  mov num, eax
```

## Comparing values
CMP is the most common way of comparing two values.
if eax and ebx contain the same number then cmp eax, ebx will set the Z flag.

### Conditional jumps using comparison operators

Instruction | What it does
--- | ---
JE | The first argument is equal to the second argument
JNE | The first argument is not equal to the second argument
JG / JNLE | First argument is Greater than second argument
JLE / JNG | First argument is Less than second argument
JGE / JNL | First argument is greater or equal than second argument

## Loops

Loops in assembley are simple

While loop

```assembley
while1:
  blah
  blah
  blah
end_while:
```

Do-while loop

```assembley
do-while:
  blah
end_while:
```

A for loop can be made in assembley. Take this example
```c
for (int x = 1; x <= 10; x++){
  y = y + x;
}
```

First attempt
```assembley
mov eax, 1 ; using eax as the variable x
floop:   ; start of for loop
  add y, eax ; update y
  inc eax ; x++
  cmp eax, 10
  jle floop ; counts up to 11, jump back to floop if cmp eax, 10 results in the less than flag
```

We can improve this by counting in reverse:
```assembley
mov eax, 10
floop:
  add y, eax
  dec eac ; x--
  jnz floop ; go to floop if previous operation does not result in 0
```

We can use ECX to improve the previous loop like so:

```assembley
mov ecx, 10
floop:
  add y, ecx
  loop floop
```

# Addresses and values
In assembley we can get the address of a variable with the LEA (load effective address) instruction
We often use EBX 
```assembley
LEA EBX, val
```
We can access the value pointed to by the address using *register indirect addressing mode* 
```assembley
mov eax, [ebx]
```

# Subroutines (functions)
Once a subroutine goes to a place in code, how does it know where to return?

It stores the return address into the instruction pointer register which always points at the next instruction.

So let's say you have the code
```
100
101
102
```
and ```101``` points to a memory location which is a subroutine. The subroutine is 5 lines long, so the code changes to
```
100
201
202
203
204
205
206
102
```
where 20-something is the address of each instruction in the sub routine.

A subroutine in assembley is programmed as
```label PROC
 BLAH
 BLAH BLAH
label ENDP
```
The procedure is called by ```call label```
You can use C functions inside assembley

The call instruction records the current value of EIP (instruction pointer) as the *return address* 

Puts the require subroutine address into EIP so the next instruction to be executed is the first instruction of the subroutine.

The RET instruction (return) retrives the stored return address and puts it back into the EIP, causing execution to return to the instruction after the CALL.

# The Stack

A stack is a memory arrangement (data structure) for storing and retrieving information (values)

the order of storing values from the stack can be described as LIFO

Stacks are incredibly useful
almost every assembley language has special instructions for implementing a stack

in the x86 assembley language there are PUSH and POP instructions

Push and POP operations make use of the stack pointer register *ESP* which holds the address of the item which is currently on top of the stack

Recall that in x86 architectur, the stack grows *dowm* in memory.

## Push
The PUSH instruction:
* decrements the address in *ESP* so that it points to a free space on the stack
* writes an item to the memory location pointed to by the ESP

ESP stands for extended stack pointer.

## Pop instruction
The POP instruction:
* fetches the item addresssed by the ESP
* Increments the ESP by the correct amount to removethe item from the stack

## Adjusting the stack

Items can be removed rom the stack or space reserved on top of the stack by directly altering the stack pointer:
ADD ESP, 8 ; take 8 bytes off the stack
SUB ESP, 256 ; Create 256 bytes on stack

ESP always puts it to the top of the stack.

The stack grows downwards so if we have a stack like

N |
:---: |
Y|
Q|
K|

And we add an item, X, like so

X |
:---:
N|
Y|
Q|
K|

So it grows downwards!!

# Parameters
The simplest kind of subroutines perform an identical function each time it runs.

## Value parameters

The information you give to a subroutine is simply a value.

## Reference parameters

Consider another subroutine: "given two variables, exchange (swap) their values".
The situation is different here, having only the values of the variables is not enough.

In calling the subroutine we will need to tell it the addresses of the variables.

Such parameters are called reference paraemters.

What you need is not the content but an address, a reference, where it is. Hence the term "pass by reference".



# Calling external functions
We can call functions, especially C functions, in assembley. We can call a function using the call command like so:
```c
call printf
```

When we call printf it can and will delete and overwrite registers. Because of this we need to store our register data somewhere. We can store this data in a *stack*. We store the data like so:

```assembley
mov ecx, 10 ; sets up loop counter
loop1:
  push ecx ; save the loop counter on stack
  lea eax, msg ; saves the address of message into eax
  push eax ; put the paraemter ontop top of stack
  call printf ; calls C function which prints first thing on stack, can mess up register data
  pop eax ; remove paraemter
  pop ecx ; restores saved loop counter
  loop loop1 ; goes back to top of loop
```

# Calling formatted printf's

We can insert data into a printf statement like so:
```c
printf("Number is %d\n", n);
```

If we want to do this in assembleu, we need to push it in reverse order. So first we push ```n``` and then we push the string ```Number is...```. This is how the stack works, items added always go to the top of the stack.

```c
#include <stdio.h>
#include <stdlib.h>
int main (void){
  char msg[] = "Number is %d\n";
  int n = 157;

  _asm {
    push n ; push the int first
    lea eax, msg
    push eax ; now stack the string
    call printf 
    add esp, 8 ; clean 8 bytes from stack
  }
  return 0;
}
```

To call Scanf we need to give it 2 paraemters, format string and num. Scanf reads info from the terminal.

```c
char fmt = "%d"; int num;
_asm {
  lea eax, num ; we need to push the address of num into eax

  push eax
  lea eax, fmt ; now the format string
  push eax
  call scanf
  add esp, 8 ; clean stack
}
```

We need to pass the address of something and not the value.

Clean stack means take stuff of that you put on. Always try to restore stack to the state you found it in. It's 8 bytes in this example because each variable is 4 bytes and we've pushed 2 things, which is 2 * 8 = 16.

 |
:---: |
ESP |

When we add data ESP goes down the stack like so:
 |
:---: |
 |
 ESP |

And in order to place it back to where the extended stack pointer (ESP) back to where it was we add some number to it like so:

 |
:---: |
ESP |

In order to know what to put to make the stack go back to where it was, you need to know the architecture and how much space things (data types) take up.

