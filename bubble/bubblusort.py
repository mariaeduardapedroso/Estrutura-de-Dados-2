

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
    print(iteracao)
        



v=[1,2,3,6,5,4]
tipo = 1

print(v)
ordenarBubbleSort(v,2)
print(v)