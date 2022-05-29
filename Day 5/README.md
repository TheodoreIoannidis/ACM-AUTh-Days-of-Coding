# Day 5 - Problem Description

## Difficulty: Easy

You are given a list of integers of length n named _height_. Now imagine that for each x=i (where i ranges from 1 to n) on the cartesian plane you draw a perpendicular line segment from y=0 to y=height[i]. Given two such segments l<sub>1</sub> at position i<sub>1</sub> and l<sub>2</sub> at position i<sub>2</sub>, let the _admissible rectangle_ formed by l<sub>1</sub> and l<sub>2</sub> be the rectangle whose two perpendicular sides have lengths |i<sub>1</sub>-i<sub>2</sub>| and min(l<sub>1</sub>,l<sub>2</sub>) respectively. The task is to find the maximal area of an admissible rectangle formed by any two line segments given a particular height list.

For example, given the height input

> 2, 8, 2, 5, 1, 6, 3, 7,

the desired output is

> 42,

which is obtained by the following admissible rectangle:

![Example](./example.png)
