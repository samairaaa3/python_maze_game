# Assignment_5.py
#
# Maze Game Program!
#
# This Python program implements a maze game where the player navigates a
# turtle through a maze. The maze map is loaded from a data file and consists
# of an entrance, an exit, walls and roads. This program contains functions 
# to read maze data from a file, compute maze dimensions, set up the game  
# canvas and draw the maze. It also contains functions that allow the player
# to move the turtle through the maze, from its entrance to the its exit,
# using the arrow keys.
#
# Authors: Sitong Zhai and Anne Lavergne
# Date: March 2024

import turtle
import random

def mazePositionToCoordinate(column, row, mazeWidth, mazeHeight, cellSize = 20):
    """
        Given the column number and the row number of a cell in the maze,
        the width and the height of the maze and considering the size of
        a cell (cellSize x cellSize), computes and returns the centre
        coordinate x and y of the cell (from a turtle canvas perspective).
        
        ***Do not modify the content of this function!***
    """
    
    x = column * cellSize - mazeWidth * cellSize / 2 + cellSize / 2
    y = mazeHeight * cellSize / 2 - row * cellSize - cellSize / 2

    return x, y

def coordinateToMazePosition(x, y, cellSize = 20):
    """
        Given the centre coordinate x and y of a cell (from a turtle canvas
        perspective) and considering the width and the height of the maze
        as well as the size of a cell (cellSize x cellSize), computes and
        returns the column number and the row number of this cell in the maze.         
      
        Because this function is called from the "listener" functions
        headUp(), headDown(), headLeft() and headRight() and that these
        "listeners" do not take parameters, the variables "mazeWidth"
        and "mazeHeight", created in the Main part of the program,
        are used directly in this function, without being passed as
        arguments.
        
        Note that the parameters x and y are computed in the "listener"
        functions.

        Implementation Details - What you need to do:
        - Using the function mazePositionToCoordinate() as inspiration,
          complete this function.
    """

    # Your code starts here:
    column = int((x + mazeWidth * cellSize / 2) / cellSize)
    row = int((mazeHeight * cellSize / 2 - y) / cellSize)

      # Use as many lines as necessary to write your code

    # Your code ends here.
    
    return int(column), int(row)

def winGame(cellSize = 20):
    """
        Brings the game to an end.
      
        Because this function is called from the "listener" functions
        headUp(), headDown(), headLeft() and headRight() and that these
        "listeners" do not take parameters, several variables, created
        in the Main part of the program, are used directly in this
        function, without being passed as arguments.
        
        ***Do not modify the content of this function,
           except for the part labelled ***Optional***
           For 1 BONUS mark, you can change what happens
           when the turtle reaches the exit gate of maze
           by modifying the code located between
           # The code you can change starts here:
           and
           # The code you can change ends here. ***
    """
    
    # Disable the "listener" functions by ending the
    # "arrow" key-to-turtle heading pairings
    manualTurtle.getscreen().onkeyrelease(None, 'Up')
    manualTurtle.getscreen().onkeyrelease(None, 'Down')
    manualTurtle.getscreen().onkeyrelease(None, 'Left')
    manualTurtle.getscreen().onkeyrelease(None, 'Right')

    # Print a congratulatory message on the shell (computer monitor screen)
    message = "Congratulations! You win!"
    print(message)

# ***Optional***
# For 1 BONUS mark - You can change what happens when the turtle reaches the
#                    exit gate of maze by modifying the code located between
                     # The code you can change starts here: and
                     # The code you can change ends here.
# The code you can change starts here:
    manualTurtle.speed(4)
    manualTurtle.color('red')

    # Add an animation and display a congratulatory message
    for _ in range(2):
        manualTurtle.penup()
        manualTurtle.forward(20)
        manualTurtle.pendown()
        manualTurtle.forward(20)
        manualTurtle.penup()
        manualTurtle.backward(20)
        manualTurtle.left(90)
        manualTurtle.forward(20)
        manualTurtle.right(90)

    manualTurtle.penup()
    manualTurtle.goto(0, 0)
    manualTurtle.color('blue')
    manualTurtle.write("Congratulations! You've completed the maze!", align="center", font=("Arial", 16, "bold"))
