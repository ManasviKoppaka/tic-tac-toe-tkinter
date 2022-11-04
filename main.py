from tkinter import *
from tkinter.messagebox import showinfo


root = Tk()
root.title("Tic Tac Toe Game")
root.geometry("330x475")

turn="X"
board = {1:" ", 2:" ", 3:" ",
         4:" ", 5:" ", 6:" ", 
         7:" ", 8:" ", 9:" "}
player1 = StringVar()
player2 = StringVar()

def play(button):
    if player1.get()=="" or player2.get() == "":
        showinfo("Alert Message", "Please enter name for Player 1 and Player 2")
        return
    if player1.get()==player2.get():
        showinfo("Alert Message", "Please use a different name")
        return
    global turn
    for i in buttons.keys():
        if i == button:
            if buttons[i]["text"]==" ":
                board[int(str(button)[-1])]=turn
                if turn == "X":
                    buttons[i]["text"]="X"
                    if CheckWhoWins(turn):
                        print(turn, "wins")
                        showinfo("Tic Tac Toe", f"{player1.get()} wins" )
                    turn="O"
                else:
                    buttons[i]["text"]="O"
                    if CheckWhoWins(turn):
                        print(turn, "wins")
                        showinfo("Tic Tac Toe", f"{player2.get()} wins" )
                    turn="X"
                if checkForDraw():
                    showinfo("Tic Tac Toe", "Draw" )


def CheckWhoWins(player):
    if board[1] == board[2] and board[1]== board[3] and board[1] == player:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == player:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == player:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == player:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == player:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == player:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == player:
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] == player:
        return True
    else:
        return False

def checkForDraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    return True
    
def restart(buttons):
    for i in board.keys():
        board[i]=" "
    for i in buttons.values():
        i["text"]=" "


    


title = Label(text="Tic Tac Toe", bg="pink", fg="black", borderwidth=5, relief=SUNKEN, height=3, width=35, font=("arial", 12))
title.grid(row=10, column=0, columnspan=3)
player1Label = Label(text="Enter name for Player X:", bg="pink", fg="black", borderwidth=3, relief=SUNKEN, width=30)
player1Label.grid(row=15, column=0, columnspan=2)
player1Entry=Entry(textvariable=player1, width=17)
player1Entry.grid(row=15, column=2, columnspan=12)
player2Label = Label(text="Enter name for Player O:", bg="pink", fg="black", borderwidth=3, relief=SUNKEN, width=30)
player2Label.grid(row=16, column=0, columnspan=2)
player2Entry=Entry(textvariable=player2, width=17)
player2Entry.grid(row=16, column=2, columnspan=12)

button1 = Button(text=" ", borderwidth=5, bg="purple", font=("arial", 40), height=1, width=3, command=lambda:play("button1"))
button1.grid(row=20, column=0)
button2 = Button(text=" ", borderwidth=5, bg="purple", font=("arial", 40), height=1, width=3, command=lambda:play("button2"))
button2.grid(row=20, column=1)
button3 = Button(text=" ", borderwidth=5, bg="purple", font=("arial", 40), height=1, width=3, command=lambda:play("button3"))
button3.grid(row=20, column=2)

button4 = Button(text=" ", borderwidth=5, bg="purple", font=("arial", 40), height=1, width=3, command=lambda:play("button4"))
button4.grid(row=30, column=0)
button5 = Button(text=" ", borderwidth=5, bg="purple", font=("arial", 40), height=1, width=3, command=lambda:play("button5"))
button5.grid(row=30, column=1)
button6 = Button(text=" ", borderwidth=5, bg="purple", font=("arial", 40), height=1, width=3, command=lambda:play("button6"))
button6.grid(row=30, column=2)

button7 = Button(text=" ", borderwidth=5, bg="purple", font=("arial", 40), height=1, width=3, command=lambda:play("button7"))
button7.grid(row=40, column=0)
button8 = Button(text=" ", borderwidth=5, bg="purple", font=("arial", 40), height=1, width=3, command=lambda:play("button8"))
button8.grid(row=40, column=1)
button9 = Button(text=" ", borderwidth=5, bg="purple", font=("arial", 40), height=1, width=3, command=lambda:play("button9"))
button9.grid(row=40, column=2)

restartButton = Button(text="Restart the game", borderwidth=5, bg="pink", fg="black", relief=RAISED, width=45, command=lambda:restart(buttons))
restartButton.grid(row=50, column=0, columnspan=3)



buttons={"button1":button1, "button2":button2, "button3":button3, "button4":button4, "button5":button5, "button6":button6, "button7":button7, "button8":button8, "button9":button9}








root.mainloop()
