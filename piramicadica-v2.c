#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
// #include <windows.h>
//CRIAR PIRAMIDE
int** createPiram(int b){
    int base = b;
    int height = b;
    int **piramide = (int**) malloc(height  * sizeof(int*));
    for(int i = 0; i < height; i++){
        piramide[i] = (int*) malloc( (i+1) * sizeof(int));
    }
     for(int l=0;l<height;l++){
       for(int c=0;c<=l;c++){
         piramide[l][c] = (rand()%100)+1;
       }
     }
    return piramide;
}
//PRINTAR PIRAMIDE
void printPiram(int **pyramMove, int **pyram, int base, int height, int choice){
    switch (choice){
    case 1:
        for( int l = 0; l < height; l++){
        printf("\n\n");
            for(int s = 0; s<height-l; s++){
              printf("\t");
            }
            for( int c = 0; c <= l; c++){
                printf("%d\t\t",pyram[l][c]);
            }
        }
        break;
    case 2:
        for( int l = 0; l < height; l++){
            printf("\n\n");
            for(int s = 0; s<height-l; s++){
              printf("\t");
            }
            for( int c = 0; c <= l; c++){
                if(pyramMove[l][c]==-1){
                  printf("\033[44m\033[30m %d \033[0m\t\t",pyram[l][c]);
                } else{
                printf("%d\t\t",pyram[l][c]);
                }
            }
        }
        break;
    }
}
//CONSEGUIR AS POSIÇÕES EM BINARIO
int* binary(int i, int height){
    int* bin = (int*) malloc(height * sizeof(int));
    for(int _ = height-1; _ >= 0; _--){
        if(!i){
            bin[_] = 0;
        }else{
            bin[_] = i % 2;
            i = (i/2);
        }
    }
    return bin;
}
//COPIAR PIRAMIDE ORIGINAL
int** copyPiram(int **pyramOrig,int b){
    int base = b;
    int height = b;
    int **piramCopia = (int**) malloc(height  * sizeof(int*));
    for(int i = 0; i < height; i++){
        piramCopia[i] = (int*) malloc(base * sizeof(int));
    }
    for(int lin = 0; lin < height; lin++){
        for(int col = 0; col < base; col++){
            piramCopia[lin][col] = pyramOrig[lin][col];
        }
    }
    return piramCopia;
}
void freePiram(int **piram, int height){
    for( int i = 0; i < height; i++){
        free(piram[i]);
    }
    free(piram);
}
//MAIN
int main() {
    while(1){
        srand(time(NULL));
        int b,score=0,**pyraMove, *bin;
        long long times=0;
        char see;
        printf("\n\nInsira a base da piramide:");
        do{
            printf("\n>>>  ");
            scanf("%i",&b);
        } while(b<=0);
        int height = b, base = b;
        int **pyramid = createPiram(b);
        int **bestWay = copyPiram(pyramid,b);
        printf("==================================================================================================================================================================================\n\n");
        printPiram(0, pyramid, base, height, 1);
        printf("\n\n\n==================================================================================================================================================================================");
        // Sleep(5000);
        //CALCULAR CAMINHOS POSSIVEIS
        for(int i = 0; i < height; i++){
            times += pow(2,i); 
        }
        for(int v = 0; v <= times; v+=2){
            int result = 0;
            int walkPyram = 0;
            pyraMove = copyPiram(pyramid,b);
            bin = binary(v,height);

            for(int lin = 0; lin < height; lin++){
                result += pyramid[lin][walkPyram];
                pyraMove[lin][walkPyram] = -1;
                if(bin[lin]){
                    walkPyram+=1;
                }
            }
            if(result>score){
                score = result;
                bestWay = copyPiram(pyraMove,b);
            }
            if(b<=10){
                printf("\033[2J\033[H");
                printPiram(pyraMove, pyramid, base, height, 2);
                printf("\n");
            }else if (b<=15){
                printf("\033[2J\033[H");
                float load = ((v*100)/times)+1;
                printf("Loading...\t [ %.2f%% ]",load);
            }
        }
        printf("\n\n\n==========================================================================================\n||\t\t\t\t\tMELHOR CAMINHO\t\t\t\t\t||\n==========================================================================================\n\n");
        printPiram(bestWay, pyramid , base, height, 2);
        printf("\n\n\n==========================================\n||\tPONTUACAO:\t%d\t\t||\n==========================================",score);
      printf("\n\n\ntimes: %lld",times);
        freePiram(pyramid,height);
        freePiram(pyraMove,height);
        freePiram(bestWay,height);
        free(bin);
    }
    return 0;
}

//by Matias, Eduardo Sampaio, Wallace, Cristian 