# The code you can change ends here.
# ***End of Optional***

    # The player can close the maze window by pressing the
    # "Return" ("Enter") key
    turtle.onkey(turtle.bye, key='Return')
    
    return

def moveForward(nextColumn, nextRow, mazeMatrix, cellSize):
    """
        Moves the turtle from its current cell in the maze
        to the next cell indicated by the "arrow" key the
        player just pressed.

    Parameters:
    - nextColumn: the column number of the next cell the turtle
                  is to move to in the maze. 
    - nextRow: the row number of the next cell the turtle
               is to move to in the maze.
    - cellSize: size of a cell in the maze (20x20).
    
    Returns:
    - None.
        
    Implementation Details - What you need to do:
    - Verify that the next cell the turtle is to move to in the maze
      is still within the maze. If the next cell is not within the maze,
      print a message such as
      "You are trying to move the turtle outside of the maze!"
      on the shell (computer monitor screen) and return.
    - If the next cell is within the maze, figure out what type of cell
      it is: "Entrance", "Exit", "Wall", "Road"?
    - If the next cell is "Entrance", move (i.e., draw) the turtle
      (using the turtle function forward()) forward by one cell,
      print a message such as "You are at the starting point!"
      on the shell (computer monitor screen) and return.
        - If moving the turtle to the next cell brings the turtle
          back where it was before, then remove (pop) the current cell
          from the "pathThroughMaze" list, otherwise add (append)
          the next cell to the "pathThroughMaze" list.
    - If the next cell is "Exit", move the turtle forward by one cell,
      add this next cell to the "pathThroughMaze" list,
      print a message such as "You have arrived at the exit gate!"
      on the shell (computer monitor screen), call winGame() and return.
    - If the next cell is "Wall", print a message such as
      "You are facing a wall so you cannot move!" on the shell
      (computer monitor screen) and return.
    - If the next cell is "Road", move the turtle forward by one cell.
      But, if moving the turtle to the next cell brings the turtle
      back where it was before, then remove (pop) the current cell
      from the "pathThroughMaze" list, otherwise add this next cell
      to the "pathThroughMaze" list and print a message such as
      "You have moved successfully!" on the shell and return.
    """

    # Your code starts here:
    nextColumn, nextRow = coordinateToMazePosition(manualTurtle.xcor(), manualTurtle.ycor())

    # Check if the next cell is within the maze bounds
    if not (0 <= nextRow < len(mazeMatrix) and 0 <= nextColumn < len(mazeMatrix[0])):
        print("You are trying to move the turtle outside of the maze!")
        return

    # Get the type of the next cell
    nextCellType = mazeMatrix[nextRow][nextColumn]

    # Handle different types of cells
    if nextCellType == symbolDict['Wall']:
        print("You are facing a wall so you cannot move!")
        manualTurtle.done()
        return
    elif nextCellType == symbolDict['Road']:
        # Move the turtle forward by one cell
        manualTurtle.forward(cellSize)
        print("You have moved successfully!")
    elif nextCellType == symbolDict['Entrance']:
        # Move the turtle forward by one cell
        manualTurtle.forward(cellSize)
        print("You are at the starting point!")
        # Remove the current cell from the pathThroughMaze list
        pathThroughMaze.pop()
    elif nextCellType == symbolDict['Exit']:
        # Move the turtle forward by one cell
        manualTurtle.forward(cellSize)
        print("You have arrived at the exit gate!")
        # Add this next cell to the pathThroughMaze list
        pathThroughMaze.append((nextColumn, nextRow))
        # Call the winGame function
        winGame(cellSize)
        return

      # Use as many lines as necessary to write your code

    # Your code ends here.

