#consiquence picker

#import
import tkinter
import random

#the list of possible chores
chores = [' Chore1',' Chore2',' Chore3',' Chore4',' Chore5',' Chore6',' Chore7',' Chore8',' Chore9',' Chore9']

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
