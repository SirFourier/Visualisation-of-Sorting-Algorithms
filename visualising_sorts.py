"""This module visualises sorting algorithms using pygame and threading"""
import random
import sys
import time
import threading
import math
import pygame

class SortVisualisation():
    """Class to encapsulate the visualisation of each sorting algorithm"""
    stop_threads = False

    def __init__(self, sort_algorithm, rect_colour):
        self.rectangles = []
        self.sort_algorithm = sort_algorithm
        self.rect_colour = rect_colour
        self.thread = None

        self.text_surface = None
        self.text_rect = None

        self.start_time = None
        self.time_surface = None
        self.time_rect = None

    def start(self, time_delay):
        """Start thread"""
        self.thread = threading.Thread(target=self.sort_algorithm, args=[self.rectangles, time_delay])
        self.thread.start()
        self.start_time = time.time()

    def draw_rectangles(self, display):
        """Render rectangles on display context"""
        for rectangle in self.rectangles:
            pygame.draw.rect(display, self.rect_colour, rectangle)

    def setup_title(self, title, font_size, text_colour, center_x, center_y):
        """Render title of sort algorithm on screen"""
        my_font = pygame.font.SysFont("Comic Sans MS", font_size)
        self.text_surface = my_font.render(title, True, text_colour)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (center_x, center_y)

    def draw_title(self, display):
        """Draw title"""
        display.blit(self.text_surface, self.text_rect)

    def calculate_time(self, font_size, text_colour, center_x, center_y):
        """Calculate elapsed time"""
        if self.thread.is_alive():
            current_stopwatch_time = time.time() - self.start_time
            time_font = pygame.font.SysFont("Comic Sans MS", font_size)
            self.time_surface = time_font.render(f"{current_stopwatch_time:.3f} s", True, text_colour)
            self.time_rect = self.time_surface.get_rect()
            self.time_rect.center = (center_x, center_y)
        else:
            self.rect_colour = pygame.Color("green")

    def draw_time(self, display):
        """Draw elapsed time"""
        display.blit(self.time_surface, self.time_rect)

def swap(rects, i, j):
    """Swap height and position of rectangles"""
    rects[i].height, rects[j].height = rects[j].height, rects[i].height
    rects[i].y, rects[j].y = rects[j].y, rects[i].y

def quick_sort(rects, delay):
    """Quick sort"""
    # Explanation of quick sort: https://www.youtube.com/watch?v=MZaf_9IZCrc
    if len(rects) < 2 or SortVisualisation.stop_threads:
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
    time.sleep(delay)

    # partition left and right side
    left = rects[:pivot_index]
    right = rects[pivot_index + 1:]

    # Call recursively on left and right side of pivot
    # No need to return anything since rects inside list are passed by reference even when sliced
    quick_sort(left, delay)
    quick_sort(right, delay)

def bubble_sort(rects, delay):
    """Bubble sort"""
    for i in range(len(rects) - 1):
        for j in range(len(rects) - i - 1):
            if SortVisualisation.stop_threads:
                return
            if rects[j].height > rects[j + 1].height:
                swap(rects, j, j + 1)
                time.sleep(delay)

def insertion_sort(rects, delay):
    """Insertion sort"""
    for i in range(len(rects) - 1):
        for j in range(i + 1, 0, -1):
            if SortVisualisation.stop_threads:
                return
            if rects[j].height > rects[j - 1].height:
                break
            swap(rects, j, j - 1)
            time.sleep(delay)

