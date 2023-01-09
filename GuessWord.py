#Get real word.
print("This is a two - player game. The first player should put the word the other should guess here. NO DOUBLE LETTERS. Guesser, don't peek.")
realWord = input()

#Ask how many chances the guesser should get.
print("First player, how many chances should the guesser get?")
howManyGuesses = input()

#Split stuff into list function.
def split(word):
    return list(word)

#Create a list out of the real word.
realWordList = split(realWord)

#Put in many enters so the guesser can't see the real word the first player inputted.
for i in range(90):
    print(
        )

print("Guesser, it's your turn at the computer. DO NOT SCROLL UP.")
print("The real word is " + str(len(realWord)) +  " letters long.")
print("You have " + str(howManyGuesses) + " chances to guess the word!")

#Guesser starts playing.
for i in range(int(howManyGuesses)):
    print(
        )
    #Ask guesser for their guess and split it into a list
    print("Enter your guess RIGHT HERE. If you want to quit, type the letter q.")
    playerGuess = input()
    playerGuessList = split(playerGuess)

    #Check if player wants to quit the game.
    if playerGuess == "q":
        break

    #Check if guesser has word of correct length.
    elif len(playerGuess) != len(realWord):
        print("You aren't even close! Guess something with a length of " + str(len(realWord)) + " letters, dummy.")

    #Check if the guesser got word right.
    elif playerGuess == realWord:
        print("You got the word correct! Let's gooo!!!")
        break

    #Scan line by line if guesser got some letters right.
    elif len(playerGuess) == len(realWord) and playerGuess != realWord:
        #Start with placeholders for each letter.
        letterFromWord = ""
        letterFromGuess = ""

        for l in realWordList:
            #letterFromWord cycles through all the letters in the real word.
            letterFromWord = l
            for g in playerGuessList:
                #letterFromGuess cycles through all the letters in the player's guess.
                letterFromGuess = g
                #Check to see if any two letters are equivalent. The for loop inside the for loop checks all combinations of two letters.
                if letterFromWord == letterFromGuess:
                    print("You got " + str(letterFromGuess) + " correct! It's in the word! (The number of times you get that some letter is in the word") 
                    print("does not correlate with the number of cases of that letter in the word.")

#Notify the player if they lost.
if realWord != playerGuess:
    print("Even if you did or didn't get something correct: YOU FAILED!")
    print("If you give up that easily, don't play this game.")
