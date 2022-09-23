
import sys

class Game:
    #construtor do objeto
    def __init__(self=None,nome=None, genero=None, plataforma=None,
     ano=None, classificacao=None, preco=None, midia=None, tamanho=None,produtora=None):
        self.nome = nome
        self.genero = genero
        self.plataforma = plataforma
        self.ano = ano
        self.classificacao = classificacao
        self.preco = preco
        self.midia = midia
        self.tamanho = tamanho
        self.produtora = produtora

    def setNome(self,nome):
        self.nome = nome

    def getNome(self):
        return self.nome

#----------------------------------------------
def escritaTamanhosFixos(file, game):

    # for i in range(0,len(game)):
        saida.write(game.nome)


# def escritaQtdeCamps(file, Game, n):

# def escritaQtdeBytesComeço(file, Game):

# def escritaDelimitador(file, Game):

# def leituraTamanhosFixos(file, Game):

# def leituraQtdeCamps(file, Game, n):

# def leituraQtdeBytesComeco(file, Game):

# def leituraDelimitador(file, Game):
#----------------------------------------------

if __name__ == '__main__':
    entrada = open('games.txt', "r")
    saida = open('saida1.txt',"w")
        
    resposta = entrada.readlines()
    
    for i in range(len(resposta)):
        game = resposta[i].split('|')
        gameobject = Game(nome = game[0],genero=game[2],plataforma=game[3],
        ano=game[4],classificacao=game[5],preco=game[6],midia=game[7],tamanho=game[8])
        escritaTamanhosFixos(saida,gameobject)

      

    # print(resposta)
    # escritaTamanhosFixos('saida.txt',resposta)

    entrada.close()
    saida.close()