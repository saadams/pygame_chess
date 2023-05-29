import pygame

# Define the chessboard
WIDTH = 800
HEIGHT = 800
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH // COLS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

circle_radius = SQUARE_SIZE // 2 - 8  # Radius of the circle
circle_color = (255, 0, 0) 

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chessboard")

#pawn_image = pygame.image.load("pawn.png")


def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

            if row == 1:
              
              square_pos = (x,y)
              #  screen.blit(pawn_image, (x, y))
              #pygame.draw.circle(screen, circle_color, circle_center, circle_radius)
              #find circle center by taking x coord and add half the square width sam with y coord.
              circle_center = (square_pos[0] + SQUARE_SIZE // 2, square_pos[1] + SQUARE_SIZE // 2)
              pygame.draw.circle(screen, circle_color, circle_center, circle_radius)
            if row == 6:
              
              square_pos = (x,y)
              #  screen.blit(pawn_image, (x, y))
              #pygame.draw.circle(screen, circle_color, circle_center, circle_radius)
              #find circle center by taking x coord and add half the square width sam with y coord.
              circle_center = (square_pos[0] + SQUARE_SIZE // 2, square_pos[1] + SQUARE_SIZE // 2)
              pygame.draw.circle(screen, circle_color, circle_center, circle_radius)
                

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)  # Clear the screen
    draw_board()  # Draw the chessboard
    pygame.display.update()

# Quit Pygame
pygame.quit()
