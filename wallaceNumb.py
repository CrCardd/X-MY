import random as rd
import os


jogando = True

while jogando:
    tent = 0
    nrsecret = [(rd.randint(0,9)) for _ in range(4)]

    while True:
        palpite = input('\n\nDigite seu palpite:\n>>> ')

        if palpite =='x':
            print(nrsecret)

        while len(palpite) != 4 or not palpite.isdigit():
            palpite = input('\n\033[31mERRO\033[0;0m.\nDigite seu palpite:\n>>> ')

        tent+=1

        nrsecretAux = nrsecret[:]
        numcerto=0
        numtem=0
        palp=[]


        for _ in palpite:
            _ = int(_)
            palp.append(_)

        for _ in range (len(palp)):
            if palp[_] == nrsecretAux[_]:
                numcerto+=1
                nrsecretAux[_] = 0

            elif palp[_] in nrsecretAux:
                numtem+=1


        if numcerto == 4:
            break


        print('==========================================\n||\t\t\t\t\t||')
        print(f'||          \033[47m {palp[0]} \033[0;0m  \033[47m {palp[1]} \033[0;0m  \033[47m {palp[2]} \033[0;0m  \033[47m {palp[3]} \033[0;0m\t        ||')
        print('||\t     -    -    -    -   \t||')
        print('||\t\t\t\t\t||')
        print(f'||\tNa posição certa:\t \033[42m {numcerto} \033[0;0m\t||')
        print(f'||\tNa posição errada:\t \033[43m {numtem} \033[0;0m\t||')
        print(f'||\t\t\t\t\t||\n==========================================')
        

    print('==========================================\n||\t           \033[32mCERTO!\033[0;0m   \t\t||')
    print('==========================================\n||\t\t\t\t\t||')
    print(f'||          \033[42m {palp[0]} \033[0;0m  \033[42m {palp[1]} \033[0;0m  \033[42m {palp[2]} \033[0;0m  \033[42m {palp[3]} \033[0;0m\t        ||')
    print('||\t     \033[32m-    -    -    -\033[0;0m   \t||')
    print(f'||\t\t\t\t\t||\n||\ttentativas -> {tent}\t\t||\n==========================================')

    i = input('Enter para jogar novamente, 0 para encerrar.\n>>> ')
    if i == "0":
        break

#NOVO