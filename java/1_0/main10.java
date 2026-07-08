import java.util.Scanner;
//methods
public class main10{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        square(16);
        getfullname("John", "Doe");
        circumference(5);

        scanner.close();
    }

    static double square(double number){
        double result = number * number;
        System.out.println("The square of " + number + " is: " + result);
        return result;
    }
    static String getfullname(String firstName, String lastName){
        String fullName = firstName + " " + lastName;
        System.out.println("Full name: " + fullName);
        return fullName;
    }
    static double circumference(double radius){
        double result = 2 * Math.PI * radius;
        System.out.printf("The circumference of a circle with radius " + radius + " is: %.3f\n", result);
        return result;
    }

}