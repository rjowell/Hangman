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
