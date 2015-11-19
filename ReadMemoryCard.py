import glob, os
import mysql.connector
# set the directory path in path variable
path="C:/Users/neeraj/Desktop/desktopOld"
os.chdir(path)

# provide the file type , here we are taking text files
for file in glob.glob("*.txt"):
    bookPath=path+"/"+file
    print(bookPath)
#Load all boooks to database by calling book.py as method below this
