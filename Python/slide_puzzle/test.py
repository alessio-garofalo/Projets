import pygame
import random
import sys

pygame.init()

windo_width, windo_height = 500, 500
window = windo_width, windo_height 
screen = pygame.display.set_mode(window)
pygame.display.set_caption('Sliding Puzzle ')

FPS = 15
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

bg = pygame.image.load('Python\python 4SEMAIN\slide_puzzle\imageE.png')
bg_rect = bg.get_rect()
bg_rect.topleft = (0, 0)

img_selected = None
finish = False

rows = 3
cols = rows
num_cells = rows *cols
cells_width = windo_width // rows
cells_height = windo_height // cols

cells = []
# Creazione di una lista di indici casuali per l'ordine delle celle
order_indices = list(range(0, num_cells))

for i in range(num_cells):
    x = (i % rows) * cells_width
    y = (i // cols) * cells_height
    rect = pygame.Rect(x, y, cells_width, cells_height)

    # Utilizza l'indice casuale per l'ordine
    random_pos = random.choice(order_indices)
    order_indices.remove(random_pos)
    cells.append({'rect': rect, 'border': white, 'order': i, 'pos': random_pos})
    print(cells[i])


def window_win(testo):
    font = pygame.font.Font(None, 50)
    testo_renderizzato = font.render(testo, True, white)

    # Posiziona il testo al centro della finestra
    testo_rect = testo_renderizzato.get_rect(center=(windo_width // 2, windo_height // 2 - 25))

    # Sfondo della finestra di dialogo
    finestra_rect = pygame.Rect(windo_width // 4, windo_height // 4, windo_width // 2, windo_height // 2)
    pygame.draw.rect(screen, black, finestra_rect)
    
    # Disegna il testo sulla finestra
    screen.blit(testo_renderizzato, testo_rect)

     # Aggiungi un pulsante "Esci"
    font_pulsante = pygame.font.Font(None, 20)
    testo_pulsante = font_pulsante.render("Esci", True, white)
    pulsante_rect = testo_pulsante.get_rect(center=(windo_width // 2, windo_height // 2 + 25))
    pygame.draw.rect(screen, red, pulsante_rect, 0)
    screen.blit(testo_pulsante, pulsante_rect)


    pygame.display.flip()

   # Attendi finché l'utente non preme un tasto o clicca su un pulsante
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
#############################################################################
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
                            #swap
                            temp = img_selected['pos']
                            cells[img_selected['order']]['pos'] = cells[current_img['order']]['pos']
                            cells[current_img['order']]['pos'] = temp

                            cells[img_selected['order']]['border'] = white
                            img_selected = None

                            finish = True
                            for cell in cells:
                                if cell['order'] != cell['pos']:
                                    finish = False

    screen.fill(white) #colore background
    # screen.blit(bg, bg_rect, (400, 300, 100, 100)) # DISEGNA L'IMMAGINE //1foto - 2posizione foto  / blit accetta 3 parametri / - 3grandezza da visualizzare(x,y,w,h)
    # Disegna le celle sulla finestra
    if not finish:
        for i, val in enumerate(cells): # ciclo per controllare ogni |i| prendendo il valore |val| di ogni cella numerata in cells |enumerate(cells)|
            pos = cells[i]['pos'] #definizione della posizione di ogni cella
            img_area = pygame.Rect(cells[pos]['rect'].x, cells[pos]['rect'].y, cells_width, cells_height) #definizione dell'area con posizione |x|y| e  con dimensioni della cella
            screen.blit(bg, cells[i]['rect'], img_area) #creazione di area per ogni cella
            pygame.draw.rect(screen, cells[i]['border'], cells[i]['rect'], 1) # disegnare il bordo che di base é bianco giá definito nel dict con le dimensione di ogni cella, per ogni cella con spessore 1
    else:
        screen.blit(bg, bg_rect)
        window_win('Hai Vinto')

    pygame.display.update()# Aggiornare lo schermo
    clock.tick(FPS)
pygame.quit()
