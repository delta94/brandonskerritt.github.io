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

```wew
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

### Answer

To encode a movement in a matrix for a 2-vector <x, y> we need to use a 3x3 matrix.

To do the same for a 4-vector <x, y, z> we need to use a 4x4 matrix.

For a 4-vector we use a 5x5 matrix.

Since this is a 4-vector:

$$ <x, y, z, t>$$

We use a 5x5 matrix.

## Question 9

In short, the movement should be done before drawing the triangle. If you draw the triangle then move it, it won't work so well.

If you're not too sure on this you can multiply the matrices together.

![img](https://i.gyazo.com/a387637b27d1dc5f8c821c51ea8c9cf7.png)

As you can see Alice's matrix looks nice. It has the 10 and -20, it has a dummy row of 1's. It looks all nice.

Bills on the other hand has some weird numbers. -19 and +11. It also has x3 and y3 which have not been moved.

## Question 10

$$ \frac{x_2 - x_1}{y_2 - y_1}$$

$$ \frac{30 - 20}{95 - 25}$$

$$\frac{10}{70} = 7$$

## Question 11

We know the gradient is 7. We need to find the equation definign the line.

We know a point on the line <20, 25>

$$ y = mx + c$$

$$ 25 = 7 * 20 + c $$

$$ 25 = 140 + c $$

$$ 25 - 140 = c$$

$$ -115 = c$$

therefore

$$ y = 7x -115 $$

Now we want to find what x is when y is 51

$$ 51 = 7x - 115$$

add 115 to both sides:

$$ 166 = 7x$$

divide by 7

$$ x = 23.741$$

This isn't any of the answers but according to other people this same line of reasoning is used in previous tests.

# Question 12
