import pandas as pd
import numpy as np
import os
import tkinter as tk
from tkinter.font import Font
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

# Local das pastas
caminho = 'destino_pastas'

# Verificar se pastas existem
def verificar_existencia_pastas():
    if(os.path.exists('./destino_pastas')):
        return os.listdir(caminho)
    else:
        os.makedirs('./destino_pastas')
        return os.listdir(caminho)

# Funcao que cria as pastas
def criar_pastas(nomes_pastas):
    for i in nomes_pastas["NameFolder"]:
        os.makedirs(caminho + "/" + str(i))

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3, rowspan=3)

#Logo
logo = Image.open('./imagens/logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructitons
instructons = tk.Label(root, text="Select a PDF on your computer to extract all its text", font="Raleway")
instructons.grid(columnspan=3, column=0, row=1)

def open_file():
    browser_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Chosse a file", filetype=[("CSV Files", "*.csv")])
    if file:
        dados_pastas_nomes = pd.read_csv(file)
        if len(verificar_existencia_pastas()) > 0:
            mensagem = "Por favor, limpe a pasta 'destino pastas'"
        else:
            criar_pastas(dados_pastas_nomes)
            mensagem = "Pastas criadas com sucesso"
        
        #text box
        instructonsFile_text.set(mensagem)

#browser_button
browser_text = tk.StringVar()
browser_btn = tk.Button(root, textvariable=browser_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browser_text.set("Browser")
browser_btn.grid(column=1, row=2)

#browser_button
instructonsFile_text = tk.StringVar()
instructonsFile = tk.Label(root, textvariable=instructonsFile_text, font="Raleway")
instructonsFile_text.set("")
instructonsFile.grid(column=1, row=3)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()