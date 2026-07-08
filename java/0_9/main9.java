import java.util.Scanner;

//calculator programm

public class main9{

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your operation (+, -, *, /): ");
        String operation = scanner.next();

        double num1, num2;

        double result = 0;
        switch (operation) {
            case "+":
                System.out.print("Enter your first number: ");
                num1 = scanner.nextDouble();

                System.out.print("Enter your second number: ");
                num2 = scanner.nextDouble();
                result = num1 + num2;

                break;
            case "-":
                System.out.print("Enter your first number: ");
                num1 = scanner.nextDouble();

                System.out.print("Enter your second number: ");
                num2 = scanner.nextDouble();
                result = num1 - num2;
                break;
            case "*":
                System.out.print("Enter your first number: ");
                num1 = scanner.nextDouble();

                System.out.print("Enter your second number: ");
                num2 = scanner.nextDouble();
                result = num1 * num2;
                break;
            case "/":
                System.out.print("Enter your first number: ");
                num1 = scanner.nextDouble();

                System.out.print("Enter your second number: ");
                num2 = scanner.nextDouble();
                if (num2 == 0) {
                    System.out.println("Error: Division by zero is not allowed.");
                    scanner.close();
                    return;
                }
                result = num1 / num2;
                break;
            default:
                System.out.println("Invalid operation!");
                scanner.close();
                return;
        }
        System.out.println("The result is: " + result);

        scanner.close();
    }
}