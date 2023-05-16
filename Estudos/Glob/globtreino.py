import numpy as np
import pandas as pd
import glob as gl

lista_arquivo = []
# Para cada arquivo que ele achar dentro desse endereço, usa o append para colocar dentro da variavel 
for arquivo in gl.glob(r"C:\Users\lucka\OneDrive\Documentos\\lalala\*xls"):
    lista_arquivo.append(arquivo)

# Para cada arquivo na lista de arquivo, ler o arquivo excel, o nome, de qual coluna ele começa a ler e adicionar na variavel
tabelas = []
for arquivo in lista_arquivo:
    tabelas.append(pd.read_excel(arquivo, index_col=0))