def headUp():
    """
        Sets turtle heading up.
        
        Note that headUp() is a special type of function called
        a "listener": it listens to the actions performed by the
        player (the user) such as pressing the "up arrow" key.
        When the player presses the "up arrow" key, this function is
        automatically executed (without being called in this program).
        Because headUp() is a "listener", it does not take parameters.
        Therefore, the variable "manualTurtle", created in the Main part
        of the program, is used directly in this function, without being
        passed as an argument.

        ***Do not modify the content of this function!***
    """
    
    # Set the heading 
    manualTurtle.setheading(90)

    # Get the current position of the turtle navigating through the maze
    currentColumn, currentRow = coordinateToMazePosition(manualTurtle.xcor(),
                                                         manualTurtle.ycor())

    # When the player presses the "up arrow" key, 
    # the turtle is meant to move one position up in the maze
    # Set "nextColumn" and "nextRow" to reflect this move up
    nextColumn = currentColumn
    nextRow = currentRow - 1

    # Report the move on the shell (computer monitor screen)
    print(f'You are moving up: \
({currentColumn}, {currentRow}) -> ({nextColumn}, {nextRow})')

    # Move the turtle up one position to (nextColumn, nextRow)
    moveForward(nextColumn, nextRow, mazeMatrix, 20)
    
    return

def headDown():
    """ 
        Sets turtle heading down.
        
        Note that headDown() is a special type of function called
        a "listener": it listens to the actions performed by the
        player (the user) such as pressing the "down arrow" key.
        When the player presses the "down arrow" key, this function is
        automatically executed (without being called in this program).
        Because headDown() is a "listener", it does not take parameters.
        Therefore, the variable "manualTurtle", created in the Main part
        of the program, is used directly in this function, without being
        passed as an argument.

        Implementation Details - What you need to do:
        - Using the function headUp() as a model, complete this function.
    """

    # Your code starts here:
    manualTurtle.setheading(270)

    # Get the current position of the turtle navigating through the maze
    currentColumn, currentRow = coordinateToMazePosition(manualTurtle.xcor(), manualTurtle.ycor())

    # When the player presses the "down arrow" key, the turtle moves one position down in the maze.
    # Set "nextColumn" and "nextRow" to reflect this move down
    nextColumn = currentColumn
    nextRow = currentRow + 1

    # Report the move on the shell (computer monitor screen)
    print(f'You are moving down: ({currentColumn}, {currentRow}) -> ({nextColumn}, {nextRow})')

    # Move the turtle down one position to (nextColumn, nextRow)
    moveForward(nextColumn, nextRow , mazeMatrix, 20)
    
    return

      # Use as many lines as necessary to write your code

    # Your code ends here.
    
    

def headLeft():
    """ 
        Sets turtle heading left.
        
        Note that headLeft() is a special type of function called
        a "listener": it listens to the actions performed by the
        player (the user) such as pressing the "left arrow" key.
        When the player presses the "left arrow" key, this function is
        automatically executed (without being called in this program).
        Because headLeft() is a "listener", it does not take parameters.
        Therefore, the variable "manualTurtle", created in the Main part
        of the program, is used directly in this function, without being
        passed as an argument.

        Implementation Details - What you need to do:
        - Using the function headUp() as a model, complete this function.
    """

    # Your code starts here:
    manualTurtle.setheading(180)

    # Get the current position of the turtle navigating through the maze
    currentColumn, currentRow = coordinateToMazePosition(manualTurtle.xcor(), manualTurtle.ycor())

    # When the player presses the "left arrow" key, the turtle moves one position left in the maze.
    # Set "nextColumn" and "nextRow" to reflect this move left
    nextColumn = currentColumn - 1
    nextRow = currentRow

    # Report the move on the shell (computer monitor screen)
    print(f'You are moving left: ({currentColumn}, {currentRow}) -> ({nextColumn}, {nextRow})')

    # Move the turtle left one position to (nextColumn, nextRow)
    moveForward(nextColumn, nextRow , mazeMatrix, 20)

      # Use as many lines as necessary to write your code

    # Your code ends here.
    
    return
    
