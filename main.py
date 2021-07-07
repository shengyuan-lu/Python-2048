from utilities import place_random, print_board

DEV_MODE = False

def listReverse(input_list): 
    return [ele for ele in reversed(input_list)] 

def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # Capture game_board from input
    board = game_board
    
    # Initialize board's first cell
    # You are not required to implement develop mode, but it is encouraged to do so.
    # Develop mode allows you to input the location of the next piece that will be
    # placed on the board, rather than attempting to debug your code with random
    # input values.
    if DEV_MODE == True:
        # This line of code handles the input of the develop mode.
        
        for _ in range(0,2):
            
            row = -1
            column = -1
            value = -1
        
            while (row not in (1,2,3,4)) and (column not in (1,2,3,4)) and (value not in (2,4)):
                a, b, c = (int(i) for i in input("column,row,value:").split(','))
                
                row = a
                column = b
                value = c

                print('Dev Mode: INITIALIZE BOARD Piece placed at row {} column {} with value {}'.format(row, column, value))
                
            row -= 1
            column -= 1
        
            # OPTIONAL: place the piece in the corresponding cell on the game board
            board[row][column] = value
        
    else:
        # Generate a random piece and location using the place_random function
        
        for _ in range(0,2):
        
            pieceAdded = place_random(game_board) #PieceAdded is a dict

            row = pieceAdded['row']
            column = pieceAdded['column']
            value = pieceAdded['value']
        
            # Place the piece at the specified location
            board[row][column] = value
            print()
            print('Debug: INITIALIZE BOARD Piece placed at row {} column {} with value {}'.format(row + 1, column + 1, value))
        
    # Initialize game state trackers
    print_board(board)
    
    users_turn = True
    
    # Game Loop
    while True:
        
        # Reset user input variable
        user_input = ''
        
        # Take user's turn
        if users_turn == True:
            
            print('>>>> User\'s turn!') 
            user_input = input('What is your next move?\n')
        
            # Take input until the user's move is a valid key
            while user_input not in ('a', 'w', 's','d','q'):
                user_input = input('Invalid input. Try again. \n')
            
            # if the user quits the game, print Goodbye and stop the Game Loop
            if user_input == 'q':
                print('Goodbye')
                break
            elif user_input == '':
                print('Something\'s wrong. No user input.')
                break
        
            # TODO: Execute the user's move
            if (user_input == 'a'):
                
                new_game_board = []
                
                numRow = 0
                for index, row in enumerate(board):
                    
                    numRow += 1
                    emptyCellNum = 0
                    
                    for index, num in enumerate(row):
                        
                        current = index + 1
                        
                        while current in (1,2,3):
                            if row[current] != 0:
                                if row[index] == row[current]:
                                    row[index] = row[current] * 2
                                    row[current] = 0
                                    break
                                current += 1
                            elif row[current] == 0:
                                current += 1
                    
                    for index, num in enumerate(row):
                        if num == 0: 
                            emptyCellNum += 1
                    
                    row = [i for i in row if i != 0]
                    
                    for _ in range(0, emptyCellNum):
                        row.append(0)
                        
                    new_game_board.append(row)
                    print('Debug: row #{} is {}'.format(numRow, row))
                   
                board = new_game_board
                
            elif user_input == 'd':
               
                new_game_board = []
                numRow = 0
                
                for index, row in enumerate(board):
                    
                    numRow += 1
                    emptyCellNum = 0
                    
                    new_row = listReverse(row)
                    print('Debug: old row is {} new row is {}'.format(row, new_row))
                    
                    for index, num in enumerate(new_row):
                        
                        current = index + 1
                        
                        while current in (1,2,3):
                            if new_row[current] != 0:
                                if new_row[index] == new_row[current]:
                                    new_row[index] = new_row[current] * 2
                                    new_row[current] = 0
                                    break
                                current += 1
                            elif new_row[current] == 0:
                                current += 1
                    
                    for index, num in enumerate(new_row):
                        if num == 0: 
                            emptyCellNum += 1
                    
                    new_row = [i for i in new_row if i != 0]
                    
                    for _ in range(0, emptyCellNum):
                        new_row.append(0)

                    new_row = listReverse(new_row)
                    new_game_board.append(new_row)
                    print('Debug: row #{} is {}'.format(numRow, new_row))
                   
                board = new_game_board

            elif user_input == 'w':
                
                tempNum = 0
                emptyCellNum = 0
                new_column = []

                for _ in range(0, 4):
                    
                    for index, row in enumerate(board):

                        new_column.append(board[index][tempNum])

                    for index, num in enumerate(new_column):

                        current = index + 1

                        while current in (1, 2, 3):
                            if new_column[current] != 0:
                                if new_column[index] == new_column[current]:
                                    new_column[index] = new_column[current] * 2
                                    new_column[current] = 0
                                    break
                                current += 1
                            elif new_column[current] == 0:
                                current += 1

                    for index, num in enumerate(new_column):
                        if num == 0:
                            emptyCellNum += 1

                    new_column = [i for i in new_column if i != 0]
    
                    for _ in range(0, emptyCellNum):
                        new_column.append(0)

                    for index, num in enumerate(new_column):
                        board[index][tempNum] = num

                    tempNum += 1
                    new_column = []
                    emptyCellNum = 0
            
            elif user_input == 's':
                
                tempNum = 0
                emptyCellNum = 0
                new_column = []

                for _ in range(0, 4):
                    
                    for index, row in enumerate(board):

                        new_column.append(board[index][tempNum])
                    
                    new_column = listReverse(new_column)

                    for index, num in enumerate(new_column):

                        current = index + 1

                        while current in (1, 2, 3):
                            if new_column[current] != 0:
                                if new_column[index] == new_column[current]:
                                    new_column[index] = new_column[current] * 2
                                    new_column[current] = 0
                                    break
                                current += 1
                            elif new_column[current] == 0:
                                current += 1

                    for index, num in enumerate(new_column):
                        if num == 0:
                            emptyCellNum += 1

                    new_column = [i for i in new_column if i != 0]
    
                    for _ in range(0, emptyCellNum):
                        new_column.append(0)

                    new_column = listReverse(new_column)
                    
                    for index, num in enumerate(new_column):
                        board[index][tempNum] = num

                    tempNum += 1
                    new_column = []
                    emptyCellNum = 0
            
            elif user_input == '':
                print('Gameboard full. Can\'t move in this direction.')
            
            # Check if the user wins
            status = game_over(board)
            if status == True:
                print('Game over, you won!')
                break
            
            elif status == False:
                users_turn = False
                
                # Show updated board using the print_board function
                print_board(board)
                
        # Take computer's turn
        if users_turn == False: 
            
            print('>>>> Computer\'s turn!')
            pieceAdded = place_random(board) #PieceAdded is a dict

            row = pieceAdded['row']
            column = pieceAdded['column']
            value = pieceAdded['value']
            
            # place a random piece on the board
            board[row][column] = value
            print('Debug: Piece placed at row {} column {} with value {}'.format(row + 1, column + 1, value))
            
            # check to see if the game is over using the game_over function
            status = game_over(board)
            if status == True:
                print('Game over, you lost!')
                break
            
            elif status == False:
                users_turn = True
                
                # Show updated board using the print_board function
                print_board(board)
                
    return board

