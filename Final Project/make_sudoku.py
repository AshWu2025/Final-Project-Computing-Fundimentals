#Creates a Sudoku Puzzle 
#Creates a Sudoku Puzzle using refursion 
#Ashley Wu 

import random
#import is_valid

def create_sudoku(matrix, counter = 1): 
    """Creates a 9 by 9 sudoku puzzle 
    
    Args: 
        counter (int): Keeps the place of the number to be filled into the puzzle
    Returns a 9 row by 9 column 2 dimentional list of lists that form a sudoku puzzle
    """
    #creates a copy of the original matrix 
    orig_matrix = [[10]*9]

    for x in range(8):
        orig_matrix.append([10]*9)

    for y in range(9):
        for q in range(9):
            orig_matrix[y][q] = matrix[y][q]

    #if the matrix is 
    if matrix[8][8] != 10: 
        return matrix

    #all of the possible numbers that can be in the sudoku 
    pos = [1,2,3,4,5,6,7,8,9]

    possible = False

    random.shuffle(pos)

    for i in range(len(pos)):
        #print (pos[i])
        if is_valid(matrix, pos[i], counter):
            #once it is valid it is not locked in, this is the major issue 
            matrix[(counter - 1)//9][((counter - 1) % 9)] = pos[i]
            stor_matrix = create_sudoku(matrix, counter + 1)
            if stor_matrix:
                if stor_matrix[8][8] != 10: 
                    return stor_matrix
                #if the move is valid, then we increase the counter and call the function again 
                matrix = stor_matrix
                possible = True
            else:
                #print ('zero was returned and the original matrix was restored')
                counter -= 1
                matrix = orig_matrix
                possible = False 
    if not possible: 
        #if the counter is not maxed out then one of the previous numbers is not viable so
        #a 0 is returned 
        #print ('this', counter, 'proved not to be possible k')
        return 0

    return matrix
    
def is_valid(matr, num, counter):
    """Makes sure that the number given is a valid sudoku solution
    
    Args:
        martrix (list): the current sudoku solution
        num (int): the number being inserted
        counter (int): the position of the number being inserted 
    
    Returns Boolean determining whether the number will fit into the 
    place given
    """

    row = (counter -1)//9 
    column = (counter - 1)%9
    
    #print (row, column)

    possible = True 
    
    for k in range(0,9):
        if matr[k][column] == num:
            possible = False 
    
    for l in range(0,9):
        if matr[row][l] == num:
            possible = False

    if 0 <= row <= 2: 
        if 0 <= column <= 2:
            #first subsquare 
            for j1 in range(0,3):
                for y1 in range(0,3):
                    if matr[j1][y1] == num: 
                        possible = False
        if 3 <= column <= 5:
            #second subsquare 
            for j2 in range(0,3):
                for y2 in range(3,6):
                    if matr[j2][y2] == num: 
                        possible = False
        if 6 <= column <= 8: 
            #third subsquare
            for j3 in range(0,3):
                for y3 in range(6,9):
                    if matr[j3][y3] == num: 
                        possible = False
    if 3 <= row <= 5: 
        if 0 <= column <= 2:
            #fourth subsquare 
            for j4 in range(3,6):
                for y4 in range(0,3):
                    if matr[j4][y4] == num: 
                        possible = False
        if 3 <= column <= 5:
            #fifth subsquare 
            for j5 in range(3,6):
                for y5 in range(3,6):
                    if matr[j5][y5] == num: 
                        possible = False
        if 6 <= column <= 8: 
            #sixth subsquare 
            for j6 in range(3,6):
                for y6 in range(6,9):
                    if matr[j6][y6] == num: 
                        possible = False
    if 6 <= row <= 8: 
        if 0 <= column <= 2:
            #seventh subsquare 
            for j7 in range(6,9):
                for y7 in range(0,3):
                    if matr[j7][y7] == num: 
                        possible = False
        if 3 <= column <= 5:
            #eigth subsquare 
            for j8 in range(6,9):
                for y8 in range(3,6):
                    if matr[j8][y8] == num: 
                        possible = False
        if 6 <= column <= 8: 
            #nineth sunsquare 
            for j9 in range(6,9):
                for y9 in range(6,9):
                    if matr[j9][y9] == num: 
                        possible = False
    
    #print (num, possible)
    #print (row, column)

    return possible



