#include <stdio.h>
#include <stdlib.h>

//dynamic memory allocation example


int main(){
    int n = 0, m = 0;

    printf("Enter a number of elements you want to store: ");
    scanf("%d", &n);
    int *allocation = (int*)malloc(n * sizeof(int));
    if (allocation == NULL){
        printf("Memory allocation failed.\n");
        return 1;
    }
    while (n != 0){
        printf("Enter a number to store: ");
        int input;
        scanf("%d", &input);
        // Store the input in the allocated memory
        allocation[m] = input;
        m++;
        n--;

    }

    for (int i = 0; i < m; i++){
        printf("Stored number: %d\n", allocation[i]);
    }


    free(allocation);
    allocation = NULL;


    return 0;
}