def headRight():
    """
        Sets turtle heading right.
        
        Note that headRight() is a special type of function called
        a "listener": it listens to the actions performed by the
        player (the user) such as pressing the "right arrow" key.
        When the player presses the "right arrow" key, this function is
        automatically executed (without being called in this program).
        Because headRight() is a "listener", it does not take parameters.
        Therefore, the variable "manualTurtle", created in the Main part
        of the program, is used directly in this function, without being
        passed as an argument.

        Implementation Details - What you need to do:
        - Using the function headUp() as a model, complete this function.
    """

    # Your code starts here:
    manualTurtle.setheading(0)

    # Get the current position of the turtle navigating through the maze
    currentColumn, currentRow = coordinateToMazePosition(manualTurtle.xcor(), manualTurtle.ycor())

    # When the player presses the "right arrow" key, the turtle moves one position right in the maze.
    # Set "nextColumn" and "nextRow" to reflect this move right
    nextColumn = currentColumn + 1
    nextRow = currentRow

    # Report the move on the shell (computer monitor screen)
    print(f'You are moving right: ({currentColumn}, {currentRow}) -> ({nextColumn}, {nextRow})')

    # Move the turtle right one position to (nextColumn, nextRow)
    moveForward(nextColumn, nextRow , mazeMatrix, 20)
    

      # Use as many lines as necessary to write your code

    # Your code ends here.
    
    return

def drawSquare(mazeTurtle, column, row, colour, mazeWidth, mazeHeight,
               cellSize = 20):
    """
        Draws a square at the specified column and row of the maze using
        the given colour. This function is used to visually represent different
        components of the maze (walls, entrance, exit, road).
        
        ***Do not modify the content of this function!***
    """
    
    # Calculate the top-left corner of the square to be drawn.
    squareTopX = column * cellSize - mazeWidth * cellSize / 2
    squareTopY = mazeHeight * cellSize / 2 - row * cellSize
    
    # Position the turtle and start drawing the square.
    mazeTurtle.penup()
    mazeTurtle.goto(squareTopX, squareTopY)
    mazeTurtle.color(colour)
    mazeTurtle.pendown()
    mazeTurtle.begin_fill()
    for i in range(4):
        mazeTurtle.forward(cellSize)
        mazeTurtle.right(90)
    mazeTurtle.end_fill()
    mazeTurtle.ht()
    
    return

def setupMazeWindow(mazeWidth, mazeHeight, cellSize = 20):
    """
        Sets up the game window dimensions based on the maze size.
        
        ***Do not modify the content of this function!***
    """
    
    # Calculate the dimensions of the game canvas
    gameCanvasWidth = mazeWidth * cellSize + 50
    gameCanvasHeight = mazeHeight * cellSize + 100
    
    # Set up the turtle screen
    turtle.setup(width=gameCanvasWidth, height=gameCanvasHeight)
    
    return

