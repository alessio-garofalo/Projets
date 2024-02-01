def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Verifica righe e colonne
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True

    # Verifica diagonali
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_player_move():
    while True:
        try:
            move = int(input("Inserisci la tua mossa (da 1 a 9): "))
            if 1 <= move <= 9:
                return (move - 1) // 3, (move - 1) % 3
            else:
                print("Mossa non valida. Riprova.")
        except ValueError:
            print("Inserisci un numero valido.")

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Benvenuto nel gioco del Tic Tac Toe!")

    while True:
        print_board(board)
        row, col = get_player_move()

        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Complimenti! Il giocatore {current_player} ha vinto!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Il gioco è finito in pareggio!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("La cella è già occupata. Riprova.")

if __name__ == "__main__":
    play_tic_tac_toe()



    