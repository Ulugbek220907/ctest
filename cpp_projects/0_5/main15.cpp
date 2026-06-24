#include <iostream>
using namespace std;

class BankAccount{
    private:
        double balance;
        int account_number;
    public:

        BankAccount (double b, int accnum) {
            balance = b;
            account_number = accnum;
        }

        void display(){
            cout << "\n\nYour balance: " << balance;
            cout << "\nAccount number is: " << account_number;
        }

        void withdraw(double amount){
            if (amount > balance){
                cout << "Not enough funding!\n";
            } else if (amount <= 0) {
                cout << "Wrong amount entered!\n";
            } else {
                balance -= amount;
            }
        }

        void deposit(double amount){
            if (amount <= 0) {
                cout << "Wrong amount entered!\n";
            } else {
                balance += amount;
            }
        }
};

int main(){
    

    
    int choice, ai = 0;
    double b = 0;
    BankAccount account(0, 123);
    
    while (choice != 5){
        cout << "1.Enter account\n2.Deposit\n3.Withdraw\n4.Display\n5.Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice)
        {
        case 1:
            
            cout << "Success!\n";
            break;
        case 2:{
            double amount = 0;
            cout << "Enter deposit amount: ";
            cin >> amount;
            account.deposit(amount);
            break;
        }
        case 3:{
            double amount = 0;
            cout << "Enter withdraw amount: ";
            cin >> amount;
            account.withdraw(amount);
            break;

        }
        case 4:
            account.display();
            break;
        default:
            cout << "\nExiting programm...\n";
            break;
        }
    }

    return 0;
}