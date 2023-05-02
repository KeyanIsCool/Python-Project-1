# Python-Project-1
A hangman game with advanced features

Hangman is a classic word game in which a computer randomly selects a word that the player must
guess by supplying each of its letter. For each incorrect guess, a part of a stick figure of a hanged man. 
Scoring system – for each letter that you guess correctly in the secret word, you will be awarded 2 points. If you guess the whole word entirely in one guess, you will be awarded 10 points. Player wins if the score is > 15 points. The maximum points for a set of 3 games will be 30 points.
===============================
|Documentation for hangman.py |
===============================

1)	When you first run the hangman.py program using CTRL + F5 on the keyboard, this log in banner will be shown. Please enter your desired username and hit enter. (The username should not contain any numbers or special characters other than the specified)
 
2)	You will then be met with game menu, which allows you to input the options 1 to 4.
Enter 1 to start the game
Enter 2 to view your current score as well as the leader boards
Enter 3 to change the game mode of the game. (Animal Names, Complex Words and Idioms)
Enter 4 to exit the game
 
3)	This is what you will see when you start the game. At the top, you will see your username, game mode as well as which attempt of the set you are on and what word of the attempt you are on. You can input your guess which can only be alphabets or ‘ . 
 
4)	If you input a correct guess, it should print out at the position where the letter is placed.
 
5)	If you input a letter that is not in the word, this message will pop up. Each attempt, you are given 2 lifelines, and each lifeline can only be used once per word. If you input “1”, it will display all the vowels in the word (A,E,I,O,U). If you input “2”, it will display the meaning of the secret word. Please note that each lifeline you use will result in the deduction of 4 points. If you do not wish to use a lifeline, you can key in any other character to skip.
 
6)	You also enter the entire secret word at one go if you can guess it. This will result in an instant win if guessed correctly and you will be automatically awarded with 10 points.
 
7)	After each secret word you guess, you will be given the option to continue playing or not. Enter “Y” to continue to the next word of that attempt or “N” to end that attempt and move on to the next attempt.
 
8)	After each attempt, you should see a message like this, alerting you that you have completed your current attempt and is moving on to the next.
 
9)	Once you have completed the final word of the last attempt, you should be brought back to the main menu. You can enter “2” to view your score as well as view the leader boards.

10)	Here, you are able to view the score you achieved and the leader boards for the top players who have the most number of points.
 
11)	When you enter “3” at the main menu, you should see 3 options for 3 different game modes (Animal Names, Complex Words, and Idioms). The mode set by default is Animal names, but you are able to change it by entering “2” for Complex words and “3” for Idioms.
 
12)	Finally, you can enter “4” to exit and quit the game.

=============================
|Documentation for admin.py |
=============================
Documentation for admin.py

This program is an admin program where admins can log in with a specified username and password to change the game settings for the main hangman game (hangman.py).

1)	When you run the program, you will be first prompted to log in. The prescribed username is admin, and the prescribed password is qQ1@. You will be able to reset the password later.
 
2)	Once you successfully log in, you will be able to see the main menu. As the admin, you are able to edit the word pool, edit the number of words per set, edit the number of attempts per set, view game logs, set the number of people displayed on the leader board, as well as reset the prescribed password like mentioned above.
 
3)	When you enter “1” to edit the word pool, you will be displayed this menu, specifically for editing the word pool. 
 
4)	When you enter option “1” in the word pool menu, it would display to you all the words in the Animal Names word list (C:\Users\keyan\OneDrive\Attachments\Desktop\SP SEM2 YR1\PSEC\Coding\CA1\wordlistanimals.json) , complex words list (C:\Users\keyan\OneDrive\Attachments\Desktop\SP SEM2 YR1\PSEC\Coding\CA1\wordlistComplex.json) and idioms word list (C:\Users\keyan\OneDrive\Attachments\Desktop\SP SEM2 YR1\PSEC\Coding\CA1\wordlistidioms.json)
 
5)	When you enter option in the word pool menu, you are able to add a word and description of the word for a specific word list. In this case, I added the word “cat” with the description “an animal that meows”.
 
6)	You can delete a word from a pool by entering “3” in the word pool menu. In this case I will be removing “cat” from the animal names word list.
 
7)	I can also change the description of the word entering “4” in the word pool menu. In this case, I will be changing the description of the word “owl” in the animal names word to “bird that is only active at night and preys on mice”

8)	Now back at the main menu, if you enter “2” you will be able to edit the number of words per set, which is the number of secret words the player has to guess per attempt during the game. In this case, I set the number to 2.
 
9)	At the main menu when you enter option “3”, you are able to change the number of attempts per set. Which is the number of tries a person gets to play a game in each set.

10)	When you enter “4” on the keyboard, you will be able to view the game logs. You are able to filter out certain game logs between the start and end date that you have specified, or you can display the entire games log by pressing any other character apart from “E” when prompted.
 
11)	You are able to change the number of players displayed on the leader board by entering “5” at the main menu, then key in your desired number.
 
12)	When you enter “6” in the main admin menu, you are able to reset the prescribed admin password. The password must contain at least one number, one upper case and one lower case character, a special symbol and must be between 4 and 20 characters long.


============
|Reflection|
============
, I have learnt how to apply and create functions, how to use certain commands like try and except value error.
I have learned how to use dictionaries and I also learned how to work with JSON files and JSON dictionaries.
Some difficulties I had while doing this CA1 was understanding the brief
I felt like it was not clear and some things inside do not make that much sense.
I also had a lot of trouble when I first started working with dictionaries as well as JSON files, but I conquered them by searching for help online.

