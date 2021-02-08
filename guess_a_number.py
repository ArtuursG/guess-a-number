import random
print("Hi what's yout name?")
name=input()
print("Nice to meet you", name, "Let's play a game")
print("I will think of a number between 1 and 20 and you have to guess it in less than 6 guesses")
number=random.randint(1,20)
guesses_no=0
while (guesses_no<10):
    print("Take a guess")
    guess=input()
    guess=int(guess)
    guesses_no=guesses_no+1
    if (guess<number):
        print("Wrong, your guess is lower than the number")
    if (guess>number):
        print("Wrong, your guess is higher than the number")
    if (guess==number):
        break;
if (guess==number):
    print("YAAAAYYY, Good job, ", name , "! You guessed my number in ", guesses_no , " guesses!")
if (guess != number):
    print("Sorry. The number I was thinking of was ", number)
    print("You should try again")