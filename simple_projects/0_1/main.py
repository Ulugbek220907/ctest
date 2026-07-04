#chess game
#board
list1 = [['OR1', 'OO1', 'OF1', 'OS', 'OA', 'OF2', 'OO2', 'OR2'],
         ['OP1', 'OP2', 'OP3', 'OP4', 'OP5', 'OP6', 'OP7', 'OP8'],
         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
         ['QP1', 'QP2', 'QP3', 'QP4', 'QP5', 'QP6', 'QP7', 'QP8'],
         ['QR1', 'QO1', 'QF1', 'QS', 'QA', 'QF2', 'QO2', 'QR2'],]#8

#figures
dict1 = {
    'OR1': (0, 0),  #rock 1 white
    'OO1': (0, 1), #knight 1 white
    'OF1': (0, 2), #bishop 1 white
    'OS': (0, 3), #king white
    'OA': (0, 4), #queen white
    'OF2': (0, 5), #bishop 2 white
    'OO2': (0, 6), #knight 2 white
    'OR2': (0, 7), #rock 2 white

    'OP1': (1, 0), #pawn 1 white
    'OP2': (1, 1), #pawn 2 white
    'OP3': (1, 2), #pawn 3 white
    'OP4': (1, 3), #pawn 4 white
    'OP5': (1, 4), #pawn 5 white
    'OP6': (1, 5), #pawn 6 white
    'OP7': (1, 6), #pawn 7 white
    'OP8': (1, 7), #pawn 8 white

    'QP1': (6, 0), #pawn 1 black
    'QP2': (6, 1), #pawn 2 black
    'QP3': (6, 2), #pawn 3 black
    'QP4': (6, 3), #pawn 4 black
    'QP5': (6, 4), #pawn 5 black
    'QP6': (6, 5), #pawn 6 black
    'QP7': (6, 6), #pawn 7 black
    'QP8': (6, 7), #pawn 8 black

    'QR1': (7, 0), #rock 1 black
    'QO1': (7, 1), #knight 1 black
    'QF1': (7, 2), #bishop 1 black
    'QS': (7, 3), #king black
    'QA': (7, 4), #queen black
    'QF2': (7, 5), #bishop 2 black
    'QO2': (7, 6), #knight 2 black
    'QR2': (7, 7) #rock 2 black
}


def print_board():
    for i in range(len(list1)):
        print(i+1, list1[i])


print_board()

movefigure = input('Enter figure to move(name, example: OP1): ')
movetargety, movetargetx = input('Enter target position(x, y): ').split(',')

"""
if list1[int(movetargetx) - 1][int(movetargety) - 1] != '   ':
    print('Target position is not empty')
"""


if movefigure=='OP1' in dict1:
    x, y = dict1[movefigure]
    list1[x][y] = '   '
    dict1[movefigure] = (int(movetargetx) - 1, int(movetargety) - 1)
    x, y = dict1[movefigure]
    list1[x][y] = movefigure
    
print_board()