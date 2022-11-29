def init(arr) :
    i = 0 # loop counter
    n = 1 # number to input into the array

    print("-------------")
    while (i < 9):
        print("| ", end="")
        arr.append(str(n))
        print(n, end=" ")
        if (n == 3 or n == 6 or n == 9):
            print("| ", end="")
            print("\n-------------")

        i += 1
        n += 1
     
    return arr

def print_board(arr) :
    count = 1
    for i in arr:
        print("| ", end="")
        print(i, end=" ")
        if (count == 3 or count == 6 or count == 9):
            print("| ", end="")
            print("\n-------------")
        count += 1

def figure(player):
    if (player == 1):
        fig = 'X'
    else :
        fig = 'O'
    return fig

def prompt(player, cur):
    fig = figure(player)

    print("Player ", player, "(", fig, "): \nThe current board state:")
    # cur = board(cur)
    print_board(cur)
    choice = input("Select your desired space: ")
    if (choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6' and choice != '7' and choice != '8' and choice != '9'):
        print("Please enter a space number!\n")
        prompt(player, cur)

    space = int(choice)
    if (cur[space - 1] == 'X' or cur[space - 1] == 'O') :
        print("Please select another option because that space is taken!\n")
        prompt(player, cur)
    else :
        cur[space - 1] = fig
        print_board(cur)

def swap(player):
    if(player == 1):
        player = 2
    else:
        player = 1
    return player

def win_con(arr, player):
    fig = figure(player)
    win = False
    
    #horizontal wins
    if (arr[0] == fig and arr[1] == fig and arr[2] == fig) :
        win = True
    elif (arr[3] == fig and arr[4] == fig and arr[5] == fig):
        win = True
    elif (arr[6] == fig and arr[7] == fig and arr[8] == fig):
        win = True    
    
    #vertical wins
    elif (arr[0] == fig and arr[3] == fig and arr[6] == fig):
        win = True
    elif (arr[1] == fig and arr[4] == fig and arr[7] == fig):
        win = True
    elif (arr[2] == fig and arr[5] == fig and arr[8] == fig):
        win = True
   
    #diagonal wins
    elif (arr[0] == fig and arr[4] == fig and arr[8] == fig):
        win = True
    elif (arr[2] == fig and arr[4] == fig and arr[6] == fig):
        win = True
    
    else :
        win = False
    
    return win

def check_tie(arr):
    number = False
    for x in arr:
        if (x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9'):
            number = True
            break
    
    return not number

def game() :
    print("Welcome to a rudimentary game of tic-tac-toe. \nPlayer 1 is X and Player 2 is O. \nTo select a position select the number that corresponds to the position on the board.\n")
    arr = []
    win = False
    tie = False
    player = 2
    cur = init(arr)
    while (win == False and tie == False):
        player = swap(player)
        prompt(player, cur)
        win = win_con(cur, player) #check who wins
        tie = check_tie(cur)

    if win == True:
        print("Player", player, "has won! Play again?\n")
    else :
        print("It was a tie. Play again?\n")

again = "yes"

while(again == "yes" or again =="Yes"):
    game()
    again = input("To play again, type yes. Otherwise, enter anything else.\n")

print("Thanks for playing!")