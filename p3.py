from tkinter import *
import random
from tkinter.messagebox import *

root = Tk()
root.title("Dice Simulation Game")
root.geometry("700x550+400+100")
root.configure(bg = "cyan")


def get_number(x) :
	if x == "\u2680" :
		return(1)
	elif x == "\u2681" :
		return(2)
	elif x == "\u2682" :
		return(3)
	elif x == "\u2683" :
		return(4)
	elif x == "\u2684" :
		return(5)
	elif x == "\u2685" :
		return(6)


def roll_dice() :
	d1= random.choice(dice)
	d2 = random.choice(dice)

	lab_label1.config(text = d1)
	lab_label2.config(text = d2)

	sd1 = get_number(d1)
	sd2 = get_number(d2)
	
	lab_dice1.config(text = sd1)
	lab_dice2.config(text = sd2)

	td1 = sd1 + sd2
	lab_total.config(text = f"You Rolled : {td1}")




dice = ['\u2680' , '\u2681' ,'\u2682' ,'\u2683' ,'\u2684' ,'\u2685' ]     # unicode for dice

lab_hd = Label(root , text = "Let's Start the Game" , font = ("Lucida Calligraphy" , 30 , "bold") , bg = "cyan")
lab_hd.pack(pady = 8)

my_frame = Frame(root , bg = "cyan"  )
my_frame.pack(pady = 20)

lab_label1 = Label(my_frame , text = "" , font = ("Calibri" , 100 , "bold") , bg = "cyan"  , fg = "red")
lab_label1.grid(row = 0 , column = 0 , padx = 5)

lab_dice1 = Label(my_frame , text = "" , font = ("Calibri" , 30 , "bold") , bg = "cyan"  , fg = "red")
lab_dice1.grid(row = 1 , column =0)

lab_label2 = Label(my_frame , text = "" , font = ("Calibri" , 100 , "bold") , bg = "cyan" , fg = "blue")
lab_label2.grid(row = 0 , column = 1, padx = 5)


lab_dice2 = Label(my_frame , text = "" , font = ("Calibri" , 30 , "bold") , bg = "cyan"  , fg = "blue")
lab_dice2.grid(row = 1 , column =1)

btn_roll = Button(root , text = "Roll The Dice" ,  font = ("Calibri" , 30 , "bold") , width = 12 , bd = 2 , relief = "solid" , command = roll_dice ) 
btn_roll.pack(pady = 20)

lab_total = Label(root , text = "" , font = ("Calibri" , 30 , "bold") , bg = "cyan"  , fg = "purple")
lab_total.pack(pady = 20)

def on_closing():
    if askyesno("Quit", "Do you want to exit the Game?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.iconbitmap("dice.ico")
root.mainloop()
