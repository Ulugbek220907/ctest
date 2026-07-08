import java.util.Scanner;
//simple banking programm
public class main11{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int choice;
        double balance = 1000.0; // Initial balance
        
        while (true) {
            System.out.println("Welcome to the simple banking program!");
            System.out.println("Please select an option:");
            System.out.println("1. Check Balance");
            System.out.println("2. Deposit Money");
            System.out.println("3. Withdraw Money");
            System.out.println("4. Exit");
            System.out.print("Enter your choice (1-4): ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Your current balance is: $" + balance);
                    break;
                case 2:
                    System.out.println("Enter the amount to deposit:");
                    double depositAmount = scanner.nextDouble();
                    balance += depositAmount;
                    System.out.println("You have deposited: $" + depositAmount);
                    break;
                case 3:
                    System.out.println("Enter the amount to withdraw:");
                    double withdrawAmount = scanner.nextDouble();
                    if (withdrawAmount <= balance) {
                        balance -= withdrawAmount;
                        System.out.println("You have withdrawn: $" + withdrawAmount);
                    } else {
                        System.out.println("Insufficient funds.");
                    }
                    break;
                case 4:
                    System.out.println("Thank you for using the simple banking program. Goodbye!");
                    scanner.close();
                    return; // Exit the program
                default:
                    System.out.println("Invalid option. Please try again.");
                    break;
            }
        }

    }
}