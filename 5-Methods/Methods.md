---
marp: true
theme: sparta
paginate: true
headingDivider: 2
title: Methods
---
<!-- _paginate: skip -->
<!-- _class: title -->
# Methods
![bg left:40%](../img/robot8.jpg)

## Link
![bg left:80% 80%](../img/qrcodeMethods.svg)

## What is it?
> A method is a callable unit of software logic. It has an identifier, potentially parameters and possibly a return value.

## Methods
### Scratch
![](../img/scratch/methods/methods.svg)

## Methods
### Python
```python
def fac(x):
    # Faculty for 0 is defined as 1
    if (x == 0):
        return 1
    else:
    # Faculty for x is x*fac(x-1)
        return fac(x-1)*x

fac(5)
```
## Scratch
[Sierpinski](https://scratch.mit.edu/projects/24584643/editor)
[Recursion Tree](https://scratch.mit.edu/projects/10240446/editor)

## Exercise
Calculator for factorial
1. Input of a number
2. Calculate factorial in method (recursivly)
3. Output result

[Factorial?](https://www.youtube.com/watch?v=wfkIiVJ-O50)

## Python / Jupyter

[![Lite](https://pypi-camo.freetls.fastly.net/4946a95afc1514558f07534b4cd78824d41d6e20/68747470733a2f2f6a7570797465726c6974652e727466642e696f2f656e2f6c61746573742f5f7374617469632f62616467652e737667)](https://oliverdenzelhfu.github.io/Programming/lite/notebooks/index.html?path=5-Methods%2FMethods.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/OliverDenzelHFU/Programming/main?filepath=5-Methods%2FMethods.ipynb)

Exercise
1. test functions abs, ascii, hex, min, max, round. (Add at point Function call with parameters)
2. Make a [binder](https://mybinder.org) of the notebook

## For next time
[Watch](https://www.youtube.com/watch?v=ohCDWZgNIU0)

Either
a) Try different higher factorials
b) Which is the highest factorial?