""""
Admin Program

StudentID: p2227395
Name:      Keyan Goh
Class:     DISM/1B/03
Assesment: CA1-1

Script name:
    admin.py

Purpose:
   This progam is an admin program where admins can log in with a specified username and password to change the settings of the main python hangman game (hangman.py)

Python Version:
   Python 3

Refernce:
   https://chat.openai.com/chat
"""

# ====================================
# imports
# ====================================v
import json
import time
import datetime
from datetime import datetime


def displayList():
    """
    Function which prints the list of words(Animal names) stored in a JSON dictionary which is in a JSON file (CA1/wordlistanimals.json)
    """    
    filename = "CA1/wordlistanimals.json"
    with open(filename, "r") as file:
        data = json.load(file)
        print(json.dumps(data, indent=4))

def displayList2():
    """
    Function which prints the list of words(Complex words) stored in a JSON dictionary which is in a JSON file (CA1/wordlistComplex.json)
    """    
    filename = "CA1/wordlistComplex.json"
    with open(filename, "r") as file:
        data = json.load(file)
        print(json.dumps(data, indent=4))

def displayList3():
    """
    Function which prints the list of words(Idioms) stored in a JSON dictionary which is in a JSON file (CA1/wordlistidioms.json)
    """    
    filename = "CA1/wordlistidioms.json"
    with open(filename, "r") as file:
        data = json.load(file)
        print(json.dumps(data, indent=4))

def wordlistAppend():
    """
    Function which appends the word(key) and decription(value) of a word that the user would like to add into the word pool a JSON dictionary stored in a JSON file(CA1/wordlistanimals.json)
    """    
    filename = "CA1/wordlistanimals.json"
    word = input("Word:")
    desc = input("Description:")
#read file content
    with open(filename, "r") as file:
        data = json.load(file)
#Write json file
    with open(filename,"w") as file:
    #as when open file as write, the code doesnt know what is indie the json file, and ends up replacing the whole thing.
        data[word.lower()] = desc
        json.dump(data,file,indent=4)

def wordlistAppend2():
    """
    Function which appends the word(key) and decription(value) of a word that the user would like to add into the word pool a JSON dictionary stored in a JSON file(CA1/wordlistComplex.json)
    """  
    filename = "CA1/wordlistComplex.json"
    word = input("Word:")
    desc = input("Description:")
#read file content
    with open(filename, "r") as file:
        data = json.load(file)
#Write json file
    with open(filename,"w") as file:
    #as when open file as write, the code doesnt know what is indie the json file, and ends up replacing the whole thing.
        data[word.lower()] = desc
        json.dump(data,file,indent=4)

def wordlistAppend3():
    """
    Function which appends the word(key) and decription(value) of a word that the user would like to add into the word pool a JSON dictionary stored in a JSON file(CA1/wordlistidioms.json)
    """  
    filename = "CA1/wordlistidioms.json"
    word = input("Word:")
    desc = input("Description:")
#read file content
    with open(filename, "r") as file:
        data = json.load(file)
#Write json file
    with open(filename,"w") as file:
    #as when open file as write, the code doesnt know what is indie the json file, and ends up replacing the whole thing.
        data[word.lower()] = desc
        json.dump(data,file,indent=4)

def wordlistDel():
    """
    Function which appends the word(key) and decription(value) of a word that the user would like to delete from the word pool a JSON dictionary stored in a JSON file(CA1/wordlistanimals.json)
    """      
    filename = "CA1/wordlistanimals.json"
    word = input("Word:")
    with open(filename, "r") as file:
        data = json.load(file)
    if word in data:
        with open(filename,"w") as file:
            del data[word]
            json.dump(data,file,indent=4)
    else:
        print("<<Error>> Word is not in list\n\n")


def wordlistDel2():
    """
    Function which appends the word(key) and decription(value) of a word that the user would like to delete from the word pool a JSON dictionary stored in a JSON file(CA1/wordlistComplex.json)
    """ 
    filename = "CA1/wordlistComplex.json"
    word = input("Word:")
    with open(filename, "r") as file:
        data = json.load(file)
    if word in data:
        with open(filename,"w") as file:
            del data[word]
            json.dump(data,file,indent=4)
    else:
        print("<<Error>> Word is not in list\n\n")


