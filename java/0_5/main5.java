import java.util.Scanner;


public class main5{


    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int age = 10;
        //if else statement

        if (age < 18){
            System.out.println("You are a minor.");
        } else if (age >= 18 && age < 65){
            System.out.println("You are an adult.");
        } else {
            System.out.println("You are a senior citizen.");
        }

        scanner.close();
    }
}