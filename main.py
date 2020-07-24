import random
import math
import time

words = []

with open("words.txt", "r") as f:
	for line in f.readlines():
		words.append(line.strip())

secret_word = random.choice(words)

lettersnum = len(secret_word)

#print('\033[91m'+" o"+'\033[0m'+" \n/|\ \n/ \ ")
#print('\033[91m'+" o \n/"+'\033[0m'+"|\ \n/ \ ")
#print('\033[91m'+" o \n/|"+'\033[0m'+"\ \n/ \ ")
#print('\033[91m'+" o \n/|\ "+'\033[0m'+"\n/ \ ")
#print('\033[91m'+" o \n/|\ \n/"+'\033[0m'+" \ ")
#print('\033[91m'+" o \n/|\ \n/ \ ")

print('\033[93m'+"Welcome to hangman! \n")
time.sleep(2)
print("The game is simple. Guess a letter; if that letter is in the word, you get a point! If it is not in the word, a body part is added to the hangman.")
time.sleep(4)
print("Once the hangman has a head, body, two arms and two legs, you loose!")
time.sleep(3)
print("Guess all the letters in the word before the hangman is complete and you win!")
time.sleep(3)
begin = input("Would you like to continue? Y/N? \n")
if begin == "N":
  print("Okay. Goodbye!")
  start = False
if begin == "Y":
  print("Let's begin!")
  print('\033[0m'+" o \n/|\ \n/ \ ")
  start = True
if start == True:
  print('\033[93m'+"The word has "+str(lettersnum)+" letters! \n")
   #while keep_going == True:
  correct_guessed = ""
  all_guessed = ""
  print(secret_word)
  while set(correct_guessed) != set(secret_word):
    if all_guessed:
      print("Letters guessed: "+", ".join(sorted(all_guessed)))
    guess = input("Guess: ")
    all_guessed += guess
    if guess in secret_word:
      print("That letter IS in the word!")
      correct_guessed += guess
    else:
      print("That letter is NOT in word!")
      
        #loop here of hangmen prints

print("You guessed the word!")


print(secret_word)