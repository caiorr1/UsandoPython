# Mode
# r - Leitura
# a - Append  / Incrementar
#  w - Escrita
# x - Criar Arquivo
# r+ - Leitura + Escrita

# Abre o arquivo, e escolhe o modo
arquivo = open("Estudos/teste.txt", "a")

# Verifica se o arquivo é legível
#print(arquivo.readable())

# Lê o arquivo
#print(arquivo.read())

# Lê linha por linha do arquivo
#print(arquivo.readline())
#print(arquivo.readline())
#print(arquivo.readline())

# Pega todas as linhas do arquivo e transforma em uma lista
# lista = arquivo.readlines()
# print(lista)
# Lê apenas um resultado
# print(lista[3])


# Incrementar coisas no Arquivo
arquivo.write("\nSQL")


# Fecha o Arquivo
arquivo.close()