import re
import sys
lista = []

def grep(arquivo, palavra):
    contador = 0
    with open(arquivo,"r") as file:
        for line in file:
            if re.search(palavra, line):
                lista.append(line)
                contador=contador+1
    return contador


if __name__ == '__main__':
    print("main")
    nomeArq = "input1.txt"
    buscaPalavra = "Professor"

    ocorrencias=grep(nomeArq,buscaPalavra)
    print(ocorrencias)
    print(lista)