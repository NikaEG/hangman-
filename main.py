import random
import math
import time

words = []

with open("words.txt", "r") as f:
	for line in f.readlines():
		words.append(line.strip())

secret_word = random.choice(words)

lettersnum = len(secret_word)

print(" o \n/|\ \n/ \ ")
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
  start = True
if start == True:
  print("The word has "+str(lettersnum)+" letters! \n")
  while keepgoing == True:
   #from here down needs editing! 
  correct_guessed = ""

  while set(correct_guessed) != set(secret_word):
    guess = input("Guess: ")
    if guess in secret_word:
      print("You got a letter!")
      correct_guessed += guess
    else:
      print("That's not in the word!")
      #loop here of hangmen prints

print("You guessed the word!")


  print(secret_word)