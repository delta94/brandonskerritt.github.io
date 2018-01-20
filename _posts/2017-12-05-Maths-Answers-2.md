---
title: "Math Answers Explained"
categories:
  - Foundations
---

# Note to my classmates

This document has been  compiled by UoL CS FB Groupchat. The answers **may not** be right. If you can solve some of them yourself, please do and inform me. This document is here to help you get the aanswers to questions you're not sure of in order to aide revision. This is a group document and can be edited on GitHub also.

# Question 1 

Let A = {2, 3} and B = {a, b, c}. List the elements of A × B.

To do this you need to make ordered pairs whereby the first element is the first element of set A and the second element is every element in set B.

{(2,a), (2,b), (2,c), (3,a), (3,b), (3,c)}

# Question 2

```Let |A| = m and |B| = n. What is the cardinality of the set A × B?```

The cardinality is how many elements are in the set, represented by |A|. Count how many elements are in set A and B and then times them.

2 * 3 = 6

# Question 3

List the set of ordered pairs of the relation R represented by the following digraph (diagraph in pdf)

```
{(1,2)
(2,1),(2,2)
(3,3)
(4,2),(4,5)
(5,1)}
```

Remember that some arrows are _bi-directional_ or just 1 direction or just repeats onto itself.

# Question 4

## Part A

Let A = {a, b, c}, B = {1, 2, 3, 4} and C = {3, 4, 5}.
List the set of ordered pairs of the relation R between A and B represented by the following
matrix.

Matrix =

F | T | T | T
--- | --- | --- | ---
F | F | T | T
F | F | T | T


Okay, so we know it's a relation between A and B, so the matrix will look something like

 | 1 | 2 | 3 | 4
--- | --- | --- | ---
a |
b |
c |

Then we will it in with the truth values from above

 | 1 | 2 | 3 | 4
--- | --- | --- | ---
a | F | T | T | T
b | F | F | T | T
c | F | F | T | T

Now we simply pull out the ordered pairs that appear as true in the matrix

```
{(a,2),(a,3),(a,4)
(b,3),(b,4)
(c,3),(c,4)}
```

## Part B

Let S ⊆ B × C be given by
S = {(x, y) | x < y}.
List the set of ordered pairs in the inverse relation S−1 of S.
B = {1, 2, 3, 4} and C = {3, 4, 5}.

To make an inverse relation, we change it from B x C to C x B.

S = {(3, 4)}

## Part C
Compute the matrix representation of S ◦ R

```
o R=  1,  2,  3,  4,  5
S 1,  F,  F,  T,  T,  T
  2,  F,  T,  F,  T,  T
  3,  F,  F,  F,  T,  T   = Matrix
  4,  F,  F,  F,  F,  T
  5,  F,  F,  F,  F,  F
```
  
# Question 5
Let T = {(2, 3),(1, 2),(3, 1)}. List the set of ordered pairs in the transitive closure of T

T = {(1, 2), (2, 1), (2, 2), (2, 3), (3, 1)}

# Question 6

Which of the following sentences are propositions?

(1) A banana is larger than its skin
(2) London is the capital of Paris
(3) Answer this question
(4) 2 + 3 = 5
(5) 5 + 7 = 10

Question 1, 2, 4, and 5 are all propositional statements as they have a true or false value.

# Question 7

Which of the following are true:

P0 V p1 = p0 ^ p1

No, P0 or p1 is not the same as p0 and p1.

p0 ^ (p0 -> p1) = p1

We can just use a truth table.

p0 | p1 | p0 -> p1 
--- | --- | ---
1 | 1 | 1
0 | 1 | 1
1 | 0 | 0
0 | 0 | 1

No, because the truth table values do not match. If p0 and p1 are false then p0 -> p1 is true. Therefore they are not equvialent.

p0 -> p1 = ¬p1 V p0

Yes, this is true. This was shown in lectures, but we can construct a truth table to prove it.

p0 | p1 | p0 -> p1 | ¬p1 V p0
--- | --- | --- | ---
1 | 1 | 1 | 1
1 | 0 | 0 | 1
0 | 1 | 1 | 1
0 | 0 | 1 | 0

Everytime p0 -> p1 is true, ¬p1 V p0 is true. Vice-versa for falsity.

(p1 ∧ (p0 → p1)) ≡ ¬p0

Again, construct a truth table,

p1 | p0 | p0 -> p1 | ¬p0 | (p1 ∧ (p0 → p1))
--- | --- | --- | --- | ---
1 | 1 | 1 | 0 | 0
1 | 0 | 0 | 1 | 0
0 | 1 | 0 | 0 | 0
0 | 0 | 1 | 1 | 1

**Note to reader**
Check my truth table.

In this instance, this is false because we have found an intrepretation under which the left handside is false and the right handside is true.

(p0 ∧ p1) ≡ (p0 ∧ (p0 → p1))

Again, we construct a truth table.

p0 | p1 | p0 ^ p1 | p0 -> p1 | p0 ∧ (p0 → p1)
--- | --- | --- | --- | ---
1 | 1 | 1 | 1 | 1
1 | 0 | 0 | 0 | 0
0 | 1 | 0 | 1 | 0
0 | 0 | 0 | 1 | 0

Thus they are the same.

# Question 8

For the table below, construct a circuit having the given table as it's input / output table.

To solve this create 3 inputs, P, Q, R and 1 output, S.

# Question 9

Represent 183 in binary notation.

128 | 64 | 32 | 16 | 8 | 4 | 2 | 1
--- | --- | --- | --- | --- | --- | --- | ---
1 | 0 | 1 | 1 | 0 | 1 | 1 | 1

Simples!

# What is the 4-bit two's complement of 5?


First, turn 5 into 4-bit binary.

8 | 4 | 2 | 1
--- | --- | --- | ---
0 | 1 | 0 | 1

Now invert the numbers

1010

Now add +1

1011

And we are done!

# Question 11

Using the 4-bit representation, compute the sum 4 + (-5)

So we know -5 is 1011

and we can quickly convert 4 into binary as 100

So now we do
1011 + 100 which is 1111. 

# Question 12

A password consists of three lower-case letters followed by a three digit number. The three digit number must satrt with 0 or with 1 or with 2. How many passwords are there?

So that's
_ _ _ _ _ _
So 3 lower cases letters, that's
26 * 26 * 26 _ _ _ 
The number must start with 0, 1, or 2. So that's

26 * 26 * 26 * 3 * 10 * 10

# Question 12

How many ways can a 2-person subcommittee be chosen from a 6-person commitee?

So here, order matters. If we have 6 people named:

John, Frank, Boris, Floriana, Bethan, Zelda and we want to pick two people we could do:

n! / (n-k)!

Which is just

6! / 4!

However, this is for permutations. In this instance, we will get {Bethan, Florianna} and {Florianna, Bethan}. We need to divide by how many permutations there are to get the pure amount of subcommittees where there are no repeats like this.

6! / 2! * 4!

Which is 15

# Question 14

How many length 4 sequences of distinct digits are there?

So, distinct is a keyword here.

_ _ _ _ 

There are 10 digits per space, but because it's distinct that makes it
10 * 9 * 8 * 7

