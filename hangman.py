""""
Main Program

StudentID: p2227395
Name:      Keyan Goh
Class:     DISM/1B/03
Assesment: CA1-1

Script name:
   hangman.py

Purpose:
   The main program to execute the hangman game. Allows user to play hangman game and choose game mode, view leaderboard.

Python Version:
   Python 3

Refernce:
   https://chat.openai.com/chat
"""

# ====================================
# imports
# ====================================
import re
import random
import json
import datetime

#Functions
# ====================================

def saveStats():
   """
      This function is to save the statistics of each player. Including: Username,Score,Date,Number of Words Guessed Per Attempt ,Number of Attempts as well as the correct and incorrect guesses
      into a JSON file (CA1/game_log.json)
   """   
   filename = 'CA1/game_log.json'
   with open(filename, 'r') as file:
      data = json.load(file)
      data['Username'].append(userName)
      data['Score'].append(scoreAccumulated)
      data['Date'].append(str(starttime))
      data['Words Guessed Per Attempt'].append(wordCount)
      data['Number of Attempts'].append(totalAttempts)
      if len(wrongLog) >= 1:
         data['Incorrect Guesses'].append(wrongLog)
      else:
         noWrong = "-None-"
         data['Incorrect Guesses'].append(noWrong)
      if len(correctLog) >= 1:
         data['Correct Guesses'].append(correctLog)
      else:
         noCorrect = "-None-"
         data['Correct Guesses'].append(noCorrect)
      
   with open(filename, 'w') as file:
      json.dump(data,file,indent=4)

#Function to display the leaderboard for the top players
def getTopPlayer():
   """
      This function is to retrieve the scores of the highest players, which is store in a JSON file(CA1/game_log.json), then prints the top players in a leaderboard.
   """   
   filename = 'CA1/game_log.json'
   with open(filename, 'r') as file:
      data = json.load(file)
      usernameList = data['Username']
      scoreList = data['Score']
      with open('CA1/settings.json', 'r') as file2:
        data2 = json.load(file2)
        numberOfTopPlayers = data2['number of top players']
# Initialize an empty list to store tuples with the indices and values of the highest [blank] numbers
      counter = []
# Iterate over the list of numbers and keep track of the index
      for i, number in enumerate(scoreList):
  # If the list is not full, just append the tuple
        if len(counter) < numberOfTopPlayers:
            counter.append((i, number))
  # If the list is full, check if the number is larger than the smallest number in the list
        else:
            if number > min(counter, key=lambda x: x[1])[1]:
      # If it is, remove the tuple with the smallest number and append the new tuple
                counter.remove(min(counter, key=lambda x: x[1]))
                counter.append((i, number))
# Print out the indices and values of the highest [blank] numbers
    # Sort counter in descending order by the second element of each tuple
      sortCounter = sorted(counter, key=lambda x: x[1], reverse=True)
      c = 1
      print(f"\nYour score:{scoreAccumulated}\n")
      print("==================================================\nLeaderboards\n==================================================\n")
      print("Player | Score")
      for index, value in sortCounter:
        print(f"{c}.{usernameList[index]}, Score: {value}")
        c+=1


#The different states of the hangman
stages = [ 
#final state of hangman
"""
   _____
  |     |
  |     o
  |    /|\\
  |    / \\
  |
 _|_
|   |_______
|           |
|___________|
""",
#stage 5
"""
   _____
  |     |
  |     o
  |    /|\\
  |    / 
  |
 _|_
|   |_______
|           |
|___________|
""",
#stages 4
"""
   _____
  |     |
  |     o
  |    /|\\
  |     
  |
 _|_
|   |_______
|           |
|___________|
""",
#stage 3
"""
   _____
  |     |
  |     o
  |    /|
  |     
  |
 _|_
|   |_______
|           |
|___________|
""",
#stage 2
"""
   _____
  |     |
  |     o
  |     |
  |     
  |
 _|_
|   |_______
|           |
|___________|
""",
#stage 1
"""
   _____
  |     |
  |     o
  |    
  |     
  |
 _|_
|   |_______
|           |
|___________|
""",
#stage 0
"""
   _____
  |     |
  |     
  |
  |     
  |
 _|_
|   |_______
|           |
|___________|
"""
            ]

#Welcome message
print("==========================================================================================================================================\n                                    Welcome to Hangman!\n==========================================================================================================================================\nPlease enter a username to begin. Username should not include any characters other than upper and lowercase letters, '-', and '/'.")

