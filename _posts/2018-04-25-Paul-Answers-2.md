---
title: "Class test 2 practice paper & answers"
categories:
- University
---

# Question 1

Starting from the base of a hill, a car drives (in a straight line) to the end of a road located at its summit. If the starting position of the car is defined by the coordinate <70, 10> and the hill peak (where the road ends) has coordinates <95, 60>, what is the **gradient** of the hill?

- 1
- 2
- 4
- 8
- 16

## Answer

The gradience is defined by the formula:

$$\frac{change \space in \space Y}{change \space in \space X}$$

So this formula is really just:

$$\frac{y_2 - y_1}{x_2 - x_1}$$

And given the 2 vectors:

$$ <70, 10> \space <95, 60>$$

then we simply take the y values which are:

$$ y_1 = 10 \space y_2 = 60$$

and the x values which are:

$$ x_1 = 70 \space x_2 = 95$$

then the formula is:

$$\frac{60 - 10}{95 - 70} = \frac{50}{25} = 2$$

So the **gradient** is 2.

You **do not** need to memorise this formula. It is given to you in the exam. **Do not memorise this formula**.

# Question 2

When the vehicle has climbed up to a height of 50 metres on the hill (i.e. y = 50) what is the **horizontal** distance that has been travelled at this point (i.e. the corresponding value of x)?

- 82 metres
- 84 metres
- 86 metres
- 88 metres
- 90 metres

## Answers

So in the first question we found out that they started at <70, 10> and then they vertically travel 50 metres. The final destination is <95, 60>. The current coordinate when they travel 50 metres up is <x, 50>. 

The gradient stays the same.

$$ \frac{60 - 50}{95 - x}$$

The 60 and 50 are the:

$$y_2 - y_1$$

the 95 and x are the :

$$x_2 - x_1$$

But since we know the gradience is 2 and we are using the gradience formula we know that this equation must be equal to 2 (since the gradience does not change):

$$ \frac{60 - 50}{95 - x} = 2$$

And then some simple algebraic manipulation gets us:

$$ \frac{10}{95 - x} = 2$$
$$ 10 = 2(95 - x)$$
$$ 10 = 190 -2x$$
$$ -180 = -2x$$
$$ 180 = 2x$$
$$\frac{180}{2} = x$$
$$90 = x$$
$$ x = 90$$

So the coordinate when it is 50 metres up is:

$$ <90, 50>$$

# Question 3

The following question refers to the setting described below.

An essay marking scheme is revised so that + grades can be given. Now the **ordered** range of grades is:

$$ <G, G+, F, F+, E, E+, D, D+, C, C+, B, B+, A>$$

These are converted to **basic** marks ranging from 0 (for G) through to 6 (for A) but with + grades scored 0.5 more than the grade which the + qualfiies for (eg F+ is 1.5, C+ is 4.5 and so on).

At the same time a new formula to convert **basic** marks (in the range 0 to 6) to **final** marks is adopted. This is the formula $$RevisedMarkScheme(x)$$ in which:

$$RevisedMarkScheme(x) = 2x^3 - 18x^2 + 30x + 40$$

What **grade** does an essay need to be awared to achieve the **maximum** possible **final** mark?

* A
* C+
* D
* F
* G

## Answer

The terms **maximum** and **minimum** come from turning points in calculus.

A turning point is the point at which the line becomes **horizontal**. Look at this gif I made:

![img](https://cdn-images-1.medium.com/max/1600/0*9f4OjQDfKOAi0Dkm.gif)

The line becomes horizontal at some point as it **turns** around the graph.

The gradient of the line touching the point <x, f(x)> is 0.

The gradient of the line touching the point <x, f(x)> is described by the **function** f'(x): the first derivative of f(x).

So the turning points of f(x) are those values, x, for which f'(x) = 0.

You calculate the first derivative of this function.

To check whether a turning point, t, is a local minimum or maximum you need to find the second derivative of f(x), f''(x) by constructing the first derivative of f'(x).

Find the value of f''(t) then if f''(t) is less than 0 then t is a local maximum.
If f''(t) > 0 then t is a local minimum.

We get given this in the exam:

![img](https://i.gyazo.com/872c0b8bbaf75ff4247544e5a8b02e0d.png)

Let's calcualte a diffrent polynomial first:

$$Final(x) = 2x^3 - 18x^2 + 30x + 27$$

We need to find the first derivative.

The first thing we're going to do is subtract 1 from the cube index, add that to the coefficient 2 (now 3) and times that by 2

$$Final'(x) = 6x^2$$

Now we get 2 * -18 which is -36x

$$Final'(x) = 6x^2 - 36x$$

Now for 30x. The first derivative of 30x is just the value 30.

$$Final'(x) = 6x^2 - 36x + 30$$

$$ 3x^2$$

then we apply the polynomial rule again:

$$3x^2 - 2x^1$$

2x^3 - 18x^2 + 30x + 40

# Question 9

Consider the **three** $$ 4 x 4$$ matrices, **P**, **Q**, and **R** below:

$$ P = \begin{pmatrix}1 & 2 & 0 & 3\\\ 1 & 4 & 0 & 6 \\\ 1 & 6 & 0 & 9 \\\ 1 & 8 & 0 & 12\end{pmatrix}$$

$$ Q = \begin{pmatrix}1 & 1 & 1 & 1\\\ 2 & 4 & 6 & 8 \\\ 0 & 0 & 0 & 0 \\\ 3 & 6 & 9 & 12\end{pmatrix}$$

$$ R = \begin{pmatrix}1 & 1 & 1 & 1\\\ 1 & 2 & 3 & 4 \\\ 2 & 4 & 6 & 8 \\\ 5 & 5 & 5 & 5\end{pmatrix}$$

* P only
* Q only
* R only
* P and Q only
* All three matrices are singular

## Answer

So anytime you see a row / column of 0's in a matrix it's singular unless the 0's look like this:

$$ R = \begin{pmatrix}0 & 1 & 1 & 1\\\ 1 & 0 & 3 & 4 \\\ 2 & 4 & 0 & 8 \\\ 5 & 5 & 5 & 0\end{pmatrix}$$
