# Author: Alexander Sutter
# Created: 05/04/2024

"""_summary_

"""

import turtle as t
from multipledispatch import dispatch
from queue import Queue

board = [
    ["", "", ""], 
    ["", "", ""], 
    ["", "", ""]
]
boardCenters = [
    [(0,0), (0,1), (0,2)], 
    [(1,0), (1,1), (1,2)], 
    [(2,0), (2,1), (2,2)]
]
default = {
    'board' : {
        'lineColor' : 'black'
    },
    'maxPlayerSpaces' : 3
}
plays = 0

oPlays = Queue(maxsize=default['maxPlayerSpaces'])
xPlays = Queue(maxsize=default['maxPlayerSpaces'])

def checkWinner():
    isWinner = False
    winner = ''
    # Top row all same
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != '' and board[0][1] != '' and board[0][2] != '':
        print("Winner1")
        isWinner = True
        if board[0][0] == 'x':
            print("X Wins")
            winner = 'x'
        elif board[0][0] == 'o': 
            print("O Wins")
            winner = 'o'
    # Center row all same
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != '' and board[1][1] != '' and board[1][2] != '':
        print("Winner2")
        isWinner = True
        if board[1][0] == 'x':
            print("X Wins")
            winner = 'x'
        elif board[1][0] == 'o': 
            print("O Wins")
            winner = 'o'
    # Bottom row all same
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != '' and board[2][1] != '' and board[2][2] != '':
        print("Winner3")
        isWinner = True
        if board[2][0] == 'x':
            print("X Wins")
            winner = 'x'
        elif board[2][0] == 'o': 
            print("O Wins")
            winner = 'o'
    
    # Left Column all same
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != '' and board[1][0] != '' and board[2][0] != '':
        print("Winner4")
        isWinner = True
        if board[0][0] == 'x':
            print("X Wins")
            winner = 'x'
        elif board[0][0] == 'o': 
            print("O Wins")
            winner = 'o'
    # Middle Column all same
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != '' and board[1][1] != '' and board[2][1] != '':
        print("Winner5")
        isWinner = True
        if board[1][0] == 'x':
            print("X Wins")
            winner = 'x'
        elif board[1][0] == 'o': 
            print("O Wins")
            winner = 'o'
    # Right Column all same
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != '' and board[1][2] != '' and board[2][2] != '':
        print("Winner6")
        isWinner = True
        if board[2][0] == 'x':
            print("X Wins")
            winner = 'x'
        elif board[2][0] == 'o': 
            print("O Wins")
            winner = 'o'
    
    # Top Left to Bottom Right Diagonal all same
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != '' and board[1][1] != '' and board[2][2] != '':
        print("Winner7")
        isWinner = True
        if board[1][1] == 'x':
            print("X Wins")
            winner = 'x'
        elif board[1][1] == 'o': 
            print("O Wins")
            winner = 'o'
    # Bottom Left to Top Right all same
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != '' and board[1][1] != '' and board[2][0] != '':
        print("Winner8")
        isWinner = True
        if board[1][1] == 'x':
            print("X Wins")
            winner = 'x'
        elif board[1][1] == 'o': 
            print("O Wins")
            winner = 'o'
    
    return isWinner

def drawBoard():
    setBoardCenters()
    
    drawLine(330, (-55, 170), 'down')

    drawLine(330, (55, 170), 'down')

    drawLine(330, (-170, 55), 'right')

    drawLine(330, (-170, -55), 'right', True)

def drawLine(length, startingPoint=(0,0), heading='right', returnToCenter=False):
    t.penup()
    
    t.goto(startingPoint)
    
    t.pendown()
    
    # headings are defined assuming turtle is in standard mode
    if (heading == 'right'):
        t.setheading(0)
    elif (heading == 'left'):
        t.setheading(180)
    elif (heading == 'up'):
        t.setheading(90)
    elif (heading == 'down'):
        t.setheading(270)
    else:
        t.setheading(heading)
    
    t.forward(length)
    
    t.penup()
    
    if (returnToCenter):
        t.goto(0,0)

def drawO(centerPostition, color):
    print(centerPostition)
    print(color)
    
    radius = 50
    circleStart = (centerPostition[0], centerPostition[1] - radius)
    print(circleStart)
    
    t.penup()
    
    t.setheading(0)
    
    t.goto(circleStart)
    
    t.pendown()
    
    t.circle(50)
    
    t.penup()

@dispatch(object, str)
def drawX(centerPosition, color):
    print(centerPosition)
    print(color)
    for i in range(4):
        drawLine(50, centerPosition, ((i + 1) * 90 + 45))

@dispatch(object)
def drawX(centerPosition):
    global default
    drawX(centerPosition, default['board']['lineColor'])

@dispatch(str, str, str)
def drawX(x, y, color):
    drawX((x, y), color)
    
@dispatch(str, str)
def drawX(x, y):
    global default
    drawX((x, y), default['board']['lineColor'])

def gameover():
    finalThoughts = input("Any final words")
    t.bye()

def getClickedSpace(playerClick):
    x = playerClick[0]
    y = playerClick[1]
    
    # Determine column clicked
    if x < -55.0:
        # x = -110.0
        column = 0
    elif x >= -55.0 and x < 55.0:
        # x = 0.0
        column = 1
    elif x >= 55.0:
        # x = 110.0
        column = 2
    
    # Determine row clicked
    if y < -55.0:
        # y = -110.0
        row = 2
    elif y >= -55.0 and y < 55.0:
        # y = 0.0
        row = 1
    elif y >= 55.0:
        # y = 110.0
        row = 0
    
    return (row, column)

def getSpaceCenter(boardSpace):
    return boardCenters[boardSpace[0]][boardSpace[1]]

def playGame(x, y):
    global plays

    print('')

    playerClicked = (x,y)
    print(str(x) + ", " + str(y))

    playerClickedSpace = getClickedSpace(playerClicked)
    print(playerClickedSpace)

    spaceCenter = getSpaceCenter(playerClickedSpace)
    print(spaceCenter)
    
    if(plays % 2 == 0):
        # x's turn
        drawX(spaceCenter)
        recordPlay('x', playerClickedSpace)
    else:
        # o's turn
        drawO(spaceCenter, 'black')
        recordPlay('o', playerClickedSpace)
    
    plays += 1
    
    print(board[0])
    print(board[1])
    print(board[2])

    winner = checkWinner()
    print("winner = " + str(winner))
    if winner: 
      gameover()

def displayQueue(queue, qName):
    print(qName)
    for i in range(queue.qsize()):
        qitem = queue.get()
        print("  " + str(qitem))
        queue.put(qitem)
    
def recordPlay(player, space):
    global board
    global oPlays
    global xPlays
    
    print(space)
    
    board[space[0]][space[1]] = player
    
    if (player == 'o'):
        if (oPlays.full()):
            # code
            print('')
        oPlays.put(space)
        displayQueue(oPlays,'oPlays')
    elif (player == 'x'):
        if (xPlays.full()):
            # code
            print('')
        xPlays.put(space)
        displayQueue(xPlays,'xPlays')

def setBoardCenters():
    global boardCenters
    boardCenters = [
        [(-110.0,  110.0), (0.0,  110.0), (110.0,  110.0)], 
        [(-110.0,    0.0), (0.0,    0.0), (110.0,    0.0)], 
        [(-110.0, -110.0), (0.0, -110.0), (110.0, -110.0)]
    ]

print('HI')

drawBoard()

t.onscreenclick(playGame)

t.done() # Keep turtle window open

""" Program Outline

# Function
drawX # and its dispatched functions
drawY # and its dispatched functions

# Main

drawBoard


"""