from tkinter import *
from PIL import Image,ImageTk
from random import randint
 
#main window
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="#9b59b6")

#picture
rock_img=ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_img=ImageTk.PhotoImage(Image.open("paper_user.png"))
scissor_img=ImageTk.PhotoImage(Image.open("scissor_user.png"))
rock_comp=ImageTk.PhotoImage(Image.open("rock.jpg"))
paper_comp=ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_comp=ImageTk.PhotoImage(Image.open("scissors.png"))

#insert picture
user_label = Label(root,image=rock_img,bg="yellow")
comp_label = Label(root,image=scissor_comp,bg="pink")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=5)

#scores
playerScore = Label(root, text=0, font = 100, bg="blue", fg="white")
ComputerScore = Label(root, text=0, font = 100, bg="blue", fg="white")
playerScore.grid(row=1,column=3)
ComputerScore.grid(row=1,column=1)

#indicators
user_indicator= Label(root, font=50,text="USER", bg="pink",fg="black")
comp_indicator= Label(root, font=50,text="COMPUTER" , bg="pink",fg="black")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg = Label(root, font=50, bg="pink",fg="black")
msg.grid(row=3, column=2)

#update message
def updateMessage(x):
	msg['text']=x

#update user score
def updateUserScore():
	score = int(playerScore["text"])
	score += 1
	playerScore["text"] = str(score)

#update computer score
def updateCompScore():
	score = int(ComputerScore["text"])
	score += 1
	ComputerScore["text"] = str(score)

#check winner
def checkWinner(player,computer):
	if player == computer:
		updateMessage("It is a TIE !!!")
	elif player == "rock":
		if computer == "paper":
			updateMessage("You Lost")
			updateCompScore()
		else:
			updateMessage("You Win")
			updateUserScore()
	elif player == "paper":
		if computer == "scissor":
			updateMessage("You Lost")
			updateCompScore()
		else:
			updateMessage("You Win")
			updateUserScore()
	elif player == "scissor":
		if computer == "rock":
			updateMessage("You Lost")
			updateCompScore()
		else:
			updateMessage("You Win")
			updateUserScore()
	else:
		pass


#update choices

choices=["rock","paper", "scissor"]

def updateChoice(x):
   
    #for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
    	comp_label.configure(image=rock_comp)
    elif compChoice == "paper":
    	comp_label.configure(image=paper_comp)
    else:
    	comp_label.configure(image=scissor_comp)

    #for user
    if x=="rock":
	    user_label.configure(image=rock_img)
    elif x=="paper":
	    user_label.configure(image=paper_img)
    else:
	    user_label.configure(image=scissor_img)

    checkWinner(x,compChoice)


#buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#FF3E4D",fg="black", command= lambda:updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#FAD02E",fg="black",command= lambda:updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#0ABDE3",fg="black",command= lambda:updateChoice("scissors")).grid(row=2, column=3)


root.mainloop()
