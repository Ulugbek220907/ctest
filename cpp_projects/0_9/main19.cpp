#include <iostream>

//Static member and functions
using namespace std;

class Car {
    static int number_of_cars;
    string color, model;
    int year;
    
    public:
        Car(){color = ""; model = ""; year = 2000; number_of_cars++;};

        Car(string c, string m, int y) : color(c), model(m), year(y){ number_of_cars++;};

        void displayinfo(){
            cout << "Color is: " << color << endl;
            cout << "Model is: " << model << endl;
            cout << "Year is: " << year << endl;
        }

        static int getTotalCars(){
            return number_of_cars;
        }

        ~Car(){
            number_of_cars--;
        }



};

int Car::number_of_cars = 0;

int main(){

    Car c1("efnk", "efnj", 1234);
    Car c2("fdnk", "defn", 345);

    cout << Car::getTotalCars();


    return 0;
}