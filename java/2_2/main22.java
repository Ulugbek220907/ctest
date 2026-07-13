import java.util.Scanner;
import java.io.FileWriter;
import java.util.ArrayList;
import java.io.IOException;



public class main22 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("---Your notebook!---");

        ArrayList<String> lines = new ArrayList<>();
        
        System.out.println("Enter your notes (type 'exit' to finish):");
        while (true) {
            String line = scanner.nextLine();
            if (line.equalsIgnoreCase("exit")) {
                break;
            }
            lines.add(line);
        }

        try (FileWriter writer = new FileWriter("notebook.txt")) {
            for (String line : lines) {
                writer.write(line + System.lineSeparator());
            }
            System.out.println("Your notes have been saved to notebook.txt.");
        } catch (IOException e) {
            System.out.println("An error occurred while saving your notes.");
        }
        finally {
            scanner.close();
        }


    }
}