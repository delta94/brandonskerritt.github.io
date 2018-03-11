---
title: "Complex Numbers"
categories:
  - University
---

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->
# Table of Contents
* [Table of Contents](#table-of-contents)
* [Origins](#origins)
* [The Formal Definition of the set of complex numbers](#the-formal-definition-of-the-set-of-complex-numbers)
* [Some facts](#some-facts)
* [Complex Numbers](#complex-numbers)
	* [Adding and Subtracting Complex Numbers](#adding-and-subtracting-complex-numbers)
	* [Multiplication using complex numbers](#multiplication-using-complex-numbers)
	* [Complex Division](#complex-division)
* [Other Representations of Complex Numbers](#other-representations-of-complex-numbers)
	* [Argand Diagrams](#argand-diagrams)
* [Polar Coordinate Representation of Complex Numbers](#polar-coordinate-representation-of-complex-numbers)
* [The Exponent or Euler Form](#the-exponent-or-euler-form)
* [Sumary of Different Representations](#sumary-of-different-representations)
* [Another idea from exponent form](#another-idea-from-exponent-form)

<!-- /code_chunk_output -->

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

The modulus of Z, denoted \|Z\| is the positive real number given by:

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

## Adding and Subtracting Complex Numbers

Given 2 complex numbers

$$ u = a + \mathbb{i}b$$

$$ v = c + \mathbb{i}d$$

Where each complex number has a real number component and an imaginery component.

So let's say we want to add them together, z = u + v then:

The real number part can be worked out as:

$$\mathbb{R}u + \mathbb{R}v$$

Where you just add the real number parts together

Likewise the imaginery parts can be added together like so:

$$\mathbb{i}u + \mathbb{i}v$$

To work out z, we simply add both of them together:

$$ (a + c) + \mathbb{i}(b + d)$$

Subtraction is similar.

Real number part is:

$$\mathbb{R}u - \mathbb{R}v$$

Imaginery part is:

$$\mathbb{i}u - \mathbb{i}v$$

z = u - v is:

$$ (a - c) + \mathbb{i}(b - d)$$

## Multiplication using complex numbers

This is where things get a little snazzy!

So to get the real number version we do:


$$\mathbb{R} = \mathbb{R} * \mathbb{R} - \mathbb{i} * \mathbb{i} $$


Remember that an imaginery number times by an imaginery number is -1.

To find the imaginery part you mix a little bit of both:


$$\mathbb{R} = \mathbb{i} * \mathbb{R} + \mathbb{i} * \mathbb{i} $$


To find the complex number you do:


$$ z = (ac - bd) + \mathbb{i}(ad + bc)$$

## Complex Division

In normal division we can view the operation p/q as multiplying p by the reciprocal of q.

A similar approach is used for complex division where we multiply p by the complex number $$v^-1$$.

As in standard arthimetic, p/q must satisfy q != 0 as dividing by 0 is bad, so we have a precondition that |z| != 0.
<br>

Here's a super simple way to divide complex numbers.

1. To divide complex numbers, you must multiply by the conjugate. To find the conjugate of a complex number all you have to do is change the sign between the two terms in the denominator.
2. Distribute (or FOIL) in both the numerator and denominator to remove the parenthesis.
3. Simplify the powers of i, specifically remember that i2 = –1.
4. Combine like terms in both the numerator and denominator, that is, combine real numbers with real numbers and imaginary numbers with imaginary numbers.
5. Write you answer in the form a + bi.
6. Reduce your answer if you can.

Let's do an example.

$$ \frac{3 + 2i}{4 - 3i}$$

To perform the division we need to multiply by the reciporcal and to find the reciporcal (called the conjugate) is change the sign between the two terms in the denominator and make that into its own fraction like so:

$$ \frac{4 + 3i}{4 + 3i}$$

See, super easy! Now we need to multiply.

$$ \frac{3 + 2i}{4 - 3i} * \frac{4 + 3i}{4 + 3i}$$

Now we distribute (or FOIL) in both the numerator and denominator to remove the parathesis.

$$\frac{12 + 9i + 8i + 6i^2}{16 + 12i - 12i - 9i^2}$$

Now we simplfy the powers of i:

$$ \frac{12 + 9i + 8i + 6(-1)}{16 + 12i - 12i - 9(-1)} = \frac{12 + 9i + 8i - 6}{16 + 12i - 12i + 9} $$

Combine the like terms:

$$ \frac{6 + 17i}{25} $$

Write your answer in the form a + bi

$$ \frac{6}{25} + {17}{25}i$$

Reduce your answer if you can. In this case we cannot.

# Other Representations of Complex Numbers

We can represent complex numbers on a **complex plane**. This idea isn't new to you, as it was used earlier to explain how complex numbers exist.

Let's say we have the complex number:

$$3 - 5i$$

The number has a real part of 3 and an imaginery part of -5.

We can express this on a plane like so:

![khan academy](https://screenshotscdn.firefoxusercontent.com/images/fe5c7624-49b0-4ddf-b6f8-82906c177a9f.png)

or we could use an Argand diagram.

## Argand Diagrams

In an Argand diagram the x axis represents the real number part and the y axis represents the imaginery part.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Complex_conjugate_picture.svg/300px-Complex_conjugate_picture.svg.png)

The x coordinate represents the real number part and the y coordinate represents the imaginery part.

The complex conjugate is shown below the original complex number.

We can think of a complex number z = x + iy as a vector from <0, 0> to <x, y>.

The _length_ of this vector is the modulus \|Z\|.

The _conjugate_ is just the reflection of z in the x-axis.

# Polar Coordinate Representation of Complex Numbers

We know that the trigonometric functions sin and cos are defined with respect to angular measure (theta in radians) and the lengths of lines formed within a circle r.

We don't want to be thinking about x and y coordinates, what we want to care about is the angle.

TK more on this? Maybe?

# The Exponent or Euler Form

This uses a link between polar coordinates and representation on the exponential function.

"Leonard Euler was a milwall support" - My lecturer ????

If we take any number, x, and multiply it by this imaginery number, i, then what Euler discovered is that $$e^{i*x}$$ is exactly the same value and position in the complex plane as $$r cos\theta + r sin\theta$$

# Sumary of Different Representations

We have the simple form which is x + iy, with the real part being x and the imaginery part being a complex number times by i.

We can view them as coordinates in 2-dimensional systems such as in Argang diagrams. The horizontal axis defines the real number part and the vertical axis gives the imaginery part.

The polar coordinate system we work in a 2 dimensional plane, the complex plane, but now insetad of thinking explicitly in terms of how far along the x axis how far along the y axis we view the complex numbers given by the length fo ap articular line and the angle formed by the vector to the origin roatetd anti-clockwise from the x axis.

In the Euler form we have a complex number who's modulus is |z| and size is z has an angle with the x axis given by theta as an argument theta and in this case the given complex number is simply r multiplied by the exponential function raised to the value r * theta.

# Another idea from exponent form

We take the size of the complex number (always a positive number) and then take the positive squareroot of that value and then we multiply the positive squareroot by e^i(0/2).
