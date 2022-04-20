# Author: Alexander Sutter
# Date: April 4, 2022
# Latest Revision: April 4, 2022

import turtle as t

count = 0
spaces = [
    ["", "", ""], 
    ["", "", ""], 
    ["", "", ""]
]
row = 0
col = 0

def drawBoard():
    t.penup()
    t.goto(-55, 170)
    t.pendown()
    t.rt(90)
    t.fd(330)
    t.penup()

    t.goto(55, 170)
    t.pendown()
    t.fd(330)
    t.penup()

    t.goto(-170, 55)
    t.pendown()
    t.lt(90)
    t.fd(330)
    t.penup()

    t.goto(-170, -55)
    t.pendown()
    t.fd(330)
    t.penup()
    t.goto(0, 0)

def makeX(Pos):
    t.goto(Pos)
    t.pendown()
    t.rt(45)
    for i in range(4):
        t.fd(50)
        t.fd(-50)
        t.rt(90)
    t.lt(45)
    t.penup()

def makeO(Pos):
    t.goto(Pos)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.pendown()
    t.circle(50)
    t.penup()
    t.lt(90)
    t.fd(50)
    t.rt(90)

def correctX(x):
    global col
    if x < -55.0:
        x = -110.0
        col = 0
    elif x >= -55.0 and x < 55.0:
        x = 0.0
        col = 1
    elif x >= 55.0:
        x = 110.0
        col = 2
    return x

def correctY(y):
    global row
    if y < -55.0:
        y = -110.0
        row = 2
    elif y >= -55.0 and y < 55.0:
        y = 0.0
        row = 1
    elif y >= 55.0:
        y = 110.0
        row = 0
    return y

def correctPosition(x, y):
    x = correctX(x)
    y = correctY(y)
    return (x, y)

def recordPlay(player):
    print(str(row) + ", " + str(col))
    global spaces
    spaces[row][col] = player   

def checkWinner():
    #Top row all same
    if spaces[0][0] == spaces[0][1] and spaces[0][1] == spaces[0][2] and spaces[0][0] != '' and spaces[0][1] != '' and spaces[0][2] != '':
        print("Winner1")
        if spaces[0][0] == 'x':
            print("X Wins")
        elif spaces[0][0] == 'o': 
            print("O Wins")
    #Center row all same
    elif spaces[1][0] == spaces[1][1] and spaces[1][1] == spaces[1][2] and spaces[1][0] != '' and spaces[1][1] != '' and spaces[1][2] != '':
        print("Winner2")
        if spaces[1][0] == 'x':
            print("X Wins")
        elif spaces[1][0] == 'o': 
            print("O Wins")
    #Bottom row all same
    elif spaces[2][0] == spaces[2][1] and spaces[2][1] == spaces[2][2] and spaces[2][0] != '' and spaces[2][1] != '' and spaces[2][2] != '':
        print("Winner3")
        if spaces[2][0] == 'x':
            print("X Wins")
        elif spaces[2][0] == 'o': 
            print("O Wins")
    
    #Left Column all same
    elif spaces[0][0] == spaces[1][0] and spaces[1][0] == spaces[2][0] and spaces[0][0] != '' and spaces[1][0] != '' and spaces[2][0] != '':
        print("Winner4")
        if spaces[0][0] == 'x':
            print("X Wins")
        elif spaces[0][0] == 'o': 
            print("O Wins")
    #Middle Column all same
    elif spaces[0][1] == spaces[1][1] and spaces[1][1] == spaces[2][1] and spaces[0][1] != '' and spaces[1][1] != '' and spaces[2][1] != '':
        print("Winner5")
        if spaces[1][0] == 'x':
            print("X Wins")
        elif spaces[1][0] == 'o': 
            print("O Wins")
    #Right Column all same
    elif spaces[0][2] == spaces[1][2] and spaces[1][2] == spaces[2][2] and spaces[0][2] != '' and spaces[1][2] != '' and spaces[2][2] != '':
        print("Winner6")
        if spaces[2][0] == 'x':
            print("X Wins")
        elif spaces[2][0] == 'o': 
            print("O Wins")
    
    #Top Left to Bottom Right Diagonal all same
    elif spaces[0][0] == spaces[1][1] and spaces[1][1] == spaces[2][2] and spaces[0][0] != '' and spaces[1][1] != '' and spaces[2][2] != '':
        print("Winner7")
        if spaces[1][1] == 'x':
            print("X Wins")
        elif spaces[1][1] == 'o': 
            print("O Wins")
    #Bottom Left to Top Right all same
    elif spaces[0][2] == spaces[1][1] and spaces[1][1] == spaces[2][0] and spaces[0][2] != '' and spaces[1][1] != '' and spaces[2][0] != '':
        print("Winner8")
        if spaces[1][1] == 'x':
            print("X Wins")
        elif spaces[1][1] == 'o': 
            print("O Wins")

def gameover():
    finalThoughts = input("Any final words")
    t.bye()

def playGame(x, y):
    global count
    t.penup()
    t.goto(x, y)
    
    #correcting position of click to make it perfect
    Position = correctPosition(x, y)
    
    if(count % 2 == 0):
        # o's turn
        makeO(Position)
        recordPlay('o')
    else:
        # x's turn
        makeX(Position)
        recordPlay('x')
    count += 1
    print(spaces)
    print(str(x) + ", " + str(y))

    winner = checkWinner()
    if winner: 
      gameover()


drawBoard()

t.onscreenclick(playGame)

t.done()