def wordlistDel3():
    """
    Function which appends the word(key) and decription(value) of a word that the user would like to delete from the word pool a JSON dictionary stored in a JSON file(CA1/wordlistidioms.json)
    """ 
    filename = "CA1/wordlistidioms.json"
    word = input("Word:")
    with open(filename, "r") as file:
        data = json.load(file)
    if word in data:
        with open(filename,"w") as file:
            del data[word]
            json.dump(data,file,indent=4)
    else:
        print("<<Error>> Word is not in list\n\n")

def editValue():
    """
    Function which allows user to change the meaning(value) of a certain word in the JSON dictionary containing the word pool in the JSON file(wordlistanimals.json)
    """    
    filename = "CA1/wordlistanimals.json"
    word = input("Word:")
    newValue = input("Enter new description:")
    with open(filename, "r") as file:
        data = json.load(file)
    if word in data:
        with open(filename,"w") as file:
            data[word.lower()] = newValue
            json.dump(data,file,indent=4)
    else:
        print("<<Error>> Word is not in list\n\n")

def editValue2():
    """
    Function which allows user to change the meaning(value) of a certain word in the JSON dictionary containing the word pool in the JSON file(wordlistComplex.json)
    """    
    filename = "CA1/wordlistComplex.json"
    word = input("Word:")
    newValue = input("Enter new description:")
    with open(filename, "r") as file:
        data = json.load(file)
    if word in data:
        with open(filename,"w") as file:
            data[word.lower()] = newValue
            json.dump(data,file,indent=4)
    else:
        print("<<Error>> Word is not in list\n\n")

def editValue3():
    """
    Function which allows user to change the meaning(value) of a certain word in the JSON dictionary containing the word pool in the JSON file(wordlistIdioms.json)
    """    
    filename = "CA1/wordlistidioms.json"
    word = input("Word:")
    newValue = input("Enter new description:")
    with open(filename, "r") as file:
        data = json.load(file)
    if word in data:
        with open(filename,"w") as file:
            data[word.lower()] = newValue
            json.dump(data,file,indent=4)
    else:
        print("<<Error>> Word is not in list\n\n")

def changenumwords():
    """
    Function which changes the number of words in each attempt, stored in a seperate settings file (CA1/settings.json)
    """    
    filename = "CA1/settings.json"
    with open(filename, "r") as file:
        data = json.load(file)
        with open(filename,"w") as file:
            data["number of words"] = newInput
            json.dump(data,file,indent=4)
    
def changenumattempts():
    """
    Function which changes the number of attempts per set, stored in a seperate settings file (CA1/settings.json)
    """        
    filename = "CA1/settings.json"
    with open(filename, "r") as file:
        data = json.load(file)
        with open(filename,"w") as file:
            data["number of attempts"] = newInput
            json.dump(data,file,indent=4)

def changepassword():
    """
    Function which allows the admin to change the log in password, stored in a seperate settings file (CA1/settings.json)
    """    
    filename = "CA1/settings.json"
    with open(filename, "r") as file:
        data = json.load(file)
        with open(filename,"w") as file:
            data["Password"] = changedPass
            json.dump(data,file,indent=4)

