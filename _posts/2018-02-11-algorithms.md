---
title: "Algorithms"
categories:
  - University
---

# What is an algorithm?

An algorithm is a set of instructions typically undertaken by a computer to reach a targeted goal.

When you make a sandwich, you are performing an algorithm. Habits are algorithms. 

>Algorithms have a long history and the word can be traced back to the 9th century. At this time the Persian scientist, astronomer and mathematician Abdullah Muhammad bin Musa al-Khwarizmi, often cited as “The father of Algebra”, was indirect responsible for the creation of the term “Algorithm”. In the 12th century one of his books was translated into Latin, where his name was rendered in Latin as “Algorithmi”.
From [here](http://cs-exhibitions.uni-klu.ac.at/index.php?id=193)

Algorithms are essential in Computer Science, you simply cannot live without them. Something computer scientists do alot is compare how long an algorithm takes to run against other algorithms.

# How do we measure algorithm complexity?

We could simply run an algorithm 10,000 times and measure the average time taken or we could use something called Big O notation.

Big 0 notation is notation used to describe how efficient an algorithm is. It's incredibly important to know this since every major employer will question you on this and it'll most likely come up in any algorithms exams (Hello University of Liverpool people <3 )

A hierarchy of functions exist:

1 | log n| n, $$n^2$$, $$n^3$$ | $$2^n$$
--- | --- | --- | ---
Constant | Logarithm | Polynomial | Exponential

Where the further right they are, the the longer take it takes. Big O notation uses these functions to describe algorithm efficiency. O(2^n) is larger than O(1).

Log is called a logarithm (typically in base 2, binary but can differ). I shan't explain the logistics of logarithms for someone has already done it far better than I can. You do not need to watch the whole video, perhaps just the first two minutes.

https://www.youtube.com/watch?v=ZIwmZ9m0byI

![img](https://www.daveperrett.com/images/articles/2010-12-07-comp-sci-101-big-o-notation/Time_Complexity.png)

In Big O notation, we always use the *worst case* scenario for our calculations.

There are other notations too, but typically we only use Big O notation.

# Some little tidbits

## Drop the constants

If you have an algorithm described as O(2n), drop the 2 so it's just O(n).

## Drop the non-dominant terms

O(n^2 + n) just becomes O(n^2). Only keep the larger one in Big O.

If you have a special sum such as
O(b^2 + a)
you can't drop either because without knowledge of what b and a are.


Bet you were expecting some hard to understand guide to Big O huh? Well, this is all it is. You just need to memorise (or learn) the hierarchy and then take some algorithms and find out what their Big O notation is. You should really practice this!

# Seqeuntial search

Let's say you have an array of items [1, 3, 7, 4, 9] and you want to find the number 4. A sequential sort would calculate it like so:

Current number | Description
--- | ---
1 | Not goal
2 | Not goal
3 | Not goal
4 | Goal found

In the *worst case scenario* the number we are looking at is either not in the list or at the very end, so in time complexity this is O(N).

# Binary search

Binary search only works on sorted arrays. It basically halves the array and checks whether the halfed item is lower or higher than the goal item in the array.

Given the array [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10] and we want to find 2 we can run binary search like this:

```
Item in middle of array = 5
is 5 less than or greater than 2? It's greater than so we throw away the right hand side (greater than) and start again.
5 / 2 = 2.5, so we round up here. 
Is 3 less than or greater than 2? It's greater than so we do:
3 / 2 = 1.5
round up to 2
2 is goal, goal is found.
```

The time complexity here is O(log n) because you're effectively asking how many times can you divide by 2 until you find the answer?

Here is a nice gif of binary search in action

![img](https://blog.penjee.com/wp-content/uploads/2015/04/binary-and-linear-search-animations.gif)

This is the worst case performance for binary search, beaten by sequential search!
![img](https://blog.penjee.com/wp-content/uploads/2015/12/linear-vs-binary-search-worst-case.gif)

# Min and Max algorithms


How do you find the biggest and smallest numbers in an array?

## Finding maximum from n +ve (positive) numbers

```python
i = 1
m = 0
while i <= n:
    if A[i] > m:
        m = A[i]
    i = i + 1
print(M)
```

Assume A is an array of n positive numbers and m is the maximum number. Also note that arrays are indexed at 1 here (my lecturer's done this, and since this is my notes for my course I'll be using her notation).

Can you guess the time complexity of this?

Answer's coming up

It's O(N).

## Finding minimum from N +ve (positive) numbers

```python
i = 1
m = A[1]
while i <= n:
    if A[i] < m:
        m = A[i]
    i = i + 1
print(m)
```

Of course this would look nicer with a for loop, but my lecturer used a while loop and so to keep it as close to the official course notes I've opted to use a while loop as well.

## Finding location of maximum number

What if we wanted to find the location of the maximum number? Well, we simply store a location variable.


```python
loc = 1
i = 2
while i <= n:
    if A[i] > A[loc]:
        loc = i
    i = i + 1
```

