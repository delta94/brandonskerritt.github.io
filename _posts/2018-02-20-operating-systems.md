---
title: "Algorithms and Data Structures"
categories:
  - University
---

# What is an Operating System?

The operating system is a piece of software whose job it is to take the base hardware of a device and turn it into a usuable machine for the user. It acts as the intermediary between hardware and user-usage, allowing the user to easily interact directly with the hardware; even when the user does not know they are accessing the hardware.

Examples of operating systems include:
* Unix
* Linux
* Windows
* Mac OS
* IOS
* Android

# Essential Managers of Operating Systems

There are 5 main managers of operating systems:
* Memory manager
* Process manager
* Device manager
* File manager
* Network manager

The network manager is a new addition to the operating system, previously all operating systems did not have networking capabillities and many still do not.

The Operating Systems manages the continious monitoring of resources and enforcement of policies across the system.

## Memory Manager

The Memory Maneger is in charge of the main memory on the computer system.

Its tasks involve:
* Preserves and protects the space in main memory that is occupied by the operating system
* Checks validity of each request from memory space. Verifies whether or not a user request is valid.
* For valid requests it allocates areas of memory not already in use for this.
* In a multi user system it keeps track of which users are using which section of memory.
* It deallocates sections of memory once they are finished with.

## Processor Manager

Decides how to allocate the Central Processing Unit (CPU)

The tasks of a processor manager are:
* Creates processes when neccesary to carry out tasks
* Performs initalisation of new processes
* Keeps track of the status of processes
* Assigns processes to the CPU when available
* Changes process states as events occur
* Handles termination of proceses on completion or abort
* Handles inter-process communication
* Manages process queues and priorisation

Something to note is that a process is not the same as a program.

## Device Manager

Monitors every device and control unit

The tasks of the device manager are:
* Allocates systems devices
* Deals with multiple requests for same device
* Performs communication with the device during operation
* Deallocates devices

## File Manager

The File manager keeps track of every file in the system.

Its tasks are:
* Organises all files
* Manages location of files
* Enforces restrictions on files
* Deals with standard file operations (delete, make new, etc)

## Network Manager

Modern operating systems require a network manager. The network manager allows users to share resources while controlling user access to them.

These resources can include hardware suhc as printers or disk drives or software such as files.

# Interaction between OS and Managers

Each Operating Systems has specific individual tasks to perform but it is not enough for each to operate on its own. Each manager must be able to work in harmony with the others at around the same time.

## Example
A user types in a command at the keyboard to execute a program. The following simplified steps might occur:

*Device Manager*: Receives keystrokes and builds up command line. Informs process manager that input has been received.

*Processor Manager*: Activates process awaiting a command. Process checks validity of command and then tries to execute the corresponding program.

*File Manager*: Checks to see if the program file is already in memory. If not, it finds ito n external storage and issues requests for it.

*Device Manager*: Communicates with the disk drive and retrives the program file from disk.

This goes on for quite a while, but you get the jist.

# Evolution of Operating Systems

In early systems jobs were loaded from punch card,s tape or other physical means. The job may include loading the compiler, assembler etc. The CPU remained idle for much of the time due to waiting for user input. The jobs ran sequentially from start to finish.

Batch systems were invented which passes a job to a human operator and then the operator would group jobs into batches with similar charecteristics which makes more efficient use of resources.

# Multi programming

Multi programming is where several programs are loaded into memory simultaenously, sharing the same CPU. When a running program cannot continue (maybe because it is waiting for input from the user) the operating systems switches to another program to run.

![img](https://screenshotscdn.firefoxusercontent.com/images/386273bc-7286-4b8c-a32c-b99a7ee735d2.png)

As you can see in this image the CPU executes whilest other programs are waiting for input.

# Multi-Access (Time-sharing)

This is an extension of multiprogramming. The CPU switches rapidly between processes to give an illusion of uninteruppted execution in parallel.

## Time-sharing the CPU

![img](https://screenshotscdn.firefoxusercontent.com/images/048c156c-ce75-4561-a680-5332b990d2d2.png)

Each program is allocated a fixed slice of time before the clock interrupts the program.

# Interrupts

The time sharing method depends on the abillity to interrupt execution at regular clock intervals. There are many circumstances in which it is desirable to interrupt the normal flow of a program to react to special events such as:
* User interrupts via keyboard / mouse usage
* Completion of an I/O task
* Power on or off

An interrupt is a form of automatical call of a sequence of instructions brought about usuaully by an event occuring outside the normal program execution.

Such a sequence of instructions is known as an *interrupt service routine (ISR)*. Unlike an ordinary subroutine call, an interrupt can take at any point in the execution sequence.

The address of each ISR is usually contained in an interrupt vector.

Certain interuppts (e.g. clock timeout) will not return control to the interupted program. Instead, control is handed to another program (context switch). If the programmer does not know when this will happen, how do we protect the register values of the original program?

The answer is for the OS to save them in a special data structure called the *process control block (PCB)*. 

The OS maintains a table of such descriptors, one for each process.

Register values can be reloaded when execution resumes at a later time.

# Processes

A program is a representation of an algorithm in some programming language.

A process refers to the activity performed by a computer when executing a program. 

A process is created when a program or command is executed.

However the correspondance is not always one to one.

A single program may have several processes.

# OS Structure
The OS has:

* A Central Kernal
    - resides permenetaly in memory
    - performs low-level, frequently needed tasks
* A set of processes
    - May be created by kernel or to service user activity
* Processes interact with kernel via system calls
    - Create processes, run programs, open files
* Kernel and some system processes may operate in *privledged* mode.

# System Initialisation

When the system powers on, an interrupt causes the computer to execute a bootstrap program stored in ROM.

This code initalises the system, runs diagnostic checks, sets up basic I/O. Basically making it ready to be used.

It loads the OS Kernel from boot partition of specified external disk drive and passes control to it.

The Kernel performs further initalisation and creates various system processes.

Further processes may be created because of user activity.

# Command Interpreter

Often called a shell.

Accepts and runs commands specified by the user.
May be graphical or textual.

The shell is just a normal user-level process

# System calls

User processes are not allowed to inspect or alter kernal code, or to make calls directly to its subroutine.

Services are requested via system calls.

Many system calls are given a ‘wrapper’ to make them look like ordinary subroutines.

Together with other useful functions, they form an Application Programmer Interface (API)