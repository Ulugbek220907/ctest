#include <iostream>
#include <cstring>


//Basic Class Structure

using namespace std;

class Person{
    int age;
    string name;
    public:
        
        void setname(string n){name = n;};
        void setage(int a) {age = a;};


        void displayinfo(){
            cout << "Age: " << age << endl;
            cout << "Name: " << name << endl;
        }


};

int main(){
    Person p1;
    p1.setname("durbek");
    p1.setage(12);

    p1.displayinfo();

    return 0;
}