#sudoku solve 
#creates a UI function that allows the user to solve the Sudoku puzzle
#Ashley Wu 

def solve_sudoku(puzzle, solution = []):
    """Creates a a UI that solves a sudoku problem 

    Args:
        puzzle (list): the sudoku puzzle that is being solved 
        solution (_type_): the solution to the sudoku puzzle
    """
    #changes all of the 10 placeholders to zero for convenience
    for i in range (9):
        for k in range (9):
            if puzzle [i][k] == 10:
                puzzle [i][k] = 0
    
    #creates the shell for the perminent numbers 
    perm = [[0] * 9]
    for o in range(8):
        perm.append([0] * 9)


    #creates a copy of the puzzle so we know which numbers are perminent 
    for z in range(9):
        for x in range(9):
            perm[z][x] = puzzle [z][x]


    #introduces the rules and how to play the game to the user
    print("The zero's represent empty spaces on the board, your job is to fill them in!")
    print("to fill in the blanks, please enter a coordinate in an Ax format")
    print("when you think the puzzle is solved, enter 'check' to see whether you have solved the puzzle")
    print("Here is the puzzle that you have loaded and are working with")
    print("enter 'exit' to exit the game, WARNING: THIS WILL EARASE YOUR PROGRESS")
    print_sudoku(puzzle)

    #initiates thre variable 
    solve = False

    while solve == False:
        ent = input('What is your next action?')
        if ent[0:1] == 'A':
            input_sudoku(0,int(ent[1:2]) - 1,puzzle,perm)
        elif ent[0:1] == 'B':
            input_sudoku(1,int(ent[1:2]) - 1,puzzle,perm)
        elif ent[0:1] == 'C':
            input_sudoku(2,int(ent[1:2]) - 1,puzzle,perm)
        elif ent[0:1] == 'D':
            input_sudoku(3,int(ent[1:2]) - 1,puzzle,perm)
        elif ent[0:1] == 'E':
            input_sudoku(4,int(ent[1:2]) - 1,puzzle,perm)
        elif ent[0:1] == "F":
            input_sudoku(5,int(ent[1:2]) - 1,puzzle,perm)
        elif ent[0:1] == "G":
            input_sudoku(6,int(ent[1:2]) - 1,puzzle,perm)
        elif ent[0:1] == "H":
            input_sudoku(7,int(ent[1:2]) - 1,puzzle,perm)
        elif ent[0:1] == "I":
            input_sudoku(8,int(ent[1:2]) - 1,puzzle,perm)
        elif ent == 'exit':
            return
        elif ent == 'check':
            #this is incorrect, fix this!!! 
            if sudoku_checker(puzzle):
                print("\n\n!!!!!!!congrats! You solved this puzzle!!!!!!!!!!\n\n")
                solve = True
            else: 
                print("sorry this puzzle isnt right, try again")
        else: 
            print ("wrong input, please try agian")
    return


def input_sudoku(num1, num2, mat, perm):
    """inputs a number to the sudoku board

    Args:
        num1 (int): x location on the board
        num2 (int): y location on the board
        mat (list): the currentt state of the sudoku board
        perm (list): the unchangable numbers on the sudoku board
    Returns: 
        mat (list): new boardstate
    """
    #if the number was originally there and can not be changed 
    if perm[num2][num1] != 0:
        print ("sorry but you can not change that number, it is perminent")
    #if the number can be changed, it changes the number
    else: 
        numb = input('what number do you want to replace that square with?')
        mat[num2][num1] = int(numb)

    #prints new boardstate
    print_sudoku(mat)

    return mat


def print_sudoku(mat):
    """prints the sudoku puzzle out
    Args: 
        mat (list): the matrix to print
    Returns nothing
    """
    #makes 10s into zeros for printing purposes 
    for i in range (9):
        for k in range (9):
            if mat [i][k] == 10:
                mat [i][k] = 0
    #sets up the number grid 
    print ("   A, B, C, D, E, F, G, H, I")
    print ('*****************************')
    num = 1

    #prints the matrix with the grid for searching and selecting
    for line in mat: 
        print(num, '|', line, '|', sep ='')
        num += 1
    print ('*****************************')


def sudoku_checker(matrix):
    """checks to make sure a sudoku board is valid. Returns a true false arugment 

    Args:
        matrix (list): a completed sudoku board 
        size (int): the size of the sudoku board
    """

    size = 9

    count = 0
    #the amount any block should add to
    for z in range(1, size + 1): 
        count += z
    
    #size of a block 
    block = int(size ** .5)
    sudoku = True

    #checks the inner squares to see whether all of the numbers add up properly
    for k in range(block):
        for y in range(block):
            stor = 0
            for i in range(block):
                for j in range (block):
                    stor += matrix[i + (k * 3)][j + (y * 3)]
            #if the numbers add up improperly, then Sudoku would be eqeual to False 
            if stor != count: 
                sudoku = False

    #checks to see if the rows and columns add to up the same number
    for o in range(len(matrix)):
        stor = 0 
        stor = sum(matrix[o])
        if stor != count: 
            sudoku = False
        store = 0
        for p in range(len(matrix[0])):
            store  += matrix[p][o]
        if stor != count: 
            sudoku = False
    
    return sudoku