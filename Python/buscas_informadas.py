import copy

def matrix_to_str(matrix):
    return ''.join(''.join(str(elem) for elem in row) for row in matrix)

def comparaMatrix(estado1, estado2):
    return matrix_to_str(estado1["Matriz"]) == matrix_to_str(estado2["Matriz"])

def getHeuristica(X, Objetivo):
    return sum(1 for i in range(3) for j in range(3) if X[i][j] != Objetivo[i][j])

Inicial = {
    "Matriz": [[2, 8, 4], [1, 6, 3], [7, 5, 0]],
    "Heuristica": -1
}
Objetivo = {
    "Matriz": [[1, 2, 3], [8, 0, 4], [7, 6, 5]],
    "Heuristica": -1
}

def geraFilhos(estado, Objetivo):
    matriz = estado["Matriz"]
    for linha in matriz:
        if 0 in linha:
            posicao = (matriz.index(linha), linha.index(0))
            break

    possiveis_movimentos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    filhos = []

    for move in possiveis_movimentos:
        nova_pos = (posicao[0] + move[0], posicao[1] + move[1])
        if 0 <= nova_pos[0] < 3 and 0 <= nova_pos[1] < 3:
            aux = copy.deepcopy(matriz)
            aux[posicao[0]][posicao[1]], aux[nova_pos[0]][nova_pos[1]] = aux[nova_pos[0]][nova_pos[1]], aux[posicao[0]][posicao[1]]
            filhos.append({
                "Matriz": aux,
                "Heuristica": getHeuristica(aux, Objetivo["Matriz"])
            })

    return sorted(filhos, key=lambda x: x["Heuristica"])

def hillClimbing(Inicial, Objetivo, max_iters=10000):
    X = copy.deepcopy(Inicial)
    X["Heuristica"] = getHeuristica(X["Matriz"], Objetivo["Matriz"])
    visitados = set()
    iteracoes = 0

    while iteracoes < max_iters:
        if comparaMatrix(X, Objetivo):
            return True
        filhos = geraFilhos(X, Objetivo)
        if not filhos or matrix_to_str(filhos[0]["Matriz"]) in visitados:
            return False
        X = filhos[0]
        visitados.add(matrix_to_str(X["Matriz"]))
        iteracoes += 1

    return False

def melhorEscolha(Inicial, Objetivo):
    X = copy.deepcopy(Inicial)
    X["Heuristica"] = getHeuristica(X["Matriz"], Objetivo["Matriz"])
    
    Abertos = [X]
    Fechados = set()  # Usamos um conjunto para armazenar rapidamente os estados já processados

    while Abertos:
        X = Abertos.pop(0)  # Obter o próximo estado a ser processado

        if comparaMatrix(X, Objetivo):
            return True

        matriz_str = matrix_to_str(X["Matriz"])
        if matriz_str in Fechados:  # Se o estado já foi processado, pule
            continue

        Fechados.add(matriz_str)  # Marcar o estado como processado
        filhos = geraFilhos(X, Objetivo)

        # Adicionar filhos que não foram fechados ou abertos
        for filho in filhos:
            if matrix_to_str(filho["Matriz"]) not in Fechados:
                Abertos.append(filho)

        # Ordenar por heurística
        Abertos.sort(key=lambda x: x["Heuristica"])

    return False

print(hillClimbing(Inicial, Objetivo))
print(melhorEscolha(Inicial, Objetivo))
