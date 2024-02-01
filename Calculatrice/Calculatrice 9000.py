def inpUser():
    x = float(input(f'Inserisci il primo numero:   '))
    z = float(input(f'Inserisci il secondo numero: '))
    y = input(f'Inserisci un simbolo:\n(+,-,*,/)    ')
    return x,y,z

def demande():
    domande = input(f"Vuoi continuare a calcolare?(y/n)").lower()
    while True:
        if domande == "y":
            return True
        elif domande == "n":
            return False
        else:
            print('Fai una scelta valida!')

def reg(log):
    with open("calcUser.txt", "a") as logcalc:
        logcalc.write(f"{log}")

def storico():
    try:
        with open("calcUser.txt", "r") as logcalc:
            contenuto = logcalc.read()
            print(contenuto)
    except FileNotFoundError:
        print("Il file 'calcUser.txt' non esiste o è vuoto.")
        logcalc = open("calcUser.txt", "w")

def calculete(x,y,z):
            if y == '+':
                result = x + z
                log = f'{x} {y} {z} = {result}'
                print(log)
                reg(log)
            elif y == '-':
                result = x - z
                log = f'{x} {y} {z} = {result}'
                print(log)
                reg(log)
            elif y == '*':
                result = x * z
                log = f'{x} {y} {z} = {result}'
                print(log)
                reg(log)
            elif y == '/':
                result = x / z
                log = f'{x} {y} {z} = {result}'
                print(log)
                reg(log)
            elif y != '+' or y != '-' or y != '*' or y != '/':
                print('Inserisci un simbolo valido, tra quelli specificati!(+,-,*,/)')
                return
        
def main():
    while True:
        try:
            x, y, z = inpUser()
            calculete(x, y, z)
            if not demande():
                break
        except ValueError:
            print('Inserisci numeri validi!')
            

def menu():
    while True:
        print('\nCalculatrice 9000\nScegli con il numero corretto:\n 1 - Calcolatrice\n 2 - Storico\n 0 - Exit')
        scelta = int(input('Scelta : '))
        if scelta == 1:
            main()
        elif scelta == 2:
            storico()
        elif scelta == 0:
            break
        else:
            print('Scegli un valore corretto!')

menu()
