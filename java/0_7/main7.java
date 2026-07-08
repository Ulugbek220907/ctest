import java.util.Scanner;


public class main7{

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        
        double pi = Math.PI;
        double eular = Math.E;

        double result1 = 10;

        /*  Math methods
        result1 = Math.pow(result1, 2);
        result1 = -result1;
        result1 = Math.abs(result1);
        result1 = Math.sqrt(2);
        double result2 = Math.round(3.14); // result1 = 3.0. if it was 3.5+ result1 = 4.0
        double result3 = Math.ceil(3.14); // result1 = 4.0 round up
        double result4 = Math.floor(3.14); // result1 = 3.0 round down
        double result5 = Math.max(10, 20); // result1 = 20.0 max variable
        double result6 = Math.min(10, 20); // result1 = 10.0 min variable
        */

        System.out.println("Value of Pi: " + pi);
        System.out.println("Value of Euler's number: " + eular);
        System.out.println("Result of raising result1 to the power of 2: " + result1);



        scanner.close();
    }
}