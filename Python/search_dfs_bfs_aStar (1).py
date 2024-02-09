# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import copy

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    """
    
    # Inicia as listas de abertos e fechados, colocando o estado inicial em abertos
    abertos = [[(problem.getStartState(), 'Start', 0), [], 0]]
    fechados = []
    iterations = 0  # Conta o numero de iteracoes para evitar loops infinitos

    print('Encontra solucao')  # Imprime uma mensagem indicando o inicio da busca

    # Enquanto houver estados nao explorados
    while abertos:
        iterations += 1  # Incrementa o numero de iteracoes
        
        # Remove o ultimo estado da lista de abertos para analise (DFS usa pilha, LIFO)
        X = abertos.pop(0)

        # Verifica se o estado atual e o estado objetivo
        if problem.isGoalState(X[0][0]):
            break  # Se for o objetivo, sai do loop
        else:
            # Adiciona o estado atual a lista de fechados para nao visita-lo novamente
            fechados.append(X)
            # Obtem os filhos do estado atual
            filhos = problem.getSuccessors(X[0][0])
            
            # Para cada filho do estado atual
            for filho in filhos:
                # Flag para verificar se o filho ja foi explorado
                estaAbertoOuFechado = False
                # Verifica se o filho ja esta na lista de abertos
                for estado in abertos:
                    if estado[0][0] == filho[0]:
                        estaAbertoOuFechado = True
                        estado[1].append(X[0][0])  # Adiciona o estado atual como pai do filho
                # Verifica se o filho ja esta na lista de fechados
                for estado in fechados:
                    if estado[0][0] == filho[0]:
                        estaAbertoOuFechado = True
                        estado[1].append(X[0][0])  # Adiciona o estado atual como pai do filho
                # Se o filho nao esta em nenhum dos dois
                if not estaAbertoOuFechado:
                    # E o movimento nao e invalido (custo diferente de 999999)
                    if filho[2] != 999999:
                        # Adiciona o filho ao inicio da lista de abertos (DFS)
                        abertos.insert(0, [filho, [X[0][0]], X[2] + 1])
    
    # Se nao encontrou uma solucao
    if not problem.isGoalState(X[0][0]):
        print("Nao encontrou caminho")  # Imprime mensagem de erro
        return None  # Retorna None indicando falha
    
    # Prepara para reconstruir o caminho encontrado
    print('Determina caminho')  # Imprime mensagem de sucesso
    metrica = X[2]  # Profundidade do estado atual
    movimentos = []  # Lista para armazenar os movimentos realizados

    # Retrocede do estado objetivo ate o estado inicial
    while metrica != 0:
        paisX = []  # Lista para manter os pais do estado atual
        
        # Adiciona o movimento atual ao inicio da lista de movimentos
        movimentos.insert(0, X[0][1])
        
        # Encontra os pais do estado atual na lista de fechados
        for estado in fechados:
            if estado[0][0] in X[1]:
                paisX.append(estado)

        # Atualiza a lista de fechados removendo os pais ja utilizados
        fechados = [estado for estado in fechados if estado not in paisX]

        # Encontra o pai correto com base na profundidade e atualiza o estado atual para o pai
        for pai in paisX:
            if pai[2] == metrica - 1:
                X = pai
                metrica = pai[2]  # Atualiza a profundidade (metrica)
                break
    
    # Anuncia o sucesso na busca
    print('Result Depth-First Search')

    # Retorna a lista de movimentos do Pac-Man para alcancar o objetivo
    return movimentos


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    # Inicia a lista de abertos com o estado inicial e a lista de fechados vazia
    abertos = [[(problem.getStartState(), 'Start', 0), [], 0]]
    fechados = []
    iterations = 0  # Conta o numero de iteracoes
    X = None  # Estado atual sendo analisado

    print('Encontra solucao')  # Mensagem inicial

    # Continua enquanto houver estados em abertos
    while abertos:
        iterations += 1  # Incrementa o contador de iteracoes

        # Pega e remove o primeiro estado da lista de abertos
        X = abertos.pop(0)
        
        # Verifica se o estado atual e o objetivo
        if problem.isGoalState(X[0][0]):
            break  # Sai do loop se alcancar o objetivo
        else:
            # Obtem os filhos (sucessores) do estado atual
            filhos = problem.getSuccessors(X[0][0])
            # Adiciona o estado atual aos fechados
            fechados.append(X)
            
            # Processa cada filho
            for filho in filhos:
                # Inicialmente, assume que o filho nao esta em abertos ou fechados
                estaAbertoOuFechado = False
                # Verifica se o filho esta na lista de abertos
                for estado in abertos:
                    if estado[0][0] == filho[0]:
                        estaAbertoOuFechado = True
                        estado[1].append(copy.deepcopy(X[0][0]))  # Adiciona o estado atual aos pais do filho
                # Verifica se o filho esta na lista de fechados
                for estado in fechados:
                    if estado[0][0] == filho[0]:
                        estaAbertoOuFechado = True
                        estado[1].append(copy.deepcopy(X[0][0]))  # Adiciona o estado atual aos pais do filho
                # Se o filho nao estiver em nenhum, adiciona aos abertos
                if not estaAbertoOuFechado and filho[2] != 999999:  # Checa se nao e um movimento invalido
                    abertos.append([filho, [copy.deepcopy(X[0][0])], X[2] + 1])  # Adiciona com a profundidade atualizada

    # Se o estado objetivo nao foi encontrado
    if not problem.isGoalState(X[0][0]):
        print("Nao encontrou caminho")
        return None

    print('Determina caminho')  # Mensagem de sucesso na busca
    metrica = X[2]  # Profundidade do caminho
    movimentos = []  # Lista para armazenar os movimentos

    # Retrocede da posicao atual ate o estado inicial
    while metrica != 0:
        # Lista para armazenar os pais do estado atual
        paisX = []
        # Adiciona o movimento atual a lista de movimentos
        movimentos.insert(0, X[0][1])
        
        # Encontra os pais do estado atual nos fechados
        for estado in fechados:
            if estado[0][0] in X[1]:
                paisX.append(estado)

        # Remove os pais da lista de fechados
        fechados = [estado for estado in fechados if estado not in paisX]

        # Encontra o pai correto com base na metrica (profundidade)
        for pai in paisX:
            if pai[2] == metrica - 1:
                X = pai  # Atualiza o estado atual para o pai
                metrica = pai[2]  # Atualiza a metrica
                break
    
    print('Result Breadth-First Search')  # Mensagem de conclusao

    # Retorna a lista de movimentos para serem executados
    return movimentos


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    # Inicializa a lista de abertos com o estado inicial, contendo a posicao, a acao, o custo ate agora (0 para o estado inicial),
    # uma lista vazia de pais (ja que e o estado inicial), a profundidade (0 para o estado inicial) e o valor da heuristica inicial (tambem 0).
    abertos = [[(problem.getStartState(), 'Start', 0), [], 0, 0]]
    fechados = []  # Lista de fechados para controlar os nos ja explorados.
    iterations = 0  # Contador de iteracoes para prevenir loops infinitos.

    while abertos != []:
        iterations += 1
        if iterations > 100000:  # Limita o numero de iteracoes para evitar travamento.
            print('Nao achou nenhuma solucao')
            return None
        
        X = abertos.pop(0)  # Pega o primeiro estado da lista de abertos.

        if problem.isGoalState(X[0][0]):  # Verifica se o estado atual e o estado objetivo.
            break  # Se for o estado objetivo, sai do loop.
        else:
            fechados.append(X)  # Se nao for, adiciona o estado a lista de fechados.
            filhos = problem.getSuccessors(X[0][0])  # Pega todos os sucessores do estado atual.

            for filho in filhos:  # Para cada sucessor, cria um novo estado filho.
                # Cria o estado filho com a posicao, acao, custo ate agora (profundidade atual + 1) e valor da heuristica.
                nodeFilho = [(filho), [X[0][0]], X[2]+1, heuristic(filho[0], problem)]
                nodeFilho[3] += nodeFilho[2]  # Adiciona o custo ate agora ao valor da heuristica para obter f(n).
                estaAbertoOuFechado = False  # Flag para verificar se o estado ja foi visitado.
                fechados_a_remover = []
                for estados in fechados:  # Verifica se o estado filho ja esta na lista de fechados.
                    if estados[0][0] == nodeFilho[0][0]:  # Compara apenas a posicao, ignorando o custo.
                        estaAbertoOuFechado = True
                        nodeFilho[1].extend(estados[0][1])  # Adiciona os pais do estado fechado ao filho.
                        if estados[2] > nodeFilho[2]:  # Se o custo do estado fechado for maior que o do filho.
                            abertos.append(nodeFilho)  # Adiciona o filho a lista de abertos para reanalise.
                            fechados_a_remover.append(estados)  # Remove o estado fechado antigo.
                for estado in fechados_a_remover:
                    fechados.remove(estado)  # Remove os estados que estavam fechados corretamente

                for estados in abertos:  # Verifica se o estado filho ja esta na lista de abertos.
                    if estados[0][0] == nodeFilho[0][0]:  # Compara apenas a posicao, ignorando o custo.
                        estaAbertoOuFechado = True
                        estados[0][1].extend(nodeFilho[0][1])  # Adiciona os pais do estado aberto ao filho.
                        if estados[2] > nodeFilho[2]:  # Se o custo do estado aberto for maior que o do filho.
                            estados[3] = nodeFilho[3]  # Atualiza o valor de f(n) do estado aberto.
                            estados[2] = nodeFilho[2]  # Atualiza a profundidade do estado aberto.
            
                if not estaAbertoOuFechado:  # Se o estado filho nao estiver em abertos ou fechados.
                    if filho[2] != 999999: # Se nao tiver um movimento invalido
                        abertos.append(nodeFilho)  # Adiciona o filho a lista de abertos.
            
            abertos.sort(key=lambda x: x[3])  # Ordena a lista de abertos pelo valor de f(n).

    # Verifica se a busca encontrou uma solucao.
    if not problem.isGoalState(X[0][0]):
        print("Nao encontrou caminho")
        return None
    
    metrica = X[2]  # Define a metrica para rastrear a profundidade do caminho.
    print('Determina caminho')

    movimentos = []  # Lista para armazenar os movimentos ate o estado objetivo.
    while metrica != 0:  # Retrocede pelo caminho ate chegar ao estado inicial.
        paisX = []  # Lista de pais do estado atual.
        movimentos.insert(0, X[0][1])  # Insere o movimento atual na lista de movimentos.
        
        # Encontra os pais do estado atual.
        for estado in fechados:
            if any(estado[0][0] == pai for pai in X[1]):
                paisX.append(estado)
        
        fechados = [estado for estado in fechados if estado not in paisX]  # Remove os pais da lista de fechados.

        # Encontra o pai com a metrica correta.
        for pai in paisX:
            if pai[2] == metrica - 1:
                X = pai  # Atualiza o estado para o pai.
                metrica = pai[2]  # Atualiza a metrica.
                break
    
    print('Result A-Star Search')  # Indica sucesso na busca.
    return movimentos  # Retorna os movimentos encontrados.   


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
