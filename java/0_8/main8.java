import java.util.Scanner;

//STRING METHODS
public class main8{

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        String name = "John Doe";

        int len = name.length();
        char letter = name.charAt(3);
        int index = name.indexOf('o');
        int lastIndex = name.lastIndexOf('o');
        String upper = name.toUpperCase();
        String lower = name.toLowerCase();
        boolean empty = name.isEmpty();


        System.out.println("Length of the name: " + len);
        System.out.println("Character at index 3: " + letter);
        System.out.println("Index of first occurrence of 'o': " + index);
        System.out.println("Index of last occurrence of 'o': " + lastIndex);
        System.out.println("Name in uppercase: " + upper);
        System.out.println("Name in lowercase: " + lower);
        System.out.println("Is the name empty? " + empty);

        scanner.close();
    }
}