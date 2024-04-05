#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
    srand(time(NULL));
    int op=0;
    int tot=0;
    printf("Digite o tamanho do array que sera gerado:");
    do
    {
        printf("\n>>>  ");
        scanf(" %d",&op);
    } while (op<1);
    printf("\n\n");
    int *array = (int*)malloc(op * sizeof(int));
    for(int i =0; i<op;i++){
        array[i] = (rand()%100)+1; 
        tot+= array[i];
        printf("[ %d ]",array[i]);
    }
    printf("\n\nA soma dos valores do array gerado e: [ %d ]",tot);
    return 0;
}