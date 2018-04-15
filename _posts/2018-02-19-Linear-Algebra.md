---
title: "Linear Algebra"
categories:
  - University
---

Linear Algebra is the algebra of "lines". It's used to create computer graphics.

# Vectors

To Computer Scientists a vector is a container where order matters and repititions are allowed. A 2d vector is considered 2 dimensional because it has 2 items in it. Example of a 2d vector: <5, 6>.

To a physicist, a vector has magnitude and direction. To a physitict you can move a vector all around the plane and it'll remain the same vector.

![img](http://www.ducksters.com/science/physics/vector_basic.gif)

So what is it? Well, it's both. A vector is both a container of numbers and a representation of magnitude and direction. In this article we'll focus on the computer science perspective.

An N-vector has n components (elements), each component called <br>
$$U_1, U_2, ... , U_n$$ <br>
The number of components a vector has is the number of dimensions a vector has.

Two vectors can be added like so:

$$ \vec{A} + \vec{B} = \vec{W} = <A_1 + B_1, A_2 + B_2, ... , A_n + B_n>$$

You can only add two vectors if the vectors have the same number of components.

Scalar multiplcation is where you increase every item in a vector by R.
Let R be a real number then:

$$ R * \vec{A} = \vec{W} = <A_1 * R, A_2 * R, ... , A_n * R>$$


The length of a vector a, \|a\|, can be calculated with Pythagoras' formula


$$ |\vec{a}| = \sqrt{({a_{1}  ^2} + {a_2  ^2} + ... + {a_n  ^2})} $$

Some important facts:

$$ |\vec{-a}| = |\vec{a}| $$

$$-v = (-1)v$$

$$u - v = u + (-v)$$

A vector space is a list, V, of n-vectors where each vector is defined strictly using a type of number (real, rational etc) and if and only if:
$$\vec(u), \vec(x) \in V \Rightarrow \vec{u} + \vec{x} \in V $$

Given any number, R, from the original space (real numbers, integers, etc) and $$\vec{u} \in V$$ then $$\vec{u} * R \in V$$

The superscript number ontop of a set of numbers such as $$R^n$$ is the set of all real valued (numbers that are in the real numbers) n-vectors where each component is in the set of Real numbers.

2-vectors have 2 dimensions, X and Y: <X, Y>. 3-vectors have <X, Y, Z>.
![img](Blank Diagram - Page 1.png)

A matrix is a container which can have many dimensions. Paul said that this won't be on the *first class test* but he might ask you to multiply matrices out.

We can represent a shape by representing its "corners" in a vector like so:

$$ <(x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4)>$$

So most shapes are just corners with them filed in.

Take this square for instance:

![img](https://screenshotscdn.firefoxusercontent.com/images/0a1b5673-94e3-43d4-b18f-62147d016753.png)

If you know the corners of this square, you just draw the corners, connect them to one another and colour it in. Almost all shapes have this property (not circles, since circles do not have corners).

If we wanted to scale this shape by a factor of s, we can use this matrix:

$$\begin{pmatrix}s & 0\\\ 0 & s\end{pmatrix} \begin{pmatrix}y_i \\\ x_i\end{pmatrix}$$

To "scale a shape" means to increase / decrease the size of the shape. If we increase how far away the corners are away from eachother then we increse the size of the shape.

So you have a vector, which can be represented as a matrix. Just to drive the point home:

$$<x_1, y_1> = \begin{pmatrix}x_1 \\\ y_1 \end{pmatrix}$$

This is just one corner, we obviously scale every corner by the scalar but we start with one corner and work our way through all the corners.

$$\begin{pmatrix}s & 0 & 0\\\ 0 & s & 0 \\\ 0 & 0 & s \end{pmatrix} \begin{pmatrix}y_i \\\ x_i \\\ z_i \end{pmatrix}$$

This is how you scale a 3-dimensional object.

The matrix applied to scale the vector is an example of a *linear transformation*.

An operation, T, is a _*linear transformation*_ if:
1. For any pair of vectors, v and u, belonging to the vector space, V:
  T(v + u) = T(v) + T(u)
2. For every vector in V and any r (real number) in the set used by R (natural numbers, real, rational):
  T(rv) = rT(v)

What if we wanted to move a point, say <1, 2> to <5, 6>?

Well, this is easy!

$$\begin{pmatrix}1 & 0 & 4 \\\ 0 & 1 & 4 \\\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix}4 \\\ 4 \\\ 1 \end{pmatrix} = \begin{pmatrix}5 \\\ 6 \\\ 1 \end{pmatrix} $$

The difference between 1 and 5 is 4, so that's why the 4 is there. 

We can generalise this like so:

Say you want to move a point <x, y> to the point <x + p, y + q>

$$\begin{pmatrix}1 & 0 & p \\\ 0 & 1 & q \\\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix}x \\\ y \\\ 1 \end{pmatrix} = \begin{pmatrix}5 \\\ 6 \\\ 1 \end{pmatrix}$$

