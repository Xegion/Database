#
#   Experimenting with data 
#   minipulation for a project
#

#A fake database for testing purposes
database = ["00010002Jane Doe", "00021100John Smith"]
#Main loop
while True:
  #Asking user what they want to do
  choice = str(input("Search User or Create?"))
  #How to end the process
  if choice == "break":
      break
  #If they want to look for a user
  elif choice == "search":
    #Asks for the users ID number
    idnum = str(input("What ID number are they?"))
    #These lines make it so if you just type 2 it will look for 0002 in the database
    if len(idnum) == 1:
      idnum = "000" + idnum
    elif len(idnum) == 2:
      idnum = "00" + idnum
    elif len(idnum) == 3:
      idnum = "0" + idnum
    elif len(idnum) >= 5:
      print("Id is too long")
      break
    else:
      break
    #This goes through the database comparing IDs
    databaselen = len(database)
    for i in range(databaselen):
      databasenum = database[i]
      if databasenum[0:4] == idnum:
        print("Found user requested")
        break
    for i in range(len(databasenum)):
      #This is used for filtering out the users name
      numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
      #Scans the users code for where their name is
      if databasenum[i] not in numbers:
        name = databasenum[i:]
        break
    #Prints the users name once found
    print("Users name is " + name)
    #Checks the next number to establish gender
    if databasenum[4:5] == "0":
      print("User is Female")
    elif databasenum[4:5] == "1":
      print("User is Male")
    #Checks the next number to establish if theu have recieved their monthly donation
    if databasenum[5:6] == "0":
      print("User has not received their monthly food")
    elif databasenum[5:6] == "1":
      print("User has received their monthly food")
    #Checks the next two numbers to find out how many children
    childnum = databasenum[6:8]
    if childnum == "00":
      print("User has no children")
    elif childnum != "00":
      #This makes it so if they have for example 5 children it doesn't display as 05 and just 5
        if childnum[0] != "0":
          print("User has " + childnum + " children")
        elif childnum[0] == "0":
          print("User has " + childnum[1] + " children")
    print("")
  #This allows for users to be added
  elif choice =="create":
    #Our variable where the users code will be peiced together
    newuser = ""
    #Getting length of the database so the correct amount of 0s can be put infront
    datalen = len(database)
    #Figuring out how many 0s are infront and adding them
    if datalen <= 9:
      newuser = newuser + "000"
    elif datalen <= 99:
      newuser = newuser + "00"
    elif datalen <= 999:
      newuser = newuser + "0"
    #Adding the users id number
    newuser = newuser + str(len(database) + 1)
    #Asking for there gender
    gender = str(input("What gender?"))
    #Takes input and adds 0 or 1 depending on gender
    if gender in ["Male", "male"]:
      newuser = newuser + "1"
    elif gender == ["Female", "female"]:
      newuser = newuser + "0"
    #Asking if they have received their monthly food
    foodformonth = str(input("Have they received their food for the month?"))
    #Taking input and adding 1 or 0 if they have or haven't
    if foodformonth in ["Yes", "yes"]:
      newuser = newuser + "1"
    elif foodformonth in ["No", "no"]:
      newuser = newuser + "0"
    #Asking how many children they have
    children = str(input("How many children do they have?"))
    #Making it so for example they have 2 children it is added to their code as 02 not just 2
    if len(children) == 1:
      children = "0" + children
      newuser = newuser + children
    elif len(children) == 2:
      newuser = newuser + children
    #Taking users name and adding it
    name = str(input("What is their name?"))
    newuser = newuser + name
    print("New users code is " + newuser)
    #Adding it to the list
    database.append(newuser)
  
        
      
      
      
      
