
def ordenarBubbleSort(v,tipo):
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
    tamanhoVetor=tamanhoVetor-1
    print(iteracao)
        



v=[1,4,2,3,5,6]
tipo = 1

print(v)
ordenarBubbleSort(v,2)
print(v)
