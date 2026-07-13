import java.io.FileWriter;
import java.io.IOException;

public class main21{
    public static void main(String[] args) {
        System.out.println("Hello, World!");

        try(FileWriter writer = new FileWriter("output.txt")) {
            writer.write("Hello, World!");
            System.out.println("Successfully wrote to the file.");
        } catch (IOException e) {
            System.out.println("An error occurred while writing to the file.");
        }
    }
}