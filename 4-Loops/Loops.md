---
marp: true
theme: gaia
footer: ':copyright: 2024 Oliver Denzel'
paginate: true
class: gaia
headingDivider: 1
backgroundImage: linear-gradient(rgb(255, 171, 14) 10%, #874624 90%);
---
<!-- _paginate: skip -->
<!-- _class: gaia lead -->
# Loops & Conditions
## Intro
![bg left:40%](../img/robot7.jpg)

# Overview
> Conditions are executed once at most, loops possibly multiple times.

# Conditions
```python
if sunUp:
    print ("Hallo Sonne!")
if onEarth:
    print ("Hello World")
else:
    print ("Hello Aliens")
```
![](../img/scratch/conditions/conditions.svg)
# Loops
```python
for x in range(10):
    print (x)
while (sunUp):
    print ("A day without sunshine, is, you know, night.)
```
![](../img/scratch/conditions/loops.svg)
# Demo Scratch
[Start Demo...](https://scratch.mit.edu/projects/398569407/)
[And Exercise...](https://studio.code.org/s/frozen/lessons/1/levels/4)
# [Demo Python](https://mybinder.org/v2/gh/OliverDenzelHFU/Programming/main?urlpath=tree%2FLoops%2FLoops.ipynb)
1. Change the latitude and longitude to your position
2. Add a fourth condition => between 12:00 and 13:00 for "Mahlzeit!"
3. Change the Pattern Examples
Create a bigger triangle
Close the triangle at the bottom
Draw a nicer rectangle using unicode
https://en.wikipedia.org/wiki/Box_Drawing_(Unicode_block)

# For Next Time
[Watch Functions video.](https://www.youtube.com/watch?v=9Os0o3wzS_I)