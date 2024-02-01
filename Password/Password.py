import random
import hashlib
import re
import json



########################Criptage Manuel################################

    
reg = ['']

def criptage_lettre():
    print('Qui puoi criptare solo lettere con altre lettere.')
    nome_user = input('Inserisci il tuo nome identificativo: ')
    input_user = input('Inserisci una frase che vuoi criptare:  ')
    input_senza_spazi = input_user.replace(" ", "")
    verifica_input(input_senza_spazi, nome_user)

def verifica_input(frase,nome):
    regex = r'^[A-Za-z]+$'  # Esempio: solo lettere maiuscole/minuscole
    # Verifica se la stringa rispetta l'espressione regolare
    if re.match(regex, frase):
        print("La stringa rispetta le regole.")
        cripta(frase,nome)
    else:
        print("La stringa non rispetta le regole.")
        return frase, False

def salvataggio(nome,key,chiaveK,input_utente):
    try:
        # Salva la chiave casuale in un file utilizzando pickle
        with open('C:/Users/Elfo98/OneDrive/Documenti/GitHub/Python/python 3SEMAIN/Password/chiave_casuale.json', 'a') as file:
            json.dump({
                    'Nome identificativo': nome,
                    'alphabet': key,
                    'alphabet_random': chiaveK,
                    'input_utente': input_utente
                }, file, indent=4)
            print("Chiave casuale generata e salvata con successo.")

    except:
    # Gestisci il caso in cui il file non esista
        try:
            with open('C:/Users/Elfo98/OneDrive/Documenti/GitHub/Python/python 3SEMAIN/Password/chiave_casuale.json', 'w') as file:
                json.dump({
                    'Nome identificativo': nome,
                    'alphabet': key,
                    'alphabet_random': chiaveK,
                    'input_utente': input_utente
                }, file, indent=4)
                print("Chiave casuale generata e salvata con successo.")
        except Exception as e:
            print(f"Errore durante il salvataggio della chiave casuale: {str(e)}")


def cripta(input_utente,nome):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = alphabet.upper()
    key = list(alphabet + alphabet2)
    print(key)

    ###########Cript###########################
    chiave_criptata = []
    #   #   #   salvare il cript base   #   #   #
    alphabet_random = key.copy()
    random.shuffle(alphabet_random)
    print(alphabet_random)
    reg.append(alphabet_random)
    criptare_lettereF(alphabet_random, input_utente)
    salvataggio(nome,key,chiave_criptata,input_utente)
    


def criptare_lettereF(lista_random, input_utente):
    chiave_criptata = []
    for x in input_utente:
        if x in lista_random:
            ascii_value =  ord(x)
            chiave_criptata.append(ascii_value)
            
    random.shuffle(chiave_criptata)
    lettere_criptate = [chr(ascii_value) for ascii_value in chiave_criptata]
    stringa_risultante = ''.join(map(str, lettere_criptate))
#    stringa_risultante = ''.join(map(str, chiave_criptata))

    print("Valori ASCII:", chiave_criptata)
    print("Lettere criptate:", lettere_criptate)
    print(stringa_risultante)
    return chiave_criptata, lettere_criptate
############################ # # Criptare solo numeri # # ##############################################

