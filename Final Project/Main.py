#Main
#creates the main program that houses the UI and calls functions
#Ashley Wu 
import make_sudoku
import sudoku_solve
import download
import upload
import make_problem
#Welcomes user to the program 
print ("Welcome to Sudoku Master")
print ("In Sudoku master, you are able to upload, download, create \n\
and solve sudoku puzzles. The program will save the most recent puzzle that you \n\
have uploaded or generated for you to solve.")

#initializes variables
loop = True

puzzle = []

while loop: 
    #gives the user all of the options
    print ("    To create a 9 by 9 sudoku puzzle, please enter 'create' \n\
    To upload a puzzle please enter 'upload'. \n\
    To download the currently loaded puzzle please enter 'download' \n\
    To solve the currently uploaded puzzle please enter 'solve' \n\
    To exit the program, please enter 'exit'")
    #takes the user's input 
    ent = input ()

    if ent == 'create':
        #makes sure that the user is okay with losing their current puzzle
        print('this will get rid of the currnet puzzle, are you okay with that? y/n?')
        yesno = input()
        proper = False

        #checks for incorrect inputs
        while proper == False: 
            if yesno == 'y':
                proper = True 
            elif yesno == 'n':
                proper = False
            else: 
                yesno = input('wrong input! please enter either y or n')

        #if the user is okay with erasing their current puzzle 
        if yesno == 'y':    
        #creates shell puzzle
            mat = [[10]*9]
            for i in range(8):
                mat.append([10]*9)
            #calls create_sudoku function to create the puzzle 
            puzzle = make_sudoku.create_sudoku(mat)
            #prints the puzzle out
            
            #prints out puzzle
            puzzle = make_problem.make_problem(puzzle)
            sudoku_solve.print_sudoku(puzzle)

    elif ent == 'upload':
        #calls the upload sudoku function and puts it to puzzle
        puzzle = upload.upload_sudoku()
    elif ent == 'download':
        #calls download game function 
        download.download_sudoku(puzzle)
    elif ent == 'solve':
        #calls solve game function 
        sudoku_solve.solve_sudoku(puzzle)
    elif ent == 'exit':
        #exists the game 
        loop = False
    else: 
        #if the user doesnt enter a valid input the menu is repeated
        print ("wrong input, please try again")
