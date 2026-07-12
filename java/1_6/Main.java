//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Car car1 = new Car("CLS", "Black", 2010);
        Vehicle vehicle = new Vehicle("sth", "pink", 1200, 23.5);

        System.out.println(car1);
        car1.display();
        car1.start();
        vehicle.display();
        vehicle.start();


    }
}