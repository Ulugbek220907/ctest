public class Vehicle extends Car {
    double weight;

    Vehicle(String model, String color, int year, double weight){
        super(model, color, year);
        this.weight = weight;
    }

    void display() {
        System.out.println("model: " + this.model + " color: " + this.color + " year: " + this.year + " weight: " + weight);
    }

    @Override

    void start(){
        System.out.println("Vehicle started!");
    }

}
