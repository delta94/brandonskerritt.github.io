---
title: "Degree of a Polynomial"
categories:
  - University
---

# Origins

We know that there are roots for every polynomial however there are 'problem polynomials' such as:

$$ x^2 + 1 $$

$$ x^2 - 2x + 2 $$

$$ x^3 - 8 $$

There are problemmatic because they do not have **real-valued** roots. For the first two cases there are _no_ real roots at all.

The idea of complex numbers is to find a way to treat problem polynomials in an unproblematic way.

In the 17th and 18th century this was a big problem for mathematicians.

Polynomials should have 2 solutions and they are where the graph crosses the x-axis. But what are the roots of a polynomial like this?

![img](https://screenshotscdn.firefoxusercontent.com/images/727f8fb9-be6c-4636-8460-1e43e9445585.png)

Decartes' calls the roots "imaginery" in his book La Geometrie

>“For the rest, neither the false nor the true roots are always real, sometimes they are only imaginary, that is to say one may imagine as many as I said in each equation, but sometimes there exists no quantity corresponding to those one imagines.”

— Rene Descartes

Let's say we have the equation:

$$ x^2 = 9$$

This is easy to solve! The answer is -3 or +3. What about:

$$x^2 = -9 $$

Uhh, square root of a negative number? Uh oh. Let's just invent a name for this, let's call it an imaginery number.

So we need to square root a negative number, let's say -1 because anything multipled by -1 is negative. Okay, so we when we square root -1 we get an imaginery number. That menas that when we square an imaginery number we get

$$\mathbb{i}^2 = -1$$

Pretending that this number exists actually makes maths easier and more elegant and it works in the wider world of mathematics.

We can actually visualise this quite well. Let's assume that we have this equation:

$$ x^2 = -1$$

This just menas x * x. Let's say that x is a roation of 90 degrees, than we we rotate 180 (90 * 2) degrees from the number 1 we get... negative 1!

![img](https://betterexplained.com/wp-content/uploads/complex/imaginary_rotation.png)

So if we multiply i twice the first multiplication would turn i into -i and the second will turn -i into i.

# The Formal Definition of the set of complex numbers

Skip this if you hate lengthy paragraphs of maths.

The complex numbers are a set described by the symbol $$\mathbb{C}$$.

Given X and Y $$\in \mathbb{R}$$

The *imaginary* or *complex* number Z is $$x + \mathbb{i}y$$ where $$\mathbb{i} = \sqrt{-1}$$ $$z = x + \mathbb{i}y$$ has a _real_ part denoted by $$\mathbb{r}$$ with:

$$ x = \mathbb{r}(x+y)$$

$$Z = x + \mathbb{i}y$$ has an imaginary part, denoted $$\mathbb{s}(z)$$ with

$$y = \mathbb{s}(x+\mathbb{i}y)$$

The complex conjugate of z is denoted $$\mathbb{z}$$ and is the complex number:

$$\hat{z} = \hat{x + \mathbb{i}} = x - \mathbb{i}y$$

The modulus of Z, denoted |Z|is the positive real number given by:

$$|Z| = |x + \mathbb{i}y| = \sqrt{x^2 + y^2}$$

# Some facts

Okay so we've learnt some new things:

* i is a "new imaginary dimension" to measure a number, much like the real numbers or natural numbers.
* i (or -i) is what numbers become when rotated
* Multiplying by i is a rotation by 90 degrees counter-clockwise

*Numbers are 2 dimensional*. That means that imaginary numbers can be represented using vectors if we so wished.

# Complex Numbers

Can a number be both real and imaginary? Absolutely.

A complex number is both real and imaginery. A complex number is made up of 2 components:

$$a + bi$$

Where a is the real number part and b is the imaginery part.

How do we "measure" the size of complex numbers? With negative and positive numbers we measure how far away it is from 0. 

But we can actually use Pythagoras' therom to measure the size of complex numbers! (Wow, is there anything that this formula ISN'T used for?).

$$ a + bi = \sqrt{a^2 + b^2}$$
