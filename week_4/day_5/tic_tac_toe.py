from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.title("Tic Tac Toe")
turn = True
rounds = 0

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or #row 1
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or #row 2
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or #row 3
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or #slant left to right
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or #slant right to left
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or #column 1
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or #column 2
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):#column 3
        tkinter.messagebox._show("TIC TAC TOE","X has won!")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or #row 1
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or #row 2
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or #row 3
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or #slant left to right
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or #slant right to left
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or #column 1
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or #column 2
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):#column 3
          tkinter.messagebox._show("TIC TAC TOE","O has won!")

def onclick(button):
    global turn,rounds
    if button["text"] == "" and turn == True:
       button["text"] = "X"
       turn = False
       rounds +=1

    elif button["text"] == "" and turn == False:
         button["text"] = "O"
         turn = True
         rounds += 1

    if rounds == 9: #checks if its tie
        tkinter.messagebox.showinfo("TIC TAC TOE","Its a tie")

    if rounds >= 5:
        checkForWin()

def onreset(button):
    global rounds
    button1['text'] = ""
    button2['text'] = ""
    button3['text'] = ""
    button4['text'] = ""
    button5['text'] = ""
    button6['text'] = ""
    button7['text'] = ""
    button8['text'] = ""
    button9['text'] = ""
    rounds = 0



button1 = Button(tk,font='Times 15 bold', bg = 'black', fg = 'white', height = 2, width = 3, command=lambda: onclick(button1))
button1.grid(row = 0, column = 0)

button2 = Button(tk, font = 'Times 15 bold', bg = 'black', fg = 'white', height = 2, width = 3, command=lambda: onclick(button2))
button2.grid(row = 0, column = 1)

button3 = Button(tk, font='Times 15 bold', bg = 'black', fg = 'white', height = 2, width = 3,command=lambda: onclick(button3))
button3.grid(row = 0, column = 2)

button4 = Button(tk,font = 'Times 15 bold', bg = 'black', fg = 'white', height = 2, width = 3,command=lambda: onclick(button4))
button4.grid(row = 1, column = 0)

button5 = Button(tk,font = 'Times 15 bold', bg = 'black', fg = 'white', height = 2, width = 3,command=lambda: onclick(button5))
button5.grid(row = 1, column = 1)

button6 = Button(tk,font = 'Times 15 bold', bg = 'black', fg = 'white', height = 2, width = 3,command=lambda: onclick(button6))
button6.grid(row = 1, column = 2)

button7 = Button(tk,font = 'Times 15 bold', bg = 'black', fg = 'white', height = 2, width = 3,command=lambda: onclick(button7))
button7.grid(row = 2, column = 0)

button8 = Button(tk,font = 'Times 15 bold', bg = 'black', fg = 'white', height = 2, width = 3,command=lambda: onclick(button8))
button8.grid(row = 2, column = 1)

button9 = Button(tk,font = 'Times 15 bold', bg = 'black', fg = 'white', height = 2, width = 3,command=lambda: onclick(button9))
button9.grid(row = 2, column = 2)

reset = Button(tk,text="RESET",font='Times 9 bold',bg='white',fg='black',height=2, width=18,command=lambda: onreset(reset))
reset.grid(row=3,columnspan=3)

tk.mainloop()