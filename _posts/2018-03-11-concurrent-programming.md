---
title: "Concurrent Programming"
categories:
  - University
---

We can run threads and programmes at the "same time".

For example, take the maths equation 3 + 4 + 3 * 2.

You can break this down into (3 + 4) + (3 * 2). 

You do not need to calculate 3 + 4 and then calculate 3 * 2, you can calculate them both at the same time.

When you do these calculations at the same time, this is called a "thread". We will show how threads work in Java.

# Threds

"A thread in computer science is short for a thread of execution. Threads are a way for a program to divide (termed "split") itself into two or more simultaneously (or pseudo-simultaneously) running tasks. Threads and processes differ from one operating system to another but, in general, a thread is contained inside a process and different threads in the same process share same resources while different processes in the same multitasking operating system do not."

# Java Threads

When a Java program starts up, a single thread is always created for the program.

New threads may be created by the programmer.

When you set up a thread, you have to write a method called __run()__. This methods defines what the thread will do during the lifetime of the thread. 

Threads may be started within a main() method, and run simultaenously, sharing variables etc.

```java
class Worker1 extends Thread{
    public void run(){
        System.out.println("I am a worker thread");
    }
}

public class First{
    public static void main (String args[]){
        Worker1 runner = new Worker1();
        runner.start();
        System.out.println("I am the main thread");
    }
}
```

So some things to note here. Class Worker1 is derived from the Thread class, it is a child of the Thread class. The work (what it does) of this new thread is defined in the run() method.

Calling the start() method seen by ```runner.start()``` allocates memory to the new thread and causes the run() thread to run.

So what we have now is two seperate threads running at the same time.

Question - What prints first? Does "I am a worker" print or "I am the main thread"? Well,we don't actually know. It's kind of up to the thread class and the CPU itself as to what runs first or if it runs at the exact same time.

Remember that we never ever call the run method, we always call the start method which will create the thread and initisalise it and then that start method will call the run method.

In Java you can have arrays of threads, all running at the same time. You can have thousands and thousands of threads if you want, but this creates complexity. We don't know the order in which things may happen.

Although Java specifies the language, it does not specify how threads are run.

# Mutual Exclusion

Indeterminacy arises because of possible simulatenous access to a share resource.

The solution is to allow only one thread at a time to access the resource, all the other threads must be excluded or must wait.

When a thread accesses any **shared** resource, it is in a **critical section (region)**.

One way to enforce mutual exclusion is via **semaphores**.

## Semaphore

In real life a semaphore is a system of flags used to send messages from boat to boat or other places. It's a system of raising and lowering flags.

In Computer Science a semaphore is used to represent whether a shared resource is being used or not being used.

A flag can either be up, or down.

# Synchronisation Problems

There are a number of famous problems that illustrates the problem of concurrency. They are used to validate and test synchronised schemes.

## Producer-Consumer Problem

The Producer-Consumer problem is a really common situation where you have a producer (thread); in real life this might be a secretary who brings in some paper work to be dealt with. The producer creates, it produces work to be done.

There's a consumer process (manager) who takes that input and deals with it in some way.

The producer and the consumer have to work together, and they do so by using an intermediate buffer. F

In real life this could look like:

Secretart puts item into letter tray
Manager Takes from letter tray and deals with the letters

We have to make sure that the:

* The producer cannot put items into the buffer if the buffer is full
* The consumer cannot take out items from the buffer if the buffer is empty
* The buffer is not accessed by two threads simultaenously

### In Java

```java
class Buffer {
    private int v;

    public void insert (int x){
        v = x;
    }

    public int remove(){
        return (v);
    }
}
```

Insert simply takes the argument passed to the method and stores that into our variable v, and remove simply returns the variable v.

```java
class Producer extends Thread{
    private Buffer b;

    public Producer (Buffer buf){
        b = buf;
    }

    public void run(){
        int m;
        b.insert(m);
    }
}
```

So this extends thread because every concurrent thread extends thread and we have a run method because every thread must hvae it's own run method.

The consumer class is similar but instead it calls n = b.remove().

```java
class Producer extends Thread{
    private Buffer b;

    public Producer (Buffer buf){
        b = buf;
    }

    public void run(){
        int m;
        b.remove(m);
    }
}
```

Here's our main method:

```java
public class Prodcon{
    public static void main (String args[]){
        // creates buffer, producer, and consumer
        Buffer b = new Buffer();
        Producer p = new Producer(b);
        Consumer c = new Consumer(b);

        p.start();
        c.start();
    }
}
```

Now this faces the problem of "Is the buffer empty?". If it isn't empty, it kinda ruins the whole program and ka-blam-'mam it's errors all the way down. Let's change the code:

```java
class Buffer{
    private int v;
    private volatile boolean empty = true;

    public void insert (int x){
        while (!empty){
            // do stuff here
        }
        empty = false;
        v = x;
    }

    public int remove(){
        while (empty){
            // do stuff here
        }
        empty = true;
    }
}
```

