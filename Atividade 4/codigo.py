
import sys

def ciatabeladeIdx(dataFile=None,debug=False):
    # print(" - Construindo uma Tabela de indices Primario")
    if(dataFile == None):
        raise Exception("Por favor, informe o nome dos arquivos de dados")
        exit(1)
    else:
        # abrindo arquivo de dados
        try:
            #print("* Arquivo de Dados: " + dataFile)
            arquivoDados = open(dataFile, "r+")
        except FileNotFoundError as error:
            print(error)
            Erro()
            exit(1)
        tabelaIndices = list()
        # imprimindo a lista de
        # print("* Lista de Tuplas")
        # print(tabelaIndices)

        #criar a tabela de indices
        linhas = arquivoDados.readlines()

        #  - percorrer o arquivo de dados
        # 0 até qtdeLinhas (len/size linhas) - header = linhas[0]
        for index in range(1, len(linhas)):
            key = criaChaveCanonica(registro = linhas[index])
            RRN = index - 1
            tupla = (RRN, key)
            tabelaIndices.append(tupla)
            if(debug == True):
                print(index,":",linhas[index])
                print("RRN: ", RRN)
                print("Key: ", key)

        # ordenar a tabela de indices
        tabelaIndices.sort(key = lambda tup: tup[1])
        if(debug == True):
            print("\n **** Depois do Sort ***** ")
            imprimeTabelaIndices(tabela = tabelaIndices)
        return tabelaIndices

#-------------------------------------------------------
#-------------------------------------------------------
def ciatabeladeIdxSecundario(dataFile=None,tipoSecundario=None,debug=False):
    # print(" - Construindo uma Tabela de indices Secundario")
    if(dataFile == None):
        raise Exception("Por favor, informe o nome dos arquivos de dados")
        exit(1)
    else:
        # abrindo arquivo de dados
        try:
            #print("* Arquivo de Dados: " + dataFile)
            arquivoDados = open(dataFile, "r+")
        except FileNotFoundError as error:
            print(error)
            Erro()
            exit(1)
        tabelaIndices = list()
        # imprimindo a lista de
        # print("* Lista de Tuplas")
        # print(tabelaIndices)

        #criar a tabela de indices
        linhas = arquivoDados.readlines()

        #  - percorrer o arquivo de dados
        # 0 até qtdeLinhas (len/size linhas) - header = linhas[0]
        for index in range(1, len(linhas)):
            key = criaChaveCanonica(registro = linhas[index])
            ChaveSecundaria = criaChaveSecundaria(linhas[index],tipoSecundario)#por numero
            tupla = (ChaveSecundaria, key)
            tabelaIndices.append(tupla)
            if(debug == True):
                print(index,":",linhas[index])
                print("ChaveSecundaria: ", ChaveSecundaria)
                print("Key: ", key)

        # ordenar a tabela de indices
        tabelaIndices.sort(key = lambda tup: tup[0])
        if(debug == True):
            print("\n **** Depois do Sort ***** ")
            imprimeTabelaIndices(tabela = tabelaIndices)
        return tabelaIndices

#-------------------------------------------------------
#-------------------------------------------------------
def criaChaveCanonica(registro):
    aux = registro.strip()
    tokens = aux.split("|")
    key = tokens[2] + tokens[3] # artista +  nome
    key = key.upper()
    key = key.replace(" ", "")
    return (key)

def criaChaveSecundaria(registro,tipoSecundario):
    aux = registro.strip()
    tokens = aux.split("|")
    match tipoSecundario:
        case "ano":
            numero = 0

        case "duracao":
             numero = 1

        case "titulo":
             numero = 2
        
        case "artista":
            numero = 3

        case "genero":
            numero = 4

        case "idioma":
             numero = 5

        case _:
            print("Busca não existente vou ordenar pelo ano")
            numero = 0

    key = tokens[numero] # tipo de busca
    key = key.upper()
    key = key.replace(" ", "")
    return (key)

