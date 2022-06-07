import random
def guessNumber():
    guess = input("Enter a number from 1 to 9")
    numbers=[1,2,3,4,5,6,7,8,9]
    num=random. choice(numbers)
    chances=5
    while chances <5:
        if(guess == num):
            print("Congratulations!You won")
            
    if not chances < 5:
            print("You loose!! The number is",num)


guessNumber()