#Get username input
def start():
   """
      This function is ask user for username input. It is designed so that users cannot enter usernames which have certain special characters.
   """   
   startGame = True
   while startGame: #while loop for username input. If startGame = False, loop will break and player will enter main menu
         global userName
         userName = input("Please input your username:") 
         checkUser = re.compile("[!@#$%^&*()-+?_=,<>.\|1234567890']")
         #To check if username has any special characters which are not allowed
         if(checkUser.search(userName) == None):
            if userName.strip():
               # the username is not empty or just spaces, so we can exit the loop
               startGame = False
            else:
               print("Error: the username cannot be blank or contain only spaces!")
         else:
            print("Username is invalid. Only the following characters are allowed - upper and lowercase letters, '-', and '/'")


wordCount = 1       #This variable defines which word of the set the player is playing on
now = datetime.datetime.now()    #To get the start time of the game.
starttime = now.strftime("%c")

#Calling the function to bring the user to the menu interface
start()

#Game start function 
def hangGame():
   """This function is the main hangman game. This function is called whenever the user wants to play the game.

   Returns:
      gameLoop(boolean): Boolean which determines if the while loop continues for the next word/attempt
      wordCount(int): Integer which counts which word of the game we are guessing
      score(int): Integer which keeps track of the players total score at the end of each attempt
      lifelineleft(int): Integer which keeps track of the number of life lines left (Max set to 2)
   """   
   inputWholeWord = 0 #This variable determines whether the player input the answer letter by letter or the entire word
   lifelinePerGame = 1 #The number of lifelines allowed for each word
   gameWordLetters = [] #List to store each character of the random word
   gameSpace = [] #Stores the spaces if any of the secret word
   for letter in gameWord: #This for loop appends each letter of the secret word into a list without repeat
      if letter == " ":
         gameSpace.append(letter)
      elif letter not in gameWordLetters:
         gameWordLetters.append(letter)
   global score   
   wrongGuess = [] #Stores the wrong guesss when player enters letter by letter
   wrongGuess2 = [] #Stores the wrong guesses when player inputs the entire word
   correctGuess = [] #Stores the correct guesses of the player
   game = True
   triesLeft = 6
   currentScore = 0
   #If game = True, game continues to run
   while game: #This while loop loops the game as many times until game = False
      global wordCount
      #Print out top page message
      print("\nH A N G M A N\n")
      print(f"Player: {userName}")
      print(f"Game mode: {currentMode}")
      print(f"Attempt: {attempt+1} of {numOfAttps}")
      print(f"Word: {wordCount} of {numOfWords}")
      print(stages[triesLeft])
      print("\nIncorrect Letters: ",' '.join(wrongGuess),"(",len(wrongGuess),")\n")
      #word blanks
      for letter in gameWord:
         if letter.lower() in correctGuess:
            print(letter, end=" ")
         elif (letter == " "):
            print(" ",end=" ")
            game = True
         else:
            print("_", end=" ")
            game = True
      
   #Get input for choice
      inputAns = input("\nSelect a valid character [a-z,']:")
      
   #If the input ans is wrong
      if len(inputAns.lower()) == 1:
         if inputAns.lower() not in gameWord.lower():
            if (inputAns.isalpha() or inputAns == "'") == True:
               if inputAns.lower() in wrongGuess: #If the letter the player guessed is already guessed
                  print("\nYou have already guessed this letter!\n")
               else:
                  wrongGuess.append(inputAns.lower())
                  triesLeft -= 1
                  global lifelineleft
                  if lifelinePerGame == 1:
                     if lifelineleft >= 1: #If number of lifelines left is 1 or more this will pop up.
                        print(f"You have {lifelineleft} lifelines remaining. Enter (1) to display all vowels in the word , (2) to display the meaning of the word , or any enter any other key to not use the lifeline. (There is a deduction of 4 points for each lifeline used)")
                        lifelineInput = input("Enter selection here >>>")
                        if lifelineInput == "1":
                           ("\nDisplaying all vowels in word...")
                           lifelineleft -= 1
                           lifelinePerGame -= 1
                           currentScore -= 4
                           findVowel = ['a','e','i','o','u']
                           for letter in gameWord.lower():
                              if letter in findVowel:
                                 if letter not in correctGuess:
                                    correctGuess.append(letter)
                        elif lifelineInput == "2":
                           print("\nDisplaying meaning of word...")
                           print(f'\n================================================================================\nMeaning of word: {meaningList[wordCount-1]}\n================================================================================\n')
                           lifelineleft -= 1
                           lifelinePerGame -= 1
                           currentScore -= 4
                     else:
                        print("\nYou have 0 life lines left.\n")
            else:
               print("You did not enter a valid input. Please ensure that you only key in alphabets.")

            if triesLeft == 0:
               #If player has used up all tries, print the final hangman stage.
               print(stages[0])
               print("\nIncorrect Letters: ",' '.join(wrongGuess),"(",len(wrongGuess),")\n")
               break
      
   #if the input string length is bigger than 1
      if len(inputAns.lower()) > 1:
         if inputAns.lower() == gameWord:
            #If the user input the whole word and it is correct
            inputWholeWord = 1
            game = False
            break
         elif len(inputAns) != len(gameWord):
            #If the length of the input is not equals to the length of the secret word
            print("<<Errror>> Please only input one letter at a time or the full answer!")
         else:
            for letter in inputAns.lower():
               if letter == "'":
                  if letter in gameWordLetters:
                     if letter not in correctGuess:
                        correctGuess.append(letter)
                  elif letter not in wrongGuess:
                     wrongGuess2.append(letter)
               elif letter.isalpha():
                  if letter in gameWordLetters: #if letter is a letter in secret word, the letter is appended to correctGuess list
                     if letter not in correctGuess:
                        correctGuess.append(letter)                     
                  elif letter not in wrongGuess:
                     if letter.isalpha(): #if letter is not a letter in secret word, the letter is appended to wrongGuess2 list
                        wrongGuess2.append(letter)
               else:
                  print("Please ensure that all letters in the input are alphabets.")

            triesLeft -= len(set(wrongGuess2)) #convert wrongGuess2 into a set to eliminate duplicates
            for x in set(wrongGuess2): #set to ensure no repeats
               wrongGuess.append(x)
            if triesLeft <= 0:
               game = False
               break
            elif len(gameWordLetters) == len(set(correctGuess)):
               game = False
            else:
               game = True
         

      if len(inputAns.lower()) == 1: #If user inputs one character
         if inputAns.lower() in gameWord.lower():
            if inputAns.lower() in correctGuess: 
               print("\nYou have already guessed this letter!\n")
            elif inputAns.lower() == " ":
               print("Please ensure that all letters in the input are alphabets.")
            else:
               correctGuess.append(inputAns.lower())
               
            
            set1 = set(sorted(correctGuess))
            set2 = set(sorted(gameWordLetters))
            if set1 == set2:
               game = False
               break

      if len(correctGuess) > 7:
         game = False


   if game == False:
      print("\nH A N G M A N\n")
      print(f"Player: {userName}")
      print(f"Game mode: {currentMode}")
      print(f"Attempt: {attempt+1} of {numOfAttps}")
      print(f"Word: {wordCount} of {numOfWords}")
      print(stages[triesLeft])
      print("\nIncorrect Letters: ",' '.join(wrongGuess),"(",len(wrongGuess),")\n")
      #word blanks
      for letter in gameWord:
         if letter.lower() in gameWord:
            print(letter, end=" ")
      print(f'\nCongratulations. (Your score was above 15 or you have guessed the secret word) The secret Word({currentMode}) is "{gameWord}": {meaningList[wordCount-1]}\n*****')
      if inputWholeWord == 1:
         currentScore += 10
      else:
         currentScore = len(correctGuess) * 2
      score += currentScore
      correctLog.append(gameWord)
   else:
      for letter in gameWord:
         if letter.lower() in correctGuess:
            print(letter, end=" ")
         else:
            print("_", end=" ")
      print(f'\nMaximum number of guesses!\nAfter {len(wrongGuess)} incorrect guesses and {len(correctGuess)} correct guess(es), the word was "{gameWord}": {meaning}\n*****')
      currentScore = len(correctGuess) * 2
      score += currentScore
      wrongLog.append(gameWord)

   if (int(wordCount) < numOfWords):
      returnOrDont = True
      while returnOrDont: #loop which determines whether user continue to next word or exits the game
         continueOrNo = input("Enter [Y]es to play again or [N] to quit:")
         global gameLoop
         if continueOrNo.lower() == "y":
            wordCount += 1
            gameLoop = True
            returnOrDont = False
            return gameLoop,wordCount,score,lifelineleft
            

         elif continueOrNo.lower() == "n":
            if (attempt + 1) < numOfAttps:
               print("\nMoving on to next attempt...\n")
            else:
               print("\nBye bye!\n")
            gameLoop = False
            returnOrDont = False
            return gameLoop,score,wordCount

         else:
            print("Please key in [Y] or [N]")
            returnOrDont = True

   elif (int(attempt)+1) == numOfAttps:
      print(f'Game over! You have completed all {numOfWords} words in attempt {attempt + 1}. Check leaderboards in main menu to check your score!\nBye bye!')
      gameLoop = False
      return gameLoop
   
   else:
      print(f'Game over! You have completed all {numOfWords} words in attempt {attempt + 1}. Moving on to next attempt')
      gameLoop = False
      return gameLoop   


