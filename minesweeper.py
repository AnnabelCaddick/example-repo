import random
#Create a function that takes a grid of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot.
#Function to create a minesweeper board
#Width : Number of columns
#Height: Number of rows
#mine_chance: The probability that the cell contains a minr (20% default)
def make_board(width, height, mine_chance=0.2):
    board = [] #Initialise an empty board
    for row in range(height):
        current_row = [] #Start a new row
        for col in range(width):
            #Randomly place a mine based on mine_chance
            if random.random() < mine_chance:
                current_row.append("#") #"#" represents a mine
            
            else:
                current_row.append("-") #"-" represents an empty spot
        board.append(current_row) #Add the row to the board
    return board


#Function to count the number of adjacent mines from each cell
#Replaces "-"with the number of adjacent mines
def count_adjacent_mines(board):
    height = len(board) #Number of rows
    width = len(board[0]) #Number of columns

#All possible directions around a cell

    directions =  [ 
        (-1,-1), (-1,0), (-1, 1),
        (0, -1),        (0, 1),
    (1,-1),  (1,0), (1,1)
    ]

    result = [] #New board to store mine counts
#Loop through each cell in the board
    for row in range(height):
        new_row = [] #Start a new row for the result
        for col in range(width):
            if board[row][col]== "#":
                new_row.append("#")
            else:
                mine_count = 0 #Counter for the adjacent mines
                #Check all the neighbours
                for row_change, column_change in directions:
                    r = row + row_change
                    c = col + column_change
                    #Check if the neighbour is inside the boundries of the board
                    if 0 <= r < height and 0 <= c < width:
                        if board[r][c] == "#":
                            mine_count += 1
            #Append the mine count as a string
                new_row.append(str(mine_count))
        result.append(new_row) #Append after finishing all columns in this row
    return result #Return the board with mine counts after finishing all rows

#Function to print the
def print_board(board):
    for row in board:
        #Join each row list into a single string and print
        print("".join(row))




#Create a random board
board = make_board(5, 5) #5x5 board

#Count the adjacent mines
print("Original board:")   
print_board(board)




#Create and print the board with the mine count
counted_board = count_adjacent_mines(board)
print("Board with adjacent mine count")
print_board(counted_board)
