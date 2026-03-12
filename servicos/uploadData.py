import pandas as pd

def carregar_arquivo(caminho):
    try:
        dados = pd.read_csv(caminho, sep=";")
        dados = dados.dropna(how="all")
        return dados
    except FileNotFoundError:
        print('Arquivo não encontrado!')