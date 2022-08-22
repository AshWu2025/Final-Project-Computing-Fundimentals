#make problem 
#makes the actual puzzle with the completed matrix 
#Ashley Wu 
import make_sudoku
from random import shuffle
import sudoku_solve
import sys

sys.setrecursionlimit(10**6)

def make_problem(puzzle):
    """comfirms that there is only one solution to the sudoku puzzle

    Args:
        matrix (list): sudoku solution that needs to be checked
    """
    #introduces the user
    print ("Here is your puzzle")

    #creates original so it can be compared to the output 
    original = [[0] *9]
    for l in range(8):
        original.append([0] * 9)

    for n in range(9):
        for m in range(9):
            original[m][n] = puzzle[m][n]

    difficulty = 'easy'


    new = remove_num(puzzle, difficulty)


    #output sometimes mixes up numbers, so this is to fix that
    for i1 in range (9):
        for k1 in range(9):
            if new[i1][k1] != puzzle[i1][k1]:
                #makes sure that the blanks are not overwritten 
                if new[i1][k1] != 10:
                    new[i1][k1] = puzzle[i1][k1]
    return new





def remove_num (matr, difficulty):
    """removes the numbers to create a puzzle 

    Args:
        matrix (list): the completed sudoku puzzle
        difficulty (string): the difficulty of the puzzle
    """
    #creates an original matrix
    original = [[0] *9]
    for l in range(8):
        original.append([0] * 9)

    for n in range(9):
        for m in range(9):
            original[m][n] = matr[m][n]

    #creates list of numbers from 0 to 80
    numbers = []
    for i in range(0,81):
        numbers.append(i)
    
    shuffle(numbers)

    #removes the numbers from the matrix randomly by taking the numbers from 
    #0 to 80 and removing those spots to create an empty board
    if difficulty == 'hard':
        for q in range(81-23):
            k = numbers[q]
            matr[k//9][k%9] = 10

    if difficulty == 'medium':
        for q1 in range(81-35):
            k1 = numbers[q1]
            matr[k1//9][k1%9] = 10
    
    if difficulty == 'easy':
        for q2 in range(81-50):
            k2 = numbers[q2]
            matr[k2//9][k2%9] =10

    #calls solve
    num_sol = solve(matr)

    #if the answer is unique, then the matrix is returned 
    if num_sol[1] ==1:
        return matr
    else: 
        return remove_num(original, difficulty)



    

def solve(matrix, counter = 0):
    """solves a sudoku puzzle

    Args:
        matrix (_type_): the sudoku puzzle that is being inputted with numbers already removed
        count (int): the amount of solutions that the given sudoku puzzle has
    """

    #print ("solve was called")

    #if there is found to be more than one solution then the program stops 
    if counter >= 2: 
        return 0, counter

    #copies the original matrix for backtracking 
    original = [[0] *9]
    for l in range(8):
        original.append([0] * 9)

    for n in range(9):
        for m in range(9):
            original[m][n] = matrix[m][n]

    #finds the next empty square in the matrix, also double checks to make sure 
    #that the matrix is not full 
    empty = False
    place = 0


    while not empty:
        place += 1            
        if matrix[(place - 1)//9][(place - 1)%9] == 10:
            empty = True 
        #no empty space was found
        if place == 81:
            #check to see if there is a valid solution in the matrix, 
            if sudoku_solve.sudoku_checker(matrix): 
                #if a valid solution is found then the matrix is returned along with a number
                return 0, 1
            
    #all of the possible numbers that can be in the sudoku 
    pos = [1,2,3,4,5,6,7,8,9]

    possible = False

    shuffle(pos)

    #chooses a random number 
    for i in range(len(pos)):
        #checks whether that random number is valid in the space
        if make_sudoku.is_valid(matrix, pos[i], place):
            #once it is confirmed it is put into the matrix
            matrix[(place - 1)//9][((place - 1) % 9)] = pos[i]
            #then the matrix is called again
            stor_matrix = solve(matrix, counter)
            #if a solution is found, then it is added to the counter
            counter += stor_matrix[1]
            if stor_matrix[0]:
                #if the move is valid, then we increase the counter and call the function again 
                matrix = stor_matrix[0]
                possible = True
            else:
                #if zero is returned, then it checks the rest of the possible solutions
                matrix = original
                possible = False 
    if not possible: 
        #if the counter is not maxed out then one of the previous numbers is not viable so
        #a 0 is returned, andother 0 is returned for the counter as no solution was found this way
        return 0, counter

    #if a solution is found, then the counter is increased
    return matrix, counter


