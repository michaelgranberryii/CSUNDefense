# Name: Michael Granberry
# Project: Tic Tac Toe
# Company: Northridge Defense
# Date: 6/20/2022

import random

# Variables
board = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]
        
orignalBoard = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]

playerOneIcon = "X"
playerTwoIcon = "Q"
currentPlayer = "X"
winner = None # init with no value
gameRunning = True # game running variable

# Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Take player input
def playerInput(board):
    print("\n")
    inp = int(input("Enter a number 1 - 9: "))
    if inp >= 1 and inp <= 9 and (str(inp) in board):
        board[inp-1] = currentPlayer
    else:
        print("Spot already taken! Pick a new spot\n")
        playerInput(board)
    
# Check for win cases
def checkRows(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "1":
        winner = board[0]
        return True
    elif board[3] == board [4] == board [5] and board[3] != "3":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "7":
        winner = board[6]
        return True

def checkColumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "3":
        winner = board[0]
        return True
    elif board[1] == board [4] == board [7] and board[4] != "4":
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "5":
        winner = board[5]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[4] != "4":
        winner = board[0]
        return True
    elif board[2] == board [4] == board [6] and board[6] != "6":
        winner = board[4]
        return True

# Win
def checkWin():
    if checkDiag(board) or checkColumn(board) or checkRows(board):
        global gameRunning
        print(f"The winner is {winner}\n")
        printBoard(board)
        print("\n")
        gameRunning = False

# Tie
def checkTie(board):
    global winner
    global gameRunning
    if checkBoard(orignalBoard, board):
        printBoard(board)
        print("It is a tie!\n")
        gameRunning = False

def checkBoard(orignalBoard, board):
    check = None
    count = 0
    for spotNum in orignalBoard:
        check = spotNum in board
        if check == False:
            count = count + 1
    if count == 9:
        return True
    else: 
        return False

# Switch thr player
def switchPlayer():
    global currentPlayer
    if currentPlayer == playerOneIcon:
        currentPlayer = playerTwoIcon
    else:
        currentPlayer = playerOneIcon

# Computer
def computer(board):
    while currentPlayer == playerTwoIcon:
        position= random.randint(0, 8)
        if str(board[position]) in orignalBoard:
            board[position] = playerTwoIcon
            switchPlayer()

# Check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)