The emtpy boolean tells us if the buffer is empty or not. "Volatile" ensures the computer will reload the variable every time it is tested.

This idea of looping until a situation changes is called **busy waiting** or sometimes called **spinlock**. It's not a very efficient way of doing things. 

In a single CPU situation if we call insert() it will loop until the buffer is empty but because it has the only CPU core no one else can empty the buffer so it's just an infinite loop of waiting on other people.

It may be more efficient for a waiting process to give up access to the CPU with a method called Yield(). The thread says "I can't continue, there's nothing useful I can do here" and this means that another thread can take over.

So let's have another go at this:

```java
class Buffer{
    private int v;
    private volatile boolean empty = true;

    public synchronized void insert (int x){
        while (!empty){
            // do stuff here
        }
        empty = false;
        v = x;
    }
}

public syncrhonized int remove(){
    while (empty){
        // do stuff here
    }
    empty = true;
    return (v);
}
```

Here we introduce the American spelt word Syncrhonized. What does this do?

Every object has what is called a lock, you can lock an object.
When a thread calls one of these syncrhonized methods it controls that lock, every other thread that tries to call the syncrhonised method on that object has to wait; it is locked out.

The synchronized method says "while I am in this method, nobody else can access this object".

But this gives us one last problem to solve, instead of having an empty loop we need to have a wait method and a notify method. 

The wait() call releases the lock, if the producer cannot continue becasue the buffer is full it doesn't just sit there and loop - it calls wait() which makes it release the lock.

Our current thread moves to the "wait set" - a set of threads waiting to access this object.

The notify() call moves an arbitrary thread from the wait set back to the empty set, which tells another thread to try and have another go.

There's another function called notifyAll() which moves all the waiting threads back to the working set.

```java
class Buffer{
    private int v'
    private volatile boolean empty = true;

    public synchronized void insert (int x){
        while (!empty){
            try{
                wait();
                catch (InterruptedException e){}
            }
        }
        empty = false;
        v = x;
        notify();
    }
    
}
```

## The Dining Philosphers

The producer-consuemr problem models a synchronization environment where each process with distinct roles have to coordinate access to a shared facillity.

In the dining philosphers problem all the roles are identical.

All they can do is eat and think, in a routine like:

Eat - think - eat - think...

Philosphers don't need anything to think, however they need 2 items of cutlerly (2 chopsticks, knife and fork) to eat.

However only n chopsticks are given to them.

If there are 5 philsophers, there are 5 chopsticks.

We can model this problem by saying that the chopsticks are a shared resource.

Here is some abstract code for a philosopher:

```java
public void run(){
    while (alive){
        think();
        stick[i].get();
        stick[(i+1)%5].get();
        eat();
        stick[i].put_down();
        stick[(i+1)%5].put_down();
    }
}
```

Chopstick code:

```java
class Chopstick{
    private volatile boolean in_use = false;

    public syncrhonized get(){
        while (in_use){
            try{
                wait();
            }
            catch {}
        }
        in_use = true;
    }

    public syncrhonized put_down(){
        in_use = false;
        notify();
    }
}
```

What if every philosopher picks up the chopstick to their right? Well, when they go to pick up the chopstick to their left they have seen that the stick on the left is being used by someone else. So all the philsophers would wait indefinitely for a chopstick to be released. A situation like this is called **deadlock (deadly embrace)**. Where every process is waiting on something.

One of the solutions to this is to only allow n-1 philosophers to dine simultaenously.

We could also make even numbered philosophers pick up chocksticks in the order right then left and we can make odd philsophers pick up left then right.

We can also insist that both chopsticks are claimed at the same time.

But all of this complicates the code.

Now let's suppose Phillosopher 0 and Phillosopher 2 grab their chopsticks first, then  P1, P3, and P4 have to wait to eat. If P0 and P2 put down their chopsticks and then immedtiailly claim them again, the others will never eat.

Even if p0 and p2 took turns, p1 would never eat!

This is called **starvation**. Starvation occurs when one or more of the partiticpants in a concurrent system is denied access to resources.

# Resource Allocation Graph

