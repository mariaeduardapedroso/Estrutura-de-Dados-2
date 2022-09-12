
def  magicaMerge(v,inicio,meio,fim):
    vaux=[]
    p1=inicio
    p2=meio+1
    while p1<=meio and p2<=fim:
        if v[p1]<v[p2]:
            vaux.append(v[p1])
            p1= p1+1
        else:
            vaux.append(v[p2])
            p2= p2+1
    if p1 == meio:
        vaux.append(v[p2:fim])
    else:
        vaux.append(v[p1:meio])
    v=vaux
        


def ordenarMergeSort(v,inicio,fim):
    if inicio<fim:
        meio = (inicio+fim)/2
        ordenarMergeSort(v,inicio,meio)
        ordenarMergeSort(v,meio+1,fim)
        magicaMerge(v,inicio,meio,fim)




v=[69, 24, -15, -95, 38, -63, 55, 74, -62, 72, 94, 87, 62, -85, 84]
tipoCrescente = True
inicio = 0
fim = len(v)-1
print(v)

ordenarMergeSort(v,inicio,fim)
print(v)

# tipoCrescente = False
# ordenarMergeSort(v,inicio,fim)
# print(v)