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

