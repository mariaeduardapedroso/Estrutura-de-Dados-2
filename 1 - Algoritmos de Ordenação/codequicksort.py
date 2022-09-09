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

def QuickSort (V, Inicio, Fim):
    if Inicio < Fim:
        Pivo = Particiona(V, Inicio, Fim)
        QuickSort(V, Inicio, Pivo-1)
        QuickSort(V, Pivo+1, Fim)


v=[69, 24, -15, -95, 38, -63, 55, 74, -62, 72, 94, 87, 62, -85, 84]
tipoCrescente = True
inicio = 0
fim = len(v)-1

print(v)

QuickSort(v,inicio,fim)
print(v)

# tipoCrescente = False
# QuickSort(v,tipoCrescente)
# print(v)