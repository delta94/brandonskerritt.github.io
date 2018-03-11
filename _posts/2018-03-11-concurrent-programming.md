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