import random as rd
import os

nrsecret = [(rd.randint(0,9)) for _ in range(4)]
#print(nrsecret)
jogando = True

tent= [0 for _ in range(4)]




while jogando:
    palpite = input('\n\nDigite seu palpite:\n>>> ')
    while len(palpite) != 4 or not palpite.isdigit():
        palpite = input('\n\033[31mERRO\033[0;0m.\nDigite seu palpite:\n>>> ')

    nrsecretAux = nrsecret[:]
    numcerto=0
    numtem=0
    palp=[]

    for _ in palpite:
        _ = int(_)
        palp.append(_)
    
    tent=palp[:]
    

    for _ in range (len(palp)):
        if palp[_] == nrsecretAux[_]:
            numcerto+=1
            nrsecretAux[_] = 0
            #print(nrsecretAux)

        elif palp[_] in nrsecretAux:
            numtem+=1

    os.system('cls')

    print('==========================================\n||\t\t\t\t\t||')
    print(f'||          \033[47m {palp[0]} \033[0;0m  \033[47m {palp[1]} \033[0;0m  \033[47m {palp[2]} \033[0;0m  \033[47m {palp[3]} \033[0;0m\t        ||')
    print('||\t     -    -    -    -   \t||')
    print('||\t\t\t\t\t||')
    print(f'||\tNa posição certa:\t \033[42m {numcerto} \033[0;0m\t||')
    print(f'||\tNa posição errada:\t \033[43m {numtem} \033[0;0m\t||')
    print(f'||\t\t\t\t\t||\n==========================================')

    
