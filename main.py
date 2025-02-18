#I import the libraries that allow it to work
import eel
import os

#I make the function callable from javascript
@eel.expose
#function that records data in the database
def registration(arg1,arg2,arg3,arg4):

   print(arg1,arg2,arg3,arg4)
   data = arg1 + " " + arg2 + " " + arg3 + " " + arg4 + "\n"
   f = open("database.dat", "a")
   f.write(data)
   f.close()

#I make the function callable from javascript
@eel.expose
#function that extracts data from the database
def extraction(word):
   f = open("database.dat", "r")
   lines = f.readlines()
   for letters in lines:

      if word.casefold() in letters.casefold():
         print(letters)
         return letters



# start the main.html file
dirname = os.path.dirname(__file__)
eel.init(os.path.join(dirname, "web/"))
eel.start('main.html',port=80)
