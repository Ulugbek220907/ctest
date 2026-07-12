import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Person person = new Person("", 0);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        person.setName(name);
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        person.setAge(age);
        System.out.println("Hello, " + person.getName() + "! You are " + person.age() + " years old.");
    }
}