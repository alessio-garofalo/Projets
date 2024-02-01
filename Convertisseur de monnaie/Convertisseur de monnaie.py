# def converter():
#     while True:
# Installa la libreria forex-python
# pip install forex-python

from forex_python.converter import CurrencyRates
def menuP():
    while True:
        print('\nConverter de Value\n1 - Converti\n2 - Elenco valute\n3 - Storico\n4 - Aggiungi Valute\n5 - Exit')
        scelta = int(input("Scegli: "))
        if scelta == 1:
            menu_convert()
        elif scelta == 2:
            print(f'\nLista Valute\n{Value}')
        elif scelta == 3:
            storico()
        elif scelta == 4:
            menu_addValue()
        elif scelta == 5:
            break

def storico():
    try:
        with open("storic_conv.txt", "r") as storic_conv:
            contenuto = storic_conv.read()
            print(contenuto)
    except FileNotFoundError:
        print("Il file 'storic_conv.txt' non esiste o è vuoto.")
        storic_conv = open("storico_conv.txt", "w")
    
    


def demande(conv):
    domande = input(f"Vuoi continuare a convertire in {conv}?\n y = Continuare a convertire in {conv}\n n = Menu principale\n Scelta: ").lower()
    while True:
        if domande == "y":
            return True
        elif domande == "n":
            return False
        else:
            print('Fai una scelta valida!')



Value = ['EUR', 'USD']
####################################################################################
def menu_addValue():
    valute_disponibili = [
        "IDR" " - Indonesia Rupiah",
        "BGN" " - Bulgaria Lev",
        "ILS" " - Israel Shekel",
        "GBP" " - United Kingdom Pound",
        "DKK" " - Denmark Krone",
        "CAD" " - Canada Dollar",
        "JPY" " - Japan Yen",
        "HUF" " - Hungary Forint",
        "RON" " - Romania New Leu",
        "MYR" " - Malaysia Ringgit",
        "SEK" " - Sweden Krona",
        "SGD" " - Singapore Dollar",
        "HKD" " - Hong Kong Dollar",
        "AUD" " - Australia Dollar",
        "CHF" " - Switzerland Franc",
        "KRW" " - Korea (South) Won",
        "CNY" " - China Yuan Renminbi",
        "TRY" " - Turkey Lira",
        "HRK" " - Croatia Kuna",
        "NZD" " - New Zealand Dollar",
        "THB" " - Thailand Baht",
        "NOK" " - Norway Krone",
        "RUB" " - Russia Ruble",
        "INR" " - India Rupee",
        "MXN" " - Mexico Peso",
        "CZK" " - Czech Republic Koruna",
        "BRL" " - Brazil Real",
        "PLN" " - Poland Zloty",
        "PHP" " - Philippines Peso",
        "ZAR" " - South Africa Rand"
    ]

    valute2_disponibili = [
        "IDR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "MYR",
        "SEK", "SGD", "HKD", "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD",
        "THB", "NOK", "RUB", "INR", "MXN", "CZK", "BRL", "PLN", "PHP", "ZAR"
    ]

    print("Scegli la valuta che vuoi aggiungere: ")
    for valuta in valute_disponibili:
        print(valuta)

    Nvaluta = input("Inserisci la sigla della valuta: ").upper()

    if Nvaluta in valute2_disponibili:
        Value.append(f'{Nvaluta}')
        print(f"Hai aggiunto la valuta {Nvaluta}")
    else:
        print("Valuta non valida. Riprova.")
#################################################################################### Finito\|/
# def convert(scelta1, scelta2):
#     c = CurrencyRates()
#     MoneyToC = float(input(f"\n0 - Exit\nQuanto vuoi convertire? {scelta1}: "))
#     rate = c.get_rate(scelta1,scelta2)
#     if MoneyToC != 0:
#         print(f"1 {scelta1} = {rate} {scelta2}")
#         conversion = c.convert(scelta1, scelta2, MoneyToC)
#         print(f"{MoneyToC} {scelta1} sono equivalenti a {conversion} {scelta2}")
#     else:
#         menu_convert()
    

def menu_convert():
    c = CurrencyRates()

    print('Esempio:\n(Domanda 1): EUR\n(Domanda 2): USD')

    print("Qual'e la valuta di partenza?" + str(Value) + "\n0 - exit")
    scelta1 = (input('Scelta: ')).upper()

    if scelta1 == "0":
        conf = input('Sei sicuro di non continuare?\n(y/n)').lower()
        if conf == "y":
            menuP()
        else:
            menu_convert()
    print("Qual'e la valuta finale?",Value, "\n0 - exit")
    scelta2 = (input('Scelta: ')).upper()
    if scelta1 in Value and scelta2 in Value:
        while scelta1 != scelta2:
            MoneyToC = float(input(f"\n0 - Exit\nQuanto vuoi convertire? {scelta1}: "))
            rate = c.get_rate(scelta1,scelta2)
            if MoneyToC != 0:
                print(f"1 {scelta1} = {rate} {scelta2}")
                conversion = c.convert(scelta1, scelta2, MoneyToC)
                print(f"{MoneyToC} {scelta1} sono equivalenti a {conversion} {scelta2}")
                with open("storic_conv.txt", "a") as storic_conv:
                    storic_conv.write(f"\n{MoneyToC} {scelta1} sono equivalenti a {conversion} {scelta2}")
            else:
                menu_convert()
        
            conv = (f'{scelta1}->{scelta2}')
            if not demande(conv):
                break  # Esci dal loop principale se l'utente ha scelto di non continuare
    else:
        scelta = int(input('Scegli una valuta disponibile!\nOppure puoi aggiungerne una dal menu.\n 1 - Aggiungi valuta adesso.\n 2 - Per tornare indietro.\n 0 - Per uscire\n Scelta: '))

        if scelta == 1 :
            menu_addValue()
        elif scelta == 0:
            menu_convert()

############################################################################Finito


menuP()





    

    