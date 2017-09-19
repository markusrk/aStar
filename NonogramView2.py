from a import A
"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
from copy import deepcopy
from Nonogram import Nonogram


# Define some colors and fonts
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
color_scheme = [WHITE, GREEN, GRAY]


pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# code for setting up a board
i = 0
filename = 'Nonogram_boards/nono-telephone.txt'
n = Nonogram(filename)
x1, x2, x_segment, y_segment = Nonogram.load_file(filename)
a = A
boards = a.run(a,n)
for x in range(len(boards)):
    boards[x] = n.calculate_locked_table(n.id_to_table(boards[x])[0],n.id_to_table(boards[x])[1])


def draw_board(x_segments, y_segments, table):
    y_dim = len(x_segments)
    x_dim = len(y_segments)
    box_size = 20
    border_size = 100

    #draw boarders
    pygame.draw.line(screen, BLACK, [border_size, border_size], [box_size * x_dim+border_size, border_size], 5)
    pygame.draw.line(screen, BLACK, [border_size, border_size], [ border_size, box_size * y_dim+border_size], 5)
    pygame.draw.line(screen, BLACK, [box_size * x_dim+border_size, border_size], [box_size * x_dim+border_size,y_dim*box_size+ border_size], 5)
    pygame.draw.line(screen, BLACK, [ border_size, box_size * y_dim+border_size], [box_size * x_dim+border_size, box_size * y_dim+border_size], 5)

    #draw clues will not be done currently because of bug in pygame font
    #for x in range(0,x_dim):
    #    text = font.render(str(x_segment), True, BLACK)
    #    screen.blit(text, [0, border_size+x*box_size])


    # Draw squares
    for y in range(0,y_dim):
        for x in range(0,x_dim):
            pygame.draw.rect(screen, color_scheme[table[y][x]], [x * box_size + border_size, y * box_size + border_size, box_size, box_size])



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                i = i - 1
            if event.key == pygame.K_RIGHT:
                i = i + 1

    # --- Game logic should go here



    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    draw_board(x_segment, y_segment, boards[i])

        # Todo
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()