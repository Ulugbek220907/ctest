public class Car {
    //attributes
    int year;
    String model;
    String color;

    Car(String model, String color, int year){
        this.color = color;
        this.model = model;
        this.year = year;
    }

    void display(){
        System.out.println("model: " + model + " color: " + color + " year: " + year);
    }

    void start(){
        System.out.println("Car started!");
    }

}
