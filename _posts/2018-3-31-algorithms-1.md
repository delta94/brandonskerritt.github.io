# What is an Algorithm?

An algorithm is a set of instructions typically undertaken by a computer to reach a targeted goal. But, what does that really mean?

When you make a sandwich, you are performing an algorithm. Even if you do not know it. Habits are algorithms. Do you put your socks and shoes on in the order sock > sock > shoe > shoe or do you do sock > shoe > sock shoe? Both of these are algorithms.

Where does the word algorithm come from? It's a bit of a funny word. Actually,

>Algorithms have a long history and the word can be traced back to the 9th century. At this time the Persian scientist, astronomer and mathematician Abdullah Muhammad bin Musa al-Khwarizmi, often cited as “The father of Algebra”, was indirect responsible for the creation of the term “Algorithm”. In the 12th century one of his books was translated into Latin, where his name was rendered in Latin as “Algorithmi”.

From [here](http://cs-exhibitions.uni-klu.ac.at/index.php?id=193)

Normally algorithms break down things that we as humans think are very simple and easy into little steps that a computer can perform, let's say that you want to find the number 3 in the list [1, 2, 3]. You look at it and you see it, but a computer can't see the number 3 in the list until it goes through every single item to check. Computers are the fastest dumbest things to ever be created, because it's so easy for us to just "look" and see.

This is a good video showing how precise and "stupid" computers can sometimes seem:

https://www.youtube.com/watch?v=cDA3_5982h8

Algorithms are essential in Computer Science, you simply cannot live without them. Something computer scientists do a lot is compare how long an algorithm takes to run against other algorithms, kind of like a race.

<a name="big-o"></a>
# How do we measure how long an algorithm takes to run?

We could simply run an algorithm 10,000 times and measure the average time taken but let's say we have an algorithm that took different inputs, like say for example we have an algorithm that takes a list of items and prints every item to the screen. If we only input lists of length 1 (1 item), the average time would be around 0.1 seconds. If we entered items of length 1500, the average would be different. Of course you can use some advance statistical knowledge to work out the true average by inputting lists of varying lengths or you could use Big O notation.

Big 0 notation is notation used to describe how efficient an algorithm is. It's incredibly important to know this since every major employer will question you on this and it'll most likely come up in any algorithms exams (Hello University of Liverpool people <3 ).

A hierarchy of functions exist:

   1     |   log n   | n, $$n^2$$, $$n^3$$ |   $$2^n$$
-------- | --------- | ------------------- | -----------
Constant | Logarithm | Polynomial          | Exponential

Where the further right they are, the longer it takes. Big O notation uses these functions to describe algorithm efficiency.

Log is called a logarithm (typically in base 2 binary but can differ). I shan't explain the logistics of logarithms for someone has already done it far better than I can. You do not need to watch the whole video, just the first two minutes.

https://www.youtube.com/watch?v=ZIwmZ9m0byI

A "constant" value is something that does not change depending on its input. So for example, adding 1 to 500 is the same as adding 1 to 4741838148, because it doesn't scale depending on the input size.

![img](https://www.daveperrett.com/images/articles/2010-12-07-comp-sci-101-big-o-notation/Time_Complexity.png)

In Big O notation, we always use the *worst case* scenario for our calculations.

To calculate the Big O of an algorithm or selection of code, well... it's basically an educated guess. If your algorithm touches EVERY item in a list, the algorithm is 0(n). If your algorithm does not rely on input size (like an algorithm which just does 2 * n) then it is considered 0(1). If your algorithm appears to be halving / going down a lot it is _probably_ log n. If your algorithm looks like it's counting up in how memory is counted (16, 32, 64, 128, 256, ..., 1024) then it is probably 2^n. 

There are some super useful rules you have to obey in order to simplify your algorithm.

<a name="big-o-tips"></a>
## Drop the constants

If you have an algorithm described as O(2n), drop the 2 so it's just O(n).

## Drop the non-dominant terms

O(n^2 + n) just becomes O(n^2). Only keep the larger one in Big O.

If you have a special sum such as
O(b^2 + a)
you can't drop either because without knowledge of what b and a are.

<a name="big-o-summary"></a>
## Summary

Bet you were expecting some hard to understand guide to Big O huh? Well, this is all it is. You just need to memorise (or learn) the hierarchy, take some algorithms and find out what their Big O notation is. 

Big O notation only represents how long an algorithm can take but sometimes we care about the memory (space complexity) of an algorithm too.

I read somewhere that if you have a for loop and another for loop nested inside of that for loop (2 for loops) then it's likely to be $$n^2$$. 3 for loops is $$n^3$$.

There are other forms of measuring algorithm time complexity such as Big Theta which is the least (smallest) amount of time an algorithm takes.

Big-O only measures how long an algorithm takes. Sometimes we care about how much "space" - memory an algorithm takes.

# Conclusion

You should now have a basic understanding of algorithms and how to measure how long an algorithm takes.

Stay tuned for part 2!

