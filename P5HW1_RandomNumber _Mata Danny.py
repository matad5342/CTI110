# Random number game
# Date: 11 July 2021
# CTI-110 P5HW1 - Random Number
# Danny Mata


import random


def main():

    rand_num = random.randrange(1, 100)
    print("MAIN MENU")
    print(" 1 Play Game")
    print(" 2 Exit")


    attempts = 0
    while 1:
        num = int(input("Guess the number: "))
        if num > rand_num:
            print("Too high, try again !")
            attempts += 1
        elif num < rand_num:
            print("Too low, try again !")
            attempts += 1
        else:
            break

    print("Congratulations you guessed the number in " + str(attempts) + " Guesses")
    again = int(input("would you like to play again? (yes=1, 2=No"))


if __name__ == '__main__':
    main()