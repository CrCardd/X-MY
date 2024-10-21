#include <stdio.h>
#include <stdlib.h>
#include <time.h>


typedef signed char int8;

int main()
{
    int n;
    printf("Please insert the base:\n>> ");
    scanf(" %d", &n);


    srand(time(NULL));
    size_t length = (n*(n+1))/2;
    int8 *pyramid = malloc(length);

    for(size_t i=0; i<length; i++)
    {
        pyramid[i] = rand()%100;
        printf("%d\t",pyramid[i]);    
    }

    

    printf("\n\n\n");
    
    int prints = 0;
    for(int m=1; m<=n; m++)
    {
        for(int b=0; b<n-m; b++)
            printf("    ");
        for(int n=0; n<m; n++)
            printf("%d      ",pyramid[prints++]);
        printf("\n");
    }

    size_t bin;

    size_t bestWay = 0;
    size_t bestAcc = 0;
    size_t acc = 0;


    size_t times = 1;

    for(int i = 0; i < (n-1); i++)
    {
        times <<= 1;
        times += 1;
    }
    printf("\n\n\n%u",times);

    for(size_t o = 0; o<=times; o++){
        acc = 0;
        // printf("\n\nTIMES: %d\n",o);
        bin = o;
        size_t step = 0;
        for(size_t x=1 ; step<length ; x++)
        {
            // printf("%d\t",pyramid[step]);
            step += x+(bin & 1);
            bin >>= 1;
            acc += pyramid[step];
        }
        if(bestAcc < acc){
            bestAcc = acc;
            bestWay = o;
        }
    }

    printf("\n\n\n%u",bestWay);
    printf("\n%u",bestAcc);
    printf("\n\n\n");
    printf("\n\n\n%d",n);
    return 0;
}
