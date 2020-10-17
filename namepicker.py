#Name Picker

#import
import tkinter
import random

#the list of possible names
names = ['name 1','name 2','name 3','name 4','name 5','name 6']

#a function that will pick (and display) a name
def pickName():
    nameLabel.configure(text=random.choice(names))

#create a window
root = tkinter.Tk()
#create a file name
root.title("Name Picker")
#set the size
root.geometry("200x100")

#add a label for displaying the name
nameLabel = tkinter.Label(root, text="", font=('Helvetica', 32))
nameLabel.pack()

#add a 'pick name' button
pickButton = tkinter.Button(text="Pick!", command=pickName)
pickButton.pack()

#start the GUI
root.mainloop()
