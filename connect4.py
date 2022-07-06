"""
The module plays connect 4. It can either played by 2 human players, 1 human player and a computer player
or 2 computer players 
Name: Abdullaah Razwan
ID: 10098348 
"""
from copy import deepcopy # you may use this for copying a board
def newGame(player1, player2):
    """
    player1 is the first player and could either be human or a computer
    player2 is the second player and could also either be human or a computer
    """
    game = {
         'player1' : player1,
         'player2' : player2,
       
         'who' : 1,
         'board' : [ [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0] ]
         }
    return game

# TODO: All the other functions of Tasks 2-11 go here.
def printBoard(board):
    """
    This function prints a formatted version of the board
    
    Variables
    ---------
    board - a lists of lists of the same format as "board" in the "game" dictionary
            we will print a formatted version of this board. With an "X" representing Player 1's pieces
            and an "O" representing player 2's pieces and an empty space representing empty places on the board.
    """
    print("|1|2|3|4|5|6|7|\n+-+-+-+-+-+-+-+")
    for i in range(0, 6):
        change_to_letters = [" ", "X", "O"] #we will use this to change "0" to " ", "1" to "X" and "2" to "O"
        board_pieces = [change_to_letters[d] for d in board[i]] #create a list which is a copy of of board with the above change applied to it
        print("|" + "|".join(board_pieces) + "|") #print the formatted board
    return

def getValidMoves(board):
    """
    returns a list of valid moves
    
    Variables
    ---------
    board : a list of lists in the same format as "board" in the "game" dictionary
    
    Returns
    -------
    validcolumns : a list of numbers from 0 to 6 corresponding to the indices of columns
                   of the board which aren't completely filled
    """
    validcolumns = list() #we will add the indices of non-filled columns to this list
    board1 = deepcopy(board)
    for i in range(0, 7):
        elements_at_i = list() #we will use this list to consider elements in the i-th column 
        for j in range(0, 6):
            if board1[j][i] == 1 or board1[j][i] == 2:
                board1[j][i] = 3 #change the j-th element in the i-th column to 3 if the above condition is satisfied
            elements_at_i.append(board1[j][i]) 
        if elements_at_i == [3,3,3,3,3,3]: #if elements#-at#-i = [3,3,3,3,3,3] the column is full
            validcolumns = validcolumns #so keep validcolumns the same
        else:
            validcolumns.append(i) #else append the current column index to valid columns
    return validcolumns

def makeMove(board, move, who):
    """
    This function takes the current board, allows a move to be made and returns the updated board
    
    Variables
    ---------
    board : list
            a list of lists of the same format as "board" in the "game" dictionary
    move : int
           an integer between 0 and 6 corresponding to the indices of the board columns
    who : int
          either the value 1 or 2, corresponding to the player making the turn
    """
    if move not in range(0,7):
        raise ValueError("move has to be in range(0, 7)")
    if who != 1 and who != 2:
        raise ValueError("who has to be either 1 or 2")
    m = move
    for i in range(0,6):
        for j in range(0, 7):
            try:
                if j == m:
                    if board[5-i][j] == 0: #check the places, from the bottom up, in the wanted column are empty 
                        board[5-i][j] = who #if place is empty then set equal to the player whose turn it is
                        return board
            except IndexError:
                continue
    return board

def hasWon(board, who):
    """
    Checks the board to see if the player with number 'who' has won the game. 
    
    Parameters
    ----------
    board : list
            it is a list of 6 lists with 7 entries each representing the positions of the connect 4 game. The 
            entries of the lists: 0 for an empty space, 1 for a space occupied by player 1 and 2 for a space 
            occupied by player 2. We will check the board to see if there are 4 consecutive entries - in a 
            horizantal, vertical or diagonal line - which have the same value as who.
    who :   int
            who takes either the value 1 or 2 and we will check the board to see if there are 4 consecutive
            entries - in a horizantal, vertical or diagonal line - which have the same value as who.
          
    Returns
    -------
    True : boolean
           if there are 4 consecutive entries with the value 'who' the function will return True.
    False: boolean
           if there aren't 4 consecutive entries with the value 'who' the function will return False.
           
    """
    if who != 1 and who != 2:
        raise ValueError("who has to be either 1 or 2")
    
    #in the below code we had to handle IndexError exceptions. We handled them by using 'continue'
    for i in range(0, 6):
        for j in range(0, 7):
            try:
                if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == who: #check for win horizantally
                   return True
            except IndexError:
                continue
    for i in range(0, 6):
        for j in range(0,7):
            try:
                if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == who: #check for win vertically
                    return True
            except IndexError:
                continue
    for i in range(0, 6):
        for j in range(0, 7):
            try:
                if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == who: #check for win diagonally
                    return True
            except IndexError:
                continue
    for i in range(0, 6):
        for j in range(0, 7):
            try:
                if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == who: #check for win diagonally but
                                                                                                #in the other direction from above
                    return True
            except IndexError:
                continue
                
    return False

