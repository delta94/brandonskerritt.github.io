---
title: "De Morgan's Laws"
categories:
  - Maths
---

# What are De Morgan's Laws?
De Morgan's Laws are a pair of laws that are heavily used in Computer Science, Propositional Calculus, Boolean logic, and Set Theory.

The laws were found (if you believe mathematics is "found" and not created) by Arisotle and many others however the laws were not formally defined until Augustus De Morgan defined them in terms of Boolean algebra.

## What are the rules?

In English the rules are:
> the negation of a disjunction is the conjunction of the negations
> the negation of a conjunction is the disjunction of the negations
Which may sound confusing, but if you have any experience with set theory or propositional logic then it is more easily understand.

Within propositional logic the first law is defined as:
$$ ~(P ^ Q) = (~P V ~Q) $$
In short, you multiply in the negation and change the "and" symbol to the "or" symbol. 
The second law is very similar and is:
$$ ~(P V Q) = (~P ^ ~Q)$$

De Morgan's laws can be used for simplfying propositional logic. In propositional logic you may be asked to simplfy a given statement and for this there are many laws you should know about to simplfy propositional statements

## Set Theory De Morgan's Laws
This is just as simple!
$$ ~(A U B) = (~A n ~B)$$


## Some things you need to remember for the exam

Note to anyone reading this that isn't from my university: This section is designed to help people (and myself) remember all the important things in propositional logic. Feel free to read this section too.

A tautology is something that is always true. So for example (P V ~P) is always true. We can simplfy this as a *T* or just a "1" to represent that it is always true.

A contradiction is something that is always false. So for example (P ^ ~P) is always false. This can be represented as an upside down T or a "0" or a "F".

These 2 statements are always equal to each other:
$$ P -> Q = ~P V Q $$

Double negation can be cancelled out. So for example
$$ ~~P = P$$
The same works for any even amount of negations. You could have
$$ ~~~~~~~~~~p = P$$

Some small helpful tips you might have forgotten
$$ 0 |= 0 = 1$$
$$ 1 -> 0 = 0$$

$$ P ^ T = P$$
Did you remember that T is a *tautology*? It's always true. Boris uses this notation in his tutorials so be careful in exams.

$$ P V F = P $$


