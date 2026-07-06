
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

def isvalid(board):
    if len(board) != 9 or len(board[0]) != 9:
        return False
    for i in range(9):
        row = set()
        col = set()
        box = set()
        for j in range(9):
            if board[i][j] != ".":
                if board[i][j] in row:
                    return False
                row.add(board[i][j])
            if board[j][i] != ".":
                if board[j][i] in col:
                    return False
                col.add(board[j][i])
            box_row = 3 * (i // 3)
            box_col = 3 * (i % 3)
            if board[box_row + j // 3][box_col + j % 3] != ".":
                if board[box_row + j // 3][box_col + j % 3] in box:
                    return False
                box.add(board[box_row + j // 3][box_col + j % 3])
    return True

print(isvalid(board))