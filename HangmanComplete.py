import random




HANGMANPICS = ['''

 +---+
 |   |
     |
     |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
     |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
 |   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


def getGuess(guessedLetters):
   while True:
       guess = input("Guess a letter: \n")
       guess = guess.lower()

       if(len(guess)) != 1:
          print("Please 1 letter")
       elif guess not in "abcdefghijklmnopqrstuvwyz":
          print("Please enter a letter in the alphabet")
       elif guess in guessedLetters:
          print("You already guessed that one :) ")
       else:
          return guess

def getRandomWord(wordList):
   wordIndex = random.randint(0, len(wordList.split())-1)
   return wordList.split()[wordIndex]





  

def displayBoard(HANGMANPICS, missedLetters, correctLetters, myWord):
   print(HANGMANPICS[len(missedLetters)])
   print("You've taken " + str(len(missedLetters)) + " Incorrect guesses.")

   for letter in missedLetters:
       print(letter)

   blanks = '_.' * len(myWord)

   for i in range(len(myWord)):
       if myWord[i] in correctLetters:
           blanks = blanks[:i] + myWord[i] + blanks[i+1:]
   print(blanks)



words = "mochi dinosaur clam cat balcony tree signature peak lightning backpack"

print("Hello, Let's play the Hangman game! ")

myWord = getRandomWord(words)

gameOver = False
correctLetters = ""
missedLetters = ""



'''
GAME LOOP
while True
  Call displayBoard and pass in HANGMANMPICS, missedLetters, correctLetters, and myWord
  Create a var called 'guess' and set it equal to a call to getGuess(correctLetters+missedLetters)
  if guess is in myWord
  add guess to correctLetters and set it back to correctLetters

'''




while True:
   displayBoard( HANGMANPICS, missedLetters, correctLetters, myWord)
   guess = getGuess (correctLetters + missedLetters)

   if guess in myWord:
       correctLetters = correctLetters + guess

       win = True
       for i in range(len(myWord)):
           if myWord[i] not in correctLetters:
               win = False
               break
       if win:
           print("Yayyy Correct! It is " + myWord)
           gameOver = True
   else:
       missedLetters = missedLetters + guess

       if(len(HANGMANPICS) - 1) == len(missedLetters):
          displayBoard(HANGMANPICS, missedLetters, correctLetters, myWord)
          print (" You Lost!")
          print (" The word was: " + myWord)
          gameOver = True

   if gameOver:
          answer = input ("Do you want to play again? yes / no")
          answer.lower()

          if answer == "yes":
              myWord = getRandomWord(words)
              gameOver = False
              correctLetters = ""
              missedLetters = ""
          else:
              break
