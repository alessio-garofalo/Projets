import PySimpleGUI as sg
from Tic_Tac_Toe import run_tic_tac_toe
from variable import single_player

# variables universal
hover_color = ('white', 'blue')
runner = True



def main_menu():
    global runner
    global single_player
    global back_to_menu
    # Layout del menu
    layout = [
        [sg.Text("Tic Tac Toe", key='text_element', font=('Helvetica', 50, 'italic'), size=(30, 2), pad=((10, 0), (50, 0)), justification='center')],
        
        [sg.Button("Inizia Gioco", key='btn_inizia', font=('Book Antiqua', 30, 'normal'), button_color=('white', sg.theme_background_color()), pad=((170, 0),(0, 40)))],
        [sg.Button("Modalità", key='btn_modalita', font=('Book Antiqua', 25, 'normal'), pad=((220, 0),(5, 0)))],

        [sg.Button("Esci", key='btn_esci', font=('Book Antiqua', 12, 'bold'), pad=((160, 0),(100, 0)), size=(25,2))]
    ]   

    # Creazione della finestra
    window = sg.Window("Menu Principale", layout, size=(600, 600), resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'btn_esci':
            runner = False  # Imposta runner su False per uscire dal ciclo
            break
            
        elif event == 'btn_inizia':
            window.hide()  # Nasconde la finestra del menu
            run_tic_tac_toe()  # Esegui il gioco Tic Tac Toe
            window.un_hide()  # Riapri la finestra del menu dopo che il gioco è finito
        
        elif event == 'btn_inizia-MOTION-':
            window['btn_inizia'].update(button_color=hover_color)
        
        elif event == 'btn_modalita':
            modalita_button()  # Chiamata alla funzione per gestire il pulsante "Modalità"
    window.close()


        
############################### MODALITA ##################################
def modalita_button():
    global single_player
    global play_game
    # Aggiungi qui la logica per il pulsante "Modalità" o impostazioni di gioco future
    layout = [
        [sg.Text("Modalitá", key='text_element', font=('Helvetica', 30, 'italic'), size=(30, 2), pad=((5, 0), (30, 0)), justification='center')],
        [sg.Text("Puoi modificare la modalitá di gioco ed altre piccole impostazioni", key='text_element', font=('Helvetica', 10, 'italic'), size=(50, 2), pad=((0, 0), (0, 0)), justification='center')],
        [sg.Text("Scegli contro chi vuoi giocare: ", font=('Helvetica', 12, 'italic'))],
        [sg.Button("Multiplayer", key='btn_modalita_gioco2', font=('Book Antiqua', 15, 'normal'), pad=((50, 0), (15, 20))), sg.Button("Single player", key='btn_modalita_giocoIA', font=('Book Antiqua', 15, 'normal'), pad=((50, 0), (15, 20)))],
        [sg.Text("Scegli a quale difficoltá vuoi giocare: ", font=('Helvetica', 12, 'italic'))],
        [sg.Button("Facile", key='btn_facile', font=('Book Antiqua', 15, 'normal'), button_color=('white', sg.theme_background_color()), pad=((55, 0),(20, 0)), size=(8, 1)),
            sg.Button("Difficile", key='btn_difficile', font=('Book Antiqua', 15, 'normal'), pad=((70, 0),(20, 0)), size=(8, 1))],
        [sg.Button("Esci", key='btn_esci', font=('Book Antiqua', 15, 'bold'), pad=((160, 0),(40, 10)), size=(12, 2))]
    ]       #pad= ((left,right),(up,down))

    window = sg.Window("Modalitá", layout, size=(500, 500))

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'btn_esci':
            break
        elif event == 'btn_facile':
            play_game = False  # Passa la difficoltà alla funzione di gioco
            sg.popup_auto_close('Hai impostato il gioco in "Facile"', auto_close_duration=3)
        elif event == 'btn_difficile':
            play_game = True  # Passa la difficoltà alla funzione di gioco
            sg.popup_auto_close('Hai impostato il gioco in "Difficile"', auto_close_duration=3)
        elif event == 'btn_modalita_giocoIA':
            single_player = True
            print(single_player)
            sg.popup_auto_close('Hai impostato il gioco in Single player', auto_close_duration=3)
            
        elif event == 'btn_modalita_gioco2':
            single_player = False
            print(single_player)
            sg.popup_auto_close('Hai impostato il gioco in Multiplayer', auto_close_duration=3)
            
    window.close()
    return single_player
        


if __name__ == '__main__':
    main_menu()