def viewGameLog():
    """
    Function which allows the admin to view the game logs stored in a seperate gamelogs JSON file (CA1/game_log.json). It specifies the username, score, words guessed, number of attempts, as well as correct and incorrect guesses of the player.
    And the admin can specify the start and end date of the gamelogs displayed
    """
    filename = 'CA1/game_log.json'
    with open(filename, "r") as file:
        data = json.load(file)
        print('\nEnter "E" to view specific start time and end time game logs, or any other character to see full game log ')
        inputChoices = input(">>>")
        if inputChoices.lower() == "e":

    # Parse the start and end dates entered by the user
            date_format = "%a %b %d %H:%M:%S %Y"
            start_date_string = input("Enter start date (e.g. Mon Dec 19 01:45:59 2022): ")
            # Try to parse the start date
            try:
                start_date = time.strptime(start_date_string, date_format)
            except ValueError:
                print("Invalid start date format. Please enter time in the format stated in the example.")
            else:
                end_date_string = input("Enter end date (e.g. Mon Dec 19 01:45:59 2022): ")
                try:
                    end_date = time.strptime(end_date_string, date_format)
                except ValueError:
                    print("Invalid end date format")
                else:
                    start_date = datetime.strptime(start_date_string, "%a %b %d %H:%M:%S %Y")
                    end_date = datetime.strptime(end_date_string, "%a %b %d %H:%M:%S %Y")
                    date_list = data["Date"]
                    data_username = data["Username"]
                    data_score = data["Score"]
                    data_numWords = data["Words Guessed Per Attempt"]
                    data_numAttps = data["Number of Attempts"]
                    data_correctGuess = data["Correct Guesses"]
                    data_wrongGuess = data["Incorrect Guesses"]
                    # Iterate over the list of dates and check if each date is between the start and end dates
                    for i, date_string in enumerate(date_list):
                        date = datetime.strptime(date_string, "%a %b %d %H:%M:%S %Y")
                        if start_date.date() <= date.date() <= end_date.date():
                            print(f"\n\nDate: {date_string}")
                            print(f"Username: {data_username[i]}")
                            print(f"Score: {data_score[i]}")
                            print(f"Number of Words Per Attempt: {data_numWords[i]}")
                            print(f"Number of Attempts: {data_numAttps[i]}")
                            print(f"Correct Guesses:{data_correctGuess[i]}")
                            print(f"Incorrect Guesses: {data_wrongGuess[i]}\n")

        else:
            print(json.dumps(data, indent=4))

def changeLeaderboard():
    """
    Function which allows the admin to change the number of top players displayed on the leaderboard in the main game. The settings are stored in a seperate JSON file (CA1/settings.json)
    """    
    filename = "CA1/settings.json"
    with open(filename, "r") as file:
        data = json.load(file)
        with open(filename,"w") as file:
            data["number of top players"] = changeTop
            json.dump(data,file,indent=4)

passWhile = True

specialCharacter = ['!','@','#','$','%']
originalPass = "qQ1@"
countUpper = 0
countLower = 0    



adminLogin = True
print("\n========================================================================================\n                            Welcome to admin settings\n========================================================================================\n\n")
while adminLogin: #while loop which displays the log in page. If log in credentials are valid, loop will break
    inputUser = input("Enter Username:")
    if inputUser == "admin":
        inputPass = input("Enter Password:")
        with open('CA1/settings.json','r') as passw:
            getpass = json.load(passw)
            password = getpass["Password"]
        if inputPass == password:
            print("\n========================================================================================\n                                Access Granted\n========================================================================================")
            break
        else:
            print("Password is invalid!")
    else:
        print("Username not in database. Please try again.")

