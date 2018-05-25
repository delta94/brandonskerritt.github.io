---
title: "COMP124 practice exam"
---

# COMP124 practice exam
## Compiled by Brandon Skerritt 💩 👍
## Answers at the bottom

### Question 1

```
Pages - | p | q | r | q | q | q | p | r | r | q
Times -   0   1   2   3   4   5   6   7   8   9
```

Predict the next working set using the principle of locality rule for the set W(10, 3)

### Question 2

```
Page - | p | q | r | q | q | q | p | r | r | q |
time -   0   1   2   3   4   5   6   7   8   9
```

What is the working set expressed as W(3, 4).

### Question 3 

```
The following statements desribe the performance of two programs 
(Where the computation and input/output could be interleaved):
* A performs a total of 20 seconds of computation adn 15 second of I/O.
* B performs a total of 30 seconds fo computation and 10 seconds of I/O.

Which of the following are true?
1. It will take up to 50 seconds to run A and B sequenctially 
2. It will take up to 75 seconds to run A and B sequenctially 
3. Using multiprogramming, the shortest time to execute both is 50 seconds
4. Using multiprogramming, the shortest time to execute both is 40 seconds
```

* a) 1 and 3
* b) 1 and 4
* c) 2 and 3
* d) 2 and 4
* e) none of the above

### Question 4
```
Suppose two users simultaneously type the following 
command at the unix shell command prompt ($): 

$ ls –l
```
Which of the following are true?

* a)  One process and one program is involved
* b)  Two processes and two programs are involved 
* c)  One process and two programs are involved 
* d)  Two processes and one program are involved 
* e)  None of the above

### Question 5 
```
If you type ‘cat prog.c’ at a UNIX command prompt, 
which of the following sequences of system calls would be invoked?
```

* a)  The shell makes an exec() call
* b)  The shell calls fork(); the child process calls exec() and the parent calls
wait()
* c)  The shell calls fork(); the child calls wait() and the parent calls exec()
* d)  The shell calls exec() and then wait() and then fork()
* e)  The shell calls wait() then fork(), creating a child which calls exec()

### Question 6 
```
If a process executes a fork() system call, which of the following are true?
```
* a)  The parent process is moved to the blocked state
* b)  The child process is placed in the running state
* c)  The parent process is moved to the ready state
* d)  The child process is placed in the blocked state
* e)  The parent process is moved to the terminated state

### Question 7 
```
A running process makes a system call to read data from a file. 
Which process state should it enter next?
```
* a)  New
* b)  Ready
* c)  Running
* d)  Blocked
* e)  Terminated

### Question 8
```
If the UNIX command ‘head file’ outputs the first 10 lines of file, 
the command ‘tail –n file’ outputs the last n lines of file, 
and the command ‘wc –w file’ counts the number of words in file, what will the following output?

head file |tail-1| wc–w
```
* a) The number of words in the tenth line from the end of file
* b) The first 10 lines of file, then the last line of file, 
then the * number of words in file
* c) The number of words in line 10 of file only
* d) The number of words in line 10, then line 9, then line 8, etc.
* e) The number of words in the first ten lines plus the last line of file

### Question 9
```
In calculating the formula ut + 1⁄2at2 using maximal concurrency, 
which of the operations might be computed in parallel?
```
* a)  u*t; a/2; t*t
* b)  u*t; t+1⁄2; a*t
* c)  u+a; t*t
* d)  u+a; t*t; 1⁄2
* e)  no parallelism is possible for this formula

### Question 10 
```
Which of the following statements about threads is FALSE?
```
* a)  A Java program need not necessarily lead to the creation of any * threads
* b)  A thread is sometimes referred to as a lightweight process
* c)  Threads share code and data access
* d)  Threads share access to open files
* e)  Threads are usually more efficient than conventional processes

### Question 11
```
The value of a semaphore s is initially 1. 
What could happen in the following situation?

T1 V(s);
critical region
P(s);

T2 P(s);
critical region
V(s);
```

* a)  Deadlock will ensue
* b)  T1 and T2 can both enter their critical regions simultaneously
* c)  Neither T1 nor T2 can enter its critical region
* d)  T1 can never enter its critical region, but T2 can enter its own
* e)  T1 can enter its critical region, but T2 can never enter its own

