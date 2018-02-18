---
title: "Algorithms and Data Structures"
categories:
  - University
---

Normally people will make entire articles out of things like Big O notation, Binary search or other algorithms. There simply is no need to blabber on about something when you can convey the same message in a shortened manner, so this is where this article comes into play.

If you're not interested in a certain algorithm (say for example, Min and Max) then simply skip it! Most of the examples given are in Python, but you need not know how Python works to understand the algorithms. Note that later in this article some algorithms may be implemented in Java.

By the end of this article you should have a good understanding of algorithms and data structures.

# What is an algorithm?

An algorithm is a set of instructions typically undertaken by a computer to reach a targeted goal.

When you make a sandwich, you are performing an algorithm. Habits are algorithms. Do you put your socks and shoes on in the order sock > sock > shoe > shoe or do you do sock > shoe > sock shoe? Both of these are algorithms.

>Algorithms have a long history and the word can be traced back to the 9th century. At this time the Persian scientist, astronomer and mathematician Abdullah Muhammad bin Musa al-Khwarizmi, often cited as “The father of Algebra”, was indirect responsible for the creation of the term “Algorithm”. In the 12th century one of his books was translated into Latin, where his name was rendered in Latin as “Algorithmi”.

From [here](http://cs-exhibitions.uni-klu.ac.at/index.php?id=193)

Normally algorithms break down things that we as humans think are very simple and easy into little steps that a computer can perform.

An example of this is let's say you want to find the number 3 in the list [1, 2, 3]. You look at it and you see it, but a computer can't see the number 3 in the list until it goes through every single item to check.

Computers are the fastest dumbest things to ever be created.

Algorithms are essential in Computer Science, you simply cannot live without them. Something computer scientists do alot is compare how long an algorithm takes to run against other algorithms.

# How do we measure how long an algorithm takes to run?

We could simply run an algorithm 10,000 times and measure the average time taken but let's say we have an algorithm that took different inputs, like say for example we have an algorithm that takes a list of items and prints every item to the screen. If we only input lists of length 1 (1 item), the average time would be around 0.1 seconds. If we entered items of length 1500, the average would be different. Of course you can use some advance statistical knowledge to work out the true average by inputting lists of varying lengths or you could use Big O notation.

Big 0 notation is notation used to describe how efficient an algorithm is. It's incredibly important to know this since every major employer will question you on this and it'll most likely come up in any algorithms exams (Hello University of Liverpool people <3 )

A hierarchy of functions exist:

1 | log n| n, $$n^2$$, $$n^3$$ | $$2^n$$
--- | --- | --- | ---
Constant | Logarithm | Polynomial | Exponential

Where the further right they are, the longer it takes. Big O notation uses these functions to describe algorithm efficiency. O(2^n) is larger than O(1).

Log is called a logarithm (typically in base 2 binary but can differ). I shan't explain the logistics of logarithms for someone has already done it far better than I can. You do not need to watch the whole video, perhaps just the first two minutes.

https://www.youtube.com/watch?v=ZIwmZ9m0byI

![img](https://www.daveperrett.com/images/articles/2010-12-07-comp-sci-101-big-o-notation/Time_Complexity.png)

In Big O notation, we always use the *worst case* scenario for our calculations.

To calculate the Big O of an algorithm or selection of code, well... it's basically an educated guess. If your algorithm touches EVERY item in a list, the algorithm is 0(n). If your algorithm does not rely on input size (like an algorithm which just does 2 * n) then it is considered 0(1). If your algorithm appears to be halfing / going down alot it is _probably_ log n. If your algorithm looks like it's counting up in how memory is counted (16, 32, 64, 128, 256, ..., 1024) then it is probably 2^n. 

There are some super useful rules you have to obey in order to simplfy your algorithm.

## Drop the constants

If you have an algorithm described as O(2n), drop the 2 so it's just O(n).

## Drop the non-dominant terms

O(n^2 + n) just becomes O(n^2). Only keep the larger one in Big O.

If you have a special sum such as
O(b^2 + a)
you can't drop either because without knowledge of what b and a are.

## Sumary

Bet you were expecting some hard to understand guide to Big O huh? Well, this is all it is. You just need to memorise (or learn) the hierarchy, take some algorithms and find out what their Big O notation is. You should really practice this!

Big O notation only represents how long an algorithm can take but sometimes we care about the memory (space complexity) of an algorithm too.

TK other forms of measuring algirhtms.

# Seqeuntial search

Let's say you have an array of items [1, 3, 7, 4, 9] and you want to find the number 4. A sequential search would calculate it like so:

Current number | Description
--- | ---
1 | Not goal
2 | Not goal
3 | Not goal
4 | Goal found

Note: this type of table is called a trace table. It shows the values and names of all variables in the algorithm every single time the algorithm / loop is run until the algorithm finishes.

Essentially you are sequentially counting up every single item in an list until you find your goal (if it exists in the list).

![img](https://www.tutorialspoint.com/data_structures_algorithms/images/linear_search.gif)

Note: this algorithm is sometimes called linear search.

In the *worst case scenario* the number we are looking at is either not in the list or at the very end, so in time complexity this is O(N).

```python
for i in list: # for every element in the list
    if i == answer: # if you selected the element and it's the answer then
        print(answer) # print it to the screen
    else:
        continue # else continue searching
```

Now this may seem stupid, but it can work on non-sorted arrays. You use this search alot in daily life, like looking for a book or looking for an item on a menu.

# Binary search

Binary search only works on sorted arrays. It basically halves the array and checks whether the halfed item is lower or higher than the goal item in the array.

Given the array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and we want to find 2 we can run binary search like this:

```
Item in middle of array = 5
is 5 less than or greater than 2? It's greater than so we throw away the right hand side (greater than) and start again.
5 / 2 = 2.5, so we round up here. 
Is 3 less than or greater than 2? It's greater than so we do:
3 / 2 = 1.5
round up to 2 (as we only accecpt integers here)
2 is goal, goal is found.
```

The time complexity here is O(log n) because you're effectively asking how many times can you divide by 2 until you find the answer.

Here is a nice gif of binary search in action

![img](https://blog.penjee.com/wp-content/uploads/2015/04/binary-and-linear-search-animations.gif)

This is the worst case performance for binary search, beaten by sequential search!

![img](https://blog.penjee.com/wp-content/uploads/2015/12/linear-vs-binary-search-worst-case.gif)

This code is taken from [here](https://stackoverflow.com/questions/41883258/how-to-implement-a-binary-search). It's not essential to understand the Python code in order to understand the algorithm. 

```python
def bsearch(alist, target):
    left = 0
    right = len(alist)-1

    while True:
        mid = int((left + right)/2)
        if alist[mid] < target :
            left = mid + 1
        elif alist[mid] > target :
            right = mid + 1
        elif alist[mid] == target :
            print ("word '" + target + "' found at " + str(mid))
            break
        elif left > right:
            print ("Not Found!")
            break  

i = input("Enter a search >")
alist = ["rat","cat","bat","sat","spat"]
alist.sort()
bsearch(alist, i)
```

If you're a Java programmer, have a look at this code:

```java
// sortdata[] is an array in ascending order, n is size of array, key is the number we want to find
static void binary_search(int[] sortdata, int n, int key) {
		int count;
		boolean found = false;

		// start binary search on the sorted array called sortdata[]
		found = false;	// to indicate if the number is found
		count = 0;	// to count how many comparisons are made
		
		int temp = n - 1;

        while (found == false){
            if (sortdata[temp] == key){
				found = true;
			}
            else {
                if (temp < key){
                    temp = temp / 2;
                }
                else {
                    temp = temp + (temp / 2);
				}
			count = count + 1;
            
            }
        }               
		System.out.print("The number " + key + " is ");
		if (found == false)
			System.out.print("not ");
		System.out.println("found by binary search and the number of comparisons used is " + count);
	}
}
```

This method may suit your book search better because books are normally sorted alphabetically! If you know the alphabet and the positional number of each letter you could easily find any author you wanted!

# Min and Max algorithms

How do you find the biggest and smallest numbers in an array?

Well, first: why is this useful? Can't you just look at a list and tell?
Yes, *you* can but a computer cannot.

## Finding maximum from n +ve (+ve means positive) numbers

So given an array, A, of positive only numbers this is how you would find the maximum.

Quick note: read ":" as "then".

```python
i = 1
m = 0
while i <= n:
    if A[i] > m:
        m = A[i]
    i = i + 1
print(M)
```

Assume A is an array of n positive numbers and m is the maximum number. Also note that arrays are indexed at 1 here (my lecturer's done this, and since this is my notes for my course I'll be using her notation). In normal computer science arrays are indexed at 0, as in they start from 0.

Can you guess the time complexity of this?

It's O(N).

Let's try a quick example. Given the array [2, 6, 3, 4] how does the computer know what number is biggest? How best can we break down this problem into little chunks?

Well, we'll simply run the code.

At first, 2 is the largest number. Then 6 is, 3 isn't larger than 6 and 4 isn't larger than 6 so we return 6 as the largest number in the array.

## Finding minimum from N +ve (positive) numbers

What if we wanted to find the minimum? Well, we simply turn the ">" sign into a "<" sign.
```python
i = 1
m = A[1]
while i <= n:
    if A[i] < m:
        m = A[i]
    i = i + 1
print(m)
```

# Dipping our toes into data structures - Queues and Stacks

A datastructure is a way to structure data in such a way that the data becomes easily usable and maybe even faster to use than a typical list or array.

## Queues

A queue is a first-in-first-out array. The *first* item into the array is the *first* item out of the array.

Queues have 2 functions:
* Enqueue - Insert element to tail (end).
* Dequeue - Retrive data from head (start) of queue.

So given an array (list) as an example

```python
[15, 20, 10, 0]
```

The *head* points to array[1] which is the first item in the array, it does not point to the data contained in the first item.
The *tail* points to array[end], where end is the length of the array + 1. In this instance tail results in 5,for their are 4 items in the list and then you add 1.

It's actually up to the developer who designs this as to whether tail points to length + 1 or whether it points to length.

The reason tail always points to something that doesn't exist is because enqueue is implemented to always put an object at [tail]. If we were to make tail the same as the length than enqueue would be changed to [tail + 1]. Either way you are adding 1, so it does not matter and may change in some languages.

If we want to *enqueue* 12 into the queue, we would add it onto the end like so:

```python
[15, 20, 10, 0, 12]
```

And the tail increases to a length of 6, but head stays at 1.

*Dequeue* takes the [head] of the list and enqueue places an item at the [tail] of the list.

```python
x = [20, 10, 0, 12]
```

which results in head = 2 and tail = 5. The head variable increased because we dequeued something. The head variable is also useful for other things such as knowing how many items have been taken out of a queue. 

If the head and the tail are the same and you have a 1 dimensional array like so:

```python
x = [1]
```

then in some programming languages you can only get the head() of the queue (Haskell, i'm looking at you) but in other languages this may differ.

![img](http://www.myassignmenthelp.net/images/queue.gif)

Why are queues useful? Well, queues are extremely useful. Imagine lining up at the bank and waiting 30 - 40 minutes to get to the front. When you get to the front, the teller decides a queue isn't useful so they start from the back, making you the last person they reach.

## Stacks

A stack is a *last-in-first-out* array.

In a lot of online tutorials stacks are drawn vertically like so:

0 |
:---: |
1 |
2 | 
3 | 

Much like a stack of plates, the first item on the top is the first item to come off. You can't pull plates out of the bottom of a stack of plates (if you can, you should become a magician!).

Stacks have 2 functions:
* Push - Insert element to the location top + 1
* Pop - Delete element from top

Where "top" is the variable for the top-most item in the stack.

Let's see some examples.

```python
x = [20, 10, 15]
```

Where top is "3" because there are 3 elements.

So to push 12 onto this stack we'll get

```python
x = [20, 10, 15, 12]
```

Now top becomes 4.

You may be wondering "what happened to adding +1 to head?". Well, like I said, you can use both notations. I want to expose you to as much variance in algorithms as possible to enrich your learning... Well, at least that's what my lecturer said to me.

Now if we want to pop() a stack we'll get:

```python
x = [20, 10, 15]
```

and head = 3, since we've popped the top!

Stacks are super useful, especially in browser history. Say for example you go to Google, then Medium, then my profile (follow me 😉). The stack will look like:

Brandon's Profile |
:---: |
Medium |
Google |

Now how much would it suck if you pressed "back" and it went back to Google? It would suck alot! So when we click "back" the browser, quite literally, pops the current webpage off of the stack and brings you to the next item.

Stacks grow _downwards_ by placing stuff on top of it. This may sound confusing, so I'll try to explain it.

When you *push* something onto a stack, you're changing the head of the stack (the head is normally the first item) to go down 1 level. We'll visualise this. Let's imagine a stack that looks like this:
```
[a][b][c]
```
There are no rules as to whether stacks can be sideways or top down, but normally they're top down. If we want to *push* something into the stack we do this:
```
[x][a][b][c]
```
Which pushes all the contents of the stack down.

In normal stack-like behavior this looks like:

Follow me on Twitter |
:---: |
Medium |
Google |

Now we push "University of Liverpool" to the stack and it becomes:

University of Liverpool |
:---: |
Follow me on Twitter |
Medium |
Google |

Literally pushing the stack down.

![img](https://www.sitesbay.com/data-structure/images/pop-operation.gif)

Think of stacks like leaving breadcrumbs for yourself. If you're ever lost in a maze and you place down all the breadcrumbs, you'll look for the last breadcrumb you placed down, which is usually the one closet to you.

# Linked Lists

Linked Lists are a linear collection of data elements except the linear order is not defined by their physical placement in memory but instead each data node points to the next.

The order is determined by a pointer (rather than array indices) TK
Each element (node) has a data field and one or two pointers linking to the next or previous elements in the list

There are two types of linked lists, singly linked and doubly linked.

Singly link looks like

```
[15][-]-> 
```

Where ```->``` represents a pointer and each ```[]``` represents a componenet.

![img](https://he-s3.s3.amazonaws.com/media/uploads/1b76d10.png)

In a singly linked list the node stores one piece of data (the 15) and it stores a pointer linking it to the right hand side. The pointer does not contain data, just a pointer. In my badly drawn diagram the pointer, the arrow which is literally pointing out of the right hand side box is a pointer pointing to the next node. Each set of these data with pointers is a node.

A singly linked list cannot point to the previous node.

Doubly linked list looks like:

```
<-[-][15][-]->
```

In a doubly linked list the node has a forward and backward pointer as well as a data object. Each node has 3 componenets, 1 piece of data and 2 pointers. In a doubly linked list you can go to the previous node.

Linked lists have a few functions we can use such as:

* node.data = get data from current node
* node.next = go to next node
* node.prev = go to previous node

The notation used may be different in programming languages.

Note: if the node you are looking at is the last node in the linked list then node.next results in None (as in, it does not exist) and if you try to run node.prev in a singly linked list it will error.


```
head -> [ ][15][<-]---[->][10][<-]---[->][20][ ]  <- tail
```

Something important to stress again is that a node in a doubly linked list has *3 components* and each ```[ ]``` represents 1 component so a group of ```[ ][ ][ ]``` represents *1 node* and in this diagram there are *3* nodes respectively.


If my badly-drawn diagrams in ASCII art are confusing then this picture may help:

![img](https://www.geeksforgeeks.org/wp-content/uploads/gq/2014/03/DLL1.png)

## Traversing Linked Lists

We can traverse and output each element of a linked list like so:

```python
node = head
while node != None: # while node does not equal None, where != is not equal to
    print(node.data) # output the data of the node using the Python print function
    node = node.next # updates the node variable to contain the next node in the list
```

Notice how we are using the node.next function to traverse a linked list.

At Merriam Webster they have dictionaries with reversed words. So Ecology would be ygolcoe. If you wanted to know how many words ended in "cology" you simply would search all words that ended in "ygolco". Of course, reading it like this is annoying so you can use a doubly linked list to be able to search a dictionary both the original alphabetical way and the reverse way. [Thanks 99PI](https://99percentinvisible.org/episode/mini-stories-volume-4/).

You could probably program a data structure (doubly linked list) that when you go to a previous node it displays the data in reverse.

## Big O

Searching for and traversing through linked lists is O(n).

# Programming Linked Lists

Because the linked lists data structure isn't in every language (very commonly it is not) we have to program linked lists ourselves.

Unfortunately my lectuer decided to switch to Java at this point in the class, however I'll do my best to explain every piece of java code.

So below is a node for a doubly linked list. The node has 3 components, previous, data, next. A class is a template you can apply to objects, so in this instance we can make new nodes using this class.

```java
class Node {
	public int data; 
	public Node next;
	public Node prev;
    
	// constructor to create a new node with data equals to parameter i
	public Node (int i) {
		next = null;
		prev = null;
		data = i;
	}
}
```

In this instance the node has 3 methods that can be applied to it. Each method can be applied like:
```
Node.next
Node.prev
Node.data
```
using the dot notation.


If we wanted to make a single node in a doubly linked list we can do this:

```java
Node newnode = new Node(5);
```

Where the node will hold a data value of 5.

If we wanted to add a new node to the front of the list we can use this function:

```java
// create a new node containing data value 
// and insert the new node to head of the list
static void insertHead(int value) {
	Node newnode = new Node(value); // makes a new node with value

	newnode.next = head; // Makes the next node the head of the linked list
	newnode.prev = null; // makes the previous node empty
	if (head != null) // if the head is empty
		head.prev = newnode; // sets the previous node to the new node to be inserted
	else
		tail = newnode; // the last node in the list is now the new node
	head = newnode; // the head of the list is the new node
	}
```

This code will create a new node and insert this node at the front of the doubly linked list. This is quite confusing, so let's draw some diagrams.

First we create a new empty node with value as data.

```
[ ][value][ ]
```

Then we set the next pointer to point at the head of the linked lists

```
[ ][value][-]-[>][HEAD][ ]
```

After this we set the previous definition to be NULL

```
NULL<-[-][value][-]-[>][HEAD][ ]
```

Then we run a simple if statement. If head is not empty, set the previous node of the head node to be our new node.

```
NULL<-[-][value][<-]-[>][HEAD][ ]
```

Notice how you can now travel from the HEAD node to the new node.

If head is empty, set the tail (last) node to be the new node. This is because if you insert this node into a linked list that doesn't exist, the next node would be nothing so the node you just inserted will be both the head and tail. Otherwise, just ignore the next node as it contains data.

The last line sets the head pointer to point to the new node which is at the front of the list.

We can also delete a node at the front of the linked list in a similar fashion:

```java
// delete the node at the head of the linked list
static Node deleteHead() {
	Node curr;

	curr = head;
	if (curr != null) {
		head = head.next;
		head.prev = null;
	}
	return curr;
}
```

We assume here that curr is a pointer that points at a node in the linked list.

So we point the current pointer at head, if head is not null (if it is not empty) then we set the head to the next node and from this new head (which is the second item in the linked list) we set the previous (old head) to null (nothing, doesn't exist). We then return the pointer.

## Inserting items into a linkedlist

Linked lists are super cool because we can insert items anywhere in them. Let's say we have a pointer, curr, which points somewhere (let's say the middle) of the list. We can insert a new node after curr like so (in Python now)

```python
def listInsert(L, curr, newnode):
    newnode.next = curr.next
    newnode.prev = curr
    if curr.next != None:
        curr.next.prev = newnode
    curr.next = newnode
```

Whenever we want to insert a new node, we just have to tell the node what the next and previous nodes are.


## Searching over a sorted list

Recall that values stored in a linked list are sorted. We could use binary search to search the list. However, this is a bad idea. We don't know where the middle of a linked list is. Everytime we wanted to find the middle we would have to count every single node in the list and half that by 2.`

We can use a modified version of sequential search to search a linked list.

Because the linked list is sorted, let's say in ascending order, we can use this information to make seqential search faster.

```python
node = head
while node != None and node.data < key:
    node = node.next
if node == None:
    print("Not found")
else if node.data > key:
    print("not found")
else:
    print("found")
```

Since the linked list is sorted sequentially we know that the nodes in the linked list go in some order, like 1, 2, 3, 4, 5 for example. If node.data is more than the key (what we're looking for) we know it's not in the list, because it is sorted in some order.

There are many, many search algorithms but most of the time if you know a little bit of information about the data you can change some search algorithm to be more efficient for that specific problem. In general, binary search is extremely effective but here it's not so good. Don't just use an algorithm because Stack Overflow says that it is the fastest, best algorithm for the job.

Algorithms are like programming languages, we all have our favourites and sometimes we say that one programming language is better than another (Python, I love you) but at the end of the day it would be foolish and naieve to say that one programming language is better than all the others. Use the right tool for the job, and change it if you want to!

Personally whenever I am presented with a problem I like to imagine it is in its own seperate world. I try to imagine what rules of life apply to this world. Once you understand the rules 


# Connect with me

upscribe

linkedlin
twitter
githib

Don't like this article or want to add something? Submit a pull request here: