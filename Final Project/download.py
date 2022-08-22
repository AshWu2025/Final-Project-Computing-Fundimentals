#download
#allows the user to download a sudoku puzzle
#Ashley Wu 

def download_sudoku(puzzle):
    """downsloads the given puzzle onto your computer with a file name of the user's choice 

    Args:
        puzzle (_type_): _description_
    Returns: 
        txt file downloaded onto your computer
    """
    #removes all the 10s and replaces them with ones 
    for i in range (9):
        for k in range (9):
            if puzzle [i][k] == 10:
                puzzle [i][k] = 0

    #asks for the name of the file to be created
    name = input("what do you want your file name to be?")
    #creates the file 
    with open(name, 'w') as f:
        for line in puzzle: 
            print(line, file = f)
            
    #confirm that the file has been downloaded
    print ("The file has been downloaded")



