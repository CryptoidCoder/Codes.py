#Name+Chore Picker

#import
import tkinter
import random

#the list of possible names
names = [' Name1',' Name2',' Name3',' Name4',' Name1+Name2',' Name3+Name4',' Name4+Name1',' Name3+Name2',' Name3+Name1',' Name2+Name4','  Everyone','Name1 Choose', 'Name2 Choose', 'Name3 Choose', 'Name4 Choose']

#the list of possible chores
chores = [' Chore1',' Chore2',' Chore3',' Chore4',' Chore5',' Chore6',' Chore7',' Chore8',' Chore9',' Chore9']

#a function that will pick (and display) a name + chore
def pick():
    nameLabel.configure(text=random.choice(names) + (' =') +(random.choice(chores)))


#create a window
root = tkinter.Tk()
#create a file name
root.title("Name+ Chore Picker")
#set the size
root.geometry("1050x100")

#add a label for displaying the answer
nameLabel = tkinter.Label(root, text="", font=('Helvetica', 35))
nameLabel.pack()

#add a 'pick person' button
pickButton = tkinter.Button(text="Pick", command=pick)
pickButton.pack()


#start the GUI
root.mainloop()