def criptage_num(nome,lunghezza_desiderata):
    lista_num = list(range(10))
    lista_ripetuta = (lista_num * (lunghezza_desiderata // len(lista_num))) + lista_num[:lunghezza_desiderata % len(lista_num)]
    random.shuffle(lista_ripetuta)
    stringa_risultante = ''.join(map(str, lista_ripetuta))  
    print(f"Valore criptato {stringa_risultante}")
    key = 'Password solo numeri'
    salvataggioN(nome,key,stringa_risultante,lunghezza_desiderata)
    return lista_ripetuta, stringa_risultante


def input_num():
    print('Qui puoi criptare solo numeri.')
    nome_user = input('Inserisci il tuo nome identificativo: ')
    lunghezza_passw = int(input('Inserisci quanto vuoi\n sia lunga la password di numeri:  '))
    criptage_num(nome_user,lunghezza_passw)

def salvataggioN(nome,key,chiaveK,input_utente):
    try:
        # Salva la chiave casuale in un file utilizzando pickle
        with open('C:/Users/Elfo98/OneDrive/Documenti/GitHub/Python/python 3SEMAIN/PyGame/chiave_casuale.json', 'a') as file:
            json.dump({
                'Nome identificativo': nome,
                'input_utente': input_utente,
                'Tipologia': key,
                'Password': chiaveK
            }, file, indent=4)
            print("Chiave casuale generata e salvata con successo.")

    except:
    # Gestisci il caso in cui il file non esista
        try:
            with open('C:/Users/Elfo98/OneDrive/Documenti/GitHub/Python/python 3SEMAIN/PyGame/chiave_casuale.json', 'w') as file:
                json.dump({
                '\nNome identificativo': nome,
                'input_utente': input_utente,
                'Tipologia': key,
                'Password': chiaveK
                }, file, indent=4)
                print("Chiave casuale generata e salvata con successo.")
        except Exception as e:
            print(f"Errore durante il salvataggio della chiave casuale: {str(e)}")
####################### # # Criptare Num e lettere # # ###############################################
def criptage_let_num():
    while True:
        print('\nCome vuoi comporre la password di Lettere e Numeri?\n\n1 - Personalizzata\n2 - Genera una password casuale\n0 - Esci')
        scelta = int(input('Scelta: '))
        while scelta == 1:
            print('\nSegui le istruzioni:\n\n1 - Scegli quante lettere\n2 - Scegli quanti numeri\n0 - Esci')
            scelta = int(input('Quante lettere? '))
            scelta2 = int(input('Quanti numeri? '))
            print('Lunghezza totale password: ',scelta + scelta2)
            criptage_let_num_code(scelta,scelta2)
            if scelta == 0:
                menu()
        while scelta == 2:
            lunghezza_tot = int(input('Quanto vuoi che sia lunga la password?'))
            criptage_let_num_code_casuale(lunghezza_tot)

        # if scelta ==
    
def criptage_let_num_code(lettere_da_prendere,numeri_da_prendere):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = alphabet.upper()
    key = list(alphabet + alphabet2)
    random.shuffle(key)
    lista_num = list(range(10))
    random.shuffle(lista_num)
    lista_ripetuta_num = (lista_num * (numeri_da_prendere // len(lista_num))) + lista_num[:numeri_da_prendere % len(lista_num)]
    lista_ripetuta_let = (key * (lettere_da_prendere // len(key))) + key[:lettere_da_prendere % len(lista_num)]
    password_grezza = lista_ripetuta_num + lista_ripetuta_let
    random.shuffle(password_grezza)
    password_raffinata = ''.join(map(str, password_grezza)) 
    print(password_raffinata)

def criptage_let_num_code_casuale(lunghezza_tot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = alphabet.upper()
    key = list(alphabet + alphabet2)
    random.shuffle(key)
    lista_num = list(range(10))
    random.shuffle(lista_num)
    lunghezza_tot = lunghezza_tot // 2
    lista_ripetuta_num = (lista_num * (lunghezza_tot // len(lista_num))) + lista_num[:lunghezza_tot % len(lista_num)]
    lista_ripetuta_let = (key * (lunghezza_tot // len(key))) + key[:lunghezza_tot % len(lista_num)]
    password_grezza = lista_ripetuta_num + lista_ripetuta_let
    random.shuffle(password_grezza)
    password_raffinata = ''.join(map(str, password_grezza)) 
    print(password_raffinata)


####################### # # Criptare solo con caratteri speciali # # #################################
def criptage_specio():
    nome = input('Inserisci un nome identificativo: ')
    key = 'Symbol'
    scelta = int(input('\nSegui le istruzioni ', nome,'\n\n1 - Scegli la lunghezza della password: '))
    utente_caratteri = input('Digita i caratteri che vuoi utilizzare:  ')
    utente_caratteri_senza_spazi = utente_caratteri.replace(" ", "")
    lista_caratteri = list(utente_caratteri_senza_spazi)    

    # Generare la password mescolando casualmente i caratteri
    password_grezza = random.sample(lista_caratteri * (scelta // len(lista_caratteri)) + lista_caratteri[:scelta % len(lista_caratteri)], scelta)
    
    # Converti la lista di caratteri in una stringa
    password_finale = ''.join(password_grezza)
    print("Password generata:", password_finale)

    if not lista_caratteri:
        print("Devi inserire almeno un carattere.")
        return
    salvataggioN(nome,key,password_finale,scelta)
####################### # # Criptare con tutti i tipi di carattere # # ###############################
def All():
    scelta = int(input('\nScegli se:\n1 - Personalizza la password\n2 - Casuale con lettere, numeri e caratteri speciali\n0 - Esci\nScelta: '))
    if scelta == 1:
        scelta_completa()
    elif scelta == 2:
        scelta_casuale()
    elif scelta == 0:
        menu()

def scelta_completa():
    nome = input('\nInserisci un nome identificativo: ')
    #   Lista lettere
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = alphabet.upper()
    key = list(alphabet + alphabet2)
    random.shuffle(key)
    #   Lista numeri
    lista_num = list(range(10))
    random.shuffle(lista_num)

    scelta = int(input('\nSegui le istruzioni\n\n1 - Scegli quante lettere usare per la password: '))
    scelta2 = int(input('2 - Scegli quanti numeri usare: '))
    scelta3 = input('3 - Scegli quali caratteri speciali usare: ')
    scelta4 = int(input('4 - Scegli quanti caratteri speciali usare: '))
    scelte_user = f'N. lettere: {scelta}\nN. numeri: {scelta2}\nSymbol usati: {scelta3}\nN. symbol: {scelta4}'
    #Formatting Symbol
    utente_caratteri_senza_spazi = scelta3.replace(" ", "")
    lista_caratteri = list(utente_caratteri_senza_spazi)
    lista_ripetuta_symbol = random.sample(lista_caratteri * (scelta4 // len(lista_caratteri)) + lista_caratteri[:scelta4 % len(lista_caratteri)], scelta4)
    tipologia = 'Personalizzata completa'
    #Formatting num
    lista_ripetuta_num = (lista_num * (scelta2 // len(lista_num))) + lista_num[:scelta2 % len(lista_num)]

    #Formatting let
    lista_ripetuta_let = (key * (scelta // len(key))) + key[:scelta % len(lista_num)]

    password_grezza = lista_ripetuta_num + lista_ripetuta_let + lista_ripetuta_symbol
    random.shuffle(password_grezza)
    password_raffinata = ''.join(map(str, password_grezza)) 
    print(password_raffinata)
    salvataggioN(nome,tipologia,password_raffinata,scelte_user)



def scelta_casuale():
    nome = input('Inserisci un nome identificativo: ')
    scelte_user = ''
    tipo = 31
    tipo2 = 22
    tipo3 = 11
    #   Lista lettere
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = alphabet.upper()
    key = list(alphabet + alphabet2)
    random.shuffle(key)
    #   Lista numeri
    lista_num = list(range(10))
    random.shuffle(lista_num)
    #   Lista caratteri
    lista_symbol = ['!', '@', '#', '$', '%', '^', '&', '*']
    random.shuffle(lista_symbol)
    lista_ripetuta_symbol = (lista_symbol * (tipo3 // len(lista_symbol))) + lista_symbol[:tipo3 % len(lista_symbol)]
    tipologia = 'Personalizzata completa'
    #Formatting num
    lista_ripetuta_num = (lista_num * (tipo2 // len(lista_num))) + lista_num[:tipo2 % len(lista_num)]
    #Formatting let
    lista_ripetuta_let = (key * (tipo // len(key))) + key[:tipo % len(lista_num)]
    
    password_grezza = lista_ripetuta_num + lista_ripetuta_let + lista_ripetuta_symbol
    random.shuffle(password_grezza)
    password_raffinata = ''.join(map(str, password_grezza)) 
    print(password_raffinata)
    salvataggioN(nome,tipologia,password_raffinata,scelte_user)



def menu():
    while True:
        print(f'\n Benvenuto nel programma di criptage\n qui puoi effettuare delle criptazioni\n in vari modi(vedi sotto):\n 1 - Criptare solo lettere.\n 2 - Criptare solo numeri.\n 3 - Criptare con lettere e numeri.\n 4 - Criptare solo con caratteri speciali. \n 5 - Voglio decidere io.\n 0 - Esci')
        scelta = int(input('Inserisci qui la tua scelta: '))
        try:
            if scelta == 1:
                criptage_lettre()
            elif scelta == 2:
                input_num()
            elif scelta == 3:
                criptage_let_num()
            elif scelta == 4:
                criptage_specio()
            elif scelta == 5:
                All()
            elif scelta == 0:
                break
            else:
                print('Inserisci un numero valido!')
                continue
        except:
            print('Errore!')
            continue

menu()