#Name+Chore Picker

#import
import tkinter
import random

#the list of possible names
names = [' Josh',' Caitlin',' Rachel',' Caleb',' Josh+Caitlin',' Rachel+Caleb',' Caleb+Josh',' Rachel+Caitlin',' Rachel+Josh',' Caitlin+Caleb','  everyone',' parents choose']

#the list of possible chores
chores = [' washing up',' loading the dishwasher',' unloading the dishwasher',' laundry',' cooking dinner',' cleaning the house',' cleaning your room',' clearing the table',' sorting the clothes into piles','  helping setup at church']

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