#-------------------------------------------------------
#-------------------------------------------------------

def imprimeTabelaIndices(tabela):
    for element in tabela:
        print(element)

# ----------------------------------------------------
# ----------------------------------------------------
def buscaIdxSecundario(lista,pesquisa):
    chavesCanonicas = list()

    for i in range(len(lista)):
        if lista[i][0] == pesquisa:
            # print(lista[i][0])
            # print(lista[i][1])
            chavesCanonicas.append(lista[i][1])

    return chavesCanonicas

def buscaIdxPrimario(tabelaIdxPrimario,resultadoBuscaSecundaria):
    listaRRN = list()
    # print(tabelaIdxPrimario)
    # print(resultadoBuscaSecundaria)
    for i in range(len(resultadoBuscaSecundaria)):
        # print(resultadoBuscaSecundaria[i])
        chave = resultadoBuscaSecundaria[i]
        inicio = 0
        fim = len(tabelaIdxPrimario)
        achou = False
        while inicio<=fim:
            meio=int((inicio+fim)/2)
            # print(inicio)
            # print(meio)
            # print(fim)
            # print(tabelaIdxPrimario[meio][1])
            # print(chave)
            # print(tabelaIdxPrimario[meio][0])
            if tabelaIdxPrimario[meio][1] == chave:
                # print("achou")
                fim = inicio - 1
                listaRRN.append(tabelaIdxPrimario[meio][0])
            elif tabelaIdxPrimario[meio][1] < chave:
                # print("menor")
                inicio=meio+1
            elif tabelaIdxPrimario[meio][1] > chave:
                # print("maior")
                fim = meio-1
    return listaRRN

def buscaBinariaIdxPrimario(lista,chave):
    chavesCanonicas = list()

    inicio = 0
    fim = len(lista)

    while inicio<=fim:
        meio=int((inicio+fim)/2)
        if lista[meio][1] == chave:
            return lista[meio][0]
        elif lista[meio][1] < chave:
            inicio=meio+1
        elif lista[meio][1] > chave:
            fim = meio-1

    return -1

def Erro():
    outfile = sys.argv[3]
    with open(outfile, "w") as saida:      
        saida.write("Erro no arquivo")

# ----------------------------------------------------
# ----------------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) == 4: 
    # abrindo arquivo de entrada
        infile = sys.argv[2]
        dadosfile = sys.argv[1]
        outfile = sys.argv[3]
        try:
            # print("* Arquivo de Entrada: " + infile)
            with open(infile, "r") as dado:
                dados=dado.readlines()
        except FileNotFoundError as error:
            print(error)
            Erro()
            exit(1)
        if len(dados)>1:
            tabelaIdxPrimario = ciatabeladeIdx(dadosfile)
            
            dados[0]=dados[0][0:len(dados[0])-1]
            dados[1]=dados[1][0:len(dados[1])-1]

            tabelaIdxSecundario = ciatabeladeIdxSecundario(dadosfile,dados[0])

            busca = dados[1].upper()
            busca = busca.replace(" ", "")
            
            resultadoBuscaSecundaria = buscaIdxSecundario(tabelaIdxSecundario,busca)
            # print(resultadoBuscaSecundaria)

            if len(resultadoBuscaSecundaria)>0:
                resultadoBuscaPrimaria = buscaIdxPrimario(tabelaIdxPrimario,resultadoBuscaSecundaria)
                # print(resultadoBuscaPrimaria)
                with open(dadosfile, "r") as conteudo:
                        conteudos = conteudo.readlines()


                with open(outfile, "w") as saida:
                    for i in range(len(resultadoBuscaPrimaria)):
                        # print(conteudos[resultadoBuscaPrimaria[i]+1])
                        saida.write(conteudos[resultadoBuscaPrimaria[i]+1])
            else:
                with open(outfile, "w") as saida:      
                    saida.write("Nenhum registro foi encontrado!")
            
                

