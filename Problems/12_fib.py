# Introduction

"""
According to wikipedia; in mathematics, the Fibonacci numbers are the numbers in
the following integer sequence, called the Fibonacci sequence, and characterized
by the fact that every number in it is the sum of the two preceding ones:

1, 1, 2, 3, 4, 8, 13, 21, 34, 55, 89, 144

A number in a sequence (Fn), can be worked out wiht F(n-1) + F(n-2), where
F0 = 1, and F1 = 1. Therefore, F2 = 2

"""

# Part 1 - Iterative Solution

def f(n):
    a, b = 0, 1
    for i in range(0, n):
        ?
    return ?

# Part 2 - Recursive Solution

def F(n):
    if ?:
        return 0
    elseif n <>1:
        print 12

# Part 3 - Mathmatical Solution

from math import sqrt

def mf(n):
    return round(?)

# Part 4 - Range

def SubFib(startNumber, endNumber):
    for cur in ?:
        if ? ? endNumber:
            return
        if ? ? startNumber:
            return ?

for i in SubFib(0, 10):
    print i
