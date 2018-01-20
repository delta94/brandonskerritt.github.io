---
title: "Everything you need to know about Binary"
categories:
  - Maths
---

# What is a number system?

A number system is a system of numbers used to represent an amount of objects. In the English speaking world, we use a number system called base 10. We have 10 numbers: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 and when we want to count past 9 we add a 1 and 0 together to make 10, and then we repeat.

But we can have as many numbers as we want, we can have 0 through to 8 or 0 through to 1, which is what we're going to talk about here.

# What is binary?

Binary is a number system which only has 2 numbers, 0 and 1. We can count any number in binary. To make binary more readable, here is a quick translation of binary numbers into base 10 (decimal) numbers.

0 | 1 | 10 | 11 | 100
--- | --- | --- | --- | ---
0 | 1 | 2 | 3 | 4

0 is equal to 0, and 1 is equal to 1. To make the number 2, we write "10" because it's physically impossible to write anything > 1, we have to start over in a new column. Much like how we cannot write 11 as a single number (unless you count in base systems more than 10).

Binary is often used in logic, 0 represents False of Off and 1 represents True or On.

# How to convert from Decimal to Binary

It is relatively easy to convert from binary to decimal. There are two popular methods.

## First method

Write down the decimal number and divide by 2 continually to give a result and a remainder of either a "1" or a "0" until the final result equals 0.

![Stolen from http://www.electronics-tutorials.ws/binary/bin_2.html](https://screenshots.firefoxusercontent.com/images/7b9d27f5-7bb0-46d5-be24-7dbb8ada4ffc.png)

## Second method

This is my personal favourite method, but to do this you need to know your powers of 2.

Powers of 2 are very important in computer science. Binary is represented as 2 numbers, so if you have 3 circuits then you will have 2^3 numbers, 0 through to 7.

The powers of 2 are:

2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192.

And to make an odd number, we add 1 to the list so the list of numbers we need to know becomes:
1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192.

Okay, say we want to represent 15 as a binary number. First we need to split up 15 so it can be made up of powers of 2 + the number 1. The nearest power of 2 that is less than 15 is 8, so we'll use that. 8 + 4 is 12. 8 + 4 + 2 is 14, so we're very nearly there! Now we just add a 1. 15 represented as powers of 2 is 8 + 4 + 2 + 1.

Now we know this, we can convert this simply.

The binary to powers of 2 graph looks like this.
8192 | 4096 | 2048 | 1024 | 512 | 256 | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0

If the number uses an 8, put a 1 in the binary box under it to represent that it uses an 8. I much prefer to use this method though:

1 | 2 | 4 | 8
--- | --- | --- | ---
1 | 1 | 1 | 1

And then normally we would need to reverse the binary numbers, but in this case because it's all just 1's we don't need to reverse. If we don't reverse them, we get the wrong binary number as binary is read with the highest order of magnitude to the left, not the lowest. Much like how in "10", the 1 is a whole place higher than the 0; the same applies for binary.

You can convert binary to decimal in the opposite method.

# Binary Addition

Let's first review addition in decimal.

```
    23
+   11
```

We first add 3 + 1, that equals 4. then we add 2 + 1, which is 3. So the answer is 34.
We add from the right to the left.

Binary addition works the same.

We will begin with one bit (binary digit) addition.

```
    0
+   0
=   1
```

and

```
    0  
+   1
=   1
```

and 

```
    1
+   1
=   10
```

1 + 1 carries us into the next column.

Try it yourself:

```
    111
+   110
=   ???
```

Also, pretty much every operator works in the same way it does with binary as with decimal.

# Representation of Negative Numbers in Binary

## Signed Representation

We can represent a binary number by applying a "sign" to it. 

In Binary, numbers can be 4 bit, 8 bit, 16 bit, 32 bit and so on. 
If we have an 8 bit number, it'll be 8 digits long.

So let's say we have the number 1 in 8-bit binary, that'll be represented as:
00000001
to turn this negative, we add a 1 to the front of it
10000001

Although this sometimes causes a problem. Given the number 0 in 8-bit binary:
00000000
we can make it negative by adding a 1 to the front of it.
10000000
But -0, what is that? It's nothing. It's impossible. And that's where the problem comes from.

## Two's Complement

We can make a binary number negative by applying **two's complement** to it without the need to sign it.

Two's complement is a really simple algorithm:
* invert all the digits so 0 becomes 1 and 1 becomes 0
* add a +1 to the number

and this makes it negative!

So given the number 15, which is 1111, in 8-bit binary it'll be:
00001111
So to make this negative we invert all the digits:
11110000
then we add a 1 to the end
11110001
and now this represents -15! How creative and cool!

## Addition in binary revisited


Let's say we have 2 numbers, -3 and -5.
In binary these are:
11, 101
and we want to add them together.

But this time we can ignore any carries that go off the end.

So we use the largest power of 2 that can fit both 5 and 3 into it, which is 8. But this time we make it negative.

Number | -8 | 4 | 2 | 1
--- | --- | --- | --- | ---
-3 | 1 | 1 | 0 | 1
-5 | 1 | 0 | 1 | 1

Now we simply add them. 
1 + 1 is 0 carry 1, the next line is 1 + 1 which is 0 so carry that, the next line is 1 + 1 which is 0 so carry that, the next line is 1 + 1 + 1 which is 1 carry 1, but this time we can throw away the carry and we're left with 1000 as an answer.

Many thanks to Jahan Ulhaque, Computer Science Student at University of Liverpool for showing me this method.


## Subtraction in Binary

Treat this as addition but negate the second operand.
So 4 - 3 is just 4 + (-3)

Which is just 

```
  0100
+ 1101
  0001
```

as we ignore the carry again.

## Overflow

Overflow is when more bits are stored in the binary value than it could hold. 

An example of this is 4 + 7 in 4-bit binary.

```
  0100  
+ 0101
  1001
```

The correct result, 9, is too big to fit into 4 bit representation, as the 1 on the front makes it negative 1.

If both inputs to an addition have the same sign, and the output sign is different, overflow has occurred.

Overflow cannot occur if the signs differ.

# Connect with me
[LinkedIn](https://www.linkedin.com/in/brandonls) | [GitHub](https://www.github.com/brandonskerritt) | [Website](https://www.brandonskerritt.github.io/about/)