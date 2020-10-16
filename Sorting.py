# Visualization of Sorting Algorithms

import pygame
import random

def quickSort(numbers):
    # https://www.youtube.com/watch?v=MZaf_9IZCrc
    if len(numbers) < 2: 
        return numbers

    pivot_index = len(numbers) - 1

    i = -1
    j = 0
    while j < pivot_index:
        # if numbers[j] > numbers[pivot_index] then do nothing
        if numbers[j] < numbers[pivot_index]:
            i += 1
            # swap numbers at i and j
            numbers[i], numbers[j] = numbers[j], numbers[i]
        j += 1
    
    # swap pivot with number at i + 1
    numbers[i + 1], numbers[pivot_index] = numbers[pivot_index], numbers[i + 1]
    pivot_index = i + 1

    # partition left and right side
    left = numbers[:pivot_index]
    right = numbers[pivot_index + 1:]

    # Call recursively on left and right side of pivot
    return quickSort(left) + [numbers[pivot_index]] + quickSort(right)
        

# Make a random set of numbers
random_numbers = random.choices([i for i in range(100)],k=100)
print(random_numbers)
sorted = quickSort(random_numbers)
print(sorted)