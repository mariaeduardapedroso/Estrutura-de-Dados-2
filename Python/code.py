import random
import time
import sys
from unittest import result
####################################################################
#                            BUBBLE   SORT                         #
####################################################################
def ordenarBubbleSort(v):
    tamanhoVetor = len(v)
    trocou = True
    iteracao = 0
    while(trocou):
        trocou=False
        for i in range(tamanhoVetor-1):
            iteracao= iteracao+1
            if v[i]>v[i+1]:
                 v[i],v[i+1]=v[i+1],v[i]
            trocou=True
        tamanhoVetor=tamanhoVetor-1 #deixa ele fazer menos coisa
    return iteracao
#########################################################################


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
#                         SELECTION SORT                                #
#########################################################################
def ordenarSelectionSort(v):
    tamanhoVetor = len(v)
    iteracao = 0
    for posicaodaiteracao in range(0,tamanhoVetor-1):
        posicao = posicaodaiteracao
        for posicaobusca in range(posicaodaiteracao+1,tamanhoVetor):
            iteracao = iteracao + 1
            if v[posicao]>v[posicaobusca]:
                posicao=posicaobusca       
        if posicaodaiteracao != posicao:
           v[posicaodaiteracao], v[posicao] = v[posicao],v[posicaodaiteracao]
    return iteracao
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

def heapSort(array):
    heapSize = len(array)
    buildMaxHeap(array, heapSize)
    idxs = range(len(array)-1, 0, -1)
    for index in idxs:
        array[0], array[index] = array[index], array[0]
        heapSize = heapSize - 1
        maxHeapify(array, 0, heapSize)
#########################################################################

#########################################################################
#                              CRIA VETORES                             #
#########################################################################
def criaVetores(vselect,vinsert,vbubble,vmerge,vquick,vheap,tipo,N):
    if tipo == 'c':
            for i in range(0,N):
                vinsert.append(i+1)
                vselect.append(i+1)
                vbubble.append(i+1)
                vmerge.append(i+1)
                vquick.append(i+1)
                vheap.append(i+1)
    if tipo == 'd':
        for i in range(0,N):
            vinsert.append(N-i)
            vselect.append(N-i)
            vbubble.append(N-i)
            vmerge.append(N-i)
            vquick.append(N-i)
            vheap.append(N-i)
    if tipo == 'r':
        for i in range(0,N):
            valor = random.randint(0,32000)
            vinsert.append(valor)            
            vselect.append(valor)
            vbubble.append(valor)
            vmerge.append(valor)
            vquick.append(valor)
            vheap.append(valor)
#########################################################################
#                                  MAIN                                 #
#########################################################################

if len(sys.argv) == 3:
    #abrindo o arquivo e lendo o número  para o tamanho do vetor
    entrada = open(sys.argv[1], "r")
    saida = open(sys.argv[2],"w")
    resposta = entrada.readlines()

    if len(resposta)==1:
        saida.write("Arquivo vazio!")
    elif len(resposta)==2:
        tipo = resposta[1]
        N = int(resposta[0])
        vselect=[]
        vinsert=[]
        vbubble=[]
        vmerge=[]
        vquick=[]
        vheap=[]

        criaVetores(vselect,vinsert,vbubble,vmerge,vquick,vheap,tipo,N)
        
        inicioTempo = time.time()
        comparacoes = ordenarInsertionSort(vinsert)
        fimTempo = time.time()
        saida.write("InsetionSort: " + str(vinsert) + ", " + str(comparacoes) + " comp, " + str((fimTempo-inicioTempo)*1000) + " ms\n")


        inicioTempo = time.time()
        comparacoes = ordenarSelectionSort(vselect)
        fimTempo = time.time()
        saida.write("SelectionSort: " + str(vselect) + ", " + str(comparacoes) + " comp, " + str((fimTempo-inicioTempo)*1000) + " ms\n")

        inicioTempo = time.time()
        comparacoes = ordenarBubbleSort(vbubble)
        fimTempo = time.time()
        saida.write("BubbleSort: "  + str(vbubble) + ", " + str(comparacoes) + " comp, " + str((fimTempo-inicioTempo)*1000) + " ms\n")

        inicioTempo = time.time()
        comparacoes = ordenarmergeSort(vmerge)
        fimTempo = time.time()
        saida.write("MergeSort: " + str(vmerge) + ", " + str(comparacoes) + " comp, " + str((fimTempo-inicioTempo)*1000) + " ms\n")

        inicioTempo = time.time()
        comparacoes = ordenarQuickSort(vquick,0,N-1)
        fimTempo = time.time()
        saida.write("QuickSort: "+ str(vquick) + ", " + str(comparacoes) + " comp, " + str((fimTempo-inicioTempo)*1000) + " ms\n")

        inicioTempo = time.time()
        comparacoes = heapSort(vheap)
        fimTempo = time.time()
        saida.write("HeapSort: "+ str(vheap) + ", " + str(comparacoes) + " comp, " + str((fimTempo-inicioTempo)*1000) + " ms\n")
    else:
        saida.write("Arquivo Inválido!")
    entrada.close()
    saida.close()