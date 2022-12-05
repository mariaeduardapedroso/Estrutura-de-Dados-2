import sys
def ciatabeladeIdxSecundarioCidade(dataFile=None,debug=False):
    # print(" - Construindo uma Tabela de indices Primario")
    if(dataFile == None):
        raise Exception("Por favor, informe o nome dos arquivos de dados")
        exit(1)
    else:
        # abrindo arquivo de dados
        try:
            print("* Arquivo de Dados: " + dataFile)
            arquivoDados = open(dataFile, "r+")
        except FileNotFoundError as error:
            print(error)
            Erro()
            exit(1)
        tabelaIndices = list()
        # imprimindo a lista de
        print("* Lista de Tuplas")
        print(tabelaIndices)

        #criar a tabela de indices
        linhas = arquivoDados.readlines()
        print(linhas)
        #  - percorrer o arquivo de dados
        # 0 até qtdeLinhas (len/size linhas) - header = linhas[0]
        for index in range(1, len(linhas)):
            key = criaChaveCanonicaCidade(registro = linhas[index])
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



def ciatabeladeIdx(dataFile=None,debug=False):
    # print(" - Construindo uma Tabela de indices Primario")
    if(dataFile == None):
        raise Exception("Por favor, informe o nome dos arquivos de dados")
        exit(1)
    else:
        # abrindo arquivo de dados
        try:
            print("* Arquivo de Dados: " + dataFile)
            arquivoDados = open(dataFile, "r+")
        except FileNotFoundError as error:
            print(error)
            Erro()
            exit(1)
        tabelaIndices = list()
        # imprimindo a lista de
        print("* Lista de Tuplas")
        print(tabelaIndices)

        #criar a tabela de indices
        linhas = arquivoDados.readlines()
        print(linhas)
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
def ciatabeladeIdxSecundario(dataFile=None,debug=False):
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
        print("* Lista de Tuplas")
        print(tabelaIndices)

        #criar a tabela de indices
        linhas = arquivoDados.readlines()

        #  - percorrer o arquivo de dados
        # 0 até qtdeLinhas (len/size linhas) - header = linhas[0]
        for index in range(1, len(linhas)):
            key = criaChaveCanonica(registro = linhas[index])
            ChaveSecundaria = criaChaveSecundaria(linhas[index])#por numero
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
    key = tokens[0] # artista +  nome
    key = key.upper()
    key = key.replace(" ", "")
    return (key)

def criaChaveCanonicaCidade(registro):
    aux = registro.strip()
    tokens = aux.split("|")
    key = tokens[3] # artista +  nome
    key = key.upper()
    key = key.replace(" ", "")
    return (key)

def criaChaveSecundaria(registro):
    aux = registro.strip()
    tokens = aux.split("|")
    numero = 2

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
def vetorTamanhoFixo(lista):
    novalista=list()
    igual=False;
    i=0
    while i<len(lista):
        curso = lista[i][0]
        cursoaux = curso
        stringaux = str(curso)
        while cursoaux == curso:
            curso = lista[i][0]
            if cursoaux == curso:
                stringaux = stringaux + " " + str(lista[i][1] )
                i=i+1
        print(stringaux)
    return novalista

    








# ----------------------------------------------------
# ----------------------------------------------------
if __name__ == '__main__':

# abrindo arquivo de entrada
    infile = "ex1.txt"
    dadosfile = "tipo.txt"
    outfile = "saida.txt"
    try:
        print("* Arquivo de Entrada: " + infile)
        with open(infile, "r") as dado:
            dados=dado.readlines()
    except FileNotFoundError as error:
        print(error)
        Erro()
        exit(1)

    tabelaIdxPrimario = ciatabeladeIdx("ex7.txt")
    tabelaIdxSecundario = ciatabeladeIdxSecundario("ex7.txt")
    TabelaIdxSeundarioForteCidade = ciatabeladeIdxSecundarioCidade("ex7.txt")
    # print(tabelaIdxSecundario)
    tabelaDeTamanhoFixo = vetorTamanhoFixo(tabelaIdxSecundario)

    with open ("saida71.txt","w+") as resposta:
        for i in range(len(tabelaIdxPrimario)):
            resposta.write(str(tabelaIdxPrimario[i][0]) + "\t" + str(tabelaIdxPrimario[i][1]) + "\n")

    with open ("saida72.txt","w+") as resposta:
        for i in range(len(tabelaIdxSecundario)):
            resposta.write(str(tabelaIdxSecundario[i][0]) + "\t" + str(tabelaIdxSecundario[i][1]) + "\n")

    with open ("saida73.txt","w+") as resposta:
        for i in range(len(TabelaIdxSeundarioForteCidade)):
            resposta.write(str(TabelaIdxSeundarioForteCidade[i][1]) + "\t" + str(TabelaIdxSeundarioForteCidade[i][0]) + "\n")

