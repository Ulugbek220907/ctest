startpos = (2, 2)  # Starting position of the ship
#map = [[0 for _ in range(5)] for _ in range(5)]  # Create a 5x5 map initialized with zeros
#player is 1
map = [[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]

#to print the map
def print_map():
    print(startpos)
    for i in range(len(map)):
        print(map[i])

#clear the map
def clear_map():
    for i in range(len(map)):
        for j in range(len(map[i])):
            map[i][j] = 0

#starting position of the player
map[int(startpos[0])][int(startpos[1])] = 1

#prints
print_map()
#takes user input for the next position of the ship
pos = int(input("Enter the position to place the ship (up(0), down(1), left(2), right(3), quit(4))): "))

#takes new cordination and clears the map and places the ship in the new position
while pos != 4:
    match pos:
        case 0:
            if startpos[0] == 0:
                print("Cannot move up. Already at the top edge of the map.")
                pos = int(input("Enter the position to place the ship (up(0), down(1), left(2), right(3), quit(4))): "))
                continue
            startpos = (startpos[0] - 1, startpos[1])
            clear_map()
            map[int(startpos[0])][int(startpos[1])] = 1
        case 1:
            if startpos[0] == len(map) - 1:
                print("Cannot move down. Already at the bottom edge of the map.")
                pos = int(input("Enter the position to place the ship (up(0), down(1), left(2), right(3), quit(4))): "))
                continue
            startpos = (startpos[0] + 1, startpos[1])
            clear_map()
            map[int(startpos[0])][int(startpos[1])] = 1
        case 2:
            if startpos[1] == 0:
                print("Cannot move left. Already at the left edge of the map.")
                pos = int(input("Enter the position to place the ship (up(0), down(1), left(2), right(3), quit(4))): "))
                continue
            startpos = (startpos[0], startpos[1]-  1)
            clear_map()
            map[int(startpos[0])][int(startpos[1])] = 1
        case 3:
            if startpos[1] == len(map[0]) - 1:
                print("Cannot move right. Already at the right edge of the map.")
                pos = int(input("Enter the position to place the ship (up(0), down(1), left(2), right(3), quit(4))): "))
                continue
            startpos = (startpos[0], startpos[1] + 1)
            clear_map()
            map[int(startpos[0])][int(startpos[1])] = 1
        case 4:
            print("Exiting the program.")
            break
        case _:
            print("Invalid input. Please enter a valid position.")
    
    print_map()
    pos = int(input("Enter the position to place the ship (up(0), down(1), left(2), right(3), quit(4))): "))
    