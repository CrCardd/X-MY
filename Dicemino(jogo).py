import random as rd
tabela = True
pecas = []
cor   = []
dados = []

pecasVertical   = ['', ' ⠐ ', '⠠⠈ ', '⠠⠊ ', '⠨⠨ ', '⠨⠪ ', '⠸⠸ ' ]
pecasHorizontal = ['', ' ⠐ ', '⠈⠠ ', '⠈⠢ ', '⠨⠨ ', '⠨⠪ ', '⠅⠅⠅ ']
dado            = [    ' ⠐ ', '⠠⠈ ', '⠠⠊ ', '⠨⠨ ', '⠨⠪ ', '⠸⠸ ','⠈⠠ ',  '⠅⠅⠅ ', '⠈⠢ ']



while tabela:
    tentativas = 0
    cores = ['48;2;255;165;0','41','42','43','44','45','46','47','100','101','102','103','104','105','106','107','46','48;2;255;165;0','47','100','44']
    pec=[[1,1],
         [1,2],[2,2],
         [1,3],[2,3],[3,3],
         [1,4],[2,4],[3,4],[4,4],
         [1,5],[2,5],[3,5],[4,5],[5,5],
         [1,6],[2,6],[3,6],[4,6],[5,6],[6,6],
         'X','X','X','X','X','X','X']
    
    quantidadeDados = [0 for _ in range(7)] #lista para armazenar a quadidade de cada dado que será sorteada, o elemente [0] não será usado.

    for i in range(21):
        for _ in range(rd.randint(1,10)): # Embaralhamento do valor das peças para que não exista um padrão
            rd.shuffle(pec[i])
    
    for _ in range(rd.randint(2,80)):  # Embaralhamento da ordem das peças que serão adicionadas na ordem sorteada dentro da matriz
        rd.shuffle(pec)
    
    refazer = True
    while refazer:
        tentativas += 1
        qtdPecas = 0
        

        pecas.clear()             #Reinicia a lista 'pecas' para ser usada novamente
        for i in range(0,28):
            pecas.append(pec[i])  #Copia os elementos de 'pec' porque os elementos serão apagados um a um nas linhas 89 e 107. Isso não poderia ocorrer com a lista 'pec' 


        cor.clear()                #Reinicia a lista 'cor' para ser usada novamente
        for i in range(0,21):
            cor.append(cores[i])   #Copia os elementos de 'cores' porque os elementos serão apagados um a um nas linhas 88 e 106. Isso não poderia ocorrer com a lista 'cores' 
        rd.shuffle(cor)            #Embaralha as cores que serão usadas no gabarito
        

        puzzle   = [[0 for _ in range(7)] for _ in range(7)] # Zerando o desafio para caso o looping esteja se repetindo
        gabarito = [[0 for _ in range(7)] for _ in range(7)] # Zerando o gabarito para caso o looping esteja se repetindo


        for l in range(0,7):
            for c in range(0,7):

                if puzzle[l][c] == 0:   # Confere se a posição está livre para adicionarmos uma peça

                    if pecas[0] == 'X': 
                         gabarito[l][c] = '\033[32m ⚀\033[0m' # Adicionando e colorindo no gabarito
                         puzzle[l][c]= ' O' # Sendo identificado como um dado para criar o desafio
                         pecas.remove(pecas[0])
                   

                    elif type(pecas[0]) == list:

                        vertical = 0    # Utilizado para conferir se o código tentou adicionar a peça tanto na horizontal quanto na vertical,
                        horizontal = 0  # então se vertical e horizontal for maior que 0 não foi possível adicionar de nenhuma maneira
                        while True:
                            
                            posicao = rd.randint(1,2) #sorteio para decidir se a peça será colocada na vertical ou na horizontal
                            match(posicao):
                                

                                case 1: # Se as condições forem verdadeiras a peça será adicionada na horizontal
                                    
                                    horizontal +=1 # explicado na linha 67/68
                                    
                                    if c<6  and  puzzle[l][c+1] == 0: 

                                        
                                        puzzle[l][c]   = pecasHorizontal[pecas[0][0]]
                                        puzzle[l][c+1] = pecasHorizontal[pecas[0][1]]

                                        gabarito[l][c]   = f'\033[{cor[0]}m{pecasHorizontal[pecas[0][0]]}\033[0m' # Adicionando a peça com a mesma cor 
                                        gabarito[l][c+1] = f'\033[{cor[0]}m{pecasHorizontal[pecas[0][1]]}\033[0m' # dentro da matriz 'gabarito'

                                        cor.remove(cor[0])
                                        pecas.remove(pecas[0])
                                        break


                                case 2: # Se as condições forem verdadeiras a peça será adicionada na horizontal
                                    
                                    vertical +=1 # explicado na linha 67/68
                                    
                                    if l<6  and  puzzle[l+1][c] == 0:
                                        
                                        
                                        puzzle[l][c]   = pecasVertical[pecas[0][0]]
                                        puzzle[l+1][c] = pecasVertical[pecas[0][1]]

                                        gabarito[l][c]   = f'\033[{cor[0]}m{pecasVertical[pecas[0][0]]}\033[0m' # Adicionando a peça com a mesma cor 
                                        gabarito[l+1][c] = f'\033[{cor[0]}m{pecasVertical[pecas[0][1]]}\033[0m' # dentro da matriz 'gabarito'

                                        cor.remove(cor[0])
                                        pecas.remove(pecas[0])
                                        break

                                
                            # Acontecerá se não for possível encaixar uma peça nem na vertical nem na horizontal, costuma ocorrer na última linha,
                            # se acontecer o elemento permanecerá '0' e será descoberto na próxima etapa
                            if vertical>0 and horizontal>0:
                                break


        # Checar para descobrir se existe algum erro no desafio formado, se não houver ' refazer ' irá retornar como falso e encerrar o looping
        for l in range(7):
            for c in range(7):  
                if puzzle[l][c] == 0:
                    puzzle[l][c] = '\033[1;31mErro\033[0m' # Apenas uma precaução visual para casa ocorra um erro na correção da tabela, o erro estará vermelho
                    refazer = True 

                elif puzzle[l][c] != 0:      # Se for diferente de 0 irá somar +1 em uma variável, que caso o total de peças seja 49 significa que não há nenhum
                    qtdPecas += 1            # espaço vazio, então retornará 'refazer = Falso' que finalizará o looping de embaralhar a posição das peças
                    if qtdPecas == 49:
                        refazer = False

    dados.clear()      # Reinicia a lista 'dados' para poder ser usada novamente sem alterações do uso anterior
    for i in range(9):        
        dados.append(dado[i])  # Copia os elementos de 'dado' porque de um em um os elementos de 'dados' serão apagados, e isso não poderia ser feito com a lista 'dado'

    for l in range(7):
        for c in range(7):
            if puzzle[l][c]==' O':
            # Definir o valor de cada um dos dados embaralhados e contando quantos de cada estão presentes no desafio
                qualDado = rd.randint(0,8)
                puzzle[l][c] = f'\033[47m\033[30m{dados[qualDado]}\033[0m'
                if qualDado == 6:
                    quantidadeDados[2] += 1
                elif qualDado == 7:
                    quantidadeDados[6] += 1
                elif qualDado == 8:
                    quantidadeDados[3] += 1
                else:
                    quantidadeDados[qualDado+1] += 1


    

    # Exibindo o desafio para o usuário.
    print(f'\n\n\n\n\033[32m=================================================================================================================\n|\t\t\t\t\t\t\tDESAFIO\t\t\t\t\t\t\t|\n=================================================================================================================\n\033[0m')
    
    for m in range (7):
        if m!=0:
            print('\n|               |               |               |               |               |               |               |')
            print('|---------------+---------------+---------------+---------------+---------------+---------------+---------------|')
        else:
            print('-----------------------------------------------------------------------------------------------------------------')

        print('|               |               |               |               |               |               |               |')
        for v in range (7):
            print(f'|\t\033[47m\033[30m{puzzle[m][v]}\033[0m',end='\t')
        print('|',end='')
        if m==6:
            print('\n|               |               |               |               |               |               |               |')
            print('-----------------------------------------------------------------------------------------------------------------')

    print(f'\033[32m\n\n=================================================================================================================\033[0m\n\n\n') 




    resposta = input("Já terminou ou está cansad@? Deseja ver o gabarito do desafio? (S/N): ")

    if resposta == '':
        print(f'Quantidade de tentativas para gerar a tabela final: {tentativas}')
    while resposta!='s' and resposta!='S' and resposta!='n' and resposta!='N':
        resposta=input("Por favor responda corretamente.\nDeseja ver o gabarito? (S/N): ")


    if resposta == 'S' or resposta == 's':
        # Exibindo o gabarito para o usuário.
        print('\n\n\n\n=================================================================================================================\n|\t\t\t\t\t\t      GABARITO      \t\t\t\t\t\t|')#\n=================================================================================================================\n')
        
        for m in range (7):
            if m!=0:
                print('\n|               |               |               |               |               |               |               |')
                print('|---------------+---------------+---------------+---------------+---------------+---------------+---------------|')
            else:
                print('-----------------------------------------------------------------------------------------------------------------')

            print('|               |               |               |               |               |               |               |')
            for v in range (7):
        
                print(f'|\t{gabarito[m][v]}',end='\t')
            print('|',end='')
        if m==6:
            print('\n|               |               |               |               |               |               |               |')
            print('-----------------------------------------------------------------------------------------------------------------')

        print('\n\n\n=================================================================================================================\n') 





        # Exibindo a tabela de quantos dados de cada estão presentes no desafio.
        print("\t\t\t\t   ========  Quantidade de cada dado  ========\n\t\t\t\t   ||                                       ||")

        for m in range(3):
            print(f'\t\t\t\t   ||    Dado {m+1} = {quantidadeDados[m+1]}     |     Dado {m+4} = {quantidadeDados[m+4]}    ||')
        print('\t\t\t\t   ||                                       ||\n\t\t\t\t   ===========================================\n\n\n')
    


    # Dando a opção de reiniciar o desafio para o usuário
    resposta = input("Quer tentar novamente nosso desafio? Digite 'S' para gerar uma nova tabela, ou 'N' para encerrar o programa: ")
    if resposta == '':  
        print(pec)
    while resposta!='s' and resposta!='S' and resposta!='n' and resposta!='N':
        resposta=input("Por favor responda corretamente.\nQuer tentar novamente nosso desafio? (S/N): ")
    
    if resposta == 'n' or resposta == 'N':
        break