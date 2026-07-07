import java.util.Scanner;

public class main2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        System.out.println("Your number is: " + number + "\nYour age is " + age);
        

        scanner.close();
    }

    
}