def suggestMove1(board, who):
    """
    This function suggests a move
    
    Parameters
    ----------
    board: list
           a list of 6 lists with 7 entries each representing the positions of the connect 4 game. The
           entries of the lists: 0 for an empty space, 1 for a space occupied by player 1 and 2 for a 
           space occupied by player 2. We will inspect the board to find a good move
    who: int
         an integer that takes either the value 1 or 2, representing player 1 and 2 respectively. The 
         function suggests a move for the player whose turn it is
    
    Returns
    -------
    j : int
        the index of the column of the suggested move after checking some conditions
    getValidMoves(board2[0]) : int
        if none of the conditions are satisfied then return the index of the first element in the
        list of valid moves
    """
    if who != 1 and who != 2:
        raise ValueError("who has to be either 1 or 2")
        
    board2 = deepcopy(board) #create a copy of board
    getValidMoves(board2) #get all valid moves using the copy
    for i in range(0, 6):
        for j in range(0, 7):
            try:
                board2 = deepcopy(board) #make a clean copy of the board
                makeMove(board2, j, who) # try all moves on the copied board for the player whose turn it is
                if hasWon(board2, who) == True: #check if after making the move player whose turn it is has won
                    return j #return the column index - suggest the move which leads to the player winning
            except IndexError:
                continue
            if who == 1:
                try:
                    board2 = deepcopy(board) #make a clean copy of the board
                    makeMove(board2, j, 2) #try all moves on the copied board using player 2
                    if hasWon(board2, 2) == True: #check if after making the move player 2 has won
                        return j #return the column index - suggest the move so that player 1 doesn't lose
                except IndexError:
                    continue
            if who == 2:
                try:
                    board2 = deepcopy(board) #make a clean copy of the board
                    makeMove(board2, j, 1) #try all moves on the copied board using player 1
                    if hasWon(board2, 1) == True: #check if after making the move player 1 has won
                        return j #return the column index - suggest the move so that player 2 doesn't lose
                except IndexError:
                    continue
    return getValidMoves(board2)[0] #if neither of the players can win then just suggest the first valid move

def loadGame(filename = 'game.txt'): #if no filename is entered then default value is 'game.txt'
    """
    This function loads a file and returns a dictionary similar to the game dictionary
    
    Parameters
    ----------
    filename : string
               The name of the file which we want to read
    Returns
    -------
    game : dictionary
           a dictionary of the same form as the dictionary in the newGame function
    """
    f = open(filename, mode = "rt", encoding = "utf8")
    game = dict() #start an empty dicitonary
    game['player1'] = f.readline().rstrip('\n')#read first line of file as value for key 'player 1'
    game['player2'] = f.readline().rstrip('\n') #read second line of file as value for key 'player2'
    game['who'] = int(f.readline().rstrip('\n')) #read third line of file as value for key 'player3'
    board = list() #create an empty list within which will make the board
    for i in range(0, 6):
        row = list() #create an emoty list within which we will read the elements of the rows
        elements_in_row = f.readline().rstrip('\n').split(',') #read in rows while also removing commas
        for j in range(0, 7):
            x = int(elements_in_row[j]) #change type of elements from str to int
            row.append(x) #put elements into their rows
        board.append(row) #append the rows to the board
    game['board'] = board #set the key 'board' to the board that we have created
    return game

