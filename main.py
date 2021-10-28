empty = " "
player = "o"
computer = "x"

class Board:
    def __init__(self):
        self.board = []

        for y in range(3):
            row = []

            for x in range(3):
                row.append(empty)

            self.board.append(row)
        
    def __str__(self):
        string = "The current board is\n"

        for row in self.board:
            for col in row:
                string += col + " "

            string += "\n"

        return string

    def place(self, x, y, token):
        self.board[y][x] = token
        return token

def are_moves_left(board):
    for y in range(3):
        for x in range(3):
            if board[y][x] == empty:
                return True; 
    return False; 

def evaluate(b):
    for y in range(3):

        if b[y][0] == b[y][1] and b[y][1] == b[y][2]:

            if b[y][0] == computer:
                return 10

            elif b[y][0] == player:
                return -10
  
    for x in range(3):

        if b[0][x] == b[1][x] and b[1][x] == b[2][x]:

            if b[0][x] == computer:
                return 10
  
            elif b[0][x] == player:
                return -10
  
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:

        if b[0][0] == computer:
            return 10
        elif b[0][0] == player:
            return -10
  
    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:

        if b[0][2] == computer:
            return 10

        elif b[0][2] == player:
            return -10
  
    return 0; 

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 10:
        return score
  
    if score == -10:
        return score

    if not are_moves_left(board):
        return 0

    if is_maximizing:
        best = -1000
  
        for y in range(3):
            for x in range(3):
                if board[y][x] == empty:
                    board[y][x] = computer
  
                    best = max(best, minimax(board, depth + 1, not is_maximizing))
  
                    board[y][x] = empty

        return best
  
    else:
        best = 1000
  
        for y in range(3):
            for x in range(3):
                if board[y][x] == empty:
                    board[y][x] = player
  
                    best = min(best, minimax(board, depth + 1, not is_maximizing))
  
                    board[y][x] = empty

        return best

def find_best_move(board):
    best_val = -1000
    best_x = -1
    best_y = -1
  
    for y in range(3):
        for x in range(3):
            if board[y][x] == empty: 
                board[y][x] = computer
  
                move_val = minimax(board, 0, True); 
  
                board[y][x] = empty
  
                if move_val > best_val:
                    best_x = x
                    best_y = y
                    best_val = move_val

    return [best_x, best_y]

def rotate_board(board):
    for x in range(3 / 2):
        for y in range(3 - x - 1):
            temp = board[x][y]
  
            board[x][y] = board[y][3 - 1 - x]
  
            board[y][3 - 1 - x] = board[3 - 1 - x][3 - 1 - y]
  
            board[3 - 1 - x][3 - 1 - y] = board[3 - 1 - y][x]
  
            board[3 - 1 - y][x] = temp

def check_winner(board):
    for i in [player, computer]:
        if board[0] == [i, i, i] or board[1] == [i, i, i] or board[2] == [i, i, i]:
            return i
        
        rotate_board(board)

        if board[0] == [i, i, i] or board[1] == [i, i, i] or board[2] == [i, i, i]:
            return i

        rotate_board(board)
        rotate_board(board)
        rotate_board(board)

        if board[0][0] == i and board[1][1] == i and board[2][2] == i:
            return i

        if board[0][2] == i and board[1][1] == i and board[2][0] == i:
            return i
    
    return empty
    

board = Board()

while True:
    print(board)

    x = input("Enter the x coordinate: ")
    y = input("Enter the y coordinate: ")

    board.place(x, y, player)

    winner = check_winner(board.board)

    if winner != empty:
        print(board)

        if winner == player:
            print("You won!")
            break
        else:
            print("You lost!")
            break

    best_move = find_best_move(board.board)

    board.place(best_move[0], best_move[1], computer)    
