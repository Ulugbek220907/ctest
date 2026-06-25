#include <iostream>
#include <vector>

using namespace std;

// Class to represent a book library, simple OOP example

class Book{
    public:
        string title;
        string author;
        int isbn;

        Book(string t, string a, int i){
            title = t;
            author = a;
            isbn = i;
        }

        void display(){
            cout << "Title: " << title << endl;
            cout << "Author: " << author << endl;
            cout << "ISBN: " << isbn << endl;
        }

        void searchtitle(string t){
            if (title == t){
                cout << "Book found!" << endl;
                display();
            }
        }
};


int main(){
    vector<Book> books;
    int choice;
    
    while (choice != 5){
        cout << "1. Enter book details\n";
        cout << "2. Display all books\n";
        cout << "3. Search for a book\n";
        cout << "4. Update book details\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice)
        {
        case 1:{
            int numofbook;
            cout << "Enter how many books you want to enter: ";
            cin >> numofbook;
            for (int i = 0; i < numofbook; i++){
                string title, author;
                int isbn;
                cout << i + 1 << ". Enter the title: ";
                cin >> title;
                cout << "Enter the author: ";
                cin >> author;
                cout << "Enter the ISBN: ";
                cin >> isbn;
                books.push_back(Book(title, author, isbn));
            }
            break;
        }
        case 2:{
            for (int i = 0; i < books.size(); i++){
                cout << "Book " << i + 1 << endl;
                books[i].display();
            }
            break;
        }
        case 3:{
            string searchTitle;
            cout << "Enter the title of the book to search for: ";
            cin >> searchTitle;
            for (int i = 0; i < books.size(); i++){
                books[i].searchtitle(searchTitle);
            }
            break;
        }
        case 4:{
            string updateTitle;
            cout << "Enter the title of the book to update: ";
            cin >> updateTitle;
            for (int i = 0; i < books.size(); i++){
                if (books[i].title == updateTitle){
                    cout << "Book found!" << endl;
                    books[i].display();
                    cout << "Enter the new title: ";
                    cin >> books[i].title;
                    cout << "Enter the new author: ";
                    cin >> books[i].author;
                    cout << "Enter the new ISBN: ";
                    cin >> books[i].isbn;
                    break;
                }
            }
            break;
        }
        case 5:
            cout << "Exiting the program." << endl;
            break;
        default:
            cout << "\nInvalid choice. Please try again.\n" << endl;
            break;
        }
    }
    
    return 0;
}