import java.util.Scanner;


public class main4{


    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        String food;
        double price, total;
        int quantity;

        System.out.print("Enter food name: ");
        food = scanner.nextLine();

        System.out.print("Enter price: ");
        price = scanner.nextDouble();

        System.out.print("Enter quantity: ");
        quantity = scanner.nextInt();

        total = quantity * price;

        System.out.println("Food name: " + food);
        System.out.println("Price: " + price);
        System.out.println("Quantity: " + quantity);
        System.out.println("Total: " + total);

        scanner.close();
    }
}