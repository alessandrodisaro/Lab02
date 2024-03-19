from dictionary import Dictionary


class Translator:

    def __init__(self):
        dt = Dictionary("dictionary.txt")  # caso di default
        pass

    def printMenu(self):
        print("1. Aggiungi una parola\n")  # 1. Aggiungi nuova parola
        print("2. Cerca una tarduzione\n")  # 2. Cerca una traduzione
        print("3. Cerca una wildcard\n")  # 3. Cerca con wildcard
        print("4. Stampa tutto il dizionario\n")  # 4. Stampa tutto il dizionario
        print("5. Exit")  # 5. Exit
        pass

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        dt = Dictionary(dict)  # dt=dictionary_translator    PERCEH POI DT NON RIMANE COME VARIABILE GLOBALE IL "DT"
        pass

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        if str(entry).count(" ") == 1:
                      #self.addWord(entry)  # metti a posto
        else:
            parts=[]
            parts=entry.split(" ")
            for x in range(len(parts)-1):
                addWord(parts[0],parts[x+1])   # aggiungo sempre la parola aliena e poi scorro le italianae creando nuove coppie



    def handleTranslate(self, query):
        # query is a string <parola_aliena>

        pass

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        pass