def readDataFile(mazeFilePath, mazeMatrix, symbolDict):
    """
        This function reads the data from the data file.
        First, it reads the symbols representing the maze's walls,
        entrance, exit and roads (paths) from the data file
        into the dictionary "symbolDict". Then it reads the maze
        from the data file into "mazeMatrix".

    Parameters:
    - mazeFilePath (string): The filename (file path) to the data file.
    - mazeMatrix (list of lists): The 2D matrix representing the maze layout,
      where each element indicates a specific maze component
      (wall, entrance, exit or road).
    - symbolDict (dictionary): A dictionary containing symbols used in the maze,
      including keys such as 'Wall', 'Entrance', 'Exit', and 'Road', and
      their corresponding symbols (the key's value).

    Returns:
    - mazeMatrix (list of lists): Updated maze matrix.
    - symbolDict (dictionary): Updated symbol dictionary containing the
      loaded symbols (1 character) for walls, entrance, exit, and road.

    Implementation Details:
    - Open the specified data file in read mode.
    - Read the symbols for walls, entrance, exit, and roads from the file and
      update the symbolDict.
    - Read the maze line by line (a line is a row, i.e., a list) from the file
      and append each row to "mazeMatrix".
    - Close the data file after reading.
    
        ***Do not modify the content of this function!***
    """

    mazeFileRead = open(mazeFilePath, 'r')
    symbolDict['Wall'] = mazeFileRead.readline().strip('\n')
    symbolDict['Entrance'] = mazeFileRead.readline().strip('\n')
    symbolDict['Exit'] = mazeFileRead.readline().strip('\n')
    symbolDict['Road'] = mazeFileRead.readline().strip('\n')
    lines = mazeFileRead.readlines()
    for line in lines:
       mazeRow = line.strip().split(" ")
       mazeMatrix.append(mazeRow)
    mazeFileRead.close()

    print('Reading Maze File Successfully!')
    
    return mazeMatrix, symbolDict

def drawMaze(mazeMatrix, mazeWidth, mazeHeight, symbolDict):
    """
        Draws the entire maze based on the content of "mazeMatrix".
        More specifically, this function iterates over each row,
        and for each row, it iterates over each cell of the row.
        For each cell, at (column,row), it draws a square on 
        the canvas using a particular colour associated with each component
        of the maze:
        - a colour to represent the walls,
        - a colour to represent the entrance,
        - a colour to represent the exit, and
        - a colour to represent the roads.

    Parameters:
    - mazeMatrix (list of lists): The 2D matrix representing the maze layout,
      where each element indicates a specific maze component
      (wall, entrance, exit or road).
    - mazeWidth(int): The width of the maze, representing the number of columns.
    - mazeHeight(int): The height of the maze, representing the number of rows.
    - symbolDict (dictionary): A dictionary containing symbols used in the maze,
      including keys such as 'Wall', 'Entrance', 'Exit', and 'Road', and
      their corresponding symbols (the key's value).

    Returns:
    - None.

    Implementation Details:
    - Iterate over each row and column of "mazeMatrix".
    - Retrieve content of each cell and determine its corresponding component:
      is this cell a wall, entrance, exit or part of the road (i.e., path)?
    - Figure out which colour you wish to associate with this component.
    - Draw the square representing this cell using the drawSquare function and
      the colour you have associated with the component, i.e.,
      the content, of this current cell in "mazeMatrix".
        
        ***Do not modify the content of this function!***
    """
    
    # Disable animation for faster rendering.
    # Use mazeTurtle as the turtle when invoking function drawSquare to draw
    # each square on the map.
    turtle.tracer(0)
    mazeTurtle = turtle.Turtle()
    mazeTurtle.speed(0)

    for row in range(mazeHeight):
        for column in range(mazeWidth):
            item = mazeMatrix[row][column]
            if item == symbolDict['Wall']: #wall:
                blue = random.randint(100, 130)
                green = random.randint(150, 180)
                wallColor = (200, green, blue)
                drawSquare(mazeTurtle, column, row, wallColor,
                           mazeWidth, mazeHeight)
            elif item == symbolDict['Entrance']: #entrance:
                entranceColor = 'green'
                drawSquare(mazeTurtle, column, row, entranceColor,
                           mazeWidth, mazeHeight)
            elif item == symbolDict['Exit']: #exit:
                ExitColor= 'red'
                drawSquare(mazeTurtle, column, row, ExitColor,
                           mazeWidth, mazeHeight)
            else: # Assume item is road or treasure.
                roadColor = (191, 217, 225)
                drawSquare(mazeTurtle, column, row, roadColor,
                           mazeWidth, mazeHeight)

    # Re-enable animation after drawing.
    turtle.tracer(1)
    return