### Question 12
```
class Buffer {
  private int v;

  public void insert(int x) {
    v = x;
    }
  public int remove() {
    return(v);
    }    
}
```
What is wrong with the following code:

### Question 13
``` 

class Buffer {
  private int v;
  private volatile boolean empty=true;

  public void insert(int x) {
    while (!empty)
      ; // null
    empty = false;
    v = x;
    }

  public int remove() {
    while (empty)
      ; // null
    empty = true;
    return(v);
    } 
}
```
What is the problem with the following code?

### Question 14
```

class Buffer {
  private int v;
  private volatile boolean empty=true;

  public synchronized void insert(int x) {
    while (!empty)
      ; // null
    empty = false;
    v = x;
    }

  public synchronized int remove() {
    while (empty)
      ; // null
    empty = true;
    return(v);
    } 
}
```
What is wrong the the following code? 

### Question 15 
```
Consider the following situation regarding two processes
 (A and B), and two resources (X and Y):
-  Process A is granted resource X and then requests resource Y.
- Process B is granted resource Y and then requests resource X.

Which of the following is (are) true about the potential for deadlock?
I.  Deadlock can be avoided by sharing resource Y between the two processes
II.  Deadlock can be avoided by taking resource X away from process A
III.  Deadlock can be avoided by process B voluntarily giving 
up its control of resource Y
``` 
* a)  I only
* b)  I and II only
* c)  I and III only
* d)  II and III only
* e)  I, II and III

### Question 16 
```
Given the CPU burst times of the processes, we know what their individual wait times will be:
–  0 milliseconds for P1 –  13 milliseconds for P2 –  18 milliseconds for P3
Thus, the average wait time will be (0 + 13 + 18)/3 = 10.3 milliseconds
```
What will the average wait time change to if the processes arrived in the order P2, P3, P1?

### Question 17
```
•  The wait times for each process are as follows:
•  3 milliseconds for P1
•  14 milliseconds for P2
•  8 milliseconds for P3
•  0 milliseconds for P4
```
What would the average wait time be if we had been using the First Come, First Served algorithm?

### Question 18
``` 
A starvation-free job-scheduling policy guarantees that no job waits indefinitely for service. 
Which of the following job-scheduling policies is starvation-free?
```
* a)  Round-robin
* b)  Priority queuing
* c)  Shortest job first
* d)  Youngest job first
* e)  None of the above

### Question 19

Suppose that a scheduling algorithm favours processes that have used the least CPU time in the recent past. 
Why will this algorithm favour I/O-bound programs and yet not permanently starve CPU- bound programs?


### Question 20
```
Suppose we have the following four processes all arriving at time 0 in the following order:
P1 with CPU burst of 8 milliseconds, 
priority 2 P2 with CPU burst of 2 milliseconds, 
priority 1 P3 with CPU burst of 5 millisecond, 
priority 3 P4 with CPU burst of 4 milliseconds, 
priority 2
```
Which of the following algorithms gives the minimum average waiting time: SJF, Priority, RR (using a time quantum of 2 milliseconds)?

### Question 21
```
In a computer memory, a 100K partition becomes available. 
In the ready list is a program image of size 300K, plus three others of sizes 100K, 85K and 15K.
```
Assuming that our current priority is to avoid starvation of the 300K program, which of those in the list should be swapped into the available partition?

* a)  The 100K program
* b)  The 85K program
* c)  The 15K program
* d)  Both the 15K and the 85K programs
* e)  None of the above

### Question 22
```
A new program requires 100K of memory to run. 
The memory management approach adopted is a simple partitioning one, 
and the operating system has the following list of empty partitions:

* 60K, 240K, 150K, 600K, 108K, 310K
```
Assuming that the 150K partition is chosen, say which of the following selection strategies is being used:

* a)  First fit
* b)  Best fit
* c)  Worst fit
* d)  All of the above e)  None of the above

### Question 23
A program is split into 3 segments. The segment table contains the following information:
```
segment       datum         limit
  0            1700         5500
  1            5600         8100
  2            8300         9985
```
Where ‘limit’ is the physical address following the end of the segment, and instructions take the form opcode segment, offset
If the program executes
–  LOAD 1, 135
What physical address is accessed?

