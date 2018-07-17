# Introduction
What the reader will get out of the article

# Functional paradigm

In an imperative paradigm, you get things done by giving the computer a sequence of tasks and then it executes them. While executing them, it can change states. For example, let's say you originally set A to 5, then later on you change the value of A. You have variables in the sense that the value inside the varable varies.

In a functional paradigm, you don't tell the computer what to do but rather you tell it what stuff is. What the greatest common divisor of a number is, what the product from 1 to n is and so on.

Because of this, variables cannot vary. Once you set a variable, it stays that way forever (note, in purely functional languages they are nto called variables because of this). Because of this, functions have no __side effects__ in the functional paradigm. An side effect is where the function changes something outside of it. Let's look at an example of some typical Python code:

```python
a = 3
def some_func():
    global a
    a = 5

some_func()
print(a)
```

The output for this code is 5. In the functional paradigm, changing variables is a big no-no and having functions effect things outside of their scope is also a big no-no. The only thing a function can do is calculate something and return it as a result.

Now you might be thinking: "no variables, no side effects? Why is this good?". Good question, gnarly stranger reading this. 

If a function is called twice with the same parameters, it's guranteed to return the same result. If you've learnt about mathematical functions, you'll know to appreciate this benefit. This is called __referential transparency__. Because functions have no side effects, if you are building a program which computes things, you can speed up the program. If the program knows that func(2) equates to 3, we can store this in a table. This prevents the program from repeatedly running the same function when we already know the answer.

Typically, in functional programming we do not use loops. We use recursion. Recursion is a mathematical concept, usually it means "feeding into itself". With a recursive function, the function repeatedly calls itself as a sub-function. Here's a nice example of a recursive function in Python:

```python
def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)
```

# Map

To understand map, let's look at what iterables are. An iterable is anything you can iterate over. Typically these are lists or arrays, but Python has many different types of iterates. You can even create your own objects which are iterable by implementing magic methods. A magic method is like an API that help your objects become more pythonic. You need to implement 2 magic methods to make an object an iterable:

```python
class Counter:
    def __int__(self, low, high):
        # set class attributes inside the magic method __init__
        # for "inistalise"
        self.current = low
        self.high = high

    def __iter__(self):
        # first magic method to make this object iterable
        return self
    
    def __next__(self):
        # second magic method
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
```

The first magic method, ```__iter__`` or dunder iter (double underscore iter) returns the iterative object, this is often used at the start of a loop. Dunder next returns what the next object is.

Let's go into a quick termianl session and check this out:

```python
for c in Counter(3, 8):
    print(c)
```

This will print

```
3
4
5
6
7
8
```

So now we know what an iterable object is, let's go back to the map function. The map function let's us apply a function to every item in an iterable. Typically we want to apply a function to every item in a list, but know that it's possible for most iterables. Map takes 2 inputs, the function to apply and the iterable object.

```python
map(function, iterable)
```

Let's say we have a list of numbers like so:

```
[1, 2, 3, 4, 5]
```

And we want to square every number, we can write code like this:

```python
x = [1, 2, 3, 4, 5]
def square(num):
    return num*num

print(list(map(square, x)))
```

Functional functions in Python are lazy. If we didn't include the ```list()``` the function would store the definition of that, and only compute it when it is needed to compute.

It's a bit weird to go from non-lazy evaluation to lazy evaluation all of a sudden in Python. 

Now it's nice to write a normal function like ```square(num)``` but it doesn't look right. We have to define a whole function just to use it once in a map? Well, we can define a function in map using a lambda (anonymous) function.

# Lambda expressions

A lambda expression is a one line function. Take, for instance, this lambda expression which squares a number given to it:

```python
square = lambda x: x * x
```

Now let's run this:

```python
>>> square(3)
9
```

I hear you. "Brandon, where are the arguments? what the heck is this? that doesn't look anything like a function???"

Well, it's kind of confusing but can be explained. So we're assignign something to the variable "square". this part:

```python
lambda x:
```

Tells Python that this is a lambda function, and the input is called x. Anything after the colon is what you do with the input, and it automatically returns whatever the resultant of that is.

To simplfy our square program into one line we can do:

```python
x = [1, 2, 3, 4, 5]
print(list(map(lambda num: num * num, x)))
```

So in a lambda expression, all the arguments go on the left and the stuff you want to do with them go on the right.

You could actually do something insane like this:

```python
x = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * map(lambda a: a + a, x), x)))
```

Which times each number in the list by the sum of all of the numbers in the list. It gets a little messy, no one can deny that. The truth is that there's a certain pleasure in writing code that only other functional programmers can read. Also, it's super cool to take a function and turn it into a one liner.

# Reduce

Reduce is a function that turns an interable into one thing. Typically you perform a computation on a list to __reduce__ it down to one number. Reduce looks like this:

``` reduce(function, list)```

We can (and often will) use lambda expressions as the function.

The product of a list is every single number multiplied together. In order to do this normally you would program:

```python
product = 1
x = [1, 2, 3, 4]
for num in x:
    product = product * num
```

But with reduce you can just write:

```python
product = reduce((lambda x, y: x * y),[1, 2, 3, 4])
```

To get the same product. The code is shorter, and with knowledge of functional programming it is neater.


# Filter
How the filter function works

# Higher order functions

Calling functions with the arguments being a function

# Partial applications
Calling functions with not all of the arguments supplied

# Why Guido doesn't believe in functional programming in Python
http://fold.sigusr2.net/2010/03/guido-on-functional.html

# First class objects in python
Relating this back to what Guido said in the link above

# List comprehensions
How you can do pretty much most of the things you want to do functionally in Python using a list comprehension

# Generator expressions

How you can generate any iterable in Python (dictionaries, hashmaps, objects)

My key values of my blog:
* Everything must be free. The information must be free and easy to access.
* I will not taint my blog with any product or company that pays me to promote them.
* I will not spam my email list with stuff that isn't directly useful to them
* My blog will be pure, unbiased, and accessible. 