#software realizzato da Mariano e di Gennaro, interfacci realizzata da Greco ed Iannuzzi.
from csv import reader
import random
import tkinter as tk

window = tk.Tk()
window.geometry("700x500")
window.title("Generatore di haiku")
window.resizable(False, False)
window.configure(background="light grey")


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
    text_output = tk.Label(window, text=x, fg="dark blue", font=("Times New Roman",20 ))
    text_output.grid(row=1, column=1)
    text_output_2 = tk.Label(window, text=y, fg="dark blue", font=("Times New Roman",20 ))
    text_output_2.grid(row=2, column=1)
    text_output_3 = tk.Label(window, text=z, fg="dark blue", font=("Times New Roman",20 ))
    text_output_3.grid(row=3, column=1)
    text_1=tk.Label(window, text="1° VERSO", fg="black", font=("Times New Roman",18 ))
    text_1.grid(row=1, column=0)
    text_2=tk.Label(window, text="2° VERSO", fg="black", font=("Times New Roman",18 ))
    text_2.grid(row=2, column=0)
    text_3=tk.Label(window, text="3° VERSO", fg="black", font=("Times New Roman",18 ))
    text_3.grid(row=3, column=0)
    text_4=tk.Label(window, text="INIZIO", fg="black", font=("Times New Roman",18 ))
    text_4.grid(row=1, column=5)
    text_5=tk.Label(window, text="AZIONE", fg="black", font=("Times New Roman",18 ))
    text_5.grid(row=2, column=5)
    text_6=tk.Label(window, text="CONCLUSIONE", fg="black", font=("Times New Roman",18 ))
    text_6.grid(row=3, column=5)




first_button = tk.Button(text="PREMI IL BOTTONE", command = software, font=20, width=20)

first_button.grid(row=0, column=0)

window.mainloop()