adminSettings = True
while adminSettings: #while loop which displays the admin settings menu
    print("(1) Edit Word Pool\n(2) Edit Number of Words Per Set\n(3) Edit Number of Attempts Per Set\n(4) View Game Logs\n(5) Set number of players displayed on the leaderboard\n(6) Reset Password\n(7) Quit")
    inputSettings = input("Please enter selection >>>")

    if inputSettings == "1": #input option 1 to edit word pool
        print("Editing word pool....")
        editWord = True
        while editWord: #loop which displays the menu to edit the word pool
            print("(1)Display word pool\n(2)Add word to Word Pool\n(3)Delete word from Word Pool\n(4)Edit description of a specific word\n(5)Cancel")
            inputWordSelect = input("Please enter selection >>>")
            if inputWordSelect == "1":
                print("============================================Animal Names============================================")
                displayList()
                print("============================================Complex Words============================================")
                displayList2()
                print("===============================================Idioms================================================")
                displayList3()
                print("=====================================================================================================")
            elif inputWordSelect == "2":
                print("Which list would you like to add a word to...\n1.Animal Names\n2.Complex Words\n3.Idioms")
                inputAddWord = input("Please enter selection >>>")
                if inputAddWord == "1":
                #Append to simple word list function
                    wordlistAppend()
                elif inputAddWord == "2":
                    wordlistAppend2()
                elif inputAddWord == "3":
                    wordlistAppend3()
                else:
                    print("Invalid selection. Please try again...")

            elif inputWordSelect == "3":
                print("Which list would you like to delete a word from...\n1.Animal Names\n2.Complex Words\n3.Idioms")
                inputDelWord = input("Please enter selection >>>")
                #Delete word from one of the list
                if inputDelWord == "1":
                    wordlistDel()
                elif inputDelWord == "2":
                    wordlistDel2()
                elif inputDelWord == "3":
                    wordlistDel3()
                else:
                    print("Invalid selection. Please try again...")

            elif inputWordSelect == "4":
                print("Which list would you like to edit the description of a word from...\n1.Animal Names\n2.Complex Words\n3.Idioms")
                inputEditWord = input("Please enter selection >>>")
                if inputEditWord == "1":
                    editValue()
                elif inputEditWord == "2":
                    editValue2()
                elif inputEditWord == "3":
                    editValue3()
            elif inputWordSelect == "5":
                print("\n\nReturning to main menu...")
                break
            else:
                print("Please enter a valid input!")
    elif inputSettings == "2": #input option 2 which changes the number of words per set
        print("Edit number of words per set. Please enter a numeric value")
        input2 = True
        while input2: #loop which ensures that user enters an integer value when changing number of words per set
            try:
                newInput = int(input("Enter new number of words per set:"))
                changenumwords()
                break
            except ValueError:
                print("Please enter a integer value!")
                input2 = True
        

    elif inputSettings == "3": #input 3 which changes the number of attempts per set
        print("Edit number of attempts per set. Please enter a numeric value")
        input3 = True
        while input3: #loop which ensures that user enters an integer value when changing number of attempts per set
            try:
                newInput = int(input("Enter new number of attempts per set:"))
                changenumattempts()
                break
            except ValueError:
                print("Please enter a integer value!")
                input3 = True
                
    elif inputSettings == "4": #input 4 which allows user to view game logs 
        print("Viewing Game Logs...")
        viewGameLog()

    elif inputSettings == "5": #input 5 which allows user to change number of people displayed on the leaderboard
        print("Changing the number of players in the leaderboard...")
        input5 = True
        while input5: #loop which ensures that user enters an integer value when changing number of people displayed on the leaderboard
            try:
                changeTop = int(input("Please input choice>>>"))
                changeLeaderboard()
                break
            except ValueError:
                print("Please enter an interger value")
                input5 = True

    elif inputSettings == "6": #input 6 which allows user to change password
        print("\n\n========================================================================================\n                                Password Reset\n========================================================================================")
        print("<<Password Requirements>>\n• Should have at least one number\n• Should have at least one uppercase and one lowercase character.\n• Should have at least one of these special symbols (!@#$%).\n• Should be between 4 to 20 characters long.")
        passWhile = False
        while passWhile == False: #loop which allows user to change password. Loop is only broken when user enters a password which fits all requirements
            passWhile = False
            inputNewPass = input("Enter new password:")
            if len(inputNewPass) < 4:
                print("Password length should be more than 4 characters long.")
                passWhile = True
            elif len(inputNewPass) > 20:
                print("Password length should be less than 20 characters long.")
                passWhile = True
            elif not any(char.isdigit() for char in inputNewPass):
                print('Password should have at least one number.')
                passWhile = True
            elif not any(char in specialCharacter for char in inputNewPass):
                print('Password should have at least one of these special symbols (!@#$%).')
                passWhile = True

            for x in inputNewPass:
                if (x.isupper()) == True:
                    countUpper += 1
                elif (x.islower()) == True:
                    countLower += 1
        
            if countUpper == 0 or countLower == 0:
                print("Password should have at least one uppercase and one lowercase character.")
                passWhile = True

            if passWhile == False:
                print("Password has been succesfully updated")
                changedPass = inputNewPass
                changepassword()
                passWhile = True

    elif inputSettings  == "7": #Leave settings
        print("\nByebye!")
        break
    else:
        print("\n<<Error>> Please input a valid choice")
    