def computeMazeWidthAndHeight(mazeMatrix):
    """
        This function computes the width and height of the maze based on the
        dimensions of the maze matrix. It determines the number of columns as
        the length of the first row of the matrix and the number of rows as
        the total number of rows in the matrix.

    Parameter:
    - mazeMatrix (list of lists): The 2D matrix representing the maze layout,
      where each element indicates a specific maze component
      (wall, entrance, exit or road).

    Returns:
    - mazeWidth(int): The width of the maze, representing the number of columns.
    - mazeHeight(int): The height of the maze, representing the number of rows.

    Implementation Details:
    - You can assume the size of "mazeMatrix" is "mazeWidth" * "mazeHeight",
      where each row of "mazeMatrix" has the same number of columns.
    - Assign the width of the maze, i.e., the length of the first row
      of "mazeMatrix", to "mazeWidth".
      Remember: "mazeMatrix" is a list of lists.
    - Assign the height of the maze, i.e., the total number of rows in
      "mazeMatrix", to "mazeHeight". 
 
        ***Do not modify the content of this function!*** 
    """

    # Initialize local variables
    mazeWidth = 0
    mazeHeight = 0

    mazeWidth = len(mazeMatrix[0])
    mazeHeight = len(mazeMatrix)

    return mazeWidth, mazeHeight

def findSymbolPosition(mazeMatrix, mazeWidth, mazeHeight, symbolDict,
                       symbolPosition):
    """
        This function finds the positions of the symbols representing
        the 'Entrance' and the 'Exit' in "mazeMarix".
        It does so by iterating over each row and by iterating over each
        cell of the row, looking for the symbol used to represent the
        'Entrance' and the 'Exit' in "mazeMarix".
        Once found, it computes the position of the symbol, i.e., (column,row),
        then updates the dictionary "symbolPosition" with these two
        positions.

    Parameters:
    - mazeMatrix (list of lists): The 2D matrix representing the maze layout,
      where each element indicates a specific maze component
      (wall, entrance, exit or road).
    - mazeWidth(int): The width of the maze, representing the number of columns.
    - mazeHeight(int): The height of the maze, representing the number of rows.
    - symbolDict (dictionary): A dictionary containing symbols used in the maze,
      including keys such as 'Wall', 'Entrance', 'Exit', and 'Road', and
      their corresponding symbols (the key's value).
    - symbolPosition (dictionary): A dictionary containing the positions of the
      symbols representing the 'Entrance' and the 'Exit' in "mazeMatrix",
      expressed as (column,row).

    Returns:
    - symbolPosition (dictionary): Updated dictionary containing the positions
      of the symbols representing the 'Entrance' and the 'Exit' in 
      "mazeMatrix", expressed as (column,row).

    Implementation Details:
    - You can assume there is only one Entrance and one Exit in the mazeMatrix
    - Iterate over each row and column of the maze matrix.
    - Retrieve the content of each cell.
    - If the content matches the symbol for the entrance or exit as specified
      in symbolDict, update the corresponding position in symbolPosition with
      the current row and column.
    - Return the updated symbolPosition dictionary.
 
        ***Do not modify the content of this function!***
    """

    for row in range(mazeHeight):
        for column in range(mazeWidth):
            item = mazeMatrix[row][column]
            if item == symbolDict['Entrance']: #entrance:
                symbolPosition['Entrance'] = (column, row)
            elif item == symbolDict['Exit']: #exit:
                symbolPosition['Exit'] = (column, row)

    return symbolPosition


