# Tema 53
# Demonstreaza utilizarea clasei si a metodelor
# PF - 31/05/2016

'''
 Creati o clasa pentru prelucrare de texte, la initializare trebuie data calea catre fisier
    Creati o metoda pentru scriere
    Creati o metoda pentru citire fisiere
    Creati o metoda care sa faca split in cuvinte
    Creati o metoda care sa numere cate aparitii are un cuvant dat.
    Utilizati metodele create
''' #

class TextProcessing():

    def __init__(self,path):
        self.path = path

    def writefile(self, chars):
        self.fileW = open(self.path, 'w')
        self.textW = self.fileW.write(chars)
        self.fileW.close()

    def readText(self):
        self.fileR = open(self.path, 'r')
        self.text = self.fileR.read()
        self.fileR.close()
        return self.text

    def readWords(self):
        self.words = self.text.split()
        return self.words

    def countWord(self, word):
        count=0
        for i in self.words:
            if i == word:
                count += 1
        return count

text = TextProcessing('file.txt')
text.writefile('hello mthfkr')
print(text.readText())
print(text.readWords())
print(text.countWord('hello'))