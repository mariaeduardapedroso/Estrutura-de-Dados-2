from operator import concat
from pickle import NONE
import shutil
import os
import re
import sys
from unittest import result
#########################################################################
#                              INSERTION SORT                           #
#########################################################################
def ordenarInsertionSort(v):
    iteracao=0
    #ir rodando o vetor para a esquerda e conseguir voltar comparando
    for posicao in range(1,len(v)):
        auxiliar = v[posicao]
        posicaocomparacao = posicao-1
        #parte para comparar e ir dando shift e voltando o vetor
        while posicaocomparacao >= 0 and auxiliar < v[posicaocomparacao]:
            v[posicaocomparacao+1] = v[posicaocomparacao]
            posicaocomparacao = posicaocomparacao - 1
            iteracao=iteracao+1
        v[posicaocomparacao+1]=auxiliar
    return iteracao
#########################################################################

#########################################################################
#                         MERGE SORT                                    #
#########################################################################
def ordenarmergeSort(vetor):
    iteracao=0

    if len(vetor) > 1:
    
        Meio = len(vetor)//2
        P1 = vetor[:Meio] 
        P2 = vetor[Meio:]

        ordenarmergeSort(P1)
        ordenarmergeSort(P2)

        i = j = k = 0

        while i < len(P1) and j < len(P2): 
            if P1[i] < P2[j]:              
                vetor[k] = P1[i]        
                i += 1    
                iteracao += 1             
            else:
                vetor[k] = P2[j]        
                j += 1    
                iteracao += 1             
            k += 1                      
                                        
        while i < len(P1):
            vetor[k] = P1[i]
            i += 1
            k += 1

        while j < len(P2):
            vetor[k] = P2[j]
            j += 1
            k += 1
    return iteracao
#########################################################################

#########################################################################
#                              QUICK SORT                               #
#########################################################################
def Particiona(V, Inicio, Fim):
    Esq = Inicio
    Dir = Fim
    Pivo = V[Inicio]
    while Esq < Dir:
        while V[Esq] <= Pivo and Esq <= Fim and Esq < len(V)-1:
            Esq= Esq+1
        while V[Dir] > Pivo and Dir >= Inicio:
            Dir=Dir-1
        if Esq < Dir:
            V[Esq],V[Dir]=V[Dir],V[Esq]
    V[Dir],V[Inicio]=V[Inicio],V[Dir]
    return Dir

def ordenarQuickSort (V, Inicio, Fim):
    if Inicio < Fim:
        Pivo = Particiona(V, Inicio, Fim)
        ordenarQuickSort(V, Inicio, Pivo-1)
        ordenarQuickSort(V, Pivo+1, Fim)
#########################################################################

#########################################################################
#                             HEAP SORT                                 #
#########################################################################
def maxHeapify(array, i, heapSize):
    left  = 2*i+1
    right = 2*i+2
    largest = i

    if(left <= (heapSize-1)) and (array[left] > array[i]):
        largest = left
    if (right <= (heapSize-1)) and (array[right] > array[largest]):
        largest = right

    if i != largest:
        array[i], array[largest] = array[largest], array[i]
        maxHeapify(array, largest, heapSize-1)

def buildMaxHeap(array, heapSize): #ok
    idxs = range(int(len(array)/2), -1, -1)
    for index in idxs:
        maxHeapify(array, index, heapSize)

def ordenarheapSort(array):
    heapSize = len(array)
    buildMaxHeap(array, heapSize)
    idxs = range(len(array)-1, 0, -1)
    for index in idxs:
        array[0], array[index] = array[index], array[0]
        heapSize = heapSize - 1
        maxHeapify(array, 0, heapSize)
#########################################################################

def ordenarArray(array,modo,tipo):
    match tipo:
        case 'Q':
            ordenarQuickSort(array,0,len(array)-1)
        case 'H':
            ordenarheapSort(array)
        case 'M':
            ordenarmergeSort(array)
        case 'I':
            ordenarInsertionSort(array)
    if modo == 'C':
        return array
    else:
        return array[::-1]

def captarArrayChaves(dados):
    arraychaves = []
    for i in range(1,len(dados)):
        splitdados = dados[i].split('|')
        arraychaves.append(str(splitdados[0]) + '|' + str(i))
    return arraychaves

def gerarArquivoOrdenado(array,file,dados):
    with open(file, "w") as dado:
        dado.write(dados[0])

        for i in range(len(array)):
            linha = array[i].split('|')
            linha = linha[1]
            dado.write(dados[int(linha)])

def invalidarArquivo(file):
    with open(file, "w") as dado:
            dado.write("Arquivo Inválido!")

if __name__ == '__main__':
    if len(sys.argv) == 3: 
        with open(sys.argv[1], "r") as dado:
            dados=dado.readlines()

        if len(dados)>1:    
            dados[len(dados)-1] = dados[len(dados)-1] + '\n'
            arraychave = captarArrayChaves(dados)
            
            metadados = dados[0].split(' ')
            metododeordenacao = metadados[3].split('SORT=')
            metododeordenacao = metododeordenacao[1]

            tipodeordenacao = metadados[4].split('ORDER=')
            tipodeordenacao = tipodeordenacao[1][0]

            if (metododeordenacao == 'Q' or metododeordenacao == 'H' or metododeordenacao == 'M' or metododeordenacao == 'I') and (tipodeordenacao == 'C' or tipodeordenacao == 'D'):
                arrayordenado = ordenarArray(arraychave,tipodeordenacao,metododeordenacao)
                gerarArquivoOrdenado(arrayordenado,sys.argv[2],dados)
            else:
                invalidarArquivo(sys.argv[2])
        else:
            invalidarArquivo(sys.argv[2])
    else:
        print("ERRO PARAMETROS")
