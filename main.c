#include <stdio.h>
#include <stdlib.h>

// Struct definition for our inventory item node
struct ItemNode {
    int itemID;
    int quantity;
    struct ItemNode *next;
};

// Function helper to print the backpack items
void printInventory(struct ItemNode *head) {
    printf("\n=== Backpack Contents ===\n");
    if (head == NULL) {
        printf("The backpack is empty!\n");
        return;
    }
    
    struct ItemNode *current = head;
    while (current != NULL) {
        //prints each element in the list
        printf("Item ID: %d | Qty: %d -> ", current->itemID, current->quantity);
        current = current->next;
    }
    printf("NULL\n=========================\n");
}

int main() {
    // ==========================================
    // Allocate and link 3 starter items
    // ==========================================
    
    // Allocate pointers
    struct ItemNode *head = (struct ItemNode*)malloc(sizeof(struct ItemNode));
    struct ItemNode *second = (struct ItemNode*)malloc(sizeof(struct ItemNode));
    struct ItemNode *third = (struct ItemNode*)malloc(sizeof(struct ItemNode));
    struct ItemNode *goldenring = (struct ItemNode*)malloc(sizeof(struct ItemNode));

    
    // Item 1 (head): ID 101, Qty 5, links to second quest - 1 done
    head->itemID = 101;
    head->quantity = 5;
    head->next = second;
    
    // Item 2 (second): ID 102, Qty 1, links to third
    second->itemID = 102;
    second->quantity = 1;
    second->next = third;
    
    // Item 3 (third): ID 103, Qty 1, links to NULL
    third->itemID = 103;
    third->quantity = 1;
    third->next = NULL;
    

    printf("Initial backpack check:");
    printInventory(head);


    // ==========================================
    // Use 3 health potions (ID: 101)
    // ==========================================
    printf("\nDrinking 3 health potions...\n");
    
    struct ItemNode *current = head;

    while (current != NULL){
        if (current->itemID == 101){
            current->quantity -= 3;
            break;
        }
        current = current->next;
    }
    
    printInventory(head);


    // ==========================================
    //  Insert "Golden Ring" (ID: 200, Qty: 1)
    //          between second (102) and third (103)
    // ==========================================
    printf("\nFound a Golden Ring! Inserting into backpack...\n");
    
    struct ItemNode *newRing = (struct ItemNode*)malloc(sizeof(struct ItemNode));
    // TODO: Initialize newRing data (ID 200, Qty 1)
    second->next = newRing;
    newRing->next = third;
    newRing->itemID = 200;
    newRing->quantity = 1;
    
    printInventory(head);


    // ==========================================
    // Free all allocated memory
    // ==========================================
    printf("\nClearing inventory and cleaning memory...\n");
    
    
    
    printf("Backpack cleared safely! Adventurer retired.\n");
    free(head);
    free(second);
    free(third);
    free(newRing);
    free(current);
    head = NULL;
    second = NULL;
    third = NULL;
    newRing = NULL;
    current = NULL;
    return 0;
}