![img](https://screenshotscdn.firefoxusercontent.com/images/d1004006-92e6-4a35-972a-112622f20db1.png)

A resource allocation graph is a graph which has processes (circles) and resources (squares). The number of dots inside a resource square is the number of resources it can give out. Arrows pointing to processes from resources indicate that Process X is using resource Y.

When a resource graph has no cycles, it has no deadlock. Typically a cycle **indicates** deadlock, but not always.

# Dealing with Deadlock

You can prevent deadlock by making a system which deadlock cannot possibly occur. You can avoid deadlock by making decisions dynamically as to which resource requests can be granted. You can always allow deadlock to occur, then cure it or to just ignore the problem.

## Deadlock Prevention

- Force processes to claim all resources in one operation
- Require processes to claim resources in pre-defined manner
- Grant requests only if all allocated resources released first

## Deadlock Avoidance

- Requires information about which resources a process plans to use
- When a request is made, system analyses allocation graph to see if it may lead to deadlock

## Detection and Recovery

- Requires analysis of graph
- Recovery could involve process termination

## Ignoring deadlock

Used by Windows, Unix, JVM. Deadlock rarely happens in the real world and its costly to avoid / prevent / recover from it.

# Process Scheduling

In any multiprogramming situation, processes must be scheduled.

The **scheduler** selects the next job from the "ready queue". The ready queue is a queue where processes go when they are ready to go onto the next step of their programming.

Scheduling algorithms may be **preemptive** or **non-preemptive**. 

None preemptive scheduling is where once the CPU has been allocated to a process the process keeps it until it is released unpon termination of the process orby switching to the "waiting" state.

## Scheduling Policies

Several criteria need to be considered:

- **Maximise Throughput** - Complete as many processes as possible in a given amount of time
- **Minimise response time** - Minimise amount of time it takes from when a request was submitted until the first response is produced
- **Minimise turnaround time** - Move entire processes in and out of the system quickly
- **Minimise waiting time** - Minimise amount of time a process spends waiting in the ready queue
- **Maximise CPU efficieny** - Keep the CPU constantly busy
- **Ensure fairness** - Give every process an equal amount of CPU and I/O time.

## Scheduling Algorithms

The scheduler relies on algorithms that are based on a specific policy to allocate the CPU.

Process scheduling algorithms that have been widely used are:

- first come, first serve
- shortest job first
- shortest remaining time first
- priority scheduling
- round robin
- multilevel queues

### First Come, First Served

Simplest of the algorithms to implement and understand. Uses a first in first out queue.

Non-preemptive algorithm that deals with jobs according to their arrival time. The sooner a process arrives in the scheduler, the sooner it gets the CPU.

When a new process enters the system its PCB is linked to the end of the "ready" queue.

The process is removed from the front of the queue when the CPU becomes available.

#### Example

Suppose we have three processes arrving in the following order:

- p1 with burst of 13 milliseconds
- p2 with cpu burst of 5 milliseconds
- p3 with cpu burst of 1 millisecond

Using the FCFS algorithm we can view the result as:

![img](https://screenshotscdn.firefoxusercontent.com/images/21896c18-590c-44d9-881e-8083296ee905.png)

### First Come, First Served

Given the CPU burst times of the process, we know what their individual wait times will be:

- 0 milliseconds for p1
- 13 milliseconds for p2
- 18 milliseconds for p3

The average wait time will be (0 + 13 + 18) / 3 = 10.3 milliseconds

**Advantages**
Very easy policy to implement

**Disadvantages**
The average wait time using a FCFS policy is generally not minimal and can vary substaniatlly.

### Shortest Job First
Non-preemptive algorithm that deals with processes addording to their CPU time.
- When the CPU becomes available it is assigned to the next process that has the smallest burst time
- If two processes have the same burst time, FCFS is used to determine which one gets the CPU


Suppose we have four processes as follows:
- P1 with CPU burst of 5 milliseconds
- P2 with CPU burst of 9 millioseconds
- P3 with CPU burst of 6 milliseconds
- P4 with CPU burst of 3 milliseconds

Using the SJF algorithm the processes can be viewed in the following Gantt chart:

![img](https://screenshotscdn.firefoxusercontent.com/images/94ffb5f6-850c-4805-97f7-5c05010aae09.png)

**Advantages**
SJF reduces the overall waiting time

**Disadvantages**

Can lead to starvation.
May be difficult to estimate execution times.

### Shortest Remaining Time First

Preemptive version of the shortest job first

Jobs can arrive at different times, doesn't have to be in queue.

CPU is allocated to job that is closet to being completed

![img](https://screenshotscdn.firefoxusercontent.com/images/6b3e747a-8ce6-4f0b-8d38-45719da93204.png)

![img](https://screenshotscdn.firefoxusercontent.com/images/dc88e67e-6cfa-42ac-a2fe-47f34cd2e95a.png)

Gantt charts **will** come up on the exan,

## Priority Scheduling

Algorithms that give preferential treatment to important jobs.

Each process is given a priority and the one with the highest prioty is granted the CPU.

With priorities, the higher the number the higher the priority.

# Round Robin

Prempetive Algorithm that gives a set CPU time to all active processes.
Similar to FCFS but allows for preemptive by switching between processes

Hence the name round robin it just goes around a queue.

Time is defined by a **time quantum**; a small unit of time varying between 10 and 100 milliseconds.

Ready queue treated as first-in-first-out queue.

CPU scheduler selects the process at the front of the queue, sets the timer, once the timer runs out takes it away from the CPU.

If the process' CPU burst timne is less than the specified time quantum it will release the CPU upon completion.

If the process' CPU burst time is more than the specified time quantum, the timer will expire and cause an interrupt.

questions:

what is pcb
When a new process enters the system its PCB is linked to the end of the "ready" queue.

what is burst
p1 with burst of 13 milliseconds
