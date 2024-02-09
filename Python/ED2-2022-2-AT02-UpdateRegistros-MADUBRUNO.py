from operator import concat
from pickle import NONE
import shutil
import os
import re
import sys
from unittest import result

def adicionaRegistro(arq, p, registro):
    with open(arq,"r+") as arquivo:
        resposta = arquivo.readlines()

    metadadosplit = resposta[0].split("top=")
    toposplit = metadadosplit[len(metadadosplit)-1].split("\n")
    topo = toposplit[0]
    linhaRegistro = procuraRegistro(resposta,id)
    if topo =='-1':
        with open(arq,"a") as arquivo:
            arquivo.write(registro)
    else:
        resposta[0] = ""
        for i in range(len(metadadosplit)-1):
            resposta[0]=resposta[0]+metadadosplit[i]
        novotopo = resposta[int(topo)+1][1:2]
        resposta[0] = resposta[0] + "top=" + str(novotopo) + "\n"
        resposta[int(topo)+1] = registro
        with open(arq,"w") as arquivo:
            for i in range(len(resposta)):
                arquivo.write(resposta[i])
            
def procuraRegistro(linhas,codigo):
    for i in range(1,len(linhas)):
        if(linhas[i][0] != '*'):
            codlinha = linhas[i][0:3]
            dados = re.search(codlinha, str(codigo))
            if dados != None:
                return i-1
    return -1

def removeRegistro(arq, id):
    with open(arq,"r+") as arquivo:
        resposta = arquivo.readlines()
    metadadosplit = resposta[0].split("top=")
    toposplit = metadadosplit[len(metadadosplit)-1].split("\n")
    topo = toposplit[0]
    linhaRegistro = procuraRegistro(resposta,id)
    if linhaRegistro != -1:
        if topo == '-1':
                resposta[linhaRegistro+1]="*" + topo +resposta[linhaRegistro+1][3:]
        else:
            resposta[linhaRegistro+1]="*" + topo + "|" +resposta[linhaRegistro+1][3:]

        resposta[0] = ""
        for i in range(len(metadadosplit)-1):
            resposta[0]=resposta[0]+metadadosplit[i]
        resposta[0] = resposta[0] + "top=" + str(linhaRegistro) + "\n"
        with open(arq,"w") as arquivo:
            for i in range(len(resposta)):
                arquivo.write(resposta[i])

def storageCompaction(arq):
    arquivo=open(arq,"r+")
    arquivotemp = open("temp.txt","w+")
    resposta = arquivo.readlines()

    metadadosplit = resposta[0].split("top=")
    resposta[0] = ""
    for i in range(len(metadadosplit)-1):
        resposta[0]=resposta[0]+metadadosplit[i]
    novotopo = "-1"
    resposta[0] = resposta[0] + "top=" + str(novotopo) + "\n"
    for i in range(len(resposta)):
        if(resposta[i][0] != '*'):
            arquivotemp.write(resposta[i])
    arquivo.close()
    arquivotemp.close()
    shutil.copyfile("temp.txt",arq)

    if os.path.exists("temp.txt"):
        os.remove("temp.txt")
    else:
        print("Erro no arquivo temporario")

def arrumarDados(stringDado):
    dados = stringDado.split(",")
    while len(dados[1]) < 30:
        dados[1] = dados[1] + " "
    dados[5] = dados[5][0:len(dados[5])-1]
    while len(dados[4]) < 30:
        dados[4] = dados[4] + " "
    dado = stringDado[2:5] + "|" + "|".join(dados[1:len(dados)]) + "|\n"
    return dado

if __name__ == '__main__':
    if len(sys.argv) == 5: 
        arquivoInput = open(sys.argv[1],"r+")
        arquivotemp = open(sys.argv[3],"w+")
        dadosarqinput = arquivoInput.readlines()
        for i in range(len(dadosarqinput)):
            arquivotemp.write(dadosarqinput[i])
        arquivoInput.close()
        arquivotemp.close()

        with open(sys.argv[2], "r") as operacao:
            operacoes=operacao.readlines()

        for i in range(len(operacoes)):
            if operacoes[i][0]=='i':
                codigo = operacoes[i][2:5]
                dado = arrumarDados(operacoes[i])
                adicionaRegistro(str(sys.argv[3]),codigo,dado)

            if operacoes[i][0]=='d':
                codigo = operacoes[i][2:5]
                removeRegistro(str(sys.argv[3]),codigo)

        arquivotemp = open(sys.argv[3],"r")
        arquivosaida = open(sys.argv[4],"w+")
        dadosarqtemp = arquivotemp.readlines()
        for i in range(len(dadosarqtemp)):
            arquivosaida.write(dadosarqtemp[i])
        arquivosaida.close()
        arquivotemp.close()

        storageCompaction(sys.argv[4])
    else:
        print("ERRO")