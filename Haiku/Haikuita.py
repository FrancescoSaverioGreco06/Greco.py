#software realizzato da Mariano e di Gennaro, interfacci realizzata da Greco ed Iannuzzi.
from csv import reader
import random
import tkinter as tk

def software():
    # Estrattore casuale
    def estrazione(lista): 
        p=random.randint(0,len(lista)-1) 
        x=lista[p] 
        lista.remove(x) 
        return x 

    #Estrazione casuale del csv
    lista_csv = ['versi.csv']
    a = estrazione(lista_csv)

    #Apertura e lettura del file csv
    with open( a , 'r') as csv_file:
        csv_reader = reader(csv_file)
        list_of_column = list(csv_reader)
    nuova_lista_1 = []
    nuova_lista_2 = []
    nuova_lista_3 = []
    for i in list_of_column: 
        nuova_lista_1.append(i[0])
        nuova_lista_2.append(i[1])
        nuova_lista_3.append(i[2])

    #Estrazione elementi da csv
    x=estrazione(nuova_lista_1) 
    y=estrazione(nuova_lista_2)
    z=estrazione(nuova_lista_3)
    lista = [x , y , z]
    text_output = tk.Label(window, text=lista)
    text_output.grid(row=2, column=0)
  



window = tk.Tk()
window.geometry("700x500")
window.title("Generatore di haiku")
window.resizable(False, False)
window.configure(background="light grey")
text = "Questo programma serve a generare casualmente Haiku, partendo da un insieme di versi. I versi sono divisi in tre categorie." 
text_output_2= tk.Label(window, text=text)
text_output_2.grid(row=0, column=0)
first_button = tk.Button(text="premi il bottone", width=100, command = software)
first_button.grid(row=1, column=0)
window.mainloop()