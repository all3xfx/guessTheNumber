'''
This program asks the user to guess a number between 1 - 20, chosen randomly by python. First, it asks the user a yes or no question to play the game. It then asks the user
to guess a number, and based on the reply, python tells the user if their guess is too high or too low, and asks the user to try again until they guess the right number.
Then, the program gives the user some statistics such as a list of their guesses, their highest and lowest guess, and the number of tries they took to guess the right number.
After the user guesses the right number, the program gives the user an option to play again or quit.
'''

import random


def guessTheNumber():

    start = input("Want to play a game?")
    while True:
        if (start == "Yes" or start == "yes" or start == "YES"):
            print ("Let's play!")
            print ("It's called guess the number.")
            print ("Let's Start!")
            print ("I'm thinking of a number between 1 and 20.")
            aList = []
    
            anyNumber = random.randrange(20) + 1 # any number between 1 and 20.
            yourGuess = int(input("What's your guess?"))
            aList.append(yourGuess)
            tryCounter = 1 # keeps track of the user's tries
        
            while (yourGuess != anyNumber):

                if (yourGuess > anyNumber):
                    print("Whoops...", yourGuess, "isn't right. Guess lower!")
                else:
                    print("Oh no...", yourGuess, "isn't right. Guess higher!")
        
                yourGuess = int(input("Guess again:"))
                aList.append(yourGuess)
                tryCounter = tryCounter + 1 # incorrect guess adds 1 to the tryCounter

            print("You guessed it! The number I was thinking of was:", anyNumber)
            print("And it only took you", tryCounter, "guesses. Your fast!")
            print("Here are some random facts about this game:")
            print("Your guesses in order are:", aList)
    
            aList.sort()
            minimum = aList[0]
            maximum = aList[len(aList)-1]
            print("Your highest guess was:", maximum)
            print("Your lowest guess was:", minimum)
            start = input("Play again?")
        elif (start == "No" or start == "no" or start =="NO"):
            print("Bye!")
            return
        else:
            print("Oops, I didn't get that. Yes to play again, No to quit!")
            start = input("Want to play a game?")


guessTheNumber()

