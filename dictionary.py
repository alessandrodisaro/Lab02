class Dictionary:
    def __init__(self, dictionary):
        # self.dictionary = dictionary  # passo il nome del file da usare come dizionario
        self.diz = {}  # creo il dizionario vuoto

    def mappaDizionario(self, dict):
        with open(dict, "r") as file:
            for riga in file:
                parts = riga.split()
                self.diz[parts[0]] = parts[1]
        # print(self.diz)         #per test

    def addWord(self, parolaAliena, parolaItaliana):
        italiano_lower = parolaItaliana.lower()  # li metto entrambi in lower case
        alieno_lower = parolaAliena.lower()

        if italiano_lower.isalpha() == False or alieno_lower.isalpha() == False:
            print("Le parole inserite non possono contenere caratteri diversi dalle lettere")
            return -1
        with open("dictionary.txt", "a") as file:
            file.write(f"{alieno_lower} {italiano_lower}\n")

        return f"La parola {alieno_lower} e' stata inserita, con la tarduzione {italiano_lower}"

    def translate(self, parola):
        traduzione = ""
        word = ""
        if parola.isalpha() == False:
            print("Le parola inserita non puo' contenere caratteri diversi dalle lettere")
            return -1
        else:
            word = parola.lower()  # la rendo lower case


        trad=(self.diz[word])  # cerco la key nella mappa per ottenre la value

        return trad

    def translateWordWildCard(self, parola):
        traduzioni = []
        inizio = ""
        fine = ""
        if parola.count("?") == 1:
            parti = parola.split("?")
            inizio = parti[0]
            fine = parti[1]
            # adesso faccio il replace
            parola_modificata = parola.replace('?', 'Z')
            if parola_modificata.isalpha() == False:
                print("La parola puo' contenere solo un '?' e deve essere composta poi solamente da lettere")
                return traduzioni  # cosi per non far fermare il rpogramma;  se no metti return -1
        # inizio ricerca
        if inizio == "":
            for key in self.diz.keys():
                if fine in key:
                    if len(fine) + 2 == len(
                            key):  # +2 per come legge i caratteri strani che sonon sempre all inizio o alla fine
                        traduzioni.append(self.diz[key])
        elif fine == "":
            for key in self.diz.keys():
                if inizio in key:
                    if len(inizio) + 2 == len(key):
                        traduzioni.append(self.diz[key])
        else:
            for key in self.diz.keys():
                if inizio in key and fine in key:
                    if len(key) == (len(inizio) + len(fine) + 1):
                        traduzioni.append(self.diz[key])
        return traduzioni

    def printAll(self):
        for key, value in self.diz.items():
            print(f"{key}   {value}")


"""
# test
d = Dictionary("dictionary.txt")
d.mappaDizionario()
print(d.diz)
# d.addWord("ASty", "gfAS")
d.mappaDizionario()
trn = d.translate("koira")  # cane
print(trn)
wild = d.translateWordWildCard("tu?li")
print(wild)
"""
