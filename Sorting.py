"""This module visualises sorting algorithms using pygame"""
import random
import sys
import time
import threading
import math
import pygame

def swap(rects, i, j):
    """Swap height and position of rectangles"""
    rects[i].height, rects[j].height = rects[j].height, rects[i].height
    rects[i].y, rects[j].y = rects[j].y, rects[i].y

def quick_sort(rects):
    """Quick sort"""
    # Explanation of quick sort: https://www.youtube.com/watch?v=MZaf_9IZCrc
    if len(rects) < 2 or stop_thread:
        return

    pivot_index = len(rects) - 1

    i = -1
    j = 0
    while j < pivot_index:
        if rects[j].height < rects[pivot_index].height:
            i += 1
            swap(rects, i, j)
        j += 1
    swap(rects, i + 1, pivot_index)
    pivot_index = i + 1
    time.sleep(TIME_DELAY)

    # partition left and right side
    left = rects[:pivot_index]
    right = rects[pivot_index + 1:]

    # Call recursively on left and right side of pivot
    # No need to return anything since rects inside list are passed by reference even when sliced
    quick_sort(left)
    quick_sort(right)

def bubble_sort(rects):
    """Bubble sort"""
    for i in range(len(rects) - 1):
        for j in range(len(rects) - i - 1):
            if stop_thread:
                return
            if rects[j].height > rects[j + 1].height:
                swap(rects, j, j + 1)
                time.sleep(TIME_DELAY)

def insertion_sort(rects):
    """Insertion sort"""
    for i in range(len(rects) - 1):
        for j in range(i + 1, 0, -1):
            if stop_thread:
                return
            if rects[j].height > rects[j - 1].height:
                break
            swap(rects, j, j - 1)
            time.sleep(TIME_DELAY)

def merge_sort(rects):
    """Merge sort"""
    if stop_thread:
        return
    length = len(rects)
    if length > 1:
        # divide list into 2 if length is more than 1
        half = math.floor(length / 2)

        left = rects[:half]
        right = rects[half:]

        merge_sort(left)
        merge_sort(right)

        merge = left + right
        quick_sort(merge)

        time.sleep(TIME_DELAY)


if __name__ == "__main__":
    # Pygame setup
    pygame.init()
    clock = pygame.time.Clock()

    # Setting up the main window
    SCREEN_WIDTH = 1500
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sorting Algorithms")

    # Rectangles
    QUANTITY = 250 #750
    TIME_DELAY = 0.01
    RECT_WIDTH = SCREEN_WIDTH / 2 / QUANTITY

    # Make a list of rectangles with random heights
    quick_sort_rectangles = []
    bubble_sort_rectangles = []
    insertion_sort_rectangles = []
    merge_sort_rectangles = []
    for n in range(QUANTITY):
        # randomise height
        RECT_HEIGHT =  random.randint(0, SCREEN_HEIGHT / 2 + 1)

        quick_sort_rectangles.append(pygame.Rect(n * RECT_WIDTH,
                                    SCREEN_HEIGHT / 2 - RECT_HEIGHT,
                                    RECT_WIDTH,
                                    RECT_HEIGHT))

        bubble_sort_rectangles.append(pygame.Rect(SCREEN_WIDTH / 2 + n * RECT_WIDTH,
                                    SCREEN_HEIGHT / 2 - RECT_HEIGHT,
                                    RECT_WIDTH,
                                    RECT_HEIGHT))

        insertion_sort_rectangles.append(pygame.Rect(n * RECT_WIDTH,
                                    SCREEN_HEIGHT - RECT_HEIGHT,
                                    RECT_WIDTH,
                                    RECT_HEIGHT))

        merge_sort_rectangles.append(pygame.Rect(SCREEN_WIDTH / 2 + n * RECT_WIDTH,
                                    SCREEN_HEIGHT - RECT_HEIGHT,
                                    RECT_WIDTH,
                                    RECT_HEIGHT))

    # Colours
    bg_colour = pygame.Color("grey12")
    rect_colour = (200, 200, 200)

    # Algorithm
    stop_thread = False
    thread_quick_sort = threading.Thread(target=quick_sort, args=[quick_sort_rectangles])
    thread_bubble_quick_sort = threading.Thread(target=bubble_sort, args=[bubble_sort_rectangles])
    thread_insertion_sort = threading.Thread(target=insertion_sort, args=[insertion_sort_rectangles])
    thread_merge_sort = threading.Thread(target=merge_sort, args=[merge_sort_rectangles])
    thread_quick_sort.start()
    thread_bubble_quick_sort.start()
    thread_insertion_sort.start()
    thread_merge_sort.start()

    while True:
        # Handling inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_thread = True
                pygame.quit()
                sys.exit()

        # Visuals
        screen.fill(bg_colour)
        for rectangle in quick_sort_rectangles:
            pygame.draw.rect(screen, rect_colour, rectangle)
        for rectangle in bubble_sort_rectangles:
            pygame.draw.rect(screen, rect_colour, rectangle)
        for rectangle in insertion_sort_rectangles:
            pygame.draw.rect(screen, rect_colour, rectangle)
        for rectangle in merge_sort_rectangles:
            pygame.draw.rect(screen, rect_colour, rectangle)


        # Update the window
        pygame.display.flip()
        clock.tick(60)
