import PySimpleGUI as sg
import pygame
import random
import pygame_menu


def run_tic_tac_toe():
    #inizializzazione di pygame
    pygame.init()

    # costanti
    larghezza, altezza = 600, 600   #Grandezza Finestra

    dimensioni_finestra = (larghezza, altezza)

    fps = 30    #velocita gioco

    board_size = 3  #utilizzo di un valore per dividere le celle in formati uguali
    spazio_celle = larghezza // board_size  #creazione dello spazio dentro le celle
    #creazione della finestra
    screen = pygame.display.set_mode(dimensioni_finestra)   #utilizzo della libreria di pygame per creare la finestra di gioco
    pygame.display.set_caption('Tic Tac Toe')   #Nome sulla finestra di gioco

    # Caricamento delle immagini
    background_image = pygame.image.load('Python/python 3SEMAIN/Tic Tac Toe/sfondo.png').convert_alpha()    #Board Tic Tac Toe
    x_image = pygame.image.load('Python/python 3SEMAIN/Tic Tac Toe/x_image.png').convert_alpha()    #Simbolo X
    o_image = pygame.image.load('Python/python 3SEMAIN/Tic Tac Toe/o_image.png').convert_alpha()    #Simbolo O

    # Inizializzazione delle liste dei giocatori
    player1 = []  # Lista delle mosse del giocatore X #registrazione importante per definire la vittoria
    player2 = []  # Lista delle mosse del giocatore O #registrazione importante per definire la vittoria
    playerPC = []  # Lista delle mosse del giocatore O #registrazione importante per definire la vittoria

    board = [' '] * 9   #Creazione del campo da gioco
    player_symbols = {'X': x_image, 'O': o_image} #dizionario con chiave : valore corrispettivo all'immagine
    current_player = 2  # Inizia con il giocatore 'X' valore giocatore di base

    clock = pygame.time.Clock() #Tempo di gioco
    running = True  #Variabile condizionata

    point_player1 = 0
    point_player2 = 0
    point_playerPC = 0

    single_player = False


    # Creazione del board
    def draw_board():
        screen.blit(background_image, (50, 50))
        # disegno griglia
        for row in range(board_size):
            for col in range(board_size):
                x = col * spazio_celle
                y = row * spazio_celle
                cell_value = board[row * board_size + col]
                # disegna il simbolo corrispondente allo stato della casella
                if cell_value in player_symbols:
                    symbol_image = player_symbols[cell_value]
                    symbol_width, symbol_height = symbol_image.get_width(), symbol_image.get_height()
                    screen.blit(symbol_image, (x + spazio_celle // 2 - symbol_width // 2, y + spazio_celle // 2 - symbol_height // 2))


    def get_clicked_cell(mouse_x, mouse_y):
        # Calcola la colonna e la riga della cella corrispondente al clic del mouse
        col = mouse_x // spazio_celle
        row = mouse_y // spazio_celle
        # Restituisci la posizione della cella nel board
        return row * board_size + col

    def winner(player_moves):
        winning_combinations = [ #lista di liste di combinazioni vincenti
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Orizzontali
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticali
            [0, 4, 8], [2, 4, 6]              # Diagonali
        ]
        for combo in winning_combinations:                  
            if all(move in player_moves for move in combo):
                return True
        return False

        '''
        ###Spiegazione condizione###
        Primo ciclo for per iterare nella lista di liste
        if all verifica tutte le condizioni vere
         per ogni 'Mossa' in 'Combo' , Se gruppo di mosse e nella lista return True, 
         al contrario con all se le condizioni non sono vere salta e return false
        '''
    #ia facile
    def play_ai_turn(board):
        empty_cells = [i for i in range(len(board)) if board[i] == ' ']  # Trova le celle vuote
        if empty_cells:
            ai_choice = random.choice(empty_cells)  # Scegli casualmente tra le celle vuote
            return ai_choice
        return None
    #ia difficile
    def play_smart_ai_turn(board):
    # 1. Controlla se l'IA può vincere
        for i in range(len(board)):
            if board[i] == ' ':
                # Prova a fare la mossa e verifica se l'IA vince
                board[i] = 'O'
                if winner(playerPC):
                    # Se l'IA vince, registra la mossa e restituisci
                    playerPC.append(i)
                    return
                # Se non vince, ripristina la board per esplorare altre mosse
                board[i] = ' '
        # 2. Controlla se il giocatore umano può vincere e blocca
        for i in range(len(board)):
            if board[i] == ' ':
                # Prova a fare la mossa del giocatore umano e verifica se può vincere
                board[i] = 'X'
                if winner(player2):
                    # Se il giocatore umano può vincere, blocca la mossa e registra
                    board[i] = 'O'
                    playerPC.append(i)
                    return
                # Se non può vincere, ripristina la board per esplorare altre mosse
                board[i] = ' '
        # 3. Se nessuna mossa vincente è possibile, scegli una mossa casuale tra le celle vuote
        empty_cells = [i for i in range(len(board)) if board[i] == ' ']
        if empty_cells:
            # Scegli casualmente tra le celle vuote e registra la mossa
            ai_choice = random.choice(empty_cells)
            board[ai_choice] = 'O'
            playerPC.append(ai_choice)




    while running and single_player:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
                back_to_menu = True
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_cell = get_clicked_cell(mouseX, mouseY)
                if 0 <= clicked_cell < len(board) and board[clicked_cell] == ' ':
                    if current_player == 2:  # Giocatore umano
                        board[clicked_cell] = 'X'
                        player1.append(clicked_cell)
                        # È il turno dell'IA dopo il giocatore umano
                        ai_choice = play_ai_turn(board)
                        if ai_choice is not None:
                            board[ai_choice] = 'O'
                            playerPC.append(ai_choice)
                    current_player = 3 - current_player  # Passa al prossimo giocatore
                    print(f"Player {current_player} Ha cliccato nella cella: {clicked_cell}")
                    if winner(player1 if current_player == 1 else playerPC): #se winner restituisce true (condizione ternaria : se player corrente == 1: player1[] else player2[]    )
                        if current_player == 1:
                            point_player1 += 1
                            winner_text = 'Vince Player 1'   #print del gioco su console
                        elif current_player == 2:
                            point_playerPC += 1
                            winner_text = 'Vince Player PC'   #print del gioco su console
                        layout = [
                            [sg.Text(winner_text, font=('Helvetica', 30, 'italic'), pad=((5, 5), (30, 30)), justification='center')],
                            [sg.Button('Esci', size=(15, 2), pad=((75, 75), (30, 5)))]
                            #pad= ((left,right),(up,down))
                        ]
                        window = sg.Window('Tic Tac Toe',  layout)
                        while True:
                            event, values = window.read()
                            if event == sg.WINDOW_CLOSED or event == 'Esci':
                                break
                        window.close()
                        running = False  # Termina il gioco #Chiusera del ciclo e del gioco
        draw_board()#disegno e rendering
        pygame.display.flip() #Aggiornamento della schermata
        clock.tick(fps) #limite fps


    #CICLO PRINCIPALE
    while running and not single_player:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
            #  Modifica la variabile back_to_menu a True prima di uscire
                running = False     #modifica della variabile per uscire e chiudere le finestre
                back_to_menu = True
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:    #condizione click mouse 
                mouseX, mouseY = pygame.mouse.get_pos()     #determinare dove si trova il mouse
                clicked_cell = get_clicked_cell(mouseX, mouseY) # cella cliccata con individuazione posizione del mouse
                # Esegui la logica del gioco solo se il clic è valido
                if 0 <= clicked_cell < len(board) and board[clicked_cell] == ' ': #se click e maggiore di zero e minore della lunghezza del board e board [cella cliccata]
                    if current_player == 2: #verifica di quale giocatore sta giocando
                        board[clicked_cell] = 'X'   #stampa x
                        player1.append(clicked_cell)    #registrazione mossa nella lista1
                    else:
                        board[clicked_cell] = 'O'   #stampa O
                        player2.append(clicked_cell)    #aggiunta mossa nella lista 2
                    # Passa al prossimo giocatore
                    current_player = 3 - current_player  # Alternanza tra 1 e 2
                    print(f"Player {current_player} Ha cliccato nella cella: {clicked_cell}") #conferma delle mosse, click nella cella giusta e verifica del player
                    if winner(player1 if current_player == 1 else player2): #se winner restituisce true (condizione ternaria : se player corrente == 1: player1[] else player2[]    )
                        if current_player == 1:
                            point_player1 += 1
                            winner_text = 'Vince Player 1'   #print del gioco su console
                        elif current_player == 2:
                            point_player2 += 1
                            winner_text = 'Vince Player 2'   #print del gioco su console
                        layout = [
                            [sg.Text(winner_text, font=('Helvetica', 30, 'italic'), pad=((5, 5), (30, 30)), justification='center')],
                            [sg.Button('Esci', size=(15, 2), pad=((75, 75), (30, 5)))]
                            #pad= ((left,right),(up,down))
                        ]
                        window = sg.Window('Tic Tac Toe',  layout)
                        while True:
                            event, values = window.read()
                            if event == sg.WINDOW_CLOSED or event == 'Esci':
                                break
                        window.close()
                        running = False  # Termina il gioco #Chiusera del ciclo e del gioco
        draw_board()#disegno e rendering
        pygame.display.flip() #Aggiornamento della schermata
        clock.tick(fps) #limite fps
    #Chiusura dei giochi!










''' Spiegazione ###Creazione del board###
 utilizza una list comprehension, una sintassi concisa in Python per creare liste. La sua forma generale è:
 [espressione if condizione else altra_espressione for elemento in iterabile]


 # linea  ternaria     [[' ' for _ in range(board_size)] for _ in range(board_size)]

    1 viene eseguito un ciclo interno viene eseguito 'board size' volte senza nome della variabile, non viene utilizzato nel corpo del ciclo, 2 dove si crea una lista  di 
        'board_size' elementi, dove ogni elemento e' uno spazio vuoto. 
        3 per ogni iterazione viene utilizzato 'board_size' volte un nuovo elenco per ogni list
        comprehension interna. creando una lista bidimensionale con 
        board_size = righe
        board_size = colonne
        elemento = ' '  #spazio vuoto


#Scritto anche cosi

        board = []
        for _ in range(board_size):
            row = []
            for _ in range(board_size):
                row.append(' ')
            board.append(row)

            borad size = 3 (di base)
'''