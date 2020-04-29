#consiquence picker

#import
import tkinter
import random

#the list of possible chores
chores = ['washing up','loading the dishwasher','unloading the dishwasher','laundry','cooking dinner','cleaning the house','cleaning your room','clearing the table','sorting the clothes into piles',' helping setup at church']

#a function that will pick (and display) a chore
def pickChore():
    choreLabel.configure(text=random.choice(chores))

#create a window
root = tkinter.Tk()
#create a file name
root.title("Chore Picker")
#set the size
root.geometry("350x100")

#add a label for displaying the name
choreLabel = tkinter.Label(root, text="", font=('Helvetica', 20))
choreLabel.pack()

#add a 'pick' button
pickButton = tkinter.Button(text="Pick!", command=pickChore)
pickButton.pack()

#start the GUI
root.mainloop()
