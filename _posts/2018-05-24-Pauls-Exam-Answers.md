---
title: "Paul's exam answers"
categories:
  - Maths
---

# Question 1

What type of number is used to count the number of individuals living at a specified address?

## Answer

Natural numbers. The question here says individualS. Implying there is more than 1 person. So we start counting at 1. Natural numbers allow us to count from 1.

If it were possible for 0 people to live at the address then it would be whole numbers.

# Question 2

What type of number is used to count the number of children (defined as anyone under 16) living at an address?

## Answer

Whole numbers. Since it's possible no children live at an address.

## Question 3

A company pays its employees using a basic unit of £X per month and a salary scale in which Senior
Management receive £X^2 per month; Trainee managers are paid £X and all other workers earn a fixed
amount of £500 per month. If the company employs 250 Senior Managers, 100 Trainee Managers and
5 others, which of the polynomials describes its monthly salary costs?

### Answer

$$ 250x^2 + 100x + 5 * 500 = 250x^2 + 100x + 2500 $$

Simple maths. The equation for a polynomial like this is:

$$ x^2 + x + y $$

## Question 4

The same company decides to appoint a single Senior Executive Vice-President who will be given
X^3 per month, and at the same time it reduces its (non-managerial) workforce to a single person who
now receive £600 per month. Which of the polynomials below describes its annual salary costs?

$$ £x^3 + £250x^2 + £100x + £600 $$
### Answer

It's important to know that this is the **annual** cost. The previous monthly costs now must be multipled by 12.

$$ £12x^3 + 12 * 250x^2 + 12 * 100x + 12 * 600 $$

$$ £12x^3 + 3000x^2 + 1200x + 7200 $$

Paul's questions are worded so weirdly so make sure to double read any question before attempting it.

## Question 5

What is the coefficient of $$x^0$$ in this formula?

$$f(x) = (x - 4)( x - 5)(x - 6)$$

### Answer

So $$x^0$$ is the same as saying "what is the number that is all on its own,  with no x value?".

Any number multiplied by $$x^0$$ is just the number.

$$ 12x^0 = 12$$.

So this is asking us "what is the number we get when we multiply out all the brackets?"

Since we specifically know we only want the singular number, we can ignore all x values and just multiply these together:

$$ -4 * -5 * -6 = -120$$

If you forget about this, you can just multiply out all the brackets.

Here's a good BBC article on it.

https://www.bbc.com/education/guides/zcqmsrd/revision/5

## Question 6

A robot crawler must move from its current position (recorded as a 2-dimensional coordinate) to a
location that is exactly 37 metres to its right. If the robot’s current location is < x, y > which of the
following describe its desired location?

### Answer

"to the right" means it's on the x axis. Because it's positive (+37) we know it's going to increase the x axis.

$$ <x + 37, y>

## Question 7

A region of pixels whose colours are described using the RGB-system in which each pixel, p, has its colour defined by a 3-vector < pR, pG, pB > is manipulated over a period of ninety seconds by the
algorithm described below in which the variable T ime counts in milliseconds.
```
T ime := 0
while Time ≤ 90000 do
  if (Time is an exact multiple of 30000)
  do:
```
$$ \begin{pmatrix} PR \\\ PG \\\ PB \end{pmatrix} := \begin{pmatrix}0 & 0 & 1 \\\ 0 & 1 & 0 \\\ 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} PR \\\ PG \\\ PB \end{pmatrix} $$

```
  end if
  
  Time := Time + 1;

end while
```
Suppose this algorithm is applied to the pixels in a 600 × 600 square in which the colour c(p) of the
pixel at position < px, py > is initially

![img](https://i.imgur.com/shLGgmm.png)

### Answers

So time is a multiple of 30000 at exactly four times:
1. 0, 0 * 30000 = 0 and so is considered a multiple
2. 1, 1 * 30000 = 30000
3. 2, 2 * 30000 = 60000
4. 3, 3 * 30000 = 90000

We include 90000 since the parameter specifies less than or more than.

```
while Time ≤ 90000 do
```

So we apply this matrix 4 times to those region of pixels.

Matrix multiplication is done like this:

![img](https://i.embed.ly/1/image?url=https%3A%2F%2Fthumbs.gfycat.com%2FPositiveExhaustedAmericangoldfinch-size_restricted.gif&key=522baf40bd3911e08d854040d3dc5c07)

If we multiply it once we get:

$$ \begin{pmatrix} PB \\\ PG \\\ PR \end{pmatrix}$$

So it moved down by 1 but the middle one didn't change. Let's multiply it again:

$$\begin{pmatrix} PR \\\ PG \\\ PB \end{pmatrix}$$

Okay, so it went back to normal. So we know if we times it by an odd number we'll get 

$$ \begin{pmatrix} PB \\\ PG \\\ PR \end{pmatrix}$$

and if we times it by an even number we get:

$$\begin{pmatrix} PR \\\ PG \\\ PB \end{pmatrix}$$

So we can stop here since

$$\begin{pmatrix} PR \\\ PG \\\ PB \end{pmatrix}$$

is the answer. We could always just go back through it again if we didn't notice this pattern.

So the answer here is "it goes back to its original setting, nothing happens".

## Question 8

A 4-vector < x, y, z, t > describes the position of an object at a given time, using < x, y, z > for its coordinates at t for the time.  Suppose s-scale (for s a Real number) is the operation of moving < x, y, z > to < sx, sy, sz > in a single time step. Which of the following is true?

1. The process of computing the new vector can be achieved by using a 3×3-matrix
2. The process of computing the new vector can be achieved by using a 4×4-matrix.
3. The process of computing the new vector requires using a 5×5-matrix
4. The process of computing the new vector requires using a 6×6-matrix.
5. Computing the new vector cannot be achieved as a result of a matrix-vector product.