def saveGame(game, filename):
    """
    This function takes a dictionary 'game' and saves it to a text file called filename
    
    Parameters
    ----------
    game : dict
           a dictionary similar to the dictionary in newGame
    filename: str
              a string corresponding to what we want the file to be named
    """
    with open(filename, mode = "wt", encoding = "utf8") as f:
        f.write(game['player1'] + '\n')
        f.write(game['player2'] + '\n')
        f.write(str(game['who']) + '\n')
        for i in range(0, 6):
            f.write(','.join(repr(a) for a in game['board'][i])  + '\n')
    return


# USE EXACTLY THE PROVIDED FUNCTION NAMES AND VARIABLES!
# ------------------- Main function --------------------
def play():
 """
 TODO in Task 7. Make sure to write meaningful docstrings!
 """
 print("*"*55)
 print("***"+" "*8+"WELCOME CONNECT FOUR!"+" "*8+"***")
 print("*"*55,"\n")
 print("Enter the players' names, or type 'C' or 'L'.\n")
 player1 = input("Enter player 1's name or C if player 1 is controlled by the computer:")
 while player1 == "":
     player1 = input("Enter player 1's name or C if player 1 is controlled by the computer:").capitalize()
 if player1 == 'L':
    filename = input("Please enter the name of the file that you wish to load?")
    loadGame(filename)
 if player1 != 'L':
     player2 = input("Enter player 2's name or C if player 2 is controlled by the computer:").capitalize()
     while player2 == "":
          player2 = input("Enter player 2's name or C if player 2 is controlled by the computer:")
     playGame = newGame(player1, player2)
 else:
     playGame = loadGame(filename)
     player1 = playGame['player1']
     player2 = playGame['player2']
 print("Let's play!")
 board = playGame['board']
 who = playGame['who']
 printBoard(board)
 while True:
    getValidMoves(board)
    if getValidMoves(board) == []:
        print("The game has ended in a draw")
        return False
    if who == 1:
        if player1 != 'C':
            while True:
                try:
                    m = input(player1.capitalize() + " (O) which column would you like to make your move in?")
                    if m == 'S':
                        game = {
                        'player1' : player1,
                        'player2' : player2,
       
                        'who' : who,
                        'board' : board
                        }
                        filename = input("Enter a filename:")
                        saveGame(game, filename)
                        return False
                    else:
                        m = int(m)
                except ValueError:
                    print("Please enter a valid move:")
                    continue
                else:
                    break
            if m == 'S':
                game = {
                        'player1' : player1,
                        'player2' : player2,
       
                        'who' : who,
                        'board' : board
         }
                filename = input("Enter a filename:")
                saveGame(game, filename)
                break
            if (m - 1) in getValidMoves(board):
                move = (m - 1)
            else:
                while (m - 1) not in getValidMoves(board):
                    m = int(input(player1.capitalize() + " (X) please enter a valid move:"))
                    if (m - 1) in getValidMoves(board):
                        move = (m - 1)
            makeMove(board, move, 1)
        else:
            makeMove(board, suggestMove1(board, 1), 1)
        if hasWon(board, 1):
            printBoard(board)
            print("Congratulations " + player1 + " (X) you have won!")
            return False
        printBoard(board)
        who = 2
        continue
    if who == 2:
        if player2 != 'C':
            while True:
                try:
                    m = (input(player2.capitalize() + " (O) which column would you like to make your move in?"))
                    if m == 'S':
                        game = {
                        'player1' : player1,
                        'player2' : player2,
                        'who' : who,
                            'board' : board
                            }
                        filename = input("Enter a filename:")
                        saveGame(game, filename)
                        return False
                    else:
                        m = int(m)
                except ValueError:
                    print("Please enter a valid move:")
                    continue
                else:
                    break
            if (m - 1) in getValidMoves(board):
                move = (m - 1)
            else:
                while (m - 1) not in getValidMoves(board):
                    m = int(input(player2.capitalize() + " (X) please enter a valid move:"))
                    if (m - 1) in getValidMoves(board):
                        move = (m - 1)
            makeMove(board, move, 2)
        else:
            makeMove(board, suggestMove1(board, 2), 2)
        if hasWon(board, 2):
            printBoard(board)
            print("Congratulations " + player2 + " (O) you have won!")
            return False
        printBoard(board)
        who = 1
        continue    
    
    continue
 # TODO: Game flow control starts here
# the following allows your module to be run as a program
if __name__ == '__main__' or __name__ == 'builtins':
 play()