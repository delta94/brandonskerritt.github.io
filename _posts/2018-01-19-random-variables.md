---
title: "Random Variables"
categories:
  - Comp105
tags:
  - maths
---

## What is a Random Variable?
A random variable is not a variable or random. It is a function that maps the output to the real numbers.

We will assume that the sample space is finite. Thus, given a random variable, F, from a sample space S, the set of numbers n that take the values of F is finite as well.

The probability that F takes the value N, in symbols (F=N), is defined as:
$$ P(f=n) = P(\{a | F(a)=r\})$$

When defining a probability distribution P for a random variable F we often do not apply it's sample space S but *directly* assign a probability to the event that F takes a certain value.

Thus we define the probability P(f=r) of the event that F has value R as:
$$ 0 ≤ P(f=r) ≤ 1 $$
$$ Σ P(f=r) = 1 $$
This is just basic probability. The probability of one single random variable is between 0 and 1. The sum of all random variables is 1.

## Notation and rules
We write 
$$ ¬(F=r) = \{a | f(a) ≠ r\} $$
$$ P(¬(F=r)) = 1 - P(F=r) $$
$$ P(f=r_1) V P(f=r_2) = P(f=r_1) + P(f=1_2) - P(f=r_1, f=r_2) $$
Where "," is used as "and" & "and" is used as "intersection"

## Conditional Probability
If p(F_2 = r\_2) does not = 0 then:
$$ P(f_1=r_1 | f_2=r_2) = \frac{p(f_1=r_1, f_2=r_2)}{p(f_2=r_2)} $$

The multiplication rule is also applicable to random variables
$$P(f_1=r_1, f_2=r_2) = P(f_1=r_1 | f_2=r_2) * P(f_2=r_2)$$

We sometimes use symbols distinct from numbers to represent the value of a random variable. Like F(weather = sunny).

## Probability distrubtion
The probability distrubtion for a random variable gives the probabilities of all the possible values of the variable. Assume the order of the variables is fixed then:

$$P(weather=sunny)=0.7$$
$$P(weather=rain)=0.2$$
$$P(weather=cloudy)=0.08$$
$$P(weather=Storm)=0.02$$