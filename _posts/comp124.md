# Question 1

The working set is defined as:

W[t - s, s]

So the next working set is:

W(7, 3)

Which means the 

# Question 2

The working set expressed as W(3, 4) is W(3, 3 + 4), W(3, 7) which is from 3 to 7: {q, p}

# Question 3

To run sequentially we do:

20 + 15 + 30 + 10 = 50 + 25 = 75 seconds sequentially

Using multi programming it'll take 20 seconds to run A, then we can run B for 15 seconds while A waits for input.
so that's 20 + 15
then once the input ends we run B for 15 seconds more to finish then we run 10 seconds of IO
20 + 30 + 10 = 50

However if we run the IO interleaved (so A does IO while B computes, B does IO while A computes)
we get:
20 + 30 = 50 seconds again

Answer is C

# Question 4

D)

# Question 5

B. 

The program has to be able to handle multiple users calling it at once. Because of this, it uses fork().
Fork() creates a new process identical to the parent.
exec() literally means "execute the program". It obviously has to have this as you want the program to do something.
Because you don't want the parent to call exec() (in case 2 people type it at the same time) you get the child to call it
It's common courtsey to wait() after you have forked(). If you don't wait() then the parent process won't know when the child is finished.

This makes the child process into what is called a "zombie". It's supposed to be dead since it's finished but its parent process doesn't understand it's dead through wait().

# Question 6

A) The blocked running state means that the process cannot continue as it does not have enough resources, this isn't true,
B) The child does not have to be in a running state, if it does not have the resources required it may not run.
C) Yes, the parent process runs wait() which means it's waiting for the CPU to be handed back to it from the child.
D) Not true
E) Not true

# Question 7

d) blocked

The process is blocked from continuing until it receives the data from the file

# Question 8

the pipe charecter means "pass data from right to left"

```
head file | tail - 1 | wc - w
```

So first we execute wc - w

So it counts the number of words in the file.

It then provides this to tail - 1 which outputs the last 1 line of the number of words in the file

this is then provided to head file which outputs the first 10 lines of the last 1 line of the number of words in the file

# Question 9

In calculating the formula ut + 1⁄2at^2 using maximal concurrency, 
which of the operations might be computed in parallel?

ut; 1/2a; tt

so u * t is an operation that can be done on its own

1/2 * a can be done on its own

t * t can be done on its own

if we were programming it we would do:

```python
# Run all 3 lines at same time
u * t
1/2 * 2
t*t
```

# question 10


* a) A Java program need not necessarily lead to the creation of any * threads
* b) A thread is sometimes referred to as a lightweight process
* c) Threads share code and data access
* d) Threads share access to open files
* e) Threads are usually more efficient than conventional processes

* a) false, all java programs create 1 thread at the start to run the actual program
* b) this could be considered true
* c) threads can do this
* d) threads can do this (if they're super careful)
* e) true

# question 11
v raises the semaphore
P lowers the semaphore

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

so if T1 gets there, it raises the semaphore again (incrementing the semaphore to 2 (which is possible)), it enters its critical region and lowers the semaphore. T2 can lower the semaphore and access the critical region at the same time as t1.

If t2 got there first, it lowers the semaphore then goes into its critical region. But t1 raises the semaphore and goes into its critical region too.

Both of them go into the critical region.

# Question 12

What happens if two threads simultaenously run insert? What if the variable is empty?

# Question 13

They're not synchronized

# Question 14

im not sure

# Question 15

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

So deadlock is caused because both processes want resource y. if we share the resource, this fixes it.
Process B wants resource X but process A has it. If we take away resource X from process A then process B will have access to resource X and thus might give up control of resource Y, making everyone happy.

If B gave up Y, resource a can have Y and proces B can have x.

# Question 16

Given the CPU burst times of the processes, we know what their individual wait times will be:
–  0 milliseconds for P1 –  13 milliseconds for P2 –  18 milliseconds for P3
Thus, the average wait time will be (0 + 13 + 18)/3 = 10.3 milliseconds

What will the average wait time change to if the processes arrived in the order P2, P3, P1?

0 + 13 + p1