What if we wanted to rotate a a point anticlockwise about <0, 0> by theta to <q, s>?

![img](https://screenshotscdn.firefoxusercontent.com/images/bd251a58-13a7-4055-beaa-013e0e474ba9.png)

# Advance Matrices

An n x n matrix has n rows and n columns. The value in row i and column j of the matrix is denoted as:

$$ a_{ij}$$

The number of rows and columns do not have to be equal, but in most cases they are.

## Directed Graphs represent in Matrices

We can represent directed graphs using matrices.

The following graph can be represented by the 5 x 5 matrix:

![img](https://screenshotscdn.firefoxusercontent.com/images/ce6d115e-d8cd-4a03-b1ba-42fae68f56e2.png)

$$\begin{pmatrix}0 & 1 & 1 & 0 & 0 \\\ 0 & 0 & 1 & 0 & 0 \\\ 1 & 0 & 0 & 1 & 1 \\\ 1 & 0 & 0 & 0 & 0 \\\ 0 & 0 & 0 & 1 & 0\end{pmatrix}$$

Where the rows are nodes 1 to 5 and so are the columns. If node 1 is connected to node 2, row 1 column 2 is set to 1. If node 2 is not connect to node 1, row 2 column 1 is set to 0.

## Operations on n x m matrices

2 matrices, N rows and M columns.

We have 2 matrices, A and B. We want to add them like so:

$$ C = A + B$$

We can add them like so:

$$ c_{ij} = a_{ij} + b_{ij} \space for \space each \space 1 \le i \le n, 1 \le j \le m$$

So we just add the corresponding element in each matrix.

We can't mix dimensions with addition of matrices.

We can scale a matrix by a real number, R, like so:

$$ C = rA \ space in \space which \space [c_{ij}] = [r * {a_ij}] = [ra_{ij}]$$

## Transposition of matrix

Suppose we have a matrix called A. The transposition $$A^t$$ is formed by "swapping the rows and columns" The entries in the first row become the entries in the first column, the entries in the second row become the entries in the second column aod so on.

## Multiplying Matrices

The matrix A with n rows and m colums and our second matrix B with m rows and r columns.

When we multiply them together the resulting matrix, C, will have n rows and r columns. The number of rows in the first matrix has to be the same as the number of columns in our second matrix.

$$ c_{ij} =\sum_{k=1}^m a_{ik} * b_{kj} = \sum_{k=1}^m a_{ik}b_{kj}$$

So we just multiply all of the entries in the ith row by all of the entries in the jth column in the two matrices.

## Symetric Matrices

With two matrices they are said to be symetric when:

$$a_{ij} = a_{ji}$$

When the item in the ith row and jth column is equal to the item in the jth row and ith column for every item in the matrices they are said to be equal.

## Identity Matrix

The n x n Identity matrix uses only the values 0 and 1.

If the values in the ith row and jth column are equal, that data point is a 1. If they are not equal, the data point is a 0.

Take any n x n matrix, A.

Then the identity matrix, I, satisfies:

$$ AI = IA = A$$

Multiplying any matrix by the identity matrix results in the original matrix.

The identity matrix is this super cool matrix that has the number "1" diagonally across it.

If we have a 2 x 2 matrix, A, then the identity matrix is:

$$\begin{pmatrix}1 & 0\\\ 0 & 1 \end{pmatrix}$$

And then a 3 x 3 matrix's identity matrix looks like:

$$\begin{pmatrix}1 & 0 & 0\\\ 0 & 1 & 0\\\0 & 0 & 1\end{pmatrix}$$

And so on. As long as you have 1's on this diagonal line and everything else is a 0 then it's an identity matrix.

Let's multiply the identity matrix by a general matrix to see how the above law obeys it. 

$$\begin{pmatrix}1 & 0\\\ 0 & 1 \end{pmatrix} * \begin{pmatrix}a & b\\\ c & d \end{pmatrix} = \begin{pmatrix}(1 * a + 0 * c)  & (1 * b + 0 * c)\\\  (0 * a + 1 * c) & (0 * b + 1 * b) \end{pmatrix} = \begin{pmatrix}a & b\\\ c & d \end$$

So any matrix multiplied by it's identity matrix is just the matrix itself.

## Inverse of a Matrix

We want to find a matrix which is the inverse of A given by the symbol:

$$ A^{-1}$$

Which has the property

$$ A * A^{-1} = A^{-1} * A = I $$

Where if you multiply the inverse of a matrix by the matrix you will find the identity matrix.

This is actually how division works with matrices. Well, it's the equivalent of division.

Not all matrices have an inverse. The singular number 0 has no inverse.

When a matrix **does not** have an inverse it is referred to singular.

Such calculations such as finding the inverse of a 4x4 matrix or larger values of n you really don't want to do that by hand so it's best left to an already programmed solution.



## The Determinant of a Matrix

There is a basic but rather tedious procedure that can be applied to decide if A (matrix) is invertible.

Suppose we take any n x n matrix A and we choose any row and any column of that matrix then we can form another matrix defined by row i and column j such as:

$$ A_{ij}$$

is the matrix A, turning it into an (n-1) x (n-1) matrix by deleting its ith row and the jth column.

In other terms, we delete the ith row and the jth column. We're deleting a column and a row from a matrix to produce a new matrix.

To calculate the determinant we can use a recursive algorithm.

1. If n = 2 (A is a 2 x 2 matrix):
$$ det \textbf{A} = a_{11}a_{22} - a_{12}a_{21}$$

2. if n > 2:
$$ det \textbf{A} = \sum^n_{j=1} (-1)^{1+j}a_{1j}det \textbf{A}_{ij}$$

Let's calculate the determinant of the following matrix:

$$\begin{pmatrix}0 & 5 & 2\\\ 3 & 0 & 4\\\ 10 & 7 & 0\end{pmatrix}$$

So because it is not a 2 x 2 matrix we have to form sub matrices by deleting the first row and then the first column, then the first row and second column, then the first row and third column to form these matrices:

$$a_{11} = \begin{pmatrix}0 & 4 \\\ 7 & 0 \end{pmatrix}; a_{12} = \begin{pmatrix}3 & 4 \\\ 10 & 0 \end{pmatrix}; a_{13} = \begin{pmatrix}3 & 0 \\\ 10 & 7 \end{pmatrix}$$

You'll notice that the notation:

$$ a_{11}$$

is used here to define what rows are **missing**. In this case, if you take off the first row and first column of the original matrix you get left with $$a__{11}$$.

To find the determinant of a 2x2 matrix, we multiply the items along the main diagonal and subtract the entries by the opposite diagonal.

$$det A_{11} = \begin{pmatrix}0 & 4\\\ 7 & 0 \end{pmatrix} = 0 * 0 - 4 * 7 = -28$$

Do you see how it's diagnonal?

If we do the same to the other matrices we get:

$$ det A_{12} = -40; det A_{13} = 21$$

Now we have to combine the three determinant values together in a particular way to construct the determinant for the matrix overall.

$$(-1)^(1+1) * 0 * (-28)$$

So you time's by -1 (I'm not sure why) but you put -1 to the power of the row and columns missing in the matrix. So for the first sub matrix we have this notation:

$$a_{11}$$

Which is why we do it to the power of (1+1). Paul doesn't actually explain this, nor does he explain why we want -1. I assume it's just part of the algorithm.

We then times this by the first item in the 1st row and 1st column in the original matrix, which is 0, and then we multiplky that by the determinant of the matrix formed by deleting the first row and first column (first sub matrix)

So in total we have:

$$ (-1)^2 * 0 * (-28)$$

Now we do something similar for the second matrix:

$$ (-1)^2 * 0 * (-28) + (-1)^(1+2)*5$$

So that's sub matrix

$$a_{12}$$

And 1 + 2 is 3, so to the power of 3. Then we multiply it by the item in the original matrix which is in the first row, second column which is 5.

$$ (-1)^2 * 0 * (-28) + (-1)^3*5*(-40)$$

Times that by the determinant of the second mini matrix.

The next one works the same.

$$ (-1)^2 * 0 * (-28) + (-1)^3 * 5 * (-40) + (-1)^4 * 2 * (21)$$

Now we just do the maths:

$$ (-1)^2 * 0 * (-28) + (-1)^3 * 5 * (-40) + (-1)^4 * 2 * (21) = 0 + 200 + 42 = 242$$

I can only guess that we times by -1 because the determinant involves the inverse of a matrix and to find the inverse of a real number that isn't 0 you times by -1, so I'm under the assumption that if we times a matrix by -1 we get the inverse of that matrix.

The determinant of the matrix is 242.

## Adjoint of a Matrix

We have an n x n matrix A, then we look at the ith row and jth column of that matrix and for each value of that matrix add the determinant formed by deleting ith row and jth column then the adjoint of any matrix is the n x n matrix whose individal lengths are given in the following way:

$$ a_{ij} = (-1)^{i+j}|A_{ji}|$$

This formula finds the inverse of a matrix.

We need the determinants of the matrix and the determinant of the three sub matrices, calculated earlier.

We work out the determinant of every possible sub matrix:

$$\begin{pmatrix}0 & 5 & 2\\\ 3 & 0 & 4\\\ 10 & 7 & 0\end{pmatrix}^{-1} = \frac{1}{242}\begin{pmatrix}-28 & 14 & 20\\\ 40 & -20 & 6\\\ 21 & 50 & -15\end{pmatrix} = \textbf{I}$$

When we multiply a matrix by its inverse matrix we get the identity matrix.

Paul explicitly said that this won't come up in the test.

# Charecteristic Matrices

Suppose we have a real valued n x n matrix, A. Suppose further we want to find all the n-vectors, X, that have the following properties with respect to A:

1. X != 0. X has no zero component.
2. There is a value, λ , for which Ax^t = λx^t

How do we go about finding X and λ?


TK work out identity matrix
TK identity matrix?