def drawTurtle(mazeWidth,mazeHeight,manualTurtle,symbolPosition,cellSize = 20):
    """
        This function initializes and configures the turtle that will
        navigate the maze. It sets the turtle's size, speed, shape, colour,
        and it sets its position to the entrance of the maze.
        Additionally, it sets up the turtle's initial heading based on the
        relative positions of the entrance and the exit in the maze.
        Finally, it draws the turtle at the 'Entrance' cell, ready to go.

    Parameters:
    - mazeWidth(int): The width of the maze, representing the number of columns.
    - mazeHeight(int): The height of the maze, representing the number of rows.
    - manualTurtle (Turtle object): The turtle that will navigate the maze.
    - symbolPosition (dictionary): A dictionary containing the positions of the
      symbols representing the 'Entrance' and the 'Exit' in "mazeMatrix",
      expressed as (column,row).
    - cellSize (int): The size of each cell at (column,row) in the maze.

    Returns:
    - None.

    Implementation Details:
    - Retrieve the 'Entrance' and the 'Exit' positions from "symbolPosition"
      dictionary.
    - Calculate the initial canvas coordinate (turtle_start_x,turtle_start_y)
      of the turtle based on the entrance coordinate.
      In implementing the above step, you may find these equations, from
      drawSquare(...), useful:
        # Calculate the top-left corner of the square to be drawn.
        squareTopX = column * cellSize - mazeWidth * cellSize / 2
        squareTopY = mazeHeight * cellSize / 2 - row * cellSize
      Note: You will have to adapt them to the current situation.
    - Calculate heading (turtle_heading_angle) of the turtle based on
      the location of the 'Entrance' and the 'Exit' in the maze.
      Note: Remember, you want the turtle to be facing toward the exit
            before you start moving your turtle about the maze.
 
        ***Do not modify the content of this function!***
    """

    # Set the turtle's size, speed, shape, colour
    manualTurtle.pensize(cellSize / 4)
    manualTurtle.speed(0)
    manualTurtle.shape('turtle')
    manualTurtle.color('yellow')
    manualTurtle.hideturtle()
    manualTurtle.clear()
    manualTurtle.penup()

    # Initialize local variables 
    turtle_heading_angle = 0
    turtle_start_x = 0
    turtle_start_y = 0

    entrance_column = symbolPosition['Entrance'][0]
    entrance_row = symbolPosition['Entrance'][1]
    exit_column = symbolPosition['Exit'][0]
    exit_row = symbolPosition['Exit'][1]    
    turtle_start_x , turtle_start_y = mazePositionToCoordinate(entrance_column,
                                      entrance_row, mazeWidth, mazeHeight)   
    if entrance_column > exit_column:
        turtle_heading_angle = 180
    else:
        turtle_heading_angle = 0
    
    # Ready the turtle for maze navigation.
    manualTurtle.setheading(turtle_heading_angle)
    manualTurtle.goto(turtle_start_x, turtle_start_y)
    manualTurtle.pendown()
    manualTurtle.showturtle()
    manualTurtle.width(3)
    
    # Bind arrow keys to movement functions.
    manualTurtle.getscreen().listen()
    manualTurtle.getscreen().onkeyrelease(headUp, 'Up')
    manualTurtle.getscreen().onkeyrelease(headDown, 'Down')
    manualTurtle.getscreen().onkeyrelease(headLeft, 'Left')
    manualTurtle.getscreen().onkeyrelease(headRight, 'Right')
        
    return


# ***Main part of the program

## Initializing variables

# 2-dimensional matrix "mazeMatrix"
# After reading the data file, "mazeMatrix" must be a 2-dimensional matrix,
# i.e., a list of lists.
# Here is an example of what "mazeMatrix" may contain after calling
# readDataFile(...) 
# mazeMatrix = [['W', 'W', 'W'],
#               ['S', '0', 'W'],
#               ['W', '0', 'E'],
#               ['W', 'W', 'W']],
# As you can see, mazeMatrix[row][column] = symbol.
# For example, in the above matrix, mazeMatrix[1][0] = 'S'
# "row 1" means the second element of the outer list, i.e., ['S', '0', 'W']
# and "column 0" means the first element of this inner list (['S', '0', 'W']),
# i.e., 'S'.
# Here, we initialize "mazeMatrix" to an empty list:
mazeMatrix = []

# "mazeWidth" signifies the number of columns in "mazeMatrix".
# Here, we initialize "mazeWidth" to 0:
mazeWidth = 0

