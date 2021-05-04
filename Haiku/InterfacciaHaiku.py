import tkinter as tk

window = tk.Tk()
window.geometry("600x400")
window.title("Generatore di haiku")
window.resizable(False, False)
window.configure(background="light blue")

first_button = tk.Button(text="premi il bottone")
first_button.grid(row=0, column=0)

window.mainloop()