* a)  1835 
* b)  5735 
* c)  8435 
* d)  8235 
* e)  5635

### Question 24
Process A and process B both share the same code segment S. Which of the following statements is (are) true?
```
I.  An entry for S appears in both segment tables
II.  The segment code must be re-entrant
III.  The segment code must be recursive
```
* a)  I only
* b)  II only
* c)  IandII
* d)  I and III
* e)  I, II and III

### Question 25 
```
In a paged memory system, why are page sizes invariably a power of 2?
```
* a)  Because computer memory is usually a multiple of 1K, which is a * powerof 2.
* b)  Because pages have to begin at address boundaries that are even.
* c)  Because virtual address spaces are usually a power of 2 in size
* d)  Because it simplifies indexing of the page table and the calculation of the page * offset.
* e)  Because most data types occupy even numbers of bytes.

### Question 26
```
A computer uses 16-bit addressing. Its page size is 512 bytes.
 What is the maximum number of entries that the page table must be capable of holding?
```
* a)  16 
* b)  64 
* c)  128 
* d)  256 
* e)  512

### Question 27 
The page table shown below is for a job in a paged virtual storage system with a page size of 1K:
```
segment     datum
 0            4
 1            2
 2            0
 3            1
```
A virtual address of [1, 352] would map on to what actual address?

* a)  354 
* b)  1376 
* c)  2352 
* d)  2400 
* e)  4448

### Question 28
Which of the following programming constructs tend to contribute 
to the phenomenon expressed in the Principle of Locality?
```
I.  Iteration (e.g. FOR and WHILE loops)
II.  Selection (e.g. IF-statements)
III.  Recursion
```
* a)  I only
* b)  III only
* c)  I and III only
* d)  II and III only
* e)  I and II only

### Question 29
```
Pages - | p | q | r | q | q | q | p | r | r | q
Times -   0   1   2   3   4   5   6   7   8   9

Page s arrives at time 10. Which of the following 
policies suggests we should throw out page p to make room for s?

I.    LRU 
II.   LFU 
III.  FIFO

```

* a)  I only
* b)  III only
* c)  I and II
* d)  I and III e)  I, II and III

### Question 30
```
Which of the following is true about linked 
filestore allocation versus contiguous allocation?
```
* a)  Linked is slower for both sequential and direct access.
* b)  Linked is faster for both sequential and direct access.
* c)  Linked is faster for sequential access, but slower for direct access.
* d)  Linked is slower for sequential access,but faster for direct access.
* e)  The performance for linked and contiguous is roughly the same for both forms of access.

### Question 31
```
When should a deleted file not be garbage collected?
```
* a)  When there are multiple links to it.
* b)  When the file contains program code.
* c)  When there is only one copy of the file.
* d)  When the file is asystem file rather than a user file.
* e)  When the file contains encrypted data.

### Question 32
To assist in locating a bug that is causing a program to crash, a programmer inserts print statements as follows:
```
begin ...
        print(“Got to point A without crashing”);
        ...
        print(“Got to B without crashing”);
        ...
end
```
Which of the following is true:

a)  Too much information will probably be written to the screen to allow location of the bug.
b)  The very insertion of the print statements will probably alter the program’s behaviour,
preventing the bug from occurring.
c)  The new diagnostic statements will interfere with the program’s existing output, introducing further bugs.
d)  The bug will probably make all print statements inoperable.
e)  The use of output buffers by the system might prevent some messages from being written.

### Question 33 
 If the symbol table for a compiler is size 4096, how many comparisons on average need to be made when performing a lookup using the binary chop method?
 ```
 a)  2 
 b)  11 
 c)  12 
 d)  16 
 e)  31
 ```

 ### Question 34 
 Concerning compilation, which of the following is NOT a method for symbol table access?
 ```
a)  Sequentiallookup
b)  Directlookup
c)  Binary chop
d)  Hashaddressing
e)  Hashchaining
```

### Question 35
Consider the following grammar, where S, A and B are non- terminals, and a and b are terminals:
```
S ::= AB 
A ::= a
A ::= BaB 
B ::= bbA
```
Which of the following is FALSE?

