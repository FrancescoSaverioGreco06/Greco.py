'''
Python3
Programmazione ad oggetti
'''

class vini:


    #Metodo costruttore
    def __init__(self,proprietario, marca, annata, tipologia, alcol, vitigni):

        # Attributi di Istanza
        self.proprietario = proprietario
        self.marca = marca
        self.annata = annata
        self.tipologia = tipologia
        self.alcol = alcol
        self.vitigni = vitigni
        
        vini.parcoVini +=1

    #Metodo di tipo Get
    def scheda(self):
        return f'\nScheda "{self.proprietario}"\n Marca: {self.marca}\n annata: {self.annata}\n tipologia: {self.tipologia}\n alcol: {self.alcol}\n vitigni: {self.vitigni}' 
    
giovanni = vini("giovanni","moet & chandon",2015 ,"Champagne AOC", "12%" , "pinot noir, meunier, chardonnay")

marco = vini("marco","Marche Rosso IGT",2017 , "Rosso", "14%", "bordò")

print("Il tipo di variabile costruita è:")
print(giovanni)
print(marco)

print("\nLa singola scheda è:")
print (giovanni.scheda())
print (marco.scheda())
print("\nauto totali: ",vini.parcoVini)

print("\n\naltro metodo per visualizzare le informazioni (__dict__):")

print(giovanni.__dict__)
print(marco.__dict__)