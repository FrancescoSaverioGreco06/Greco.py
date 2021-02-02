# mi ha aiutato RAFFAELE MARIANO 

from tkinter import *
from tkinter import filedialog 
import tkinter as tk
from PIL import ImageTk, Image 
import string
import numpy as np
import matplotlib.pyplot as plt

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
    plt.savefig("grafico.png", dpi=100, facecolor = "#f1f1f1")
    img = ImageTk.PhotoImage(Image.open("grafico.png")) 
    panel = tk.Label(window, image = img) 
    panel.pack(side = "bottom", expand = "yes") 

window = tk.Tk() 

text_box = tk.Entry(window, text="")
text_box.pack()

button_genera_grafico = tk.Button(window, text = "Genera grafico", width = 100, height = 2, command = grafico)
button_genera_grafico.pack()
window.mainloop()