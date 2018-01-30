---
title: "Computer Systems"
categories:
  - University
---

# Von Neumann Model

![img](http://www.polytechnichub.com/wp-content/uploads/2017/04/Von-Neumann-architecture.jpg)

The input device loads programs into memory, the CPU fetches program instructions from memory and generates data before outputting this data to the output device. This computer system was proposed by John Von Neumann in the 1940s.

# A personal computer
![Img](https://screenshotscdn.firefoxusercontent.com/images/2aa24dc3-c96f-4713-a862-a7afcb2b46e7.png)

The clock is a literal clock which keeps the entire system in check. 

The system bus is a collection of wires which allows parts of the computer to put data on a wire and have another part read that data.

# CPU
The CPU fetches and executes instructions from the main memory.
The instructions it executes are very basic such as simple addition, subtraction.

CPU operation is synchronised by the clock.

# System Bus

The system bus is a collection of wires used to transmit data between different parts of the computer. The sender places a message onto the bus and the receiver takes off the data from the bus.

The system bus has 3 components:
* The address bus
* The data bus
* The control bus
++
The address bus is used to specify what memory locations need to be accessed, the data bus is used to carry values and the control bus tells the receiver what to do with the data and addresses.

In reality there are usually several interconnected buses.

There needs to be one communication per bus per cycle or else bus contention happens.

# I/O Devices

When performing I/O operations the CPU needs to know when a device is ready. There are two ways to do this:
* Polling
* Interrupt

Polling is where the CPU checks periodically to see whether or not the I/O device is ready or has finished or has an input.

Interrupt is where the I/O device interrupts the CPU, preventing it from completing what it's currently doing to deal with I/O actions.

# Memory

All programs and data must be converted to binary form and stored in main memory before being processed.

There are 3 types of memory:

*  RAM (Random Access Memory)
Read and Write, Volatile. Forms bulk of main memory.

* ROM (Read Only Memory)
Read Only. Non-Volatile. Used to hold system boot code.

* Flash
Read and Write. Non- Volatile. Used in pen drives and SSDs.

Memory can be thought of as a sequence of words which each have their own unique address. Most modern systems are byte-addressable and often use 8-bits.

Simplified example of memory:

Addressable | Content
--- | ---
0 | "Blah"
1 | "I miss Boris Konev
2 | Raz Mondays

Bit zero is called the first item in the memory address (0th item) and is often called least significant bit. Most significant bit is the highest item in the memory list.

# Memory Units
A word is formed from one or more bytes. Individual bits are zero-indexed from right to left like most things in computer science. Bit zero may be referred to as the least significant bit (lsb) as it generally has the least influence on the combined total due to it representing the smallest unit. 

1 nibble = 4 bits

1 byte = 8 bits

1 KB (kilobyte) = 210 (1024) bytes

1 MB (megabyte) = 210 KB

1GB (gigabyte) = 210 MB

1TB (terabyte) = 210 GB

Note that manufacturers often use a factor of 1000 than 1024. 

# Machine Code Instructions
All machine code uses these basic commands:
* Data transfer
  * Load, store, push, pop
* Arithmetic
  * Add, subtract, multiply, divide, etc
* Logical
  * And, or, not, shift, rotate
* Test and Compare
* Control flow
  * conditional jump, unconditional jump, subroutine call and return

# Instruction format
The simplest instruction may be represented by a single byte while others may require many bytes.

<Opcode> <Data Len> <Operand Specifiers>

Opcode: Specifies the operation to be performed (see previous header).

Data Len: Specifies the length of data we are working with.

Operand Specifiers: the locations of source operands and destinations for results. Often one operand will operate as both the source and destination. 

# Addressing modes
The locations of operands are specified using addressing modes:

- Immediate
  * The operand value is encoded directly into the instruction
- Register
  * The operand is in a CPU register
- Direct
  * The operand is in main memory, the instruction encodes its address
- Register Direct
  * The instruction specifies a register which holds the main memory address of the operand. 