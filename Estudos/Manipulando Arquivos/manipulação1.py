# Mode
# r - Leitura
# a - Append  / Incrementar -> Continua colocando no arquivo que ja existe
#  w - Escrita -> Limpa o arquivo ou até criar um arquivo novo
# x - Criar Arquivo
# r+ - Leitura + Escrita

# Abre o arquivo, e escolhe o modo
arquivo = open("Estudos/teste3.txt", "x")

# Verifica se o arquivo é legível
print(arquivo.readable())

# Lê o arquivo
print(arquivo.read())

# Lê linha por linha do arquivo
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

# Pega todas as linhas do arquivo e transforma em uma lista
lista = arquivo.readlines()
print(lista)
# Lê apenas um resultado
print(lista[3])


# Incrementar coisas no Arquivo
arquivo.write("Python\n")
arquivo.write("C++\n")
arquivo.write("Terraform\n")



# Fecha o Arquivo
arquivo.close()

# Exclui arquivo
import os 
os.remove("Estudos/teste2.txt")

# Verificar se o arquivo existe
if os.path.exists("Estudos/teste3.txt"):
    os.remove("Estudos/teste3.txt")
else:
    print ("Arquivo não existe")

# Exclui pasta
os.rmdir("Estudos/nova pasta")