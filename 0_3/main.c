#include <stdio.h>

int main(){
    double balance = 0.0;
    int choice;
    while (choice != 4){
        printf("1.Check Balance\n");
        printf("2.Deposit\n");
        printf("3.Withdraw\n");
        printf("4.Exit\n");
        printf("Enter your choice(1-4): ");
        scanf("%d", &choice);
        switch(choice) {
            case 1:
                printf("Your balance is: $%.2f\n", balance);
                break;
            case 2:
                printf("Enter amount to deposit: ");
                double deposit;
                scanf("%lf", &deposit);
                balance += deposit;
                printf("You have deposited $%.2f\n", deposit);
                break;
            case 3:
                printf("Enter amount to withdraw: ");
                double withdraw;
                scanf("%lf", &withdraw);
                if (withdraw > balance) {
                    printf("Insufficient funds. Your balance is $%.2f\n", balance);
                } else {
                    balance -= withdraw;
                    printf("You have withdrawn $%.2f\n", withdraw);
                }
                break;
            case 4:
                printf("Exiting the program... :)\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}