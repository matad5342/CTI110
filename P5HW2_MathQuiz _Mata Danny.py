# Add/Subtract Quiz
    # 12 July 2021
    # CTI-110 P5HW2 - Math Quiz
    # Danny Mata
    



import random


def addRandom():
    a1 = random.randint(0, 300)
    a2 = random.randint(0, 300)
    print(f"{a1:>1}")
    print(f"{a2:>3}")
    print("Enter answer")
    ans = int(input())
    while ans != a1 + a2:

        if ans == a1 + a2:
            print("Congratulation your answer is correct.")
        else:
            print("Sorry, the correct answer is : ",a1+a2 )


        ans = int(input("try again : "))
    print("Congratulations!!!! your answer is correct...")


def subRandom():
    a1 = random.randint(0, 300)
    a2 = random.randint(0, 300)
    print(f"{a1:>1}")
    print(f"-{a2:>3}")
    print("Enter answer")
    ans = int(input())
    while ans != a1 - a2:

        if ans == a1 - a2:
            print("Congratulation your answer is correct.")
        else:
            print("Sorry, the correct answer is : ",a1-a2)
        ans = int(input("try again : "))
    print("Congratulations!!!! your answer is correct...")


if __name__ == "__main__":

    while 1:

        print("MAIN MENU")
        print("----------------------")
        print("1) Add Random Numbers ")
        print("2) Subtract Random Numbers")
        print("3) Exit")
        num = int(input("Please choose one of the menu options: "))
        if num == 3:
            print("Thank you for playing")
            print("Bye")
            break
        if num == 1:
            addRandom()
        if num == 2:
            subRandom()
