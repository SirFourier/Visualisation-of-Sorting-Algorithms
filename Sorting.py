# Visualization of Sorting Algorithms

# import pygame
import random

# pygame.init()

# Make a random set of numbers
random_numbers = random.choices([i for i in range(20)],k=20)
print(random_numbers)

def QuickSort(numbers):
    print(numbers)
    pivot = numbers[-1]
    pivot_index = len(numbers) - 1

    index = 0
    number = numbers[index]
    while number != pivot:
        if number > pivot:
            # swap pivot with number to the left of it
            numbers[pivot_index - 1], numbers[pivot_index] = numbers[pivot_index], numbers[pivot_index - 1]
            # swap number with previous pivot position
            numbers[index], numbers[pivot_index] = numbers[pivot_index], numbers[index]
            # set new pivot index
            pivot_index -= 1
    print(numbers)
            
QuickSort(random_numbers)