import os
 
# Get the list of all files and directories
path = input("Path to the directory you want to index: ")
indexlocation = input("Path to the index file to be created: ")
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)

def addnewline(file,text):
    # Open the file in append & read mode ('a+')
    with open(file, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text)
        file_object.close()

for file in dir_list:
    addnewline(indexlocation, file)
