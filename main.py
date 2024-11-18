import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
BOARD_SIZE = 8
SQUARE_SIZE = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SELECT_COLOR = (0, 255, 0)

window = pygame.display.set_mode((BOARD_SIZE * SQUARE_SIZE, BOARD_SIZE * SQUARE_SIZE))
pygame.display.set_caption("Chess Game")

PIECES = {
    'WP': pygame.Surface((SQUARE_SIZE, SQUARE_SIZE)),
    'BP': pygame.Surface((SQUARE_SIZE, SQUARE_SIZE)),
    'WR': pygame.Surface((SQUARE_SIZE, SQUARE_SIZE)),
    'BR': pygame.Surface((SQUARE_SIZE, SQUARE_SIZE)),
    'WN': pygame.Surface((SQUARE_SIZE, SQUARE_SIZE)),
    'BN': pygame.Surface((SQUARE_SIZE, SQUARE_SIZE)),
    'WB': pygame.Surface((SQUARE_SIZE, SQUARE_SIZE)),
    'BB': pygame.Surface((SQUARE_SIZE, SQUARE_SIZE)),
    'WQ': pygame.Surface((SQUARE_SIZE, SQUARE_SIZE)),
    'BQ': pygame.Surface((SQUARE_SIZE, SQUARE_SIZE)),
    'WK': pygame.Surface((SQUARE_SIZE, SQUARE_SIZE)),
    'BK': pygame.Surface((SQUARE_SIZE, SQUARE_SIZE)),
}

# Create a simple circle for pieces (just for visual representation)
for piece in PIECES.values():
    pygame.draw.circle(piece, (255, 0, 0), (SQUARE_SIZE//2, SQUARE_SIZE//2), SQUARE_SIZE//3)

# 8x8 Matrix representing the board
# 1 represents white pieces, -1 represents black pieces, 0 represents empty spaces
board = [
    ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
    ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
    ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
]

def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Draw squares
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(window, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            # Draw pieces
            piece = board[row][col]
            if piece != 0:
                window.blit(PIECES[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Main game loop
selected_piece = None
selected_pos = None
while True:
    window.fill(BLACK)
    draw_board()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col, row = x // SQUARE_SIZE, y // SQUARE_SIZE

            if selected_piece:
                if board[row][col] == 0:  # If the square is empty
                    board[row][col] = selected_piece
                    board[selected_pos[1]][selected_pos[0]] = 0
                selected_piece = None
            else:
                piece = board[row][col]
                if piece != 0:  # Only select if there's a piece
                    selected_piece = piece
                    selected_pos = (col, row)

    if selected_pos:
        pygame.draw.rect(window, SELECT_COLOR, (selected_pos[0] * SQUARE_SIZE, selected_pos[1] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)

    pygame.display.update()
