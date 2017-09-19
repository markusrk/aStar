import pygame
import board as wrapper
from a import A

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (155, 0, 255)
RAND1 = (111, 111, 255)
RAND2 = (255, 0, 255)
RAND3 = (0, 0, 200)
RAND4 = (0, 0, 255)
RAND5 = (55, 55, 55)
RAND6 = (0, 40, 40)
RAND7 = (0, 160, 80)
RAND8 = (0, 120, 120)
RAND9 = (0, 80, 120)
RAND10 = (0, 120, 80)

color_scheme = [RED, BLUE, BLACK, GREEN, RAND1, RAND2, RAND3, RAND4, RAND5, RAND6, RAND7, RAND8, RAND9, RAND10]
PI = 3.141592653

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# load some boards, only for testing
i = 0

#legal_test_boards = board.generate_successors(board.load_file('hard-3.txt'))
#legal_test_boards.insert(0,board.id_to_board( board.load_file('hard-3.txt')))
a = A
boards = a.run(a,'Rushhour_boards/easy-3.txt')
print(boards)

def draw_board(board):
    if isinstance(board, str):
        board = wrapper.id_to_board(board)
    for x in range(len(board)):
        car = board[x]
        box_size = 50
        x_pos = car[1]
        y_pos = car[2]
        orientation = car[0]
        length = car[3]

        if orientation == 0:
            for i in range(0, length):
                pygame.draw.rect(screen, color_scheme[x],
                                 [x_pos * box_size + i * box_size, y_pos * box_size, box_size, box_size])
        else:
            for i in range(0, length):
                pygame.draw.rect(screen, color_scheme[x],
                                 [x_pos * box_size, y_pos * box_size + i * box_size, box_size, box_size])
    pygame.draw.line(screen, BLACK, [0, 0], [box_size*6, 0], 5)
    pygame.draw.line(screen, BLACK, [0, 0], [0, box_size*6], 5)
    pygame.draw.line(screen, BLACK, [box_size*6, 0], [box_size*6, box_size*2], 5)
    pygame.draw.line(screen, BLACK, [box_size * 6, box_size*3], [box_size * 6, box_size * 6], 5)
    pygame.draw.line(screen, BLACK, [0, box_size*6], [box_size*6, box_size*6], 5)
    pygame.display.flip()


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here

    # draw boards in "boards" as defined in top of file.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                i = i - 1
            if event.key == pygame.K_RIGHT:
                i = i + 1

    draw_board(boards[i])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
