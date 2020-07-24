import random
import math
import time

words = []
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
elif begin == "Y":
  print("Let's begin!")
  print('\033[0m'+" o \n/|\ \n/ \ ")
  start = True
  if start == True:
    GO = True
    man = 0
    with open("words.txt", "r") as f:
      for line in f.readlines():
        words.append(line.strip())

    secret_word = random.choice(words)

    letters_num = len(secret_word)
    print(secret_word)
    print('\033[93m'+"The word has "+str(letters_num)+" letters! \n")
    correct_guessed = ""
    all_guessed = ""
    while set(correct_guessed) != set(secret_word):
      if all_guessed:
        print('\033[91m'+"All letters guessed: "+", ".join(sorted(all_guessed)))
        print('\033[91m'+"Correct letters guessed: "+", ".join(sorted(correct_guessed)))
      guess = input('\033[0m'+"Guess: ").lower()
      all_guessed += guess
      if guess in secret_word:
        print('\033[93m'+"That letter IS in the word!")
        correct_guessed += guess
        for letter in secret_word:
          if letter in correct_guessed:
            print(letter, end = " ")
          else:
            print("_", end = " ")
        print()
      else:
        man += 1
        print('\033[93m'+"That letter is NOT in word!")

        if man == 1:
          print('\033[91m'+" o"+'\033[0m'+" \n/|\ \n/ \ ")
        elif man == 2:
          print('\033[91m'+" o \n/"+'\033[0m'+"|\ \n/ \ ")
        elif man == 3:
          print('\033[91m'+" o \n/|"+'\033[0m'+"\ \n/ \ ")
        elif man == 4:
          print('\033[91m'+" o \n/|\ "+'\033[0m'+"\n/ \ ")
        elif man == 5:
          print('\033[91m'+" o \n/|\ \n/"+'\033[0m'+" \ ")
        elif man == 6:
          print('\033[91m'+" o \n/|\ \n/ \ ")
          print('\033[96m'+"You loose!")
          GO = False
          time.sleep(3)
          again1 = input('\033[91m'+"Would you like to play again? Y/N? \n")
          if again1 == "Y":
            Start = True
          elif again1 == "N":
            Start = False
            print("Okay. Bye!")

  while GO == True:
    print("\nYou guessed the word!")
    print('\033[96m'+secret_word)
    time.sleep(3)
    again2 = input('\033[91m'+"Would you like to play again? Y/N? \n")
    if again1 == "Y":
      start = True
    elif again1 == "N":
      start = False
      print("Okay. Bye!")