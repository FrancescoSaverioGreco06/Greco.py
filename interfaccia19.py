
from tkinter import *
from tkinter import filedialog 
import matplotlib as mpl 
mpl.use('tkagg')
import string
import numpy as np
import matplotlib.pyplot as plt

def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File ", 
                                          filetypes = (("Text files", 
                                                        ".txt"), 
                                                       ("all files", 
                                                        "."))) 
       
   
    label_file_explorer.configure(text="File aperto: "+filename)


def grafico () :  
    f = open("dati.txt", 'r')
    coordX = []
    coordY = []
    for riga in f:
        valori = str(f.readline())  
        Nval = len(valori)          
        valori = valori.strip('\n')
        valori = valori.split(',')  
        valori = list(valori)       
        print(valori)
        coordX.append(int(valori[0]))
        coordY.append(int(valori[1])) 

    f.close()  
    print ("X: ",coordX)
    print ("Y: ",coordY)

    coordX.sort()
    coordY.sort()

    print("liste ordinate:") 
    print ("X: ",coordX)
    print ("Y: ",coordY)

    print(type(coordX))
    print(type(coordY))

    plt.scatter(coordX,coordY)
    plt.ylabel('some numbers')
    plt.show()

window = Tk() 

button_explore = Button(window,  
                        text = "Inserisci file", 
                        command = browseFiles)



button_genera_grafico = Button(window,  
                        text = "Genera grafico", 
                        command = grafico)

label_file_explorer = Label(window,  
                            text = "Insrisci un file e genera un grafico", 
                            width = 100, height = 4,  
                            fg = "black")

label_file_explorer.grid(column = 1, row = 2)

button_explore.grid(column = 1, row = 1)

button_genera_grafico.grid(column = 1, row = 3)
   
window.mainloop() 

root.geometry('1000x1000')

