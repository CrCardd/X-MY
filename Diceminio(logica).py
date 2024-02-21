import random as rd
tabela = True
refazer = True
pecas = []
tentativas = 0
pecasVertical =   ['', ' ⠐', '⠠⠈', '⠠⠊', '⠨⠨', '⠨⠪', '⠸⠸' ]
pecasHorizontal = ['', ' ⠐', '⠈⠠', '⠈⠢', '⠨⠨', '⠨⠪', '⠅⠅⠅']


while tabela:
   
    pec=[[1,1],
         [1,2],[2,2],
         [1,3],[2,3],[3,3],
         [1,4],[2,4],[3,4],[4,4],
         [1,5],[2,5],[3,5],[4,5],[5,5],
         [1,6],[2,6],[3,6],[4,6],[5,6],[6,6],
         'X','X','X','X','X','X','X']
    
    for _ in range(rd.randint(1,50)):
        rd.shuffle(pec)
    
    while refazer:
        qtdPecas = 0
        tentativas += 1
        
        pecas.clear()
        
        for i in range(0,28):
            pecas.append(pec[i])
            
        # print('\n\nPECAS\n',pecas)
        # print('\n\nPEC\n',pec)
        
        puzzle = [[0 for _ in range(7)] for _ in range(7)]

        for l in range(0,7):
            for c in range(0,7):

                if puzzle[l][c] == 0:
                    
                    if pecas[0] == 'X':
                         puzzle[l][c]= '\033[1;36m ⚀\033[0m' 
                         pecas.remove(pecas[0])
                   
                    elif type(pecas[0]) == list:
                        check = True
                        vertical = 0
                        horizontal = 0
                        while check == True:
                            posicao = rd.randint(1,2)
                            match(posicao):

                                case 1:
                
                                    horizontal +=1
                                    
                                    if c<6  and  puzzle[l][c+1] == 0:

                                        puzzle[l][c] = pecasHorizontal[pecas[0][0]]
                                        puzzle[l][c+1] = pecasHorizontal[pecas[0][1]]
                                        pecas.remove(pecas[0])
                                        break

                                case 2:
                                
                                    vertical +=1
                                    
                                    if l<6  and  puzzle[l+1][c] == 0:

                                        puzzle[l][c] = pecasVertical[pecas[0][0]]
                                        puzzle[l+1][c] = pecasVertical[pecas[0][1]]
                                        pecas.remove(pecas[0])
                                        break

                                
                                
                           
                            if vertical>0 and horizontal>0:
                                break
                        
                       
                    
        for l in range(7):
            for c in range(7):
                if puzzle[l][c] == 0:
                    puzzle[l][c] = '\033[1;31m[]\033[0m'
                    refazer = True                  
                else:
                    qtdPecas += 1
                    if qtdPecas == 49:
                        refazer = False

        if refazer == True:
            print('\033[1;31m==================================================================\n| \t\t\t\t\t\t\t\t|\033[0m')          
            for m in range (7):
                print('\n\033[1;31m|\033[0m')
                for v in range (7):
                    print(f'      {puzzle[m][v]}',end='')
                    if v == 6:
                        print('\t\033[1;31m|\033[0m')
            print('\n')
            print('\033[1;31m|\t\t\t\t\t\t\t\t|\n=================================================================\n\033[0m') 
    break  
    

print(f'\n\n\n\n\033[32m=========================================================================\n|\t\tCONCLUÍDO\t    |\t\ttentativas = {tentativas}\t\t|\n=========================================================================\n\033[0m')
for m in range (7):
    print('\n')
    for v in range (7):
        print(f'\t{puzzle[m][v]}',end='')

print('\033[32m\n\n\n========================================================================\033[0m') 

print(f'\n\n\nPEÇAS: \n {pec}\n\n\n\n')