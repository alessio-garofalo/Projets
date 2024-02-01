import pygame
import random
import sys

pygame.init()

window_width, window_height = 500, 500
window = window_width, window_height
screen = pygame.display.set_mode(window)
pygame.display.set_caption('Sliding Puzzle')

FPS = 15
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

bg = pygame.image.load('Python\python 4SEMAIN\slide_puzzle\imageE.png')
bg_rect = bg.get_rect()
bg_rect.topleft = (0, 0)

img_selected = None
finish = False

rows = 3
cols = rows
num_cells = rows * cols
cells_width = window_width // rows
cells_height = window_height // cols

cells = []
order_indices = list(range(0, num_cells))

for i in range(num_cells):
    x = (i % rows) * cells_width
    y = (i // cols) * cells_height
    rect = pygame.Rect(x, y, cells_width, cells_height)

    random_pos = random.choice(order_indices)
    order_indices.remove(random_pos)
    cells.append({'rect': rect, 'border': white, 'order': i, 'pos': random_pos})
    print(cells[i])


def window_win(testo):
    font = pygame.font.Font(None, 50)
    testo_renderizzato = font.render(testo, True, white)
    testo_rect = testo_renderizzato.get_rect(center=(window_width // 2, window_height // 2 - 25))
    finestra_rect = pygame.Rect(window_width // 4, window_height // 4, window_width // 2, window_height // 2)
    pygame.draw.rect(screen, black, finestra_rect)

    screen.blit(testo_renderizzato, testo_rect)

    font_pulsante = pygame.font.Font(None, 20)
    testo_pulsante = font_pulsante.render("Esci", True, white)
    pulsante_rect = testo_pulsante.get_rect(center=(window_width // 2, window_height // 2 + 25))
    pygame.draw.rect(screen, red, pulsante_rect, 0)
    screen.blit(testo_pulsante, pulsante_rect)

    pygame.display.flip()

    attesa = True
    while attesa:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    attesa = False
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if pulsante_rect.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()
                elif not pulsante_rect.collidepoint(evento.pos):
                    attesa = False


def main_menu():
    screen.fill(white)

    font = pygame.font.Font(None, 60)
    testo_renderizzato = font.render("S l i d i n g     P u z z l e", True, black)
    testo_rect = testo_renderizzato.get_rect(center=(window_width // 2, window_height // 4))
    screen.blit(testo_renderizzato, testo_rect)

    #Pulsante gioca
    font_pulsante_gioca = pygame.font.Font(None, 100)
    testo_pulsante_gioca = font_pulsante_gioca.render("GIOCA", True, red)
    pulsante_rect_gioca = testo_pulsante_gioca.get_rect(center=(window_width // 2, window_height // 2))

    screen.blit(testo_pulsante_gioca, pulsante_rect_gioca)
    
    # sottotesto
    font_pulsante_sottotesto = pygame.font.Font(None, 25)
    testo_pulsante_sottotesto = font_pulsante_sottotesto.render("(Oppure premi spazio per giocare)", True, black)
    pulsante_rect_sottotesto = testo_pulsante_sottotesto.get_rect(center=(window_width // 2, window_height // 2 + 35))
    screen.blit(testo_pulsante_sottotesto, pulsante_rect_sottotesto)
    
    # Pulsante img
    font_pulsante_img = pygame.font.Font(None, 40)
    testo_pulsante_img = font_pulsante_img.render("Scegli un'immagine", True, black)
    pulsante_rect_img = testo_pulsante_img.get_rect(center=(window_width // 2, window_height // 2 + 90))
    sfondo_rect_img = pygame.Rect(pulsante_rect_img.x - 10, pulsante_rect_img.y - 5, pulsante_rect_img.width + 20, pulsante_rect_img.height + 10)
    pygame.draw.rect(screen, blue, sfondo_rect_img)
    screen.blit(testo_pulsante_img, pulsante_rect_img)

    # Pulsante modalitá
    font_pulsante_modalitá = pygame.font.Font(None, 40)
    testo_pulsante_modalitá = font_pulsante_modalitá.render("Numero di caselle", True, black)
    pulsante_rect_modalitá = testo_pulsante_modalitá.get_rect(center=(window_width // 2, window_height // 2 + 160))
    sfondo_rect_modalita = pygame.Rect(pulsante_rect_modalitá.x - 10, pulsante_rect_modalitá.y - 5, pulsante_rect_modalitá.width + 20, pulsante_rect_modalitá.height + 10)
    pygame.draw.rect(screen, blue, sfondo_rect_modalita)
    screen.blit(testo_pulsante_modalitá, pulsante_rect_modalitá)

    pygame.display.flip()

    attesa = True
    while attesa:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                attesa = False


# Esegui il menu principale
main_menu()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            mouse_pos = pygame.mouse.get_pos()

            for cell in cells:
                rect = cell['rect']
                order = cell['order']

                if rect.collidepoint(mouse_pos):
                    if not img_selected:
                        img_selected = cell
                        cell['border'] = red
                    else:
                        current_img = cell
                        if current_img['order'] != img_selected['order']:
                            temp = img_selected['pos']
                            cells[img_selected['order']]['pos'] = cells[current_img['order']]['pos']
                            cells[current_img['order']]['pos'] = temp

                            cells[img_selected['order']]['border'] = white
                            img_selected = None

                            finish = True
                            for cell in cells:
                                if cell['order'] != cell['pos']:
                                    finish = False

    screen.fill(white)
    if not finish:
        for i, val in enumerate(cells):
            pos = cells[i]['pos']
            img_area = pygame.Rect(cells[pos]['rect'].x, cells[pos]['rect'].y, cells_width, cells_height)
            screen.blit(bg, cells[i]['rect'], img_area)
            pygame.draw.rect(screen, cells[i]['border'], cells[i]['rect'], 1)
    else:
        screen.blit(bg, bg_rect)
        window_win('Hai Vinto')

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
