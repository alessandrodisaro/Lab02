import translator as Translator

t = Translator()
vivo=True
while (vivo):

    t.printMenu()

    print("Seleziona la funzione da utilizzare: ")

    t.loadDictionary("filename.txt")

    txtIn = input()

    # Add input control here!
    if int(txtIn)<6 and int(txtIn)>0:

        if int(txtIn) == 1:
            # esegui l' aggiunta di parola
            print("Aggiungi la parola aliena seguita da uno spazio e la parola italiana")
            txtIn = input()
            t.handleAdd()
            # fai il check se tutto a posto e poi fai i due return diversi in baase ala caso

            pass
        if int(txtIn) == 2:
            # esegui la riverca di una traduzione da parola aliena a italiana

            pass
        if int(txtIn) == 3:
            # esegui la traduzione di una wildcard

            pass
        if int(txtIn) == 4:
            # stampa tutto il dizionario

            pass
        if int(txtIn) == 5:
            # esegue l' uscita

            break
    else:
        print("Il valore immesso non e' valido")

    txtIn=input("Se vuoi continuare premi 'y'\n")
    if txtIn!="y":
        vivo=False