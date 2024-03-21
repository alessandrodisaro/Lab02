from dictionary import Dictionary


class Translator:

    def __init__(self):
        self.dt = Dictionary("dictionary.txt")  # caso di default


    def printMenu(self):
        print("1. Aggiungi una parola\n")  # 1. Aggiungi nuova parola
        print("2. Cerca una tarduzione\n")  # 2. Cerca una traduzione
        print("3. Cerca una wildcard\n")  # 3. Cerca con wildcard
        print("4. Stampa tutto il dizionario\n")  # 4. Stampa tutto il dizionario
        print("5. Exit")  # 5. Exit


    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        self.dt.mappaDizionario(dict)


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        if str(entry).count(" ") == 1:
            parts=[]
            parts=entry.split()
            self.dt.addWord(parts[0],parts[1])
        else:
            parts=[]
            parts=entry.split(" ")
            for x in range(len(parts)-1):
                self.dt.addWord(parts[0],parts[x+1])   # aggiungo sempre la parola aliena e poi scorro le italianae creando nuove coppie



    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        trad=self.dt.translate(query)
        print(trad)


    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        possibili_traduzioni=[]
        possibili_traduzioni=self.dt.translateWordWildCard(query)
        for parola in possibili_traduzioni:
            print(parola)

    def printDictionary(self):
        self.dt.printAll()