# "mazeHeight" signifies the number of rows in "mazeMatrix".
# Here, we initialize "mazeHeight" to 0:
mazeHeight = 0

# "symbolDict" is a dictionary used to save the symbol indicating
# the 'Entrance' to the maze, the symbol indicating the 'Exit' of the maze,
# the symbol indicating the 'Wall' of the maze and the symbol indicating
# the 'Road' (i.e., the path) within the maze.
# These symbols are used in constructing the maze found in the text files.
# The format in this dictionary is <key>:<value>.
# For example, 'Wall': 'W', where the key is 'Wall' and the value is 'W'
# (the symbol indicating the walls of the maze, read from the data file).
# Here, we initialize "symbolDict" such that all its keys are set to an
# empty string:
symbolDict = {'Wall'    : '',
              'Entrance': '',
              'Exit'    : '',
              'Road'    : ''}

# "symbolPosition" is also a dictionary used to save the location of the
# 'Entrance' and the 'Exit' of the maze. This location is expressed using
# the format: (column,row), i.e., a tuple made of two elements.
# These two positions are computed in the function computeSymbolPosition(...).
# You can add other useful positions in this dictionary, but you
# cannot remove 'Entrance':<key> and 'Exit':<key> from this dictionary.
symbolPosition = {'Entrance': (0, 0),
                  'Exit'    : (0, 0)}

## Setting the game


# Hide the turtle.
turtle.hideturtle()

# Set up the game canvas.
turtle.title('Turtle Maze Game')
turtle.setup(width=700, height=650)
turtle.colormode(255)
turtle.clear()

# Get a turtle for the game.
manualTurtle = turtle.Turtle()

# Prompt the user for a data file via a dialogue box.
title = 'Maze Filename'
prompt = 'Please, enter the maze filename: '
mazeFile = turtle.textinput(title=title, prompt=prompt)

# Call the function readDataFile(...).
# This function reads the entrance, exit, wall and road symbols
# and "mazeMatrix" from the user-supplied data file.
# Notice: this function returns not one , but two "returned values"!
mazeMatrix, symbolDict = readDataFile(mazeFile, mazeMatrix, symbolDict)

# Call the function computeMazeWidthAndHeight(...).
# This function computes and returns "mazeWidth" and "mazeHeight"
# using "mazeMatrix".
mazeWidth, mazeHeight = computeMazeWidthAndHeight(mazeMatrix)

# Call the function setupMazeWindow(...).
# This function sets up the game window size based on "mazeWidth" and
# "mazeHeight" of "mazeMatrix".
setupMazeWindow(mazeWidth, mazeHeight)

# Call the function findSymbolPosition(...).
# This function finds the position of the symbol indicating the 'Entrance' 
# to the maze in the "mazeMatrix" as well as the position of the symbol
# indicating the 'Exit' of the maze and stores these two positions in the
# "symbolPosition" dictionary.
symbolPosition = findSymbolPosition(mazeMatrix, mazeWidth, mazeHeight,
                                    symbolDict, symbolPosition)

# Call the function drawMaze(...).
# This function draws the maze.
drawMaze(mazeMatrix, mazeWidth, mazeHeight, symbolDict)

# A list of the cells making up the shortest path
# taken by the turtle through the maze.
# Each cell, in this list, is represented by its location: 
# a (column, row) tuple. 
pathThroughMaze = []

# The "Entrance" cell must be the first cell (i.e., the first tuple)
# added to the "pathThroughMaze" list.
(entrance_column, entrance_row) = symbolPosition['Entrance']
pathThroughMaze.append((entrance_column, entrance_row))

# Call the function drawTurtle(...).
# This function draws the "manualTurtle", i.e., the turtle
# that will navigate through the maze, from its entrance to its exit.
drawTurtle(mazeWidth, mazeHeight, manualTurtle, symbolPosition)

# This keeps the drawing of the maze displayed on the computer monitor screen.
turtle.done()