* a)  The length of every string derived from S is even.
* b)  No string derived from S has an odd number of consecutive b’s.
* c)  No string derived from S has three consecutive a’s.
* d)  No string derived from S has four consecutive b’s.
* e)  Every string derived from S has at least as many b’s as a’s.

### Question 36
If the array x contains 20 ints, as defined by the following declaration:
```
 int x[] = new int[20];

What kind of message would be generated by the following line of
code?
 a := 22; val := x[a];
```
* a)  A Syntax Error.
* b)  A Static Semantic Error.
* c)  A Dynamic Semantic Error.
* d)  A Warning,rather than an error.
* e)  None of the above.

### Question 37
A BNF grammar includes the following statement:
```
<statement> ::= <iden> := ( <expr> );

What kind of message would be produced by the following line of code?

a:=(2+b;
```
* a)  A Syntax rror.
* b)  A Static Semantic Error.
* c)  A Dynamic Semantic Error.
* d)  A Warning,rather than an error.
* e)  None of the above.

### Question 38
Which of the following postfix expressions is equivalent to the following expression?
```
a*b – c/d
```
* a)  abcd *-  /
* b)  ab * - cd /
* c)  abcd / - *
* d)  ab * cd / -
* e)  abc * - d /

### Question 39

Which of the following is NOT a form of intermediate representation used by compilers?
```
a)  Postfix
b)  Tuples
c)  Context-free grammar
d)  Abstractsyntaxtree
e)  Virtualmachinecode
```

### Question 40
What optimisation technique could be applied in the following examples?
```
a = b^2 
a = a/2
```
a)  Constant Folding
b)  Code Deletion
c)  Common Sub-Expression Elimination
d)  Strength Reduction
e)  Global Register Allocation

### Question 41
Why can’t we allocate data frames statically, i.e. have one fixed area for each subprogram? Which of the following are true
```
I.   Data Structures may be dynamically allocated
II.  Object Orientation demands the creation of Instances
III. Recursion causes data frames to grow arbitrarily
```
a)  I only
b)  III only
c)  I and II only
d)  II and III only
e)  I, ll and lII only

### Question 42
Which of the following is usually NOT represented in a subroutine’s activation record frame for a stack-based programming language?
```
a)  Values of locally declared variables
b)  A heap area
c)  The return address
d)  Apointer to the calling activation record
e)  Parameter values passed to the subroutine
```

### Question 43
Lex is a software tool that can be used to aid compiler construction. It is an example of which of the following?
```
•  A scanner generator
•  A parser generator
•  A code generator generator
•  A semantic analyser
•  A code debugger
```
## Answers
### Question 1

W(t - s, s) = W(10 - 3, 3) = W(7, 3) = {r, r, q} = {r, q}

### Question 2

The working set of a process is defined to be the set of resources (T, s) defined in the time interval [T, T+s].

W(3, 4) = W(3, 3 + 4) = W(3, 7) = {q, q, q, p} = {q, p} 

### Question 3 
Answer: c
* Runs sequentially. A has to finish running before B starts
* With multiprogramming, I/O for one process can take pave whilst the computation takes place for another. Therefore 3 is true

### Question 4
Answer: d
Only one program (ls) is involved, but this will be run as two pocesses.

### Question 5
Answer: b
The shell calls fork(); the child process calls exec() and the parent calls wait(). The shell is just another process that can take a string as standard input, look for the program referenced by the string, and then run this program. Unless the program is put in the background, the shell will wait until the program has finished.

### Question 6 
Answer: c
The parent process will be moved back to the ready state (depending on the scheduling policy), and once the child has been admitted, will also be placed in the ready state

### Question 7 
Answer: d
Blocked; it may take some time before the file system can read the file (e.g. on a networked file store), so the process is blocked until the data is available.

### Question 8 
Answer: c
Only line 10 will be passed to wc -w

### Question 9
Answer: a
u*t; a/2; and t*t – i.e. only those parts of the formula that have no dependencies on other parts of the formula can be run concurrently. Think how the formula could be written in 3-code...

### Question 10 
Answer: a
Every Java program starts as a thread! The rest of the statements are true...

