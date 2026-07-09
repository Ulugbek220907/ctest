import java.util.Arrays;
import java.util.Scanner;

public class main13{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        // array has fixed size, cannot be changed after initialization
        String[] names = {"Alice", "Bob", "Charlie", "David", "Eve"};
        int len = names.length;

        Arrays.sort(names); // sort the array in ascending order
        Arrays.fill(names, "Unknown"); // fill the array with a specific value. all the values will be Unknown

        System.out.println("Name: " + names[0]);
        System.out.println("Length: " + len);

        int elements;

        System.out.print("Enter how many elements you want to add to the array: ");
        elements = scanner.nextInt();
        scanner.nextLine(); // consume the newline character

        String[] items = new String[elements]; // create a new array with the specified size
        for(int i = 0; i < elements; i++){
            System.out.print("Enter an item: ");
            items[i] = scanner.nextLine();
        }


        scanner.close();
    }
}