def merge_sort(rects, delay):
    """Merge sort"""
    if SortVisualisation.stop_threads:
        return
    length = len(rects)
    if length > 1:
        # divide list into 2 if length is more than 1
        half = math.floor(length / 2)

        left = rects[:half]
        right = rects[half:]

        merge_sort(left, delay)
        merge_sort(right, delay)

        merge = left + right
        quick_sort(merge, delay)

        time.sleep(delay)

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
    QUANTITY = 750
    RECT_WIDTH = SCREEN_WIDTH / 2 / QUANTITY

    # Colours
    BG_COLOUR = pygame.Color("grey12")
    RECT_COLOUR = (200, 200, 200)

    # Make a list of rectangles with random heights
    quick_sort_visualisation = SortVisualisation(quick_sort, RECT_COLOUR)
    bubble_sort_visualisation = SortVisualisation(bubble_sort, RECT_COLOUR)
    insertion_sort_visualisation = SortVisualisation(insertion_sort, RECT_COLOUR)
    merge_sort_visualisation = SortVisualisation(merge_sort, RECT_COLOUR)
    for n in range(QUANTITY):
        # randomise height
        RECT_HEIGHT =  random.randint(0, SCREEN_HEIGHT / 2 + 1)

        quick_sort_visualisation.rectangles.append(pygame.Rect(n * RECT_WIDTH,
                                                    SCREEN_HEIGHT / 2 - RECT_HEIGHT,
                                                    RECT_WIDTH,
                                                    RECT_HEIGHT))

        bubble_sort_visualisation.rectangles.append(pygame.Rect(SCREEN_WIDTH / 2 + n * RECT_WIDTH,
                                                    SCREEN_HEIGHT / 2 - RECT_HEIGHT,
                                                    RECT_WIDTH,
                                                    RECT_HEIGHT))

        insertion_sort_visualisation.rectangles.append(pygame.Rect(n * RECT_WIDTH,
                                                        SCREEN_HEIGHT - RECT_HEIGHT,
                                                        RECT_WIDTH,
                                                        RECT_HEIGHT))

        merge_sort_visualisation.rectangles.append(pygame.Rect(SCREEN_WIDTH / 2 + n * RECT_WIDTH,
                                                    SCREEN_HEIGHT - RECT_HEIGHT,
                                                    RECT_WIDTH,
                                                    RECT_HEIGHT))

    # Borders
    BORDER_THICKNESS = 5
    BORDER_COLOUR = pygame.Color("red")
    horizontal_border = pygame.Rect(0, SCREEN_HEIGHT/2 - BORDER_THICKNESS/2, SCREEN_WIDTH, BORDER_THICKNESS)
    vertical_border = pygame.Rect(SCREEN_WIDTH/2 - BORDER_THICKNESS/2, 0, BORDER_THICKNESS, SCREEN_HEIGHT)

    # Title
    TEXT_COLOUR = pygame.Color("yellow")
    FONT_SIZE = 30
    quick_sort_visualisation.setup_title("Quick sort", FONT_SIZE, TEXT_COLOUR, SCREEN_WIDTH / 4, FONT_SIZE / 2)
    bubble_sort_visualisation.setup_title("Bubble sort", FONT_SIZE, TEXT_COLOUR, 3 * SCREEN_WIDTH / 4, FONT_SIZE / 2)
    insertion_sort_visualisation.setup_title("Insertion sort", FONT_SIZE, TEXT_COLOUR, SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 + FONT_SIZE / 2)
    merge_sort_visualisation.setup_title("Merge sort", FONT_SIZE, TEXT_COLOUR, 3 * SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 + FONT_SIZE / 2)
    
    # Algorithm
    TIME_DELAY = 0.0001
    quick_sort_visualisation.start(TIME_DELAY)
    bubble_sort_visualisation.start(TIME_DELAY)
    insertion_sort_visualisation.start(TIME_DELAY)
    merge_sort_visualisation.start(TIME_DELAY)

    start = time.time()

    while True:
        # Handling inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SortVisualisation.stop_threads = True
                pygame.quit()
                sys.exit()

        # Stopwatch
        quick_sort_visualisation.calculate_time(FONT_SIZE, TEXT_COLOUR, SCREEN_WIDTH / 4, 2 * FONT_SIZE)
        bubble_sort_visualisation.calculate_time(FONT_SIZE, TEXT_COLOUR, 3 * SCREEN_WIDTH / 4, 2 * FONT_SIZE)
        insertion_sort_visualisation.calculate_time(FONT_SIZE, TEXT_COLOUR, SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 + 2 * FONT_SIZE)
        merge_sort_visualisation.calculate_time(FONT_SIZE, TEXT_COLOUR, 3 * SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 + 2 * FONT_SIZE)

        # Visuals
        screen.fill(BG_COLOUR)

        quick_sort_visualisation.draw_rectangles(screen)
        bubble_sort_visualisation.draw_rectangles(screen)
        insertion_sort_visualisation.draw_rectangles(screen)
        merge_sort_visualisation.draw_rectangles(screen)

        pygame.draw.rect(screen, BORDER_COLOUR, horizontal_border)
        pygame.draw.rect(screen, BORDER_COLOUR, vertical_border)

        quick_sort_visualisation.draw_title(screen)
        bubble_sort_visualisation.draw_title(screen)
        insertion_sort_visualisation.draw_title(screen)
        merge_sort_visualisation.draw_title(screen)

        quick_sort_visualisation.draw_time(screen)
        bubble_sort_visualisation.draw_time(screen)
        insertion_sort_visualisation.draw_time(screen)
        merge_sort_visualisation.draw_time(screen)
  
        # Update the window
        pygame.display.flip()
        clock.tick(60)