### Question 11
Answer: b
If T1 executes first, then it acquires the semaphore, which is immediately released by T2. Both then execute the critical region.
If T2 executes first, it releases a semaphore it does not have, which can be acquired by T1. Again, both can execute the critical region.

### Question 12 

We have to ensure the following (problems with synchronsization):
–  producer cannot put items in buffer if it is full
–  consumer cannot extract items from buffer if it is empty
–  buffer is not accessed by two threads simultaneously 

### Question 13

*  Two threads can still access the buffer simultaneously – there is nothing to stop this
* Note: The problem gets even worse when there are several consumers and producers

### Question 14
* Deadlock can arise
* If the consumer tries to remove an item from an empty buffer, it will *ve to wait for the buffer to be filled by the producer
* But the buffer will not be filled as the consumer has the lock
* Similarly for the producer

### Question1 15 
Answer: e
I, II and III – as all three options will avoid exclusive ownership of the resources.

### Question 16
*  P2 with CPU burst of 5 milliseconds
*  P3 with CPU burst of 1 millisecond
*  P1 with CPU burst of 13 milliseconds
 Thus, the average wait time will be (0 + 5 + 6)/3 = 3.7 milliseconds

### Question 17
(0 + 5 + 14 + 20)/4 = 9.75 milliseconds

### Question 18
Answer: a
Round Robin – this gives all processes equal access to the processor. The other techniques each select some “types” of processes to others (e.g. short processes, high priority processes etc).

### Question 19
It will favour the I/O-bound programs because of their relatively short CPU burst times but, the CPU-bound programs will not starve because the I/O-bound programs will relinquish the CPU relatively often to do their I/O.

### Question 20
* p1 - 8ms priority 2
* p2 - 2ms priority 1
* p3 - 5ms priority 3
* p4 - 4ms priority 2
 Average waiting time is (11 + 0 + 6 + 2)/4 = 4.75 milliseconds

### Question 21 
Answer: e
If we are avoiding the starvation of the 300K program, then we need to wait for an adjacent partition to become available to allow for the 300K program to run

### Question 22
Answer: e
First Fit would select 240K
Best Fit would select 108K
Worst Fit would select 600K
... as none of these select the 150K partition, then some other strategy has been used!

### Question 23
Answer: b
5600 (from segment 1) + 135 (offset)

### Question 24
Answer: c
I and II – as the segment is shared, both processes need to index it (i.e. include an entry in their respective segment tables, and, the code must not be changed by its use (i.e. it should be re-entrant). Recursion is irrelevant to this issue.

### Question 25
Answer: d
Because it simplifies indexing of the page table and the calculation of the page offset.

### Question 26 
Answer: c
128; 9 bits are used for addressing the 512 bytes in each page, so the remaining 7 bits are used to address the pages

### Question 27
Answer: d
2048 (from page 1) + 352 (offset)

### Question 28
Answer: c
I and III only

### Question 29
Answer: e
I, II and III

### Question 30 
Answer: a
Linked is slower for both sequential and direct access

### Question 31
Answer: a
When there are multiple links to it.

### Question 32
Answer: e
The buffers may not be flushed, and the program may continue (and crash) giving misleading information.

### Question 33
Answer: b
11 – as there are log2N-1 comparisons on average

### Question 34
Answer: b
Direct Lookup

### Question 35
Answer:d
No string derived from S has four consecutive b’s

### Question 36
Answer: c
A dynamic semantic error – the value of a would cause an array out of bounds error

### Question 37
Answer: a
A syntax error – all the tokens are valid, but the close parenthesis is missing, resulting in an error in the grammar

### Question 38
Answer: d
ab*cd/-

### Question 39
Answer: c
A context-free grammar defines the language used by the compiler; the rest are intermediate representations

### Question 40
Answer: d
Both expressions can be reduced by changing the operator: a = b ^ 2 can be reduced to a = b * b
a = a / 2 is a right shift operation: a = a >> 1

### Question 41
Answer: c
I and II only; recursion does not affect the size of data frames

### Question 42
Answer: b
A heap area

### Question 43
Answer: a
Lex is responsible for identifying tokens using regular expressions. It is therefore a scanner generator
