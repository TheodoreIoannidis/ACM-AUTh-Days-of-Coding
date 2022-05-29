# Day 4 - Problem Description

## Difficulty: Medium

You are given an n x m matrix which represents a 2-dimensional box containing three types of elements:

- spheres (represented by "O");
- obstacles (represented by "#");
- empty spaces (represented by "X").

The task is to write an algorithm which determines the state of the box if it tilts 90 degrees to the left (L) or to the right (R), assuming that the spheres will change their position according to the force of gravity and the location of the obstacles, as per the following example:

![Example](./example.png)

For this problem, matrices will be represented as strings consisting of the symbols O, # and X, separated by commas. For example, the 4x3 matrix

> X X X  
> X O X  
> O # X  
> O X #

will be represented as the string

> "X,X,X,X,O,X,O,#,X,O,X,#".

In particular, the algorithm should take as input the two dimensions n and m, the direction of the tilt (L or R), and the matrix in a string form, and print out the tilted matrix in a string form. So as seen in the above example, given the 4x3 matrix represented by the string "X,X,X,X,O,X,O,#,X,O,X,#" and the L direction, the output should be the string

> "X,X,X,#,X,X,#,X,X,O,O,O".
