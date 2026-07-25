
list1 = []
while(True):
    print("---   ---")
    print("1.Enter numbers to store")
    print("2.Display numbers")
    print("3.Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter number please!")
    match(choice):
        case 1:
            
            num = int(input("Enter a number to store: "))
            list1.append(num)

        case 2:
            print(list1)
        case 3:
            print("Exiting...")
            break
        case _:
            print("Enter a valid choice!")
            pass

