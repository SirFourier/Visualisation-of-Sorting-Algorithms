# Visualization-of-Sorting-Algorithms

![sorting_gif](sorting.gif?raw=true)

## Inspiration
I was inspired to have a go at visualising sorting algorithms from a Youtube video by Timo Bingmann: https://www.youtube.com/watch?v=kPRA0W1kECg. I wanted to see if I could display multiple visualisations in one screen which lead me to learn pygame and threading. The code has an infinite while loop which deals with displaying the rectangles. And 4 seperate threads that deal with sorting the rectangles based on their heights on the screen. These 4 seperate threads correspond to the 4 sorting algorithms I had chosen which are the following.

## Requirements to run
The only requirement is to install pygame with pip -install pygame. Everything else is included in the standard library.

### Quick sort (O(nlogn) on average)
quick_sort(rects, delay)
  1) If length of list < 2 then return
  2) Choose last element of list to be pivot
  3) Let i and j be the starting indexs. Where  i = j - 1 and j = 0
  4) While j < pivot index
      - If rects[j].height < rects

### Bubble sort (O(n^2) on average)

### Insertion sort (O(n^2) on average)

### Merge sort (O(nlogn) on average)

## Possible future additions
