#upload
#allows the user to upload a suduku puzzle
#Ashley Wu 

def upload_sudoku():
    """reads and uploads a sudoku function to the program
    returns: 
        puzzle (list): sudoku puzzle in the file
    """

    #asks for file name of the file the user wants to upload
    name = input('please input the name of the file you want to upload')
    #creates the puzzle 
    puzzle = [[10] * 9]
    for i in range(8):
        puzzle.append([10] * 9)

    try: 
        open(name, 'r')

    except FileNotFoundError:  
        #tells the user that an error has occurred 
        print ("the file was not found")
        #ends function 
        return

    #uploads the puzzle 
    with open(name, 'r') as f:
        numbs =[]
        #takes all of the lines from the file and saves as a list using sep
        for line in f: 
            #removes all of the punctuation characters in the file
            line = line.replace('[', "")
            line = line.replace(']', "")
            line = line.replace(',', "")
            line = line.strip()
            line = line.replace(" ", "")
            #appends the number into the list numbs
            for char in line:
                numbs.append(char)

        #puts the numbers from numbs into the puzzle matrix 
        for k in range(81):
            puzzle[(k//9)][(k%9)] = int(numbs[k])
    
    return puzzle