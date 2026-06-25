#include <iostream>

using namespace std;


class Shape{
    public:
        double area = 0;

        virtual double Area(){
            return area;
        }

        virtual void display(){
            cout << "\nArea is: " << area;
        }
        virtual ~Shape() = default;
};

class Triangle : public Shape{
    public:
        double height, base;
        Triangle(double h, double b) : height(h), base(b){};
        double Area() override {
            area = base*height*0.5;
            return area;
        }
        void display() override{
            cout << "\nTriangle area is: " << area;
        }
};


class Circle : public Shape{
    public:
        double radius;
        Circle(double r) : radius(r){};
        double Area() override {
            area = 3.14159 * radius * radius;
            return area;
        }
        void display() override{
            cout << "\nCircle area is: " << area;
        }
};

class Rectangle : public Shape{
    public:
        double length, width;
        Rectangle(double l, double w) : length(l), width(w){};

        double Area() override {
            area = length*width;
            return area;
        }
        void display() override{
            cout << "\nRectangle area is: " << area;
        }
};



int main(){
    Shape *a = new Triangle(11, 7);
    Shape *b = new Circle(12);
    Shape *c = new Rectangle(23, 45);

    a->Area();
    a->display();
    b->Area();
    b->display();
    c->Area();
    c->display();

    delete b;
    delete c;
    delete a;

    return 0;
}