#Game main menu
gameMenu = True
scoreAccumulated = 0
score = 0
currentMode = "Animal Names"
gameWordList = []
meaningList = []
correctLog = []
wrongLog = []
while gameMenu: #While loop which continues to display the game menu when equals to true
   totalAttempts = 0
   print("\n<<Game Menu>>\n\nPlease selection an option.\n(1)Start Game\n(2)Leaderboard\n(3)Change Game Mode\n(4)Quit")
   menuInput = input("\nInput option here >>")
   filename = "CA1/settings.json"
   with open(filename,"r") as file:
      data = json.load(file)
      numOfAttps = data["number of attempts"]
      numOfWords = data["number of words"]
   if menuInput == "1": #Option 1 which starts the game
      scoreAccumulated = 0
      for attempt in range(numOfAttps): #to get selected number of random words from the word list
         if currentMode == "Animal Names":
            filename = "CA1/wordlistanimals.json"
            with open(filename,"r") as file:
               ranWord = json.load(file)
               for x in range(numOfWords):
                  selectedWords = random.choice(list(ranWord.keys()))
                  gameWordList.append(selectedWords)
                  meaning = ranWord[selectedWords]
                  meaningList.append(meaning)

         if currentMode == "Complex Words":
            filename = "CA1/wordlistComplex.json"
            with open(filename,"r") as file:
               ranWord = json.load(file)
               for x in range(numOfWords):
                  selectedWords = random.choice(list(ranWord.keys()))
                  gameWordList.append(selectedWords)
                  meaning = ranWord[selectedWords]
                  meaningList.append(meaning)
                  
         if currentMode == "Idioms":
            filename = "CA1/wordlistidioms.json"
            with open(filename,"r") as file:
               ranWord = json.load(file)
               for x in range(numOfWords):
                  selectedWords = random.choice(list(ranWord.keys()))
                  gameWordList.append(selectedWords)
                  meaning = ranWord[selectedWords]
                  meaningList.append(meaning)


         wordCount = 1
         score = 0
         global lifelineleft
         lifelineleft = 2
         gameLoop = True
         while gameLoop: #loop which determines if the game continues or not
            for x in gameWordList:
               gameWord = x
               hangGame() #calling function which starts the game
               if gameLoop == False:
                  if score > (10*int(numOfWords)):
                     score = 10*int(numOfWords)
                  scoreAccumulated += score            
                  gameWordList.clear()
                  meaningList.clear()
                  break
         totalAttempts += 1
      saveStats() #calling function which saves stats in the game logs
   elif menuInput == "2": #menu option 2 which allows the user to view his score and the leaderboards
      getTopPlayer()
   elif menuInput == "3":
      currentMode1 = ""
      print('There are 3 different game modes:\n1.Animal Names\n2.Complex Words\n3.Idioms')
      if currentMode == "Animals Names":
         currentMode1 = "Animals Names"
      if currentMode == "Complex Words":
         currentMode1 = "Complex Words"
      if currentMode == "Idioms":
         currentMode1 = "Idioms"
      print(f'\nCurrent game mode is set to {currentMode}\n')
      setgamemode = input("Please enter your desired mode here>>")
      if setgamemode == "1":
         currentMode = "Animal Names"
      elif setgamemode == "2":
         currentMode = "Complex Words"
      elif setgamemode == "3":
         currentMode = "Idioms"
      else:
         print("You have selected a invalid gamemode. Please try again")
   elif menuInput == "4":
      print("Bye bye!")
      break
   else:
      print("Please enter a valid input.")