# END OF main() Function

def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    # Loop over the board and determine if the game is over
    num_of_empty_blocks = 0
    
    # Determine how many empty blocks are there and the win condition
    for row in game_board:
        
        for num in row:
            if num == 0:
                num_of_empty_blocks += 1
            elif num == 2048:
                print('Condition Debug: Game OVER, user won, achieved 2048')
                return True 

    
    # Determine lose conditon
    if num_of_empty_blocks == 0:
    
        # Check if there are match blocks in horizontal direction

        for index, row in enumerate(game_board):
            
            for index, num in enumerate(row):
            
                if index in (0, 1, 2):
                    
                    if row[index] == row[index + 1]:
                        print('Condition Debug: Game NOT over, Gameboard FULL, there can be more matches in the horizonal direction')
                        return False 
                        
        # Check if there are match blocks in vertical direction
        for index, row in enumerate(game_board):
            
            if index in (0,1,2):
                
                for i in range(0, 3):
                    
                    if game_board[index][i] == game_board[index + 1][i]:
                        print('Condition Debug: Game NOT over, Gameboard FULL, there can be more matches in the vertical direction')
                        return False 
                        
        print('Condition Debug: Game OVER, user lost, there are no more empty blocks and no potential matches')
        return True 
            
    elif num_of_empty_blocks != 0:
        print('Condition Debug: Game NOT over, there are more empty blocks')
        return False
    
# End of game_over function
    
if __name__ == "__main__":
   
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])
