import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Hello, World!");

        //Arraylist is dynamic array which can grow as needed
        ArrayList<Integer> arrayl = new ArrayList<>();
        arrayl.add(10);
        arrayl.add(243);
        arrayl.add(3);
        arrayl.add(4);
        arrayl.add(1);
        arrayl.add(1);

        //methods

        // remove = removes an element from the arraylist
        arrayl.remove(1);

        // size = returns the number of elements in the arraylist
        System.out.println(arrayl.size());

        // set = replaces an element at a specific index with a new value
        arrayl.set(1, 4);

        // get = returns the element at a specific index
        int element = arrayl.get(1);
        System.out.println(element);

        // clear = removes all elements from the arraylist
        // arrayl.clear();

        Collections.sort(arrayl);

        System.out.println(arrayl);

        while (true) {
            System.out.println("Enter number(-1 to quit): ");
            int num = scanner.nextInt();
            if (num == -1) {
                break;
            }
            arrayl.add(num);
        }

        System.out.println("Final ArrayList: " + arrayl);

        scanner.close();

    }
}




