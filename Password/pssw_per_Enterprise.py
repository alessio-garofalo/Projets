import random
import hashlib
import re
import json
############CRIPTAGE SHA-256######################################


def salvataggio(nome, tipologia, chiave, password):
    try:
        # Salva la chiave casuale in un file utilizzando pickle
        with open('Python/python 3SEMAIN/Password/password.json', 'a') as file:
            json.dump({
                'Nome identificativo': nome,
                'Password': password,
                'Tipologia': tipologia,
                'input_utente': chiave
            }, file, indent=4)
            print("Chiave casuale generata e salvata con successo.")
    except Exception as e:
        print(f"Errore durante il salvataggio della chiave casuale: {str(e)}")

def verifica_input(password):
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'
    # Verifica se la stringa rispetta l'espressione regolare
    if re.match(regex, password):
        print("La stringa rispetta le regole.")
        return True
    else:
        print("La stringa non rispetta le regole.")
        return False
        
def verifica_password(password_inserita, hash_salvato):
    # Calcola l'hash della password inserita
    password_hash = hash_password(password_inserita)

    # Confronta l'hash calcolato con l'hash salvato
    if password_hash == hash_salvato:
        return True
    else:
        return False

def hash_password(password):
    # Crea un oggetto hash SHA-256
    sha256 = hashlib.sha256()

    # Aggiungi la password alla stringa hash
    sha256.update(password.encode('utf-8'))

    # Restituisci la rappresentazione esadecimale dell'hash
    return sha256.hexdigest()
def menu():
    # Input utente
    nome = input('Inserisci il tuo nome: ')
    tipologia = 'SHA-256'
    pssw = input("\n    Segui le istruzioni:\n\nLa password deve contenere almeno 8 caratteri.\n\n      Una lettera maiuscola e minuscola.\n\n  Almeno un numero ed un carattere speciale \npresente nell'elenco (!, @, #, $, %, ^, &, *).   \n\nInserisci la password:  ")
    
    if verifica_input(pssw):
        hex_dig = hash_password(pssw)
        salvataggio(nome, tipologia, pssw, hex_dig)

        #convertire la frase in bytes
        pssw_encode = pssw.encode('utf-8')
        # Creazione di un oggetto hash SHA-256
        hash_object = hashlib.sha256(pssw_encode)
        # Ottenere l'hash come stringa esadecimale  
        hex_dig = hash_object.hexdigest() 
        print(hex_dig)

menu()