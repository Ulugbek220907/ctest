#include <stdio.h>
#include <string.h>


int main() {
    char names[100][50] = {{0}};
    char tokens[100][50] = {{0}};
    int formula_count = 0;
    int choice = 0;
    while(4){
        printf("1.Add\n2.View all\n3.Search\n4.Exit\nEnter your choice: ");
        scanf("%d", &choice);
        switch(choice){
        case 1:
            printf("Enter your formula: ");
            fgets(names[formula_count], sizeof(names[formula_count][50]), stdin);
            
            break;
        case 2:
            break;
        case 3:

            break;
        case 4:
        printf("Exiting program...\n");
            break;
        default:
            printf("Something is wrong!\n");
            break;
        }
    }
    
    return 0;
}