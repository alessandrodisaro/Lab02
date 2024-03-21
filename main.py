import translator
import translator as Translator

t = translator.Translator()
vivo = True
while (vivo):

    t.printMenu()

    print("Seleziona la funzione da utilizzare: ")

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!
    if int(txtIn) < 6 and int(txtIn) > 0:

        if int(txtIn) == 1:
            # esegui l' aggiunta di parola
            agg=input("Aggiungi la parola aliena seguita da uno spazio e la parola italiana")
            t.handleAdd(agg)
            # fai il check se tutto a posto e poi fai i due return diversi in base al caso

        if int(txtIn) == 2:
            # esegui la riverca di una traduzione da parola aliena a italiana
            coppia=input("Scrivi la parola aliena da tradurre")
            t.handleTranslate(coppia)

        if int(txtIn) == 3:
            # esegui la traduzione di una wildcard
            wild=input("Scrivi la parola da cercare con un carattere sconosciuto")
            t.handleWildCard(wild)

        if int(txtIn) == 4:
            # stampa tutto il dizionario
            t.printDictionary()

        if int(txtIn) == 5:
            # esegue l' uscita
            break
    else:
        print("Il valore immesso non e' valido")

    txtIn = input("Se vuoi continuare premi 'y'\n")
    if txtIn != "y":
        vivo = False
