#include <iostream>
#include <vector>

//OOP
using namespace std;

class Car {
    private:
    string color, model;
    int year;
    
    public:
        Car(){color = ""; model = ""; year = 2000;};

        Car(string c, string m, int y) : color(c), model(m), year(y){};

        void displayinfo(){
            cout << "Color is: " << color << endl;
            cout << "Model is: " << model << endl;
            cout << "Year is: " << year << endl;
        }


        ~Car(){
            
        }



};


int main(){
    vector<Car> cars;

    int choice;
    while (choice != 3){
        cout << "1.Enter car\n2.Display\n3.Exit\nEnter your choice: ";
        cin >> choice;
        switch (choice)
        {
        case 1:
            {
            string model, color;
            int year;
            cout << "Enter car model: ";
            cin >> model;
            cout << "Enter car color: ";
            cin >> color;
            cout << "Enter car year: ";
            cin >> year;
            cars.push_back(Car(color, model, year));
            break;
            }
        case 2:
            for (int i = 0; i < cars.size(); i++){
                cout << "\n---------------\n\n";
                cars[i].displayinfo();
                

            }
            break;
        case 3:
            cout << "Exitting...\n";

            break;
        default:
            break;
        }
    }



    return 0;
}