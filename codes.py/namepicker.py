#Name Picker

#import
import tkinter
import random

#the list of possible names
names = ['Josh','Caitlin','Rachel','Caleb','Josh+Caitlin','Rachel+Caleb','Caleb+Josh','Rachel+Caitlin','Rachel+Josh','Caitlin+Caleb',' everyone','parents choose']

#a function that will pick (and display) a name
def pickName():
    nameLabel.configure(text=random.choice(names))

#create a window
root = tkinter.Tk()
#create a file name
root.title("Name Picker")
#set the size
root.geometry("350x100")
 
#add a label for displaying the name
nameLabel = tkinter.Label(root, text="", font=('Helvetica', 35))
nameLabel.pack()

#add a 'pick' button
pickButton = tkinter.Button(text="Pick!", command=pickName)
pickButton.pack()

#start the GUI
root.mainloop()
