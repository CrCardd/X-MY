import random as rd
import os





def printPiram(piramideAux):
    alt = len(piramideAux)
    larg = len(piramideAux[0])

    for l in range(alt):
        print('\n')
        for c in range(larg):

            if piramideAux[l][c] == 1000:
                print('💎', end='\t')

            elif piramideAux[l][c] == '1000':
                print('\033[46m 💎 \033[0m', end='\t')

            elif piramideAux[l][c] == 300:
                print('✳️', end='\t')

            elif piramideAux[l][c] == '300':
                print('\033[46m ✳️   \033[0m', end='\t')

            elif piramideAux[l][c] == -900:
                print('🧨',end='\t')

            elif piramideAux[l][c] == '-900':
                print('\033[46m 🧨 \033[0m',end='\t')
            

            elif piramideAux[l][c] == 0:
                print('\t',end='')
            
            elif type(piramideAux[l][c]) == str:
                print(f'\033[46m {piramideAux[l][c]} \033[0m', end='\t')

            else:
                print(piramideAux[l][c],end='\t')







def possibilidades(qtdDiagonal, ateOTopo, inicio, posicoes, piramideAlteradaParaMovimento, piramideOriginal, base, altura, c, VerTentativas):

    
    global melhorCaminho
    global pontuacaoDaBase


    if inicio == qtdDiagonal:
        return


    for i in range(ateOTopo):
        
        for backup in range(i):

            piramideAlteradaParaMovimento[posicoes[inicio][0]-backup] [posicoes[inicio][1]+backup] = 0


        o = c


        piramideApresentada = [[0 for _ in range(base)] for _ in range(altura)]
        for linha in range(altura):
            for coluna in range(base):
                piramideApresentada[linha][coluna] = piramideOriginal[linha][coluna]


        pontuacaoAux = 0
        for l in range(altura-1,-1,-1):
           
            pontuacaoAux += piramideOriginal[l][o]
         
            piramideApresentada[l][o] = f'{piramideApresentada[l][o]}'


            if  o != 0 and piramideAlteradaParaMovimento[l-1][o-1] != 0:
                o -= 1
            else: 
                o += 1
     



        if pontuacaoAux > pontuacaoDaBase:
            pontuacaoDaBase = pontuacaoAux   
            for linha in range(altura):
                for coluna in range(base):
                    melhorCaminho[linha][coluna] = piramideApresentada[linha][coluna]

                

        if VerTentativas == True:
            os.system('cls')
            printPiram(piramideApresentada)

        possibilidades(qtdDiagonal, ateOTopo, inicio+1, posicoes, piramideAlteradaParaMovimento, piramideOriginal, base, altura, c, VerTentativas)


                
        


    for resetando in range(ateOTopo):
        piramideAlteradaParaMovimento[posicoes[inicio][0]-resetando] [posicoes[inicio][1]+resetando] = piramideOriginal[posicoes[inicio][0]-resetando] [posicoes[inicio][1]+resetando] 


    return (pontuacaoDaBase, melhorCaminho)
    





def criarPiram(meio,altura,piramideAux):
    for linha in range(0,altura,2):
        andarPiramide = 0
        for l in range(linha,altura):
            sort = rd.randint(1,2)
            sorteio = rd.randint(1,15)
            if sort == 1:
                sort = -andarPiramide
            else: 
                sort = +andarPiramide

            if sorteio == 6:
                piramideAux[l][meio+sort] = 1000
                piramideAux[l][meio-sort] = rd.randint(1,100)
            elif sorteio == 15 or sorteio == 12 or sorteio == 2 or sorteio == 3 or sorteio == 10:
                piramideAux[l][meio-sort] = rd.randint(1,100)
                piramideAux[l][meio+sort] = -900
            elif sorteio == 1:
                piramideAux[l][meio+sort] = 300
                piramideAux[l][meio-sort] = rd.randint(1,100)
            else:    
                piramideAux[l][meio-andarPiramide] = rd.randint(1,100)
                piramideAux[l][meio+andarPiramide] = rd.randint(1,100)
            
            andarPiramide += 1
    return piramideAux






        
#=======================================================================================================================================================================
#=======================================================================================================================================================================
#=======================================================================================================================================================================



#INICIO

print('\n\n\n\n\n\n\n\n\n\n')
baseOriginal =input('Por favor digite o tamanho da base que a pirâmide deve possuir.\n( recomendado: max12  |  Rodará normalmente com valor maior ).\n>> ')
while type(baseOriginal) == str:
    

    try: 
        baseOriginal = int(baseOriginal)
        break
    except:
        baseOriginal = input('\033[91mErro. por favor insira um \033[1mnúmero inteiro.\033[0m\nPor favor digite o tamanho da base que a pirâmide deve possuir.\n\n>> ')



