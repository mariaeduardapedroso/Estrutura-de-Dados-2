
def ordenarSelectionSort(v,tipoCrescente):
    tamanhoVetor = len(v)
    for posicaodaiteracao in range(0,tamanhoVetor-1):
        posicao = posicaodaiteracao
        for posicaobusca in range(posicaodaiteracao+1,tamanhoVetor):
            if tipoCrescente:   
                if v[posicao]>v[posicaobusca]:
                    posicao=posicaobusca
            else:
                if v[posicao]<v[posicaobusca]:
                    posicao=posicaobusca        
        if posicaodaiteracao != posicao:
           v[posicaodaiteracao], v[posicao] = v[posicao],v[posicaodaiteracao]




v=[69, 24, -15, -95, 38, -63, 55, 74, -62, 72, 94, 87, 62, -85, 84]
tipoCrescente = True

print(v)

ordenarSelectionSort(v,tipoCrescente)
print(v)

tipoCrescente = False
ordenarSelectionSort(v,tipoCrescente)
print(v)