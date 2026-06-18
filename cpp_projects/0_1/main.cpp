#include <iostream>
using namespace std;
//switch case and while loop
int main(){
    int choice = 0;

    while(choice != 4){
        cout << "Enter number (1-4): ";
        cin >> choice;
        switch (choice)
        {
        case 1:
            cout << "it's 1st choice";
            break;
        case 2:
            cout << "it's 2nd choice";
            break;
        case 3:
            cout << "it's 3rd choice";
            break;
        case 4:
            cout << "it's 4th choice";
            break;
        default:
            cout << "default";
            break;
        }
    }




    return 0;
}