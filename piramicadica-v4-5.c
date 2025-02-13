#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

typedef signed char int8;

int search(size_t pivot, int8 * data, int8 * ways, size_t base, size_t * count)
{
    float sqrt_ = sqrt( 8 * pivot + 2);
    unsigned int label = (int)((sqrt_ - 1) / 2) + (int)(sqrt_ > (int)sqrt_);
    if(label == base)
        return data[pivot];

    int left = search(pivot + label, data, ways, base, count);
    int right = search(pivot + label + 1, data, ways, base, count);
    ways[pivot] = (int)(right > left);

    // *(count++);

    return left > right ?  data[pivot] + left :  data[pivot] + right;
}

void main()
{
    srand(time(NULL));

    unsigned int base = 0;
    printf("Please insert the base of the pyramid-v4:\n>> ");
    scanf(" %u", &base);

    size_t length = (base * (base + 1)) / 2;
    size_t * count = 0;

    int8 * data = malloc(length);
    int8 * ways = malloc(length-base);
    for(size_t i = 0; i < length; i++)
        data[i] = rand() % 10;


    size_t prints = 0;
    for(int m=1; m<=base; m++)
    {
        for(int b=0; b<base-m; b++)
            printf("    ");
        for(int n=0; n<m; n++)
            printf("%d      ", data[prints++]);
        printf("\n");
    }

    printf("\n\nFINISH");
    printf("\n best acc:\t %d\n\n\n\n", search(0, data, ways, base, count));


    prints = 0;
    for(int m=1; m<=base-1; m++)
    {
        for(int b=0; b<base-m; b++)
            printf("    ");
        for(int n=0; n<m; n++)
            printf("%d      ", ways[prints++]);
        printf("\n");
    }
    free(data);
    free(ways);
    // printf("\n\n\n aqui\n%zu", *count);
}