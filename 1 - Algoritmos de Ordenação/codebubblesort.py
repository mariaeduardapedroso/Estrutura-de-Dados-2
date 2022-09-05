

def ordenarBubbleSort(v,tipoCrescente):
    tamanhoVetor = len(v)
    trocou = True
    iteracao = 0
    while(trocou):
        trocou=False
        for i in range(tamanhoVetor-1):
            iteracao= iteracao+1
            if tipoCrescente:#tipoCrescente
                if v[i]>v[i+1]:
                    v[i],v[i+1]=v[i+1],v[i]
                    trocou=True
            else:#tipoDecrescente
                if v[i]<v[i+1]:
                    v[i],v[i+1]=v[i+1],v[i]
                    trocou=True
        tamanhoVetor=tamanhoVetor-1 #deixa ele fazer menos coisa
    print(iteracao)
        



v=[69, 24, -15, -95, 38, -63, 55, 74, -62, 72, 94, 87, 62, -85, 84]
tipoCrescente = True

print(v)

ordenarBubbleSort(v,tipoCrescente)
print(v)

tipoCrescente = False
ordenarBubbleSort(v,tipoCrescente)
print(v)
