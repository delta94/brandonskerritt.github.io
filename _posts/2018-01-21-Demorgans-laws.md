---
title: "De Morgan's Laws"
categories:
  - Maths
---

# What are De Morgan's Laws?
De Morgan's Laws are a pair of laws that are heavily used in Computer Science, Propositional Calculus, Boolean logic, and Set Theory.

The laws were found (if you believe mathematics is "found" and not created) by Aristotle and many others however the laws were not formally defined until Augustus De Morgan defined them in terms of Boolean algebra.

## What are the rules?

In English the rules are:

> the negation of a disjunction is the conjunction of the negations

> the negation of a conjunction is the disjunction of the negations

Which may sound confusing, but if you have any experience with set theory or propositional logic then it is more easily understand.

Within propositional logic the first law is defined as:

$$ ¬(P \land Q) = (¬P V ¬Q) $$

In short, you multiply in the negation and change the "and" symbol to the "or" symbol. 
The second law is very similar and is:

$$ ¬(P V Q) = (¬P \land ¬Q)$$

De Morgan's laws can be used for simplifying propositional logic. In propositional logic you may be asked to simplify a given statement and for this there are many laws you should know about to simplify propositional statements

## Set Theory De Morgan's Laws
This is just as simple!

$$ ¬(A U B) = (¬A n ¬B)$$


## Some things you need to remember for the exam

Note to anyone reading this that isn't from my university: This section is designed to help people (and myself) remember all the important things in propositional logic. Feel free to read this section too.

A tautology is something that is always true. So for example (P V ¬P) is always true. We can simplify this as a *T* or just a "1" to represent that it is always true.

A contradiction is something that is always false. So for example (P \land ¬P) is always false. This can be represented as an upside down T or a "0" or a "F".

These 2 statements are always equal to each other:

$$ P -> Q = ¬P V Q $$

Double negation can be canceled out. So for example

$$ ¬¬P = P$$

The same works for any even amount of negations. You could have

$$ ¬¬¬¬¬¬¬¬¬¬p = P$$

Some small helpful tips you might have forgotten

$$ 0 |= 0 = 1$$
$$ 1 -> 0 = 0$$

*Identity laws*
So these are called identity laws, but they're not really anything special. Quite simple to understand actually.

$$ P \land T = P$$

Did you remember that T is a *tautology*? It's always true. Boris uses this notation in his tutorials so be careful in exams.

$$ P V F = P $$

*Domination Laws*

$$ P V T = T $$

$$ P \land F = F $$

I know it sucks to read over this notation because you just want it explained in English (don't we all) but it's super super simple once you dip your toes into some notation!

*Distributive Law*
$$ P \land (Q V R) = (P \land Q)V(P \landR)$$

So this is simple distribution. Much like how in maths you get 3(1+2) which is just equal to (3*1) + (3\*2). Same rules but with propositional logic.

$$P V (Q \land R) = (P V Q) \land (P V R)$$

*Absorption Laws*

$$P \land (P V Q) = P$$
$$P V (P \land Q) = P$$

*Commutativity*

$$P \land Q = Q \land P$$

*Associativity*
$$P\land(q \land r)=(p \land q) \land r$$

*Inverse laws*

$$ P \land ¬P = F$$
$$P V ¬P = T$$

Note: Boris / Frank have used these laws in class tests before.

*Conditional Law*
$$P->Q = ¬p v Q$$


