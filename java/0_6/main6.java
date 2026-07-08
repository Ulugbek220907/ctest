import java.util.Scanner;
import java.util.Random;

public class main6{

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int number;
        double number2;
        boolean isEven;

        number = random.nextInt(1, 101);
        number2 = random.nextDouble(0.0, 10.0);
        isEven = random.nextBoolean();

        System.out.println("Random number generated: " + number);
        System.out.println("Random double generated: " + number2);
        System.out.println("Random boolean generated: " + isEven);

        scanner.close();
    }
}