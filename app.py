import pandas as pd
import numpy as np
import os

# Importando arquivo CSV
dados_pastas_nomes = pd.read_csv('./csv/folders_names.csv')

# Local das pastas
caminho = 'destino_pastas'

# Verificar se pastas existem
def verificar_existencia_pastas():
    return os.listdir(caminho)

# Funcao que cria as pastas
def criar_pastas():
    if len(verificar_existencia_pastas()) > 0:
        print("Por favor, limpe a pasta 'destino pastas'")
    else:
        for i in dados_pastas_nomes["NameFolder"]:
            os.makedirs(caminho + "/" + str(i))

criar_pastas()