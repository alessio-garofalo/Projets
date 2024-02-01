import pygame
import sys
import random

# Inizializzare pygame
pygame.init()

# Definizione delle costanti Fisse
screen_size = 900
grid_board = 3 
dimensione_casella = screen_size // grid_board

# Colori generali
white = (255, 255, 255)
black = (0, 0, 0,)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)


class menu:
    pass
class casella_x:
    def __init__(self, number, row, col):
        self.number = number
        self.row = row
        self.col = col
        self.rectangle = pygame.Rect(col * dimensione_casella, row * dimensione_casella, dimensione_casella, dimensione_casella) 

    def draw(self, screen):
        pygame.draw.rect(screen, red, self.rectangle)
        if self.number is not None:  # Disegna il numero solo se non è None
            font = pygame.font.Font(None, 50)
            text = font.render(str(self.number), True, black)
            text_rect = text.get_rect(center=self.rectangle.center)
            screen.blit(text, text_rect) # blit = scrivere/disegnare

class SlidePuzzle:
    def __init__(self):
        self.puzzle = self.inizialize_puzzle()
        self.empty_row, self.empty_col = grid_board - 1, grid_board - 1 #casella vuota in basso a destra

    def inizialize_puzzle(self):
        puzzle = [[None for _ in range(grid_board)] for _ in range(grid_board)] # matrice puzzle
        numbers = list(range(1, grid_board ** 2))
        random.shuffle(numbers)
        count = 0

        for row in range(grid_board):
            for col in range(grid_board):
                if count == grid_board ** 2 - 1:  # Casella vuota in basso a destra
                    puzzle[row][col] = casella_x(None, row, col)
                    self.empty_row, self.empty_col = row, col
                else:
                    puzzle[row][col] = casella_x(numbers[count % len(numbers)], row, col)
                    count += 1
        return puzzle
    
    def swap_casella(self, row1, col1, row2, col2):
        # Salva le coordinate della casella cliccata
        clicked_row, clicked_col = row1, col1
        # Effettua lo swap
        self.puzzle[row1][col1], self.puzzle[row2][col2] = self.puzzle[row2][col2], self.puzzle[row1][col1]
        
        # Aggiorna le coordinate delle caselle dopo lo swap
        self.puzzle[row1][col1].row, self.puzzle[row1][col1].col = row1, col1
        self.puzzle[row2][col2].row, self.puzzle[row2][col2].col = row2, col2

        # Aggiorna le coordinate della casella vuota
        if self.puzzle[row2][col2].number is None:
            self.empty_row, self.empty_col = row2, col2
        else:
            self.empty_row, self.empty_col = clicked_row, clicked_col

# Inizializzazione della finestra
screen = pygame.display.set_mode((screen_size, screen_size))
# Creazione dell'oggetto SlidePuzzle
slide_puzzle = SlidePuzzle()
clicked_row, clicked_col = 0, 0  # Inizializza le variabili fuori dal ciclo degli eventi

# Ciclo principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     # Gestione del click del mouse
        #     mouse_pos = pygame.mouse.get_pos()
        #     clicked_row = mouse_pos[1] // dimensione_casella
        #     clicked_col = mouse_pos[0] // dimensione_casella
        #     if ((clicked_row == slide_puzzle.empty_row and abs(clicked_col - slide_puzzle.empty_col) == 1)
        #         or (clicked_col == slide_puzzle.empty_col and abs(clicked_row - slide_puzzle.empty_row) == 1)):
        #         # La casella cliccata può essere mossa verso la casella vuota
        #         new_row, new_col = slide_puzzle.empty_row, slide_puzzle.empty_col
        #         slide_puzzle.swap_casella(clicked_row, clicked_col, new_row, new_col)

        elif event.type == pygame.KEYDOWN:
            # Gestione delle freccette 
            new_row, new_col = clicked_row, clicked_col  # Inizializza con la posizione attuale della casella cliccata

            if event.key == pygame.K_UP:
                new_row -= 1
            elif event.key == pygame.K_DOWN:
                new_row += 1
            elif event.key == pygame.K_LEFT:
                new_col -= 1
            elif event.key == pygame.K_RIGHT:
                new_col += 1
            if all(0 <= x < grid_board for x in (new_row, new_col)):
                slide_puzzle.swap_casella(clicked_row, clicked_col, new_row, new_col)
    # disegno puzzle
    screen.fill(black)
    for row in slide_puzzle.puzzle:
        for casella in row:
            casella.draw(screen)

    # Aggiornamento della finestra
    pygame.display.flip()