# Visualization of Sorting Algorithms

import pygame
import random
import sys

# def quickSort(numbers):
#     # https://www.youtube.com/watch?v=MZaf_9IZCrc
#     if len(numbers) < 2: 
#         return numbers

#     pivot_index = len(numbers) - 1

#     i = -1
#     j = 0
#     while j < pivot_index:
#         if numbers[j] < numbers[pivot_index]:
#             i += 1
#             # swap numbers at i and j
#             numbers[i], numbers[j] = numbers[j], numbers[i]
#         j += 1
    
#     # swap pivot with number at i + 1
#     numbers[i + 1], numbers[pivot_index] = numbers[pivot_index], numbers[i + 1]
#     pivot_index = i + 1

#     # partition left and right side
#     left = numbers[:pivot_index]
#     right = numbers[pivot_index + 1:]

#     # Call recursively on left and right side of pivot
#     return quickSort(left) + [numbers[pivot_index]] + quickSort(right)

def quickSortRect(rectangles):
    # https://www.youtube.com/watch?v=MZaf_9IZCrc
    if len(rectangles) < 2: 
        return rectangles

    pivot_index = len(rectangles) - 1

    i = -1
    j = 0
    while j < pivot_index:
        if rectangles[j].height < rectangles[pivot_index].height:
            i += 1
            # swap rectangle heights and positions of rectangles at index i and j
            rectangles[i].height, rectangles[j].height = rectangles[j].height, rectangles[i].height
            rectangles[i].y, rectangles[j].y = rectangles[j].y, rectangles[i].y
        j += 1
    
    # swap pivot with rectangle at i + 1
    rectangles[i + 1].height, rectangles[pivot_index].height = rectangles[pivot_index].height, rectangles[i + 1].height
    rectangles[i + 1].y, rectangles[pivot_index].y = rectangles[pivot_index].y, rectangles[i + 1].y
    pivot_index = i + 1

    # partition left and right side
    left = rectangles[:pivot_index]
    right = rectangles[pivot_index + 1:]

    # Call recursively on left and right side of pivot
    return quickSortRect(left) + [rectangles[pivot_index]] + quickSortRect(right)
        

# Make a random set of numbers
max = 20
length = 20
random_numbers = random.choices([i for i in range(max)],k=length)
print(random_numbers)
# sorted = quickSort(random_numbers)
# print(sorted)

# Pygame setup
pygame.init()
clock = pygame.time.Clock()

# Setting up thhe main window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Quick sort algorithm")

# Rectangles
rect_width = screen_width / length
rect_height = screen_height / 2
rectangles = []

for i, number in enumerate(random_numbers):
    # randomise height
    rect_height = random.randint(0, screen_height + 1)
    rect_height =  screen_height * number / max

    x = i * rect_width
    y = screen_height - rect_height
    width = rect_width
    height = rect_height

    rectangles.append(pygame.Rect(x, y, width, height))

# Colours
bg_colour = pygame.Color("grey12")
rect_colour = (200, 200, 200)

while True:
    # Handling inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Algorithm
    quickSortRect(rectangles)

    #Visuals
    screen.fill(bg_colour)
    for rectangle in rectangles:
        pygame.draw.rect(screen, rect_colour, rectangle)

    # Update the window
    pygame.display.flip()
    clock.tick(60)
