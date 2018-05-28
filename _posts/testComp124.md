All of these questions were asked in class.

# Question 1


```
Pages - | p | q | r | q | q | q | p | r | r | q
Times -   0   1   2   3   4   5   6   7   8   9
```
Predict the next working set using the principle of locality rule for the set W(10, 3)

## Answer

So we look at the 3 and we see what the first 3 are. In this case, it's {p, q, r}. We then know that in the next 10 pages that {p, q, r} will come up at least once.


# Question 2

On the 1967 version of Unix what did the command:

```
list -k -d -f -z
```

Do to an Fairchild PPS-25; Intel 8008; Rockwell PPS-4?

1. Resets the CPU
2. Activates the terminal memory unit
3. Lists everyone who has used the keyboard
4. Lists all Wi-Fi devices

## Answer

Since in the Unix versions before 1979 (when Linus Torvalds took over and made it into Linux) each user had to be logged in one at a time. Wi-Fi was not invented back then. So this command records every single user who is logged in (who of course uses the keyboard) and lists them.

It's a bit of a weird one but Dave is just being awkward.

# Question 2

Suppose two users simultaneously type the following 
command at the unix shell command prompt ($): 

```
$ ls –l
```

Which of the following are true?

* a) One process and one program is involved
* b) Two processes and two programs are involved
* c) One process and two programs are involved
* d) Two processes and one program are involved
* e) None of the above

## Answer

ls lists all the files the current user has. Because it can be different for different users that makes this a new program for every single user. So it's two processes and two programs.

# Question 3

Which of the following statements about threads is FALSE?

* a) A Java program need not necessarily lead to the creation of any threads
* b) A thread is sometimes referred to as a lightweight process
* c) Threads share code and data access
* d) Threads share access to open files
* e) Threads are usually more efficient than conventional processes

## Answer

A thread is only created if the user creates a thread (assignment 2 of comp124) so a) is correct.

# Question 4

Process A and process B both share the same code segment S. Which of the following statements is (are) true?

I.  An entry for S appears in both segment tables
II.  The segment code must be re-entrant
III.  The segment code must be recursive

* a) I only
* b) II only
* c) IandII
* d) I and III
* e) I, II and III

## Answer

The segment code must be recursive. It's risky that both processes access the same code segment at the same time. We want to make sure that it doesn't access the item at the same time.

In the lectures, we used a loop like this:

```
while(variable is being used)
    wait until variable isn't being used
```

You can do this with recursion. The idea is to get one process to wait for the other process to finish using the code before that process can use it.
