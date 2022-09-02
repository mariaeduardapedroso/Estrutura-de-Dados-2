def ordenarInsertionSort(v,tipoCrescente):
    #ir rodando o vetor para a esquerda e conseguir voltar comparando
    for posicao in range(1,len(v)):
        auxiliar = v[posicao]
        posicaocomparacao = posicao-1
        if tipoCrescente:
            #parte para comparar e ir dando shift e voltando o vetor
            while posicaocomparacao >= 0 and auxiliar < v[posicaocomparacao]:
                v[posicaocomparacao+1] = v[posicaocomparacao]
                posicaocomparacao = posicaocomparacao - 1
        else:
            #parte para comparar e ir dando shift e voltando o vetor
            while posicaocomparacao >= 0 and auxiliar > v[posicaocomparacao]:
                v[posicaocomparacao+1] = v[posicaocomparacao]
                posicaocomparacao = posicaocomparacao - 1
        #trocar a variavel do indice que comecamos para depois dos shifts
        v[posicaocomparacao+1]=auxiliar




v=[69, 24, -15, -95, 38, -63, 55, 74, -62, 72, 94, 87, 62, -85, 84]
tipoCrescente = True

print(v)

ordenarInsertionSort(v,tipoCrescente)
print(v)

tipoCrescente = False
ordenarInsertionSort(v,tipoCrescente)
print(v)