#Extremes of an Array

This problem introduces the popular algorithm called "linear search";
it is helpful to know this algorithm as it is often used in programming
more complex tasks, like sorting.

A very common operation carried out on a list (array) of values is to find the
extremal values - the minimum or maximum.

To achieve this you will need to store current maximum (or minimum respectively)
value in a separate variable, and then run through array, comparing each of its
elements to this variable. Whenever the next value is greater than the temporary
variable, this value should be copied into the variable (as a new maximum).

To achieve this problem you must not use any min or max functions that already
exist.

At the end of the pass this temporary variable will hold the extreme value.

Start with the following numbers in a list (array):

```
3, 1, 56, 3, 7, 8, 6, 87, 34, 56, 23, 90, 47, 21, 16, 84, 91, 72, 93, 105
```

Find the minimum and maximum values. Output:

```
Min: ?, Max: ?
```
