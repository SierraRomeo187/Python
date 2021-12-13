from random import randint

randomNumberGuess = randint(0, 100)

playerInput = -1
message = "Try to Guess the number (between 1 and 100).. "

while playerInput != randomNumberGuess:
    playerInput = int(input(message))
    
    if playerInput > randomNumberGuess:
        message = "Too high! Guess Lower: "
    elif playerInput < randomNumberGuess:
        message = "Too low! Guess Higher: "
        
    elif playerInput == randomNumberGuess:
        print("You Win, the number to guess was "
              + str(randomNumberGuess) + " indeed.")
        break


