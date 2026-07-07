import java.util.Scanner;

public class main2 {
    public static void main(String[] args) {
        //Area calculator
        double height, width, area;

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter width: ");
        width = scanner.nextDouble();

        System.out.print("Enter height: ");
        height = scanner.nextDouble();

        area = height*width;

        System.out.print("Area is " + area + "\n");


        //Volume calc

        System.out.print("Enter width: ");
        width = scanner.nextDouble();

        System.out.print("Enter height: ");
        height = scanner.nextDouble();

        System.out.print("Enter length: ");
        double length = scanner.nextDouble();

        double volume = length*width*height;

        System.out.print("Volume is " + volume + "\n");

        // student check

        System.out.print("Are you a student?: ");
        boolean isstudent = scanner.nextBoolean();

        System.out.print(isstudent);

        
        scanner.close();
    }

    
}
