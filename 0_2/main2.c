#include <stdio.h>


int main()
{
    double temperature = 0.0;
    double farenheit = 0.0;

    double kilometers = 0.0;
    double miles = 0.0;

    int choice;
    while (choice != 5){
        printf("\n");
        printf("Unit Converter Menu:\n");
        printf("1. Convert Celsius to Farenheit\n");
        printf("2. Convert Farenheit to Celsius\n");
        printf("3. Convert Kilometers to Miles\n");
        printf("4. Convert Miles to Kilometers\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            printf("\n");
            case 1:
                printf("Enter temperature in Celsius: ");
                scanf("%lf", &temperature);
                farenheit = (temperature * 9.0 / 5.0) + 32.0;
                printf("%.2lf Celsius is %.2lf Farenheit\n", temperature, farenheit);
                break;
            case 2:
                printf("Enter temperature in Farenheit: ");
                scanf("%lf", &farenheit);
                temperature = (farenheit - 32.0) * 5.0 / 9.0;
                printf("%.2lf Farenheit is %.2lf Celsius\n", farenheit, temperature);
                break;
            case 3:
                printf("Enter distance in Kilometers: ");
                scanf("%lf", &kilometers);
                miles = kilometers * 0.621371;
                printf("%.2lf Kilometers is %.2lf Miles\n", kilometers, miles);
                break;
            case 4:
                printf("Enter distance in Miles: ");
                scanf("%lf", &miles);
                kilometers = miles / 0.621371;
                printf("%.2lf Miles is %.2lf Kilometers\n", miles, kilometers);
                break;
            case 5:
                printf("Exiting the program... :)\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }
    

}