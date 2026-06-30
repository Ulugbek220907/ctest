#include <stdio.h>
//simple struct example
typedef struct  {
    int id;
    char name[20];
    double price;

}Item;

int main(){
    Item item1 = {1, "Laptop", 999.99};
    Item item2 = {2, "Smartphone", 499.99};
    Item item3 = {3, "Tablet", 299.99};
    printf("Item ID: %d\n", item1.id);
    printf("Item Name: %s\n", item1.name);
    printf("Item Price: $%.2f\n", item1.price);
    printf("Item ID: %d\n", item2.id);
    printf("Item Name: %s\n", item2.name);
    printf("Item Price: $%.2f\n", item2.price);
    printf("Item ID: %d\n", item3.id);
    printf("Item Name: %s\n", item3.name);
    printf("Item Price: $%.2f\n", item3.price);
    return 0;
}