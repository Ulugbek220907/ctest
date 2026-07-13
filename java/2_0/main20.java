import java.util.Scanner;
// exception handling
public class main20 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Hello, World!");
        
        int a = 10;
        int b = 0;

        System.out.print("Enter a number to divide 10 by: ");
        b = scanner.nextInt();
        
        try {
            int c = a / b;
            System.out.println(c);
        } catch (ArithmeticException e) {
            System.out.println("Error: Division by zero is not allowed.");
        } finally {
            System.out.println("This block will always execute.");
        }

        scanner.close();

    }
}
