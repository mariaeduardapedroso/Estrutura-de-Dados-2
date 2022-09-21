def criaHeap(v):
    tamanho=len(v)
    for i in range(len(v)/2):
        heapifyMaximo(v,i)

def heapifyMaximo(v,indice):
    filhoesquerda = 2*indice
    filhodireita = 2*indice+1
    maior=indice
    if filhoesquerda<=(indice-1) and v[filhoesquerda]>v[indice]:
        maior = filhoesquerda
    if filhodireita<=(indice-1) and v[filhodireita]>v[maior]:
        maior = filhodireita
    if maior!=indice:
        v[indice],v[maior]=v[maior],v[indice]
        heapifyMaximo(v,maior,indice-1)
        
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
    idxs = range(len(array)/2, -1, -1)
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