#VARIAVEIS
base = (baseOriginal-1)+baseOriginal
altura = baseOriginal
piramide = [[0 for _ in range(base)] for _ in range(altura)]
prmdEx = [[0 for _ in range(base)] for _ in range(altura)]
meio = ( baseOriginal - 1)
caminhosDasBases = []
topPontuacoes = []


#CRIANDO A PIRÂMIDE
criarPiram(meio,altura,piramide)


#EXIBINDO A PIRÂMIDE ORIGINAL
os.system('cls')
print('\033[38;5;208m========================================================================================================================================================================================\033[0m')
print('\033[38;5;208m- PIRÂMIDE:\033[0m\n\n')
printPiram(piramide)
print('\n\n\033[38;5;208m========================================================================================================================================================================================\033[0m')

#RECOLHENDO DADOS
VerTentativas = input('\n\n\nInsira \'S\' se deseja vizualizar o processo de calculo para encontrar o melhor caminho (mais lento), ou \'N\' se prefere receber apenas o resultado final (mais rápido).\n>> ')

while VerTentativas != 's' and VerTentativas != 'S' and VerTentativas != 'n' and VerTentativas != 'N':
    VerTentativas = input('\n\033[91mErro.\033[0m\nPor favor responda com \'S\' ou \'N\'\n>> ')

if VerTentativas == 's' or VerTentativas == 'S':
    VerTentativas = True
else:
    VerTentativas = False













#PERCORRENDO TODOS OS CAMINHOS DE TODAS AS BASES
for c in range(0,base,2):
    linCol = []
    o = c

    pontuacaoDaBase = altura * -1000
    melhorCaminho = [[0 for _ in range(base)] for _ in range(altura)]

    for linha in range(altura):
        for coluna in range(base):
            prmdEx[linha][coluna] = piramide[linha][coluna]

    blockC = (c/2)
    blockC = int(blockC)

    blockL = (altura - 1) - ( blockC )
    blockL = int(blockL)

    blockAndar =  ( meio - blockC)
    blockAndar = int(blockAndar)

    for x in range(1,blockC+1):
        linha=[]

        linha.append((blockC - x ) + blockL )
        linha.append((blockC - x ) + blockC )
        linCol.append(linha)



    retorno = possibilidades(blockC, blockAndar+1, 0, linCol, prmdEx, piramide, base, altura, c, VerTentativas)


    if retorno is None:
        caminho = 0
        pontuacao = 0
    else:
        pontuacao = retorno [0]
        caminho = retorno[1]


    caminhosDasBases.append(caminho)
    topPontuacoes.append(pontuacao)



for linha in range(altura):
        for coluna in range(base):
            prmdEx[linha][coluna] = piramide[linha][coluna]

c=0
pontuacao = 0
for l in range(altura-1,-1,-1):
    pontuacao += prmdEx[l][c]
    prmdEx[l][c] = f'{prmdEx[l][c]}'
    c+=1

topPontuacoes[0] = pontuacao
caminhosDasBases[0] = prmdEx


#COMPARANDO OS MELHORES CAMINHOS PARA SABER QUAL O MELHOR
pontuacao = altura * -1000
caminho = []
for i in range(baseOriginal):
    if topPontuacoes[i] > pontuacao:
        pontuacao = topPontuacoes[i]
        caminho = caminhosDasBases[i]




#LIMPANDO E EXBINDO O MELHOR CAMINHO POSSÍVEL
os.system('cls')
print('\n\n\n\033[92m========================================================================================================================================================================================\033[0m')
print('\033[92m||\033[0m\t\t\t\t\t\t\t\t\t\t\033[93mMELHOR\tCAMINHO\033[0m\t\t\t\t\t\t\t\t\t\t\t      \033[92m||\033[0m')
print('\033[92m========================================================================================================================================================================================\033[0m\n\n\n\n')


printPiram(caminho)

print('\n\n\n\n')
print('\033[92m==================================================================\033[0m')
print(f'\033[92m||\033[0m\t\033[93mPontuação ->\033[0m\t\t {pontuacao}.pnts\t\t\t\033[92m||\033[0m')
print('\033[92m==================================================================\033[0m')
# print(topPontuacoes)

# for i in range(baseOriginal):
#     caminho = caminhosDasBases[i]
#     printPiram(caminho)
#     print(f'\n\n\nPontuação: {topPontuacoes[i]}')
