#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

typedef signed char int8;

int banana(size_t pivot, int8 * data, size_t base )
{
    float sqrt_ = sqrt( 8 * pivot + 2);
    unsigned int label = (int)((sqrt_ - 1) / 2) + (int)(sqrt_ > (int)sqrt_);
    
    if(label == base)
        return data[pivot];

    int left = data[pivot] + banana(pivot + label, data, base);


    int right = data[pivot] + banana(pivot + label + 1, data, base);

    return left > right ? left : right;
}

void main()
{
    srand(time(NULL));

    unsigned int base = 0;
    printf("Please insert the base of the pyramid-v4:\n>> ");
    scanf(" %llu", &base);

    size_t length = (base * (base + 1)) / 2;

    int8 * data = malloc(length);
    for(size_t i = 0; i < length; i++)
        data[i] = rand() % 100;


    size_t prints = 0;
    for(int m=1; m<=base; m++)
    {
        for(int b=0; b<base-m; b++)
            printf("    ");
        for(int n=0; n<m; n++)
            printf("%d      ", data[prints++]);
        printf("\n");
    }


    int a = banana(0, data, base);
    printf("FINISH");
    printf("\n best acc:\t %d", a);
}