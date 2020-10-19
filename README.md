# Visualization-of-Sorting-Algorithms

![sorting_gif](sorting.gif?raw=true)

## Requirements to run
The only requirement is to install pygame with pip -install pygame. Everything else is included in the standard library.

## Important variables that can be changed
  - The number of rectangles to sort with the QUANTITY variable
  - The delay each algorithm has with the TIME_DELAY variable

## Inspiration
I was inspired to have a go at visualising sorting algorithms from a Youtube video by Timo Bingmann: https://www.youtube.com/watch?v=kPRA0W1kECg. I wanted to see if I could display multiple visualisations in one screen which lead me to learn pygame and threading. The code has an infinite while loop which deals with displaying the rectangles. And 4 seperate threads that deal with sorting the rectangles based on their heights on the screen. These 4 seperate threads correspond to the 4 sorting algorithms I had chosen which are the following:
  - Quick sort (O(nlogn) on average)
  - Bubble sort (O(n^2) on average)
  - Insertion sort (O(n^2) on average)
  - Merge sort (O(nlogn) on average)

## Learning outcomes
  - How to use threading to run multiple functions concurrently 
  - How to use pygame (Works similar to SDL2 in C++ so it was nice to see an abstraction of it)

## Possible future additions
  - Colour rectangles that are